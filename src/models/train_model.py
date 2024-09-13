from sklearn.ensemble import GradientBoostingClassifier

def train_model(X_train, y_train) -> GradientBoostingClassifier:
    
    model = GradientBoostingClassifier(
        random_state=1337
        )
    model.fit(X_train, y_train)
    return model