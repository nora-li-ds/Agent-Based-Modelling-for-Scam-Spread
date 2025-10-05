import matplotlib.pyplot as plt
def memory_mb(df):
    """Return memory usage of a DataFrame in MB."""
    return df.memory_usage(deep=True).sum() / 1024**2

def summarize_amounts(df, col="amount"):
    """Quick summary stats for transaction amounts (or any numeric col)."""
    return {
        "min": df[col].min(),
        "median": df[col].median(),
        "mean": df[col].mean(),
        "max": df[col].max(),
    }
def plot_hist(series, bins=50, title=None, xlabel=None, ylabel="Frequency"):
    """Quick histogram wrapper for clean plotting."""
    import matplotlib.pyplot as plt
    plt.figure(figsize=(6, 3))
    series.plot(kind="hist", bins=bins, alpha=0.7)
    plt.title(title or series.name)
    plt.xlabel(xlabel or series.name)
    plt.ylabel(ylabel)
    plt.show()

def zoom_yaxis(ax, factor=0.02):
    """
    Slightly zoom in the y-axis range to highlight variation in bar/line plots.
    factor: proportion of range to trim from both ends (default 0.02 = 2%)
    """
    try:
        ymin, ymax = ax.get_ylim()
        span = ymax - ymin
        ax.set_ylim(ymin + span * factor, ymax - span * factor)
    except Exception as e:
        print(f"[zoom_yaxis] Warning: failed to adjust y-axis → {e}")
    return ax
