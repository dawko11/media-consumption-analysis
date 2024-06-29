import pandas as pd

df = pd.read_csv('data/fake_media_consumption.csv')

print(df.isnull().sum())

df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df = pd.get_dummies(df, columns=['ContentType', 'Device'], drop_first=True)

df.to_csv('data/processed_media_consumption.csv', index=False)

print("Dane zostały przetworzone i zapisane w pliku 'data/processed_media_consumption.csv'.")

