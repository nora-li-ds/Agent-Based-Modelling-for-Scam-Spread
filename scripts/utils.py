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
