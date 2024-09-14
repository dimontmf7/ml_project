import pandas as pd
from sklearn.datasets import load_iris

def save_iris_dataset():
    
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    feature_names = iris.feature_names
    target_name = 'target'
    
    df = pd.DataFrame(X, columns=feature_names)
    df[target_name] = y
    
    df.to_csv('data/raw/iris_raw.csv', index=False)
    print("Датасет Iris сохранен в 'data/raw/iris_raw.csv'.")
    

if __name__ == "__main__":
    save_iris_dataset()


