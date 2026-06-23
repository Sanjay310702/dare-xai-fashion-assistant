import os
import pandas as pd

def analyze_dataset():
    # Get the absolute directory where this specific script is saved
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Searching for dataset files inside: {script_dir}\n")
    
    dataset_path = None
    # Scan for any CSV or JSON metadata file in the ML-TASK folder
    for root, dirs, files in os.walk(script_dir):
        # Skip virtual environment folders so we don't look there
        if 'venv' in root or '.git' in root:
            continue
        for file in files:
            if file.endswith('.csv') or file.endswith('.json'):
                dataset_path = os.path.join(root, file)
                break
        if dataset_path:
            break
            
    if not dataset_path:
        print("Could not find a metadata file (.csv or .json) inside ML-TASK.")
        print("Let's see what directories exist here:")
        print(os.listdir(script_dir))
        return

    print(f"Found dataset at: {dataset_path}")
    print("-" * 50)
    
    # Load the data
    try:
        if dataset_path.endswith('.csv'):
            df = pd.read_csv(dataset_path, on_bad_lines='skip')
        else:
            df = pd.read_json(dataset_path)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # 1. Dataset Structure
    print(f"Dataset Shape: {df.shape[0]} rows (items) and {df.shape[1]} columns.\n")
    
    # 2. Available Metadata
    print("Available Columns (Metadata):")
    for col in df.columns:
        print(f" - {col}")
    print("\n" + "-" * 50)
    
    # 3. Data Quality (Missing Values)
    print("Missing Values per Column:")
    missing = df.isnull().sum()
    print(missing[missing > 0])
    if missing.sum() == 0:
        print("No missing values found! High quality data.")
    print("\n" + "-" * 50)
    
    # 4. Categories Overview
    potential_category_cols = ['masterCategory', 'subCategory', 'articleType', 'gender', 'usage', 'category', 'type']
    for col in potential_category_cols:
        if col in df.columns:
            print(f"Top 5 Categories in '{col}':")
            print(df[col].value_counts().head(5))
            print("\n")

if __name__ == "__main__":
    analyze_dataset()