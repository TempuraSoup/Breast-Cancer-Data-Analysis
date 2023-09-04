'''
    numpy
    matplotlib
    pandas
    skilearn
    flask
    flask-cors
'''
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('backend/assets/data/breast-cancer.data', header=None, names=["Class", "Age", "Menopause", "TumorSize", "Inv-Nodes", "Node-Caps", "Deg-Malig", "Breast", "breast-Quad", "Irrdiat"])

age = df.loc[:, "Age"].sort_values()

tumorSize = df.loc[:, "TumorSize"]

tumorSizeLabels = tumorSize.sort_values().unique()

print(tumorSizeLabels)

dict = {'30-34': 0, '20-24': 0}

print(dict)

for tumor in tumorSize:
    print(tumor)
    dict[tumor] += 1

print(dict)


'''
plt.bar(age, tumorSize, color="red")

plt.xlabel("Age")
plt.ylabel("Tumor Size")
plt.title("Age vs Tumor Size")
plt.show()
'''
