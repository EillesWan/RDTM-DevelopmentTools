# -*- coding: utf-8 -*-
'''
   Copyright © 2023 Eilles Wan & Team-Ryoun

   Licensed under the Apache License, Version 2.0
   You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
'''
C='utf-8';B=b'execute';A=b'-----BEGIN RSA PUBLIC KEY-----';S=True;R=str;import brotli as D;P=False;M=sum;import uuid as Q;
def I(sth):
	try:float(sth);return S
	except:return P
def N(A):
	T='detect';U='\\"';V='run';J='';K='execute';G=']';F='[';E='@';B='~';C='^';D=' '
	if not K in A:return A
	elif V in A:return A[:A.find(V)+4]+N(A[A.find(V)+4:])
	A=(((__:=R(Q.uuid4())),(O:=[(U,__)]),A.replace(U,__))if U in A else(None,(O:=[]),A))[2]
	def W(sent,ptnA,ptnB):
		A=sent;B=P;C=J
		for D in A:
			if B:
				if D==ptnB:B=P;E='{}'.format(C);F=R(Q.uuid4());A=A.replace(E,F);O.append((E,F));C=J # type: ignore
				else:C+=D
			elif D==ptnA:B=S
		return A
	A=(A[:A.find(E)+2]+A[A.find(F):]if M(0 if A==D else 1 for A in A[A.find(E)+2:A.find(F)])==0 else A).replace('/',D).lower();A=W(W(W(A,'"','"'),F,G),'{','}');A=list(A)
	for L in range(len(A)):
		if A[L]in(C,B):
			H=L+1
			while I(J.join(A[L+1:H+1]))or A[L+1]=='-'and I(J.join(A[L+1:H+2])):H+=1
			if A[H]==D or I(A[H]):continue
			else:A.insert(H,D)
	A=J.join(A)
	def X(a):return[(a:=a.replace(C,B))for(B,C)in O[::-1]][-1]if O else a
	if T in A[:A.find(K,8)if K in A[8:]else-1]:___=[B for A in[[A]if M([I(A)for A in A])else([B+A for A in A[1:].split(B)]if A.startswith(B)else[B+A for A in A.split(B)])if B in A else[A]if not C in A else[C+A for A in A[1:].split(C)]if A.startswith(C)else[C+A for A in A.split(C)]for A in A[A.find(T)+6:].strip().split(D,4)]for B in A];____=D.join(___[3:]).split(D);return X('execute as {0} positioned as @s positioned {1} if block {2} {3} {4} at @s positioned {1} run {5}'.format(A[A.find(K)+7:(A.find(G)if F in A[:A.find(E)+5]else A.find(E)+1)+1].strip(),A[(A.find(G)if F in A[:A.find(E)+3]else A.find(E)+1)+1:A.find(T)-1].strip(),D.join(___[0:3]),____[0],____[1],N(D.join(____[2:]))))
	else:___=[B for A in[[A]if M([I(A)for A in A])else([B+A for A in A[1:].split(B)]if A.startswith(B)else[B+A for A in A.split(B)])if B in A else[A]if not C in A else[C+A for A in A[1:].split(C)]if A.startswith(C)else[C+A for A in A.split(C)]for A in A[(A.find(G)if G in A and M(0 if A==D else 1 for A in A[A.find(E)+2:A.find(F)])==0 else A.find(E)+1)+1:].strip().split(D,4)]for B in A];return X('execute as {0} positioned as @s positioned {1} at @s positioned {1} run {2}'.format(A[A.find(K)+7:(A.find(G)if F in A[:A.find(E)+5]else A.find(E)+1)+1].strip(),D.join(___[0:3]),N(D.join(___[3:]))))
while S:
	____=open((__:=input('请输入BDX文件地址：')),'rb+').read();_____=D.decompress(____[3:]);________________________________________________=_____ if not A in _____ else _____[:_____.find(A)-_____[:_____.find(A)][::-1].find(b'X')]+b'E';______=[]
	while B in ________________________________________________:__________=R(Q.uuid4()).encode(C);____________________________=________________________________________________[________________________________________________.find(B):][:________________________________________________[________________________________________________.find(B):].find(b'\x00')];________________________________________________=________________________________________________.replace(____________________________,__________);______.append((____________________________,__________))
	for(____________________________,__________)in ______:________________________________________________=________________________________________________.replace(__________,N(____________________________.decode(C)).encode(C))
	with open(__,'wb+')as ____________________________________:____________________________________.write(b'BD@'+D.compress(________________________________________________))
	print('完成')