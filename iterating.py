#!/usr/bin/python3

#Given a number N, how to generate the all the unique (0,1), (0,2)....(N-2,N-1) sets?
#for example: 4 ~ (0,1),(0,2),(0,3),(1,2),(2,3),(2,3)

Num=5
tupleList=[]

for i in range(0,Num-1):
  for j in range(i+1,Num-1):
    tupleList.append((i,j))

print(tupleList)
