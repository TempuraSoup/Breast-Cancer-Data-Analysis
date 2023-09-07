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

tumorSizeLabels = tumorSize.unique()
#tumorSizeLabels = tumorSize.sort_values().unique()

print(f'TumorSizeLabels: {tumorSizeLabels}')

#dict = {'0-4': 0, '5-9':0, '10-14':0, '15-19':0, '20-24': 0, '25-29':0, '30-34': 0, '35-39':0, '40-44':0, '45-49':0, '50-54':0, '55-59':0}

tumorSizeCount = defaultdict(lambda:0, {})

for tumor in tumorSize:
    tumorSizeCount[tumor] += 1

tumorArr = np.array([]).astype(int)

for tumor in tumorSizeCount:
    tumorArr = np.append(tumorArr, tumorSizeCount[tumor])

print(f'TumorArr: {tumorArr}')

def display(pct, vals):
    absolute = int(pct / 100.*np.sum(vals))
    return f'{absolute}'

explode = (0, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots()
ax.pie(tumorArr, labels=tumorSizeLabels, autopct=lambda pct: display(pct, tumorArr), shadow=True, explode=explode)
ax.set_title('Yo Mama')

plt.show()

'''
plt.bar(age, tumorSize, color="red")

plt.xlabel("Age")
plt.ylabel("Tumor Size")
plt.title("Age vs Tumor Size")
plt.show()
'''
