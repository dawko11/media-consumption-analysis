import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(df['TimeSpent'], bins=20)
plt.title('Rozkład czasu spędzonego na konsumpcji mediów')
plt.xlabel('Czas (minuty)')
plt.ylabel('Liczba użytkowników')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='TimeSpent', data=df)
plt.title('Czas spędzony na konsumpcji mediów według płci')
plt.xlabel('Płeć')
plt.ylabel('Czas (minuty)')
plt.show()
