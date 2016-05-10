import sys
from copy import deepcopy
from random import randint
In=str(sys.argv[1])
def V(n,f=10,t=14):
 n=str(n);z=0;s='';d='0123456789';d1='N123ABCXYZRTFU'
 for i in n:z=z*f+d.index(i)
 while z:z,m=divmod(z,t);s=d1[m]+s
 while len(s)<3:s='N'+s
 return s
In=In.split(';')
number=In[0:3]
players=In[3:]
for x in range(0,len(players)):players[x]=players[x].split('_')
for x in players:
 if number[1] in x[0]:self=x
for x in range(0,len(players)):
 for y in range(0,len(players[x])):
  players[x][y]=int(players[x][y])
for x in range(0,len(number)):number[x]=int(number[x])
Pos=list(map(V,range(0,14**3)))
B=[]
C=[]
P1=deepcopy(players)
N1=deepcopy(number)
for x in range(len(Pos)):
    P=True
    y=Pos[x]
    if '1A'in y or '2B'in y or '3C'in y or 'FU'in y or 'A1'in y or 'B2'in y or 'C3'in y or 'UF'in y:
            P=False#stupid check
    if P:#legality check
        z=0
        players=deepcopy(P1)
        number=deepcopy(N1)
        for x in players:
            if str(number[1]) in str(x[0]):self=x
        for w in range(0,3):
            if y[w] in '3':
                if int(number[2])<3:P=False;break
                else:z-=3;self[3]+=3;number[2]-=3
            if y[w] in '2':
                if int(number[2])<2:P=False;break
                else:z-=2;self[3]+=2;number[2]-=2
            if y[w] in '1':
                if int(number[2])<1:P=False;break
                else:z-=1;self[3]+=1;number[2]-=1
            if y[w] in 'A':
                if int(self[3])<1:P=False;break
                else:z+=1;self[3]-=3;number[2]+=3
            if y[w] in 'B':
                if int(self[3])<2:P=False;break
                else:z+=2;self[3]-=2;number[2]+=2
            if y[w] in 'C':
                if int(self[3])<3:P=False;break
                else:z+=3;self[3]-=1;number[2]+=1
            if y[w] in 'X':
                if int(self[3])<1:P=False;break
                else:self[3]-=1
            if y[w] in 'Y':
                if int(self[3])<2:P=False;break
                else:self[3]-=2
            if y[w] in 'Z':
                if int(self[3])<3:P=False;break
                else:self[3]-=3
            if y[w] in 'F':
                if int(self[3])<1:P=False;break
                else:z+=2;self[3]-=1;self[2]+=1
            if y[w] in 'U':
                if int(self[3])<1:P=False;break
                else:z-=2;self[3]+=1;self[2]-=1
            if y[w] in 'R':
                self[2:4]=players[(players.index(self)+1)%len(players)][2:4]
                z+=int(self[3])*-1
                z+=int(self[2])*2
            if y[w] in 'T':
                self[2:4]=players[(players.index(self)-1)%len(players)][2:4]
                z+=int(self[3])*-1
                z+=int(self[2])*2
    if P:
        C.append(z);B.append((z,y))
c=list(set(C))[::-1][1];D=[]
for x in B:
    if c in x:D.append(x)
print(D[randint(0,len(D)-1)][1])