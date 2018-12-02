#coding=utf-8

'''
@author=Wangminhao Gou
'''

import numpy as np
import csv
inputfile1=r'/Users/tianyu/PycharmProjects/DataAnalysis2/dataset/users.txt'
#inputfile2=r'/Users/tianyu/PycharmProjects/DataAnalysis2/dataset/netflix_train.txt'
inputfile3=r'/Users/tianyu/PycharmProjects/DataAnalysis2/dataset/netflix_test.txt'
outputfile=r'/Users/tianyu/PycharmProjects/DataAnalysis2/dataset/testSet.csv'
def data_gen():
    data_all=[]

    with open(inputfile1,'r') as inp1,open(inputfile3,'r') as inp3,open(outputfile,'w') as out:
        users=csv.reader(inp1,delimiter=' ', quotechar='|')
        data2 = csv.reader(inp3, delimiter=' ', quotechar='|')
        writer=csv.writer(out)
        dataTrain = []
        for line in data2:
            dataTrain.append(line)
        #print(dataTrain)
        len=0
        #dat2 = [None]
        for user in users:
            oneUser_data = [None] * 10000
            #if user[0]==dat2[0]:
                #col = int(dat[1])
                #oneUser_data[col - 1] = int(dat[2])
            for dat in dataTrain:
                if user[0]==dat[0]:
                    col=int(dat[1])
                    oneUser_data[col-1]=int(dat[2])
                    dataTrain.remove(dat)
                    len += 1
            writer.writerow(oneUser_data)
            data_all.append(oneUser_data)

    print(len)

if __name__=='__main__':
    data_gen()
