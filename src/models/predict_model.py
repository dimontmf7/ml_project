def predict_model(model, X):
    """
    Делает предсказания на основе модели и данных.

    Args:
        model: Обученная модель.
        X (pd.DataFrame): Данные для предсказания.

    Returns:
        np.ndarray: Предсказания.
    """
    prediction = model.predict(X)
    return prediction