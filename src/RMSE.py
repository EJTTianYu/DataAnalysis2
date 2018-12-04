#coding=utf-8
'''
@author=Wangminhao Gou
'''
import csv
import numpy as np
import math
inputFile1=r'E:\DataAnalysis2\dataset\trainResult.csv'
inputFile2=r'E:\DataAnalysis2\dataset\testSample.csv'


#在这里，把RMSE定位到一个用户
def RMSE():
    with open(inputFile1, 'r') as inp1:
        lines = csv.reader(inp1)
        data = []
        for line in lines:
            if (len(line) != 0):
                for k in range(0, 100):
                    line[k] = int(line[k])
                data.append(line)
        dataMat = np.array(data)
    with open(inputFile2, 'r') as inp2:
        rows = csv.reader(inp2)
        data2 = []
        for row in rows:
            if (len(row) != 0):
                for m in range(0, 100):
                    row[m] = int(row[m])
                data2.append(row)
        dataMat2 = np.array(data2)
    length=0
    total=0
    for row in range(0,100):
        for col in range(0,100):
            if(dataMat2[row][col]!=0):
                rmse=(dataMat2[row][col]-dataMat[row][col])**2
                total+=rmse
                length+=1
    return math.sqrt(total/length)


if __name__=='__main__':
    print(RMSE())
