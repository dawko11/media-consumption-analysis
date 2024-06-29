import pandas as pd
import numpy as np

data = {
    'UserID': range(1, 101),
    'Age': np.random.randint(18, 65, size=100),
    'Gender': np.random.choice(['Male', 'Female'], size=100),
    'TimeSpent': np.random.randint(5, 300, size=100), 
    'ContentType': np.random.choice(['News', 'Sports', 'Entertainment', 'Education'], size=100),
    'Device': np.random.choice(['Mobile', 'Desktop', 'Tablet'], size=100)
}

df = pd.DataFrame(data)

df.to_csv('data/fake_media_consumption.csv', index=False)

print("Fikcyjne dane zostały wygenerowane i zapisane w pliku 'data/fake_media_consumption.csv'.")
