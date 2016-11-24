# coding:utf-8
import pandas as pd
import csv
from sklearn import linear_model


def get_data(file_name):
    data = pd.read_csv(file_name)
    x = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]

    csvfile = file('outcome.csv', 'wb')
    writer = csv.writer(csvfile)

    for id,type,x1,x2,x3,x4,x5,x6,x7,x8,x9 in \
            zip(data['id'],data['type'],data['1'],data['2'],data['3'],data['4'],data['5']\
            ,data['6'],data['7'],data['8'],data['9']):
        if type == "PM25":
            y = []
            y.append(float(x1))
            y.append(float(x2))
            y.append(float(x3))
            y.append(float(x4))
            y.append(float(x5))
            y.append(float(x6))
            y.append(float(x7))
            y.append(float(x8))
            y.append(float(x9))

            regr = linear_model.LinearRegression()
            regr.fit(x, y)
            predict_outcome = regr.predict(10)
            # print id,predict_outcome[0]
            # The results generated excel
            writer.writerow([id, int(round(predict_outcome[0]))])

    csvfile.close()


get_data("test_X.csv")