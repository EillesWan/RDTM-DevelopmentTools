R=False;A=print;Q=True;G=sum;import uuid as V
def F(sth):
    try:float(sth);return Q
    except:return R
def O(sentence):
    U='\\"';T='run';N='';M='execute';K='detect';I=']';H='[';E='@';D=' ';C='~';B='^';A=sentence
    if not M in A:return A
    elif T in A:return A[:A.find(T)+4]+O(A[A.find(T)+4:])
    A=(((__:=str(V.uuid4())),(P:=[(U,__)]),A.replace(U,__))if U in A else(None,(P:=[]),A))[2]
    def S(sent,ptnA,ptnB):
        A=sent;B=R;C=N
        for D in A:
            if B:
                if D==ptnB:B=R;E='{}'.format(C);F=str(V.uuid4());A=A.replace(E,F);P.append((E,F));C=N
                else:C+=D
            elif D==ptnA:B=Q
        return A
    A=(A[:A.find(E)+2]+A[A.find(H):]if G(0 if A==D else 1 for A in A[A.find(E)+2:A.find(H)])==0 else A).replace('/',D).lower();A=S(S(S(A,'"','"'),H,I),'{','}');A=list(A)
    for L in range(len(A)):
        if A[L]in(B,C):
            J=L+1
            while F(N.join(A[L+1:J+1]))or A[L+1]=='-'and F(N.join(A[L+1:J+2])):J+=1
            if A[J]==D or F(A[J]):continue
            else:A.insert(J,D)
    A=N.join(A);return(lambda a:[(a:=a.replace(C,B))for(B,C)in P[::-1]][-1]if P else a)('execute as {0} positioned as @s positioned {1} if block {2} {3} {4} at @s positioned {1} run {5}'.format(A[A.find(M)+7:(A.find(I)if H in A[:A.find(E)+5]else A.find(E)+1)+1].strip(),A[(A.find(I)if H in A[:A.find(E)+3]else A.find(E)+1)+1:A.find(K)-1].strip(),D.join([B for A in[[A]if G([F(A)for A in A])else([C+A for A in A[1:].split(C)]if A.startswith(C)else[C+A for A in A.split(C)])if C in A else[A]if not B in A else[B+A for A in A[1:].split(B)]if A.startswith(B)else[B+A for A in A.split(B)]for A in A[A.find(K)+6:].strip().split(D,4)]for B in A][0:3]),D.join([B for A in[[A]if G([F(A)for A in A])else([C+A for A in A[1:].split(C)]if A.startswith(C)else[C+A for A in A.split(C)])if C in A else[A]if not B in A else[B+A for A in A[1:].split(B)]if A.startswith(B)else[B+A for A in A.split(B)]for A in A[A.find(K)+6:].strip().split(D,4)]for B in A][3:]).split(D)[0],D.join([B for A in[[A]if G([F(A)for A in A])else([C+A for A in A[1:].split(C)]if A.startswith(C)else[C+A for A in A.split(C)])if C in A else[A]if not B in A else[B+A for A in A[1:].split(B)]if A.startswith(B)else[B+A for A in A.split(B)]for A in A[A.find(K)+6:].strip().split(D,4)]for B in A][3:]).split(D)[1],O(D.join(D.join([B for A in[[A]if G([F(A)for A in A])else([C+A for A in A[1:].split(C)]if A.startswith(C)else[C+A for A in A.split(C)])if C in A else[A]if not B in A else[B+A for A in A[1:].split(B)]if A.startswith(B)else[B+A for A in A.split(B)]for A in A[A.find(K)+6:].strip().split(D,4)]for B in A][3:]).split(D)[2:])))if K in A[:A.find(M,8)if M in A[8:]else-1]else'execute as {0} positioned as @s positioned {1} at @s positioned {1} run {2}'.format(A[A.find(M)+7:(A.find(I)if H in A[:A.find(E)+5]else A.find(E)+1)+1].strip(),D.join([B for A in[[A]if G([F(A)for A in A])else([C+A for A in A[1:].split(C)]if A.startswith(C)else[C+A for A in A.split(C)])if C in A else[A]if not B in A else[B+A for A in A[1:].split(B)]if A.startswith(B)else[B+A for A in A.split(B)]for A in A[(A.find(I)if I in A and G(0 if A==D else 1 for A in A[A.find(E)+2:A.find(H)])==0 else A.find(E)+1)+1:].strip().split(D,4)]for B in A][0:3]),O(D.join([B for A in[[A]if G([F(A)for A in A])else([C+A for A in A[1:].split(C)]if A.startswith(C)else[C+A for A in A.split(C)])if C in A else[A]if not B in A else[B+A for A in A[1:].split(B)]if A.startswith(B)else[B+A for A in A.split(B)]for A in A[(A.find(I)if I in A and G(0 if A==D else 1 for A in A[A.find(E)+2:A.find(H)])==0 else A.find(E)+1)+1:].strip().split(D,4)]for B in A][3:]))))
while Q:
    try:B=input();A();A(O(B));A('='*10)
    except EOFError:break
    except Exception as C:A(C);continue