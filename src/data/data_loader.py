import pandas as pd

def load_data(filepath):
    """

    Returns:
        data: pd.DataFrame
    """
    data = pd.read_csv(filepath)
    return data