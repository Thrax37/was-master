import sys
file=sys.argv[0].split('\\')[::-1][0]
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
P1=deepcopy(players)
N1=deepcopy(number)
for x in range(len(Pos)):
    P=True
    y=Pos[x]
    if '1A'in y or '2B'in y or '3C'in y or 'FU'in y or 'A1'in y or 'B2'in y or 'C3'in y or 'UF'in y:
            P=False
    if P:
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
        B.append(y)
Pos=list(B)
B=[]
#
C=[['NNN', 0], ['NN1', -1], ['NN2', -2], ['NN3', -3], ['NNR', -6], ['NNT', -1], ['N1N', -1], ['N11', -2], ['N12', -3], ['N13', -4], ['N1X', -1], ['N1R', -7], ['N1T', -2], ['N1F', 1], ['N1U', -3], ['N2N', -2], ['N21', -3], ['N22', -4], ['N23', -5], ['N2A', -1], ['N2X', -2], ['N2Y', -2], ['N2R', -8], ['N2T', -3], ['N2F', 0], ['N2U', -4], ['N3N', -3], ['N31', -4], ['N32', -5], ['N33', -6], ['N3A', -2], ['N3B', -1], ['N3X', -3], ['N3Y', -3], ['N3Z', -3], ['N3R', -9], ['N3T', -4], ['N3F', -1], ['N3U', -5], ['NRN', -6], ['NR1', -7], ['NR2', -8], ['NR3', -9], ['NRA', -5], ['NRB', -4], ['NRC', -3], ['NRX', -6], ['NRY', -6], ['NRZ', -6], ['NRR', -12], ['NRT', -7], ['NRF', -4], ['NRU', -8], ['NTN', -1], ['NT1', -2], ['NT2', -3], ['NT3', -4], ['NTA', 0], ['NTX', -1], ['NTR', -7], ['NTT', -2], ['NTF', 1], ['NTU', -3], ['1NN', -1], ['1N1', -2], ['1N2', -3], ['1N3', -4], ['1NA', 0], ['1NX', -1], ['1NR', -7], ['1NT', -2], ['1NF', 1], ['1NU', -3], ['11N', -2], ['111', -3], ['112', -4], ['113', -5], ['11B', 0], ['11X', -2], ['11Y', -2], ['11R', -8], ['11T', -3], ['11F', 0], ['11U', -4], ['12N', -3], ['121', -4], ['122', -5], ['123', -6], ['12A', -2], ['12C', 0], ['12X', -3], ['12Y', -3], ['12Z', -3], ['12R', -9], ['12T', -4], ['12F', -1], ['12U', -5], ['13N', -4], ['131', -5], ['132', -6], ['133', -7], ['13A', -3], ['13B', -2], ['13X', -4], ['13Y', -4], ['13Z', -4], ['13R', -10], ['13T', -5], ['13F', -2], ['13U', -6], ['1XN', -1], ['1X1', -2], ['1X2', -3], ['1X3', -4], ['1XR', -7], ['1XT', -2], ['1RN', -7], ['1R1', -8], ['1R2', -9], ['1R3', -10], ['1RA', -6], ['1RB', -5], ['1RC', -4], ['1RX', -7], ['1RY', -7], ['1RZ', -7], ['1RR', -13], ['1RT', -8], ['1RF', -5], ['1RU', -9], ['1TN', -2], ['1T1', -3], ['1T2', -4], ['1T3', -5], ['1TA', -1], ['1TX', -2], ['1TR', -8], ['1TT', -3], ['1TF', 0], ['1TU', -4], ['1FN', 1], ['1F1', 0], ['1F2', -1], ['1F3', -2], ['1FR', -5], ['1FT', 0], ['1UN', -3], ['1U1', -4], ['1U2', -5], ['1U3', -6], ['1UA', -2], ['1UB', -1], ['1UX', -3], ['1UY', -3], ['1UR', -9], ['1UT', -4], ['1UU', -5], ['2NN', -2], ['2N1', -3], ['2N2', -4], ['2N3', -5], ['2NA', -1], ['2NB', 0], ['2NX', -2], ['2NY', -2], ['2NR', -8], ['2NT', -3], ['2NF', 0], ['2NU', -4], ['21N', -3], ['211', -4], ['212', -5], ['213', -6], ['21B', -1], ['21C', 0], ['21X', -3], ['21Y', -3], ['21Z', -3], ['21R', -9], ['21T', -4], ['21F', -1], ['21U', -5], ['22N', -4], ['221', -5], ['222', -6], ['223', -7], ['22A', -3], ['22C', -1], ['22X', -4], ['22Y', -4], ['22Z', -4], ['22R', -10], ['22T', -5], ['22F', -2], ['22U', -6], ['23N', -5], ['231', -6], ['232', -7], ['233', -8], ['23A', -4], ['23B', -3], ['23X', -5], ['23Y', -5], ['23Z', -5], ['23R', -11], ['23T', -6], ['23F', -3], ['23U', -7], ['2AN', -1], ['2A2', -3], ['2A3', -4], ['2AR', -7], ['2AT', -2], ['2XN', -2], ['2X1', -3], ['2X2', -4], ['2X3', -5], ['2XA', -1], ['2XX', -2], ['2XR', -8], ['2XT', -3], ['2XF', 0], ['2XU', -4], ['2YN', -2], ['2Y1', -3], ['2Y2', -4], ['2Y3', -5], ['2YR', -8], ['2YT', -3], ['2RN', -8], ['2R1', -9], ['2R2', -10], ['2R3', -11], ['2RA', -7], ['2RB', -6], ['2RC', -5], ['2RX', -8], ['2RY', -8], ['2RZ', -8], ['2RR', -14], ['2RT', -9], ['2RF', -6], ['2RU', -10], ['2TN', -3], ['2T1', -4], ['2T2', -5], ['2T3', -6], ['2TA', -2], ['2TX', -3], ['2TR', -9], ['2TT', -4], ['2TF', -1], ['2TU', -5], ['2FN', 0], ['2F1', -1], ['2F2', -2], ['2F3', -3], ['2FA', 1], ['2FX', 0], ['2FR', -6], ['2FT', -1], ['2FF', 2], ['2UN', -4], ['2U1', -5], ['2U2', -6], ['2U3', -7], ['2UA', -3], ['2UB', -2], ['2UC', -1], ['2UX', -4], ['2UY', -4], ['2UZ', -4], ['2UR', -10], ['2UT', -5], ['2UU', -6], ['3NN', -3], ['3N1', -4], ['3N2', -5], ['3N3', -6], ['3NA', -2], ['3NB', -1], ['3NC', 0], ['3NX', -3], ['3NY', -3], ['3NZ', -3], ['3NR', -9], ['3NT', -4], ['3NF', -1], ['3NU', -5], ['31N', -4], ['311', -5], ['312', -6], ['313', -7], ['31B', -2], ['31C', -1], ['31X', -4], ['31Y', -4], ['31Z', -4], ['31R', -10], ['31T', -5], ['31F', -2], ['31U', -6], ['32N', -5], ['321', -6], ['322', -7], ['323', -8], ['32A', -4], ['32C', -2], ['32X', -5], ['32Y', -5], ['32Z', -5], ['32R', -11], ['32T', -6], ['32F', -3], ['32U', -7], ['33N', -6], ['331', -7], ['332', -8], ['333', -9], ['33A', -5], ['33B', -4], ['33X', -6], ['33Y', -6], ['33Z', -6], ['33R', -12], ['33T', -7], ['33F', -4], ['33U', -8], ['3AN', -2], ['3A2', -4], ['3A3', -5], ['3AR', -8], ['3AT', -3], ['3BN', -1], ['3B1', -2], ['3B3', -4], ['3BA', 0], ['3BX', -1], ['3BR', -7], ['3BT', -2], ['3BF', 1], ['3BU', -3], ['3XN', -3], ['3X1', -4], ['3X2', -5], ['3X3', -6], ['3XA', -2], ['3XB', -1], ['3XX', -3], ['3XY', -3], ['3XR', -9], ['3XT', -4], ['3XF', -1], ['3XU', -5], ['3YN', -3], ['3Y1', -4], ['3Y2', -5], ['3Y3', -6], ['3YA', -2], ['3YX', -3], ['3YR', -9], ['3YT', -4], ['3YF', -1], ['3YU', -5], ['3ZN', -3], ['3Z1', -4], ['3Z2', -5], ['3Z3', -6], ['3ZR', -9], ['3ZT', -4], ['3RN', -9], ['3R1', -10], ['3R2', -11], ['3R3', -12], ['3RA', -8], ['3RB', -7], ['3RC', -6], ['3RX', -9], ['3RY', -9], ['3RZ', -9], ['3RR', -15], ['3RT', -10], ['3RF', -7], ['3RU', -11], ['3TN', -4], ['3T1', -5], ['3T2', -6], ['3T3', -7], ['3TA', -3], ['3TX', -4], ['3TR', -10], ['3TT', -5], ['3TF', -2], ['3TU', -6], ['3FN', -1], ['3F1', -2], ['3F2', -3], ['3F3', -4], ['3FA', 0], ['3FB', 1], ['3FX', -1], ['3FY', -1], ['3FR', -7], ['3FT', -2], ['3FF', 1], ['3UN', -5], ['3U1', -6], ['3U2', -7], ['3U3', -8], ['3UA', -4], ['3UB', -3], ['3UC', -2], ['3UX', -5], ['3UY', -5], ['3UZ', -5], ['3UR', -11], ['3UT', -6], ['3UU', -7], ['RNN', -6], ['RN1', -7], ['RN2', -8], ['RN3', -9], ['RNA', -5], ['RNB', -4], ['RNC', -3], ['RNX', -6], ['RNY', -6], ['RNZ', -6], ['RNR', -12], ['RNT', -7], ['RNF', -4], ['RNU', -8], ['R1N', -7], ['R11', -8], ['R12', -9], ['R13', -10], ['R1B', -5], ['R1C', -4], ['R1X', -7], ['R1Y', -7], ['R1Z', -7], ['R1R', -13], ['R1T', -8], ['R1F', -5], ['R1U', -9], ['R2N', -8], ['R21', -9], ['R22', -10], ['R23', -11], ['R2A', -7], ['R2C', -5], ['R2X', -8], ['R2Y', -8], ['R2Z', -8], ['R2R', -14], ['R2T', -9], ['R2F', -6], ['R2U', -10], ['R3N', -9], ['R31', -10], ['R32', -11], ['R33', -12], ['R3A', -8], ['R3B', -7], ['R3X', -9], ['R3Y', -9], ['R3Z', -9], ['R3R', -15], ['R3T', -10], ['R3F', -7], ['R3U', -11], ['RAN', -5], ['RA2', -7], ['RA3', -8], ['RAA', -4], ['RAB', -3], ['RAC', -2], ['RAX', -5], ['RAY', -5], ['RAZ', -5], ['RAR', -11], ['RAT', -6], ['RAF', -3], ['RAU', -7], ['RBN', -4], ['RB1', -5], ['RB3', -7], ['RBA', -3], ['RBB', -2], ['RBC', -1], ['RBX', -4], ['RBY', -4], ['RBZ', -4], ['RBR', -10], ['RBT', -5], ['RBF', -2], ['RBU', -6], ['RCN', -3], ['RC1', -4], ['RC2', -5], ['RCA', -2], ['RCB', -1], ['RCC', 0], ['RCX', -3], ['RCY', -3], ['RCZ', -3], ['RCR', -9], ['RCT', -4], ['RCF', -1], ['RCU', -5], ['RXN', -6], ['RX1', -7], ['RX2', -8], ['RX3', -9], ['RXA', -5], ['RXB', -4], ['RXC', -3], ['RXX', -6], ['RXY', -6], ['RXZ', -6], ['RXR', -12], ['RXT', -7], ['RXF', -4], ['RXU', -8], ['RYN', -6], ['RY1', -7], ['RY2', -8], ['RY3', -9], ['RYA', -5], ['RYB', -4], ['RYC', -3], ['RYX', -6], ['RYY', -6], ['RYZ', -6], ['RYR', -12], ['RYT', -7], ['RYF', -4], ['RYU', -8], ['RZN', -6], ['RZ1', -7], ['RZ2', -8], ['RZ3', -9], ['RZA', -5], ['RZB', -4], ['RZC', -3], ['RZX', -6], ['RZY', -6], ['RZZ', -6], ['RZR', -12], ['RZT', -7], ['RZF', -4], ['RZU', -8], ['RRN', -12], ['RR1', -13], ['RR2', -14], ['RR3', -15], ['RRA', -11], ['RRB', -10], ['RRC', -9], ['RRX', -12], ['RRY', -12], ['RRZ', -12], ['RRR', -18], ['RRT', -13], ['RRF', -10], ['RRU', -14], ['RTN', -7], ['RT1', -8], ['RT2', -9], ['RT3', -10], ['RTA', -6], ['RTX', -7], ['RTR', -13], ['RTT', -8], ['RTF', -5], ['RTU', -9], ['RFN', -4], ['RF1', -5], ['RF2', -6], ['RF3', -7], ['RFA', -3], ['RFB', -2], ['RFC', -1], ['RFX', -4], ['RFY', -4], ['RFZ', -4], ['RFR', -10], ['RFT', -5], ['RFF', -2], ['RUN', -8], ['RU1', -9], ['RU2', -10], ['RU3', -11], ['RUA', -7], ['RUB', -6], ['RUC', -5], ['RUX', -8], ['RUY', -8], ['RUZ', -8], ['RUR', -14], ['RUT', -9], ['RUU', -10], ['TNN', -1], ['TN1', -2], ['TN2', -3], ['TN3', -4], ['TNA', 0], ['TNX', -1], ['TNR', -7], ['TNT', -2], ['TNF', 1], ['TNU', -3], ['T1N', -2], ['T11', -3], ['T12', -4], ['T13', -5], ['T1B', 0], ['T1X', -2], ['T1Y', -2], ['T1R', -8], ['T1T', -3], ['T1F', 0], ['T1U', -4], ['T2N', -3], ['T21', -4], ['T22', -5], ['T23', -6], ['T2A', -2], ['T2C', 0], ['T2X', -3], ['T2Y', -3], ['T2Z', -3], ['T2R', -9], ['T2T', -4], ['T2F', -1], ['T2U', -5], ['T3N', -4], ['T31', -5], ['T32', -6], ['T33', -7], ['T3A', -3], ['T3B', -2], ['T3X', -4], ['T3Y', -4], ['T3Z', -4], ['T3R', -10], ['T3T', -5], ['T3F', -2], ['T3U', -6], ['TAN', 0], ['TA2', -2], ['TA3', -3], ['TAR', -6], ['TAT', -1], ['TXN', -1], ['TX1', -2], ['TX2', -3], ['TX3', -4], ['TXR', -7], ['TXT', -2], ['TRN', -7], ['TR1', -8], ['TR2', -9], ['TR3', -10], ['TRA', -6], ['TRB', -5], ['TRC', -4], ['TRX', -7], ['TRY', -7], ['TRZ', -7], ['TRR', -13], ['TRT', -8], ['TRF', -5], ['TRU', -9], ['TTN', -2], ['TT1', -3], ['TT2', -4], ['TT3', -5], ['TTA', -1], ['TTX', -2], ['TTR', -8], ['TTT', -3], ['TTF', 0], ['TTU', -4], ['TFN', 1], ['TF1', 0], ['TF2', -1], ['TF3', -2], ['TFR', -5], ['TFT', 0], ['TUN', -3], ['TU1', -4], ['TU2', -5], ['TU3', -6], ['TUA', -2], ['TUB', -1], ['TUX', -3], ['TUY', -3], ['TUR', -9], ['TUT', -4], ['TUU', -5]]
#
points=10
#
dpoints=self[1]-points
z=0
for x in range(len(Pos)):
    y=Pos[x]
    z=0
    for x in C:
     if x[0]==y:z=x[1]
    B.append((z,y))
B.sort()
B=B[::-1]
G=open(file,'r')
H=G.read().split('#')[::-1]
G.close()
G=open(file,'w')
H[3]=H[3].replace(H[3][8:-1],str(self[1]))
J=eval(H[4][3:-1])
A=[B[0][1],dpoints]
P=1
for x in range(0,len(J)):
 if J[x][0]==A[0]:J[x][1]+=A[1];P=0
if P:J.append(A)
H[4]='\nC='+str(J)+'\n'
s=''
for x in H[::-1]:s+=x;s+='#'
G.write(s[:-1])
G.close()
print(B[0][1])