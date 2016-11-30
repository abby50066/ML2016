# coding: utf-8
from __future__ import print_function
import sys

'''
print ('參數個數為：', len(sys.argv), '個參數。')
print ('參數列表：', str(sys.argv))
'''

num = int(sys.argv[2])+1

def main():
    with open(sys.argv[1], 'r') as inFile:
        for i in range(0, num):
            line = inFile.readline()
        numList = line.split(' ')
        arr = list()
        
        for i in range(1,len(numList)):
            arr.append(float(numList[i].split('\n')[0]))
        arr.sort()
        with open('ans1.txt', 'w') as outFile:
            for i in arr:
                outFile.write(str(i) + ' ')
            outFile.write('\n')
main()
