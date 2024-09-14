import pandas as pd


def preprocess_data(input_filepath, output_filepath):
    
    """
    Предобрабатывает сырые данные и сохраняет обработанные.

    Args:
        input_filepath (str): Путь к сырым данным.
        output_filepath (str): Путь для сохранения обработанных данных.
    """
    
    data = pd.read_csv(input_filepath)
    
    data = data.drop_duplicates()
    data = data.dropna()
    
    data.to_csv(output_filepath)
    print(f'File saved to {output_filepath}')
    
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Предобработка сырых данных.')
    parser.add_argument('--input', type=str, required=True, help='Путь к файлу с сырыми данными.')
    parser.add_argument('--output', type=str, required=True, help='Путь для сохранения обработанных данных.')

    args = parser.parse_args()

    preprocess_data(args.input, args.output)