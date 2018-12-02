#coding=utf-8

import csv
inputFile=r'E:\DataAnalysis2\dataset\trainSet2.csv'
outputFile=r'E:\DataAnalysis2\dataset\trainSample.csv'
def sapmle_gen():
    with open(inputFile,'r') as inp1,open(outputFile,'w',newline='') as out1:
        lines=csv.reader(inp1)
        writer=csv.writer(out1)
        i=200
        for line in lines:
            if i>0:
                data=line[0:100]
            else:
                break
            writer.writerow(data)
            i-=1
sapmle_gen()


