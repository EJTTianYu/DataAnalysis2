#coding=utf-8
'''
@author=Wangminhao Gou
'''

import csv
inputFile=r'E:\DataAnalysis2\dataset\trainSet.csv'
outputFile=r'E:\DataAnalysis2\dataset\trainSet2.csv'
def datafill():
    with open(inputFile,'r') as inp1,open(outputFile,'w',newline='') as out1:
        rows=csv.reader(inp1)

        writer=csv.writer(out1,dialect='excel')
        for row in rows:
            for i in range(0,len(row)):
                if row[i]=='':
                    row[i]=0
            writer.writerow(row)

if __name__=='__main__':
    datafill()