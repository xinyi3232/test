# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n=eval(input('请输入:'))
s=1
t=1
for i in range(1,n):
    t=-t*(2*i)*(2*i+1)
    s=s+t
print(s)
##################    ##################
for i in range(1,10):
    for j in range(1,i+1):
        r=i*j
        print('%d*%d=%d'%(j,i,r),end=' ')
    print(' ')
#################     ##################
L=[3,6,4,8,5]
L.sort()
print(L)
#################      ##################
F=[i**2 for i in range(1,1000,2)]
print(F)
#########################################
import numpy as np
A = np.linspace(-1,1, 5)
print(A)
#########################################
a = {'数学':95}
a['语文'] = 89 #添加新键值对
a['英语'] = 90
del a['数学']
a['语文'] = 100
print(a)
########################################
names=['张三','李四','李四','王武','张三','李四']
a=0
b=0
c=0
for i in names:
    if i=='张三':
        a=a+1
    elif i=='李四':
        b=b+1
    elif i=='王武':
        c=c+1
dic=dict(张三=a,李四=b,王武=c)
print(dic)
######################################
str4="python.biancheng.net"
#找出最大的字符
print(max(str4))
#找出最小的字符
print(min(str4))
#对字符串中的元素进行排序
print(sorted(str4))
###################################
str1='acfshtdbe'
sorted(str1)
####################################
def print1(): 
	print("这是第一个函数") 
def print2(): 
	print("这是定义的第二个函数") 
	print1() #在print2()中调用print1() 
print2()
########################################
def move(n,a,b,c):
    if n == 1: 
        print(a,"--->",c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

n=10
move(n,"A","B","C")
#########################################
n=eval(input())
def f(n):
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        return f(n-1)+f(n-2)
print(f(n))
##########################################
n=eval(input())
a,b=1,1
for i in range(n):
    a,b=b,a+b
print(a)
##########################################
import math
Q=[]
h=30
c=50
D=input().split(',')
D=[int(i) for i in D]
for i in D:
    q=str(int(math.sqrt((2*c*i)/h)))
    Q.append(q)
Q=','.join(Q)
print(Q)
#########################################
import numpy as np
np.random.seed(17)
n= int(input())
m = int(input())
a = np.random.randint(1,100,size=(n,m))
for i in range(n):
    for j in range(m):
        if i==0 or i==n-1 or j==0 or j==m-1:
            s=s+a[i][j]
print(s)
###########################################
import numpy as np
a=eval(input())
b=eval(input())
#创建数组使其元素为整数
arr=np.arange(1,13,1)
print(arr)
#改变数组形状为3行4列的二维数组
arr1=arr.reshape(3,4)
print(arr1)
#将数组中值小于3或大于9的元素值设为0
arr1[(arr1<a)|(arr1>b)]=0
print(arr1)
#选取数组的第一列和最后一列输出
print(arr1[:,[0,-1]])
######################################
for i in range(1, 10):
    print ()
    for j in range(1, i+1):
        print("%d*%d=%d"%(j, i, i*j),end="  ")
####################################
employee_dict = {'name':['david','brain'] , 'dept':['ops', 'auto'] , 'salary': [12000,13000]}