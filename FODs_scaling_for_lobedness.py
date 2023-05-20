#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
data1=np.genfromtxt('data1.txt', delimiter='\t')
# data1 is FODs position
data2=np.genfromtxt('data2.txt', delimiter='\t')
# data 2 is nuclear position other than hydrogen
data3=np.genfromtxt('data3.txt', delimiter='\t')
#data3 is hydrogen nuclear position
nonHatom=1; Hatom=4; t =0.05; s =0.5; #t is tolerance and s is scale
A=np.zeros(len(data2))
B=np.zeros(len(data3))

for i in range(len(data1)):
   
    for j in range(0, nonHatom):
        A[j]=math.sqrt(pow(data1[i][0]-data2[j][0],2)+pow(data1[i][1]-data2[j][1],2)+pow(data1[i][2]-data2[j][2],2))*0.529177
    x=min(A)
    if(x < 2.5):
            p=0;q=0;r=0;l=0;
            for j in range(0, nonHatom):
                
                if(abs(A[j]-x) < t):
                    p=p + data2[j][0]
                    q=q + data2[j][1]
                    r=r + data2[j][2]
                    l=l+1
            if(l > 1):
                data1[i][0]=s*(data1[i][0] + (0.5*p))
                data1[i][1]=s*(data1[i][1] + (0.5*q))
                data1[i][2]=s*(data1[i][2] + (0.5*r))
            else:
                for k in range(len(A)):
                    if(A[k] == x):
                        m=k
                        data1[i][0]=s*(data1[i][0] + data2[m][0])
                        data1[i][1]=s*(data1[i][1] + data2[m][1])
                        data1[i][2]=s*(data1[i][2] + data2[m][2])
                    
    else:
        for j in range(0, Hatom):
            B[j]=math.sqrt(pow(data1[i][0]-data3[j][0],2)+pow(data1[i][1]-data3[j][1],2)+pow(data1[i][2]-data3[j][2],2))*0.529177
        y=min(B)
        if(y < 2.5):
            p=0;q=0;r=0;l=0;
            for j in range(0, Hatom):
                if(abs(B[j]-y) < t):
                    p=p + data3[j][0]
                    q=q + data3[j][1]
                    r=r + data3[j][2]
                    l=l+1
                if(l > 1):
                    data1[i][0]=s*(data1[i][0] + (0.5*p))
                    data1[i][1]=s*(data1[i][1] + (0.5*q))
                    data1[i][2]=s*(data1[i][2] + (0.5*r))
                else:
                    for k in range(len(B)):
                        if(B[k] == x):
                            m=k
                            data1[i][0]=s*(data1[i][0] + data3[m][0])
                            data1[i][1]=s*(data1[i][1] + data3[m][1])
                            data1[i][2]=s*(data1[i][2] + data3[m][2])
np.savetxt('FODs_Final_C2H2O2.txt',data1,fmt='%.11f')  
# FODs final is final FODs for lobedness calculations


# In[2]:


i=0
for j in range(0, nonHatom):
        A[j]=math.sqrt(pow(data1[i][0]-data2[j][0],2)+pow(data1[i][1]-data2[j][1],2)+pow(data1[i][2]-data2[j][2],2))*0.529177


# In[3]:


A[0]


# In[ ]:




