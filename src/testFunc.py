#coding=utf-8
'''
@author=Wangminhao Gou
'''
import numpy as np
if __name__=='__main__':
    data=[[1,1,1],[1,1,1]]
    A=np.array(data)
    B=np.array(data)
    print(np.dot(A,B.T))