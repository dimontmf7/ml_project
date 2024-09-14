from sklearn.model_selection import train_test_split

def split_data(X, y, test_size=0.2, random_state=1337):
    """
    Разделяет данные на обучающую и валидационную выборки.

    Args:
        X (pd.DataFrame): Признаки.
        y (pd.Series): Целевая переменная.
        test_size (float): Доля данных для валидации.
        random_state (int): Фиксирует рандомизацию.

    Returns:
        tuple: X_train, X_val, y_train, y_val
    """    
    X_train, x_val, y_train, y_val = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )
    
    return X_train, x_val, y_train, y_val