# coding:utf-8
import pandas as pd
import csv
from sklearn import linear_model
import numpy as np


def get_data(file_name):
    data = pd.read_csv(file_name)
    x = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
    rate = 0.001


    # csvfile = file('outcome.csv', 'wb')
    # writer = csv.writer(csvfile)

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

            theta = [np.random.normal(), np.random.normal()]
            last_l = 0;

            while True:
                current_l = 0
                diff = [0, 0]  # 偏微分

                for x_i, y_i in zip(x, y):
                    y_f = theta[0] + theta[1] * x_i[0]
                    y_l = pow((y_i - y_f), 2)
                    current_l = current_l + y_l
                    diff[0] += 2 * (y_i - y_f) * -1
                    diff[1] += 2 * (y_i - y_f) * -x_i[0]

                # if iter > max_iter:
                if ((current_l >= last_l and last_l != 0)):
                    break
                else:
                    last_l = current_l

                    # 梯度下降求新的theta
                    theta[0] = theta[0] - rate * diff[0]
                    theta[1] = theta[1] - rate * diff[1]

            print id,(theta[0] + theta[1] * 10)

    # csvfile.close()


get_data("test_X.csv")