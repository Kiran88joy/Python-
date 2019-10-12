'''
from random import randint
n=int(input())
i=0
l=[]
c=[]
while i<n:
	i+=1
	c.append(input())
for i in c:
	l.append(int(i))
g=0
v=0
while v<=1000:
	m=1
	l.append(0)
	for i in range(0,n-1):
		if l[i]<=l[i+1]:
			m+=1
			if m==n:
				l.pop()
				for i in l:  
					print(i,end=' ')
				g=1
			else:
				pass
	l.pop()
	if g==1:
		break
	k=random.randint(0,n-1)
	j=random.randint(0,n-1)
	if k==j:
		continue
	a=l[k]
	b=l[j]
	l.remove(a)
	l.remove(b)
	l.insert(k,b)
	l.insert(j,a)
	v+=1
'''
#try this method
from random import randint
a1=int(input())
a=[]
b=[]
for i in range(0,a1) :
	a.append(int(input()))
	
b=a
b.sort()
while True :
	if a==b :
		print(*a,end='')
		break
	else :
		n1=randint(0,a1+1)
		n2=randint(0,a1+1)
		m1=a[n1]
		m2=a[n2]
		a[n1]=m2
		a[n2]=m1

