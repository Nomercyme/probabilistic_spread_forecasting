import matplotlib.pyplot as plt

def plot_predictions(y_true, predictions_dict, last_hours=96, title="Predictions", xlabel="Time (hours)", ylabel="DA -> DA2 Price Spread (£/MWh)"):
    fig, ax = plt.subplots(figsize=(12, 4))
    fig.suptitle(title)

    ax.plot(y_true.values[-last_hours:], "x-", alpha=0.2, label="Actual Spread", color="black")
    for label, pred in predictions_dict.items():
        ax.plot(pred[-last_hours:], "x-", label=label)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.legend()
    plt.show()