import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.ensemble import HistGradientBoostingRegressor
from rich.console import Console

from src.features.transformers import sin_transformer, cos_transformer, periodic_spline_transformer
from src.utils.plotting import plot_predictions

console = Console()

def main():
    # 1. Load data
    console.rule("[bold blue]Step 1: Loading Data")
    df = pd.read_csv("data/processed/imputed_training_data_20250723_165119_vars_39_len_22392_knn.csv", parse_dates=True)
    df['datetime_UTC'] = pd.to_datetime(df['datetime_UTC'])
    df['hour'] = df['datetime_UTC'].dt.hour
    df['weekday'] = df['datetime_UTC'].dt.weekday
    df['month'] = df['datetime_UTC'].dt.month

    X = df.drop(columns=['target', "datetime_UTC"])
    y = df.target

    ts_cv = TimeSeriesSplit(n_splits=5, test_size=24*30)
    all_splits = list(ts_cv.split(X, y))
    train_0, test_0 = all_splits[0]

    # 2. Pipelines
    console.rule("[bold blue]Step 2: Creating Pipelines")
    one_hot_encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    alphas = np.logspace(-4, 1, 20)

    naive_linear_pipeline = make_pipeline(
        ColumnTransformer([("one_hot_time", one_hot_encoder, ["hour", "weekday", "month"])],
                          remainder=MinMaxScaler()),
        RidgeCV(alphas=alphas),
    )

    cyclic_cossin_transformer = ColumnTransformer([
        ("month_sin", sin_transformer(12), ["month"]),
        ("month_cos", cos_transformer(12), ["month"]),
        ("weekday_sin", sin_transformer(7), ["weekday"]),
        ("weekday_cos", cos_transformer(7), ["weekday"]),
        ("hour_sin", sin_transformer(24), ["hour"]),
        ("hour_cos", cos_transformer(24), ["hour"]),
    ], remainder=MinMaxScaler())
    cyclic_cossin_linear_pipeline = make_pipeline(cyclic_cossin_transformer, RidgeCV(alphas=alphas))

    cyclic_spline_transformer = ColumnTransformer([
        ("cyclic_month", periodic_spline_transformer(12, 6), ["month"]),
        ("cyclic_weekday", periodic_spline_transformer(7, 3), ["weekday"]),
        ("cyclic_hour", periodic_spline_transformer(24, 12), ["hour"]),
    ], remainder=MinMaxScaler())
    cyclic_spline_linear_pipeline = make_pipeline(cyclic_spline_transformer, RidgeCV(alphas=alphas))

    gbr_pipeline = make_pipeline(cyclic_cossin_transformer, HistGradientBoostingRegressor(max_iter=500))

    # 3. Train & Predict
    console.rule("[bold blue]Step 3: Training and Predicting")
    predictions = {}
    for name, model in {
        "Ordinal time features": naive_linear_pipeline,
        "Trigonometric time features": cyclic_cossin_linear_pipeline,
        "Spline-based time features": cyclic_spline_linear_pipeline,
        "Gradient Boost + Spline": gbr_pipeline,
    }.items():
        model.fit(X.iloc[train_0], y.iloc[train_0])
        predictions[name] = model.predict(X.iloc[test_0])

    # 4. Plot
    console.rule("[bold blue]Step 4: Plotting Predictions")
    plot_predictions(y.iloc[test_0], predictions, last_hours=2*96, title='Actual vs Predicted')

if __name__ == "__main__":
    main()