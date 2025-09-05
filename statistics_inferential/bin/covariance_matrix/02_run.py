import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load covariance matrix
df_cov = pd.read_csv("/workspaces/stats-foundations-python/statistics_inferential/bin/covariance_matrix/covariance_matrix.csv", index_col=0)

# Convert to NumPy array
cov_matrix = df_cov.values

# -------------------------------
# 1️⃣ Eigen Decomposition
# -------------------------------
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Sort by descending eigenvalue
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

# -------------------------------
# 2️⃣ Visualize Eigenvalues
# -------------------------------
plt.figure(figsize=(10, 4))
plt.plot(eigenvalues, marker='o')
plt.title("Eigenvalues of Covariance Matrix")
plt.xlabel("Component Index")
plt.ylabel("Eigenvalue (Variance Explained)")
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/covariance_matrix/covariance_matrix_Eigenvalues.png")

# -------------------------------
# 3️⃣ Visualize Top Eigenvector
# -------------------------------
top_eigenvector = eigenvectors[:, 0]
plt.figure(figsize=(10, 4))
sns.barplot(x=df_cov.columns, y=top_eigenvector)
plt.xticks(rotation=90)
plt.title("Top Eigenvector (Principal Portfolio Direction)")
plt.ylabel("Weight")
plt.tight_layout()
plt.show()
plt.savefig("/workspaces/stats-foundations-python/statistics_inferential/bin/covariance_matrix/covariance_matrix_Eigenvector.png")
