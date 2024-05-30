import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)

    # Supprimer les lignes avec des valeurs nulles
    df = df.dropna()

    # Convertir les colonnes à des types appropriés
    df['date'] = pd.to_datetime(df['date'])
    df['value'] = df['value'].astype(float)

    # Supprimer les doublons
    df = df.drop_duplicates()

    return df

if __name__ == "__main__":
    cleaned_df = clean_data('path/to/your/data.csv')
    print(cleaned_df.head())
