from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

features = ['Age', 'Gender', 'TimeSpent']
features += [col for col in df.columns if 'ContentType' in col or 'Device' in col]
X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)
df['Segment'] = kmeans.fit_predict(X_scaled)

print(df[['UserID', 'Segment']])
