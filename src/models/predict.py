import joblib
from src.data.data_loader import load_data
from src.features.feature_engineering import create_features
from src.models.predict_model import predict

def run_prediction(input_filepath, output_filepath):
    """
    Запускает процесс предсказания.

    Args:
        input_filepath (str): Путь к входным данным.
        output_filepath (str): Путь для сохранения предсказаний.
    """
    model = joblib.load('models/gb_model.pkl')
    print('Модель загружена')
    
    data = load_data(input_filepath)
    data_processed = create_features(data)
    print("Данные загружены и предобработаны")
    
    X_new = data_processed
    predictions = predict(X_new)
    
    output = data.copy()
    output['prediction'] = predictions
    output.to_csv(output_filepath, index=False)
    print(f"Предсказания сохранены в '{output_filepath}'")
    
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Запуск предсказания модели.')
    parser.add_argument('--input', type=str, required=True, help='Путь к входному файлу с данными.')
    parser.add_argument('--output', type=str, required=True, help='Путь для сохранения предсказаний.')

    args = parser.parse_args()

    run_prediction(args.input, args.output)
    