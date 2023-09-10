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

print(age.unique())

tumorSize = df.loc[:, "TumorSize"].sort_values()

ageTumorSize = df.loc[:, ["Age", "TumorSize"]].sort_values("Age")

tumorSizeLabels = tumorSize.unique()

