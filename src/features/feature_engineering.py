import pandas as pd

def create_features(data):
    """
    Выполняет инженеринг признаков для датасета Iris.

    Args:
        data (pd.DataFrame): Входные данные.

    Returns:
        pd.DataFrame: Данные с новыми признаками.
    """
    data['sepal_ratio'] = data['sepal lengthcm)'] / data['sepal width (cm)']
    
    return data