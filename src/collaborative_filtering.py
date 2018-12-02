#coding=utf-8
'''
@author=Wangminhao Gou
'''
import numpy as np
from pandas import read_csv
import csv

inputFile=r'E:\DataAnalysis2\dataset\trainSample.csv'

#对第i个用户对第j部电影打分的预测
def colla_filter(i,j):
    #获得数据矩阵
    with open(inputFile,'r') as inp1:
        lines=csv.reader(inp1)
        data=[]
        for line in lines:
            if (len(line)!=0):
                for k in range(0,100):
                    line[k]=int(line[k])
                data.append(line)
        dataMat=np.array(data)
        print(dataMat[0][0])
    if(dataMat[i-1][j-1]==0):
        pass
    else:
        print('该用户已对电影打分')


if __name__=='__main__':
    colla_filter(1,1)