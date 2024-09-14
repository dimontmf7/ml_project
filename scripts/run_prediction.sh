INPUT_FILE="data/processed/new_data.csv"
OUTPUT_FILE="predictions/predictions.csv"

echo "Начало предсказания модели..."
python src/models/predict.py --input $INPUT_FILE --output $OUTPUT_FILE
echo "Предсказание завершено."