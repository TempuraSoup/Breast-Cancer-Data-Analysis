import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


from collections import defaultdict
import backend.cleaning as clean

import io
import base64


def display(pct, vals):
        absolute = int(pct / 100.*np.sum(vals))
        return f'{absolute}'

'''ALL AGES COUNT'''
def displayAll():
    tumorSizeCount = defaultdict(lambda:0, {})

    for tumor in clean.tumorSize:
        tumorSizeCount[tumor] += 1

    tumorArr = np.array([]).astype(int)

    for tumor in tumorSizeCount:
        tumorArr = np.append(tumorArr, tumorSizeCount[tumor])

    #print(f'TumorArr: {tumorArr}')


    explode = (0, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    fig, ax = plt.subplots()
    ax.pie(tumorArr, labels=clean.tumorSizeLabels, autopct=lambda pct: display(pct, tumorArr), shadow=True, explode=explode)
    ax.set_title('All Ages Tumor Size Count')



def displayCount(ageRange):
    tumorLabels = np.array([])

    for index, row in clean.ageTumorSize.iterrows():
         if (row['Age'] == ageRange and not np.isin(tumorLabels, row['TumorSize']).any()):
              tumorLabels = np.append(tumorLabels, row['TumorSize'])

    tumorSizeCount = defaultdict(lambda:0, {})

    print(f'AgeRange: {ageRange}')

    for index, row in clean.ageTumorSize.iterrows():
        if (ageRange == row['Age']):
            tumorSizeCount[row['TumorSize']] += 1

    tumorArr = np.array([]).astype(int)

    for tumor in tumorSizeCount:
        tumorArr = np.append(tumorArr, tumorSizeCount[tumor])

    print(f'DisplayCount TumorArray: {tumorArr}')
    print(tumorLabels)



    fig, ax = plt.subplots()
    ax.pie(tumorArr, labels=tumorLabels, autopct=lambda pct: display(pct, tumorArr), shadow=True)
    ax.set_title(f'{ageRange} Tumor Size Count')


def plotToImg(ageRange):
    if (ageRange == 'All Ages'):
        displayAll()
    else:
        displayCount(ageRange)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    img_b64 = base64.b64encode(img.getvalue()).decode()

    return img_b64