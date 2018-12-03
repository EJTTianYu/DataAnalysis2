#coding=utf-8
'''
@author=Wangminhao Gou
'''
import numpy as np
from pandas import read_csv
import csv

inputFile=r'E:\DataAnalysis2\dataset\trainSample.csv'
inputFile2=r'E:\DataAnalysis2\dataset\testSample.csv'
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
        print(dataMat[0][1])
        x=dataMat[i]
        #print(np.linalg.norm(x))
        #y=dataMat[i]
        #print(np.dot(x,y))
        sum_score=0
        sum_sim=0
    if(dataMat[i][j]==0):
        for user in range(0,100):
            if user!=i:
                #只有当其他用户的该项值不为0才具有预测价值
                if dataMat[user][j]!=0:
                    y=dataMat[user]
                    sim=np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))
                    sum_sim+=sim
                    sum_score+=sim*dataMat[user][j]
    else:
        print('该用户已对电影打分')
    return i,j,sum_score/sum_sim
#在这里，把RMSE定位到一个用户
def RMSE(i,j,ts):
    sum_error=0
    with open(inputFile2,'r') as inp2:
        lines=csv.reader(inp2)
        data = []
        for line in lines:
            if (len(line) != 0):
                for k in range(0, 100):
                    line[k] = int(line[k])
                data.append(line)
        dataMat = np.array(data)
        sum_error=abs(dataMat[i][j]-ts)
    return sum_error

if __name__=='__main__':
    i,j,ts=colla_filter(1,1)
    print(RMSE(i,j,ts))