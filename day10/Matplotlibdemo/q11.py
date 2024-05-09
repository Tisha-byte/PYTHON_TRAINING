import matplotlib.pyplot as plt
import seaborn as sns

sns.set_context('paper')

titanic = sns.load_dataset('titanic')
print(titanic)

sns.countplot(x='class',hue='who',data=titanic,palette='magma')
plt.title('Survivors')
plt.show()