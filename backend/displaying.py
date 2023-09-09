import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


from collections import defaultdict
from cleaning import tumorSize, tumorSizeLabels, age, ageTumorSize

'''ALL AGES COUNT'''
def displayAll():
    tumorSizeCount = defaultdict(lambda:0, {})

    for tumor in tumorSize:
        tumorSizeCount[tumor] += 1

    tumorArr = np.array([]).astype(int)

    for tumor in tumorSizeCount:
        tumorArr = np.append(tumorArr, tumorSizeCount[tumor])

    #print(f'TumorArr: {tumorArr}')

    def display(pct, vals):
        absolute = int(pct / 100.*np.sum(vals))
        return f'{absolute}'

    explode = (0, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    fig, ax = plt.subplots()
    ax.pie(tumorArr, labels=tumorSizeLabels, autopct=lambda pct: display(pct, tumorArr), shadow=True, explode=explode)
    ax.set_title('All Ages Tumor Size Count')

    plt.show()


def displayCount(ageRange):
    tumorLabels = ageTumorSize['TumorSize'].unique()

    tumorSizeCount = defaultdict(lambda:0, {})

    print(f'AgeRange: {ageRange}')

    for index, row in ageTumorSize.iterrows():
        if (ageRange == row['Age']):
            tumorSizeCount[row['TumorSize']] += 1

    tumorArr = np.array([]).astype(int)

    for tumor in tumorSizeCount:
        tumorArr = np.append(tumorArr, tumorSizeCount[tumor])

    print(f'DisplayCount TumorArray: {tumorArr}')
    print(tumorLabels)

displayAll()
displayCount('30-39')