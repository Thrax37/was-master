import sys;
def Parse(S):
    T = S.split(';');
    me = eval(T[1]);
    N = len(T)-3;
    A = list(map(lambda x: list(map(lambda y:int(y),T[3+((2*N+x+me)%N)].split('_'))),range(-3,4)));    
    Dic = {}
    for a in A:
        Dic[a[0]] = a[1:];
    Dic[-1] = [me];
    return Dic;
def Recursive(Dic,me,D):
    if D==3: return '';
    V = Dic[me];
    N = max(Dic.keys());
    Next = (me+1)%N;
    Prev = (N+1+me)%N;
    for i in range(3,0,-1):
        if V[2]>=i:
            Dic[me][2] = Dic[me][2]-i;
            return chr((i-1)+ord('A'))+Recursive(Dic,me,D+1);
    if V[1]>0:
        Dic[me][1] = Dic[me][1]-1;
        Dic[me][2] = Dic[me][2]+1;
        return 'U'+Recursive(Dic,me,D+1);
    if Dic[Next][2]>Dic[Prev][2]:
        return 'T'+Recursive(Dic,Next,D+1);
    return 'R'+Recursive(Dic,Prev,D+1);
Dic = Parse(sys.argv[1]);
me = Dic[-1][0];
print(Recursive(Dic,me,0));