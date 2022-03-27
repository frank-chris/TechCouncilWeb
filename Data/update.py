import pandas as pd


def collectData(filepath):
    data = dict()
    df = pd.read_excel(filepath)

    for index, row in df.iterrows():
        for info in ['img', 'name', 'pos', 'email', 'phone']:
            data['member_' + str(index+1) + '_' + info] = row[info]

    return data


def createJS(data):
    newJSFile = open("team_data.js", "w")
    newJSFile.write("var data = " + str(data) + ";")


createJS(collectData('team_data.xlsx'))