import numpy as np
import pandas as pd
data = pd.DataFrame({'Height': [160, 165, 170, 175, 180], 'Weight': [60, 65, 70, 75, 80]})
corr = np.corrcoef(data['Height'], data['Weight'])[0, 1]
print(f"Correlation Coefficient: {corr:.2f}")