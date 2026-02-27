import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Convert the dataset to a pandas DataFrame for easier visualization
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df["species"] = iris.target
iris_df["species"] = iris_df["species"].map(
    {0: "setosa", 1: "versicolor", 2: "virginica"}
)

# Use a more distinct palette
custom_palette = sns.color_palette("Set2", n_colors=3)

# Scatter plot: Sepal length vs Sepal width
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=iris_df,
    x="sepal length (cm)",
    y="sepal width (cm)",
    hue="species",
    palette=custom_palette,
)
plt.title("Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.legend(title="Species")
plt.show()

# Pair plot for all features
sns.pairplot(
    iris_df, hue="species", palette=custom_palette, diag_kind="kde", corner=True
)
plt.suptitle("Pair Plot of Iris Features", y=1.02)
plt.show()

# Violin plot for petal length across species
plt.figure(figsize=(8, 6))
sns.violinplot(data=iris_df, x="species", y="petal length (cm)", palette=custom_palette)
plt.title("Distribution of Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()
