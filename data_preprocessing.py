print(df.isnull().sum())

df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df = pd.get_dummies(df, columns=['ContentType', 'Device'], drop_first=True)
