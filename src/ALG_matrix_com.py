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
    U=np.random.rand(siz,k)
    V=np.random.rand(siz,k)
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
    J=1/2*((np.linalg.norm(A*(X-np.dot(U,V.T)),ord=None))**2)+p*((np.linalg.norm(U,ord=None))**2)+p*((np.linalg.norm(V,ord=None))**2)
    return J
def cal_der_U(A,X,U,V,p):
    der_U=np.dot((A*((np.dot(U,V.T)-X))),V)+2*p*U
    return der_U
def cal_der_V(A,X,U,V,p):
    der_V=np.dot((A*((np.dot(U,V.T)-X))).T,U)+2*p*V
    return der_V
def ALG_matrix_com(data_direct,data,U,V,p,RATE):
    while 1:
        J_initial=cal_j(data_direct,data,U,V,p)
        #print(J_initial)
        tmp=U
        U=U-RATE*cal_der_U(data_direct,data,U,V,p)
        #print(tmp)
        #print(U)
        V=V-RATE*cal_der_V(data_direct,data,tmp,V,p)
        J=cal_j(data_direct,data,U,V,p)
        if(abs(J-J_initial)<0.000001):
            break
    return U,V

if __name__=='__main__':
    inputFile1=r'E:\DataAnalysis2\dataset\trainSample.csv'
    #公式中的X
    data=read_data(inputFile1)
    #公式中的A
    data_direct=direct_mat(inputFile1)
    #print(data)
    #print(data_direct)
    U,V=gen_UV(100,10)
    U,V=ALG_matrix_com(data,data_direct,U,V,0.01,0.001)
    print(np.dot(U,V.T))
    #print(type(U))
    #J=cal_j(data_direct,data,U,V,0.1)
    #der_U=cal_der_U(data_direct,data,U,V,0.1)
    #print(der_U)
    #der_V=cal_der_V(data_direct,data,U,V,0.1)
    #print(der_V)
    #print(np.linalg.norm(U,ord='fro'))