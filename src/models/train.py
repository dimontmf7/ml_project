import joblib
from src.data.data_loader import load_data
from src.data.split_data import split_data
from src.features.feature_engineering import create_features
from src.models.train_model import train_model

def run_training():
    """
    Запускает процесс обучения модели.
    """
    
    data = load_data('datasets/processed/processed_data.csv')
    data = create_features(data)
    
    X = data.drop('target', axis=1)
    y = data['target']
    
    X_train, X_val, y_train, y_val = split_data(X, y)
    
    model = train_model(X_train, y_train)
    
    score = model.score(X_val, y_val)
    print(f"Validation Accuracy: {score:.2f}")
    
    joblib.dump(model, 'models/gb_model.pkl')
    print("Модель сохранена в 'models/gb_model.pkl'.")
    
if __name__ == "__main__":
    run_training()