#coding=utf-8
'''
@author=Wangminhao Gou
'''
import csv
import numpy as np
from math import *
def read_data(inputFile):
    with open(inputFile,'r') as inp1:
        lines=csv.reader(inp1)
        data=[]
        for line in lines:
            if (len(line)!=0):
                for k in range(0,100):
                    line[k]=int(line[k])
                data.append(line)
        dataMat=np.array(data)
    return dataMat
def direct_mat(inputFile):
    with open(inputFile,'r') as inp1:
        lines=csv.reader(inp1)
        data=[]
        for line in lines:
            if (len(line)!=0):
                for k in range(0,100):
                    line[k] = int(line[k])
                    if(line[k]==0):
                        pass
                    else:
                        line[k]=1
                data.append(line)
        dataMat=np.array(data)
    return dataMat
def gen_UV(siz,k):
    U=np.random.random(size=(siz,k))
    V=np.random.random(size=(k,siz))
    return U,V
'''
def norm_Fro(Matr):
    sum=0
    row_num=Matr.shape[0]
    col_num=Matr.shape[1]
    for i in range(0,row_num):
        for j in range(0,col_num):
            sum+=Matr[i][j]**2
    return sqrt(sum)
    '''
def cal_j(A,X,U,V,p):
    J=1/2*np.linalg.norm(A*(X-np.dot(U,V)),ord='fro')+p*np.linalg.norm(U,ord='fro')+p*np.linalg.norm(V,ord='fro')
    return J
def cal_der_U(A,X,U,V,p):
    der_U=(A*(np.dot(U,V)-X))*V+2*p*U
    return der_U
def ALG_matrix_com():
    pass
    #while (1/2)

if __name__=='__main__':
    inputFile1=r'E:\DataAnalysis2\dataset\trainSample.csv'
    #公式中的X
    data=read_data(inputFile1)
    #公式中的A
    data_direct=direct_mat(inputFile1)
    #print(data)
    #print(data_direct)
    U,V=gen_UV(100,10)
    #print(U*U)
    #print(type(U))
    J=cal_j(data_direct,data,U,V,0.1)
    der_U=cal_der_U(data_direct,data,U,V,0.1)
    print(J)
    #print(np.linalg.norm(U,ord='fro'))