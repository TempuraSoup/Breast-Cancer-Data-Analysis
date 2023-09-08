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


from collections import defaultdict

df = pd.read_csv('backend/assets/data/breast-cancer.data', header=None, names=["Class", "Age", "Menopause", "TumorSize", "Inv-Nodes", "Node-Caps", "Deg-Malig", "Breast", "breast-Quad", "Irrdiat"])

age = df.loc[:, "Age"].sort_values()

tumorSize = df.loc[:, "TumorSize"].sort_values()

ageTumorSize = df.loc[:, ["Age", "TumorSize"]].sort_values("Age")

print(ageTumorSize)

tumorSizeLabels = tumorSize.unique()

print(f'TumorSizeLabels: {tumorSizeLabels}')

#dict = {'0-4': 0, '5-9':0, '10-14':0, '15-19':0, '20-24': 0, '25-29':0, '30-34': 0, '35-39':0, '40-44':0, '45-49':0, '50-54':0, '55-59':0}




'''
plt.bar(age, tumorSize, color="red")

plt.xlabel("Age")
plt.ylabel("Tumor Size")
plt.title("Age vs Tumor Size")
plt.show()
'''
