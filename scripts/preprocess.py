import pandas as pd

def load_and_sample(input_path, output_path=None, sample_size=None, random_state=42):
    """
    Load a CSV dataset, optionally downsample it, and (optionally) save the result.
    """
    df = pd.read_csv(input_path, low_memory=False)

    if sample_size and len(df) > sample_size:
        df = df.sample(n=sample_size, random_state=random_state)

    if output_path:
        df.to_csv(output_path, index=False)

    return df
