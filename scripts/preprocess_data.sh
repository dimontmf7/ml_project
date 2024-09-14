INPUT_FILE = "data/raw/iris_raw.csv"
OUTPUT_FILE="data/processed/processed_data.csv"

echo "Начало предобработки данных..."
python src/data/preprocess_data.py --input $INPUT_FILE --output $OUTPUT_FILE
echo "Предобработка завершена."