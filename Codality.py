

for i in range (0,100):
    print (i)

for i in range(100):
    print (i)

factorial = 1
for i in range(1,100):
    factorial *=i
    print(factorial)

def solution(N):
    return len(max(format(N, 'b').strip('0').split('1')))


def solition2(N):
    x=int(format(N,'b'))
    while x%10==0:
        x=x//10
    else:
        x=x
    

solition2(10100)    

def binary_gap(n):
    max_gap = 0
    current_gap = 0

    # Skip the tailing zero(s)
    while n > 0 and n % 2 == 0:
        n //= 2

    while n > 0:
        remainder = n % 2
        if remainder == 0:
            # Inside a gap
            current_gap += 1
        else:
            # Gap ends
            if current_gap != 0:
                max_gap = max(current_gap, max_gap)
                current_gap = 0
        n //= 2

    return max_gap

binary_gap(1010)

def sollution(A,K):
    X=[]
    N=len(A)
    for j in range(N):
        if K+j<N:
            X[j]=A[j+K-1]
        else:
            X[j]=A[j-N+K]
        return X

sollution([3,4,7],2)

K=[3,4,5]

len(K)

def solution(A):
    N=len(A)
    for i in range(0,N):
        count=0
        for j in range(0,N):
            if A[i]==A[j]:
                count+=1
        if (count % 2 !=0):
            return A[i]
    return -1

solution([1,2])

def XOR(A):
    res = 0
    for i in A:
        res = res ^ i
    return res

XOR([3,3,4,5,6,5,4])


def solution(X, Y, D):
    return (Y-X)//D+1

solution(3,1500,12)


def solution(X, Y, D):
    # write your code in Python 3.6
    k=(Y-X)%D
    z=(Y-X)//D
    if k = 0:
        return z
    else:
        return z+1

def task(A):
    sum=0
    sumall=(2+len(A))*(len(A)+1)/2
    for i in range (0,len(A)):
        sum+=A[i]
    return sumall-sum

task([4,2,3,5])


def mindif(A):
    P=1
    sum1=sum(A[:P])
    N=len(A)
    sum2=sum(A[P:])
    dif=abs(sum1 - sum2)
    for P in range (2,N):
        x=A[P-1]
        sum1+=x
        sum2-=x
        dif=min(dif,abs(sum1-sum2))
    return dif

        

mindif([1,2,3,4,5])


def frog(X,A):
    N=len(A)
    k=[]
    for i in range (0,N):
        while j in range(1,X+1):
            if A[i]==j:
                k.append(i)
    return k 


frog(3,[2,3,4,5])

def solution(A,B,K):
    number=0
    if A==B and A!=0:
        if A%K==0:
            return 1
        else:
            return 0
    else:
        for i in range (A,B+1):
            if i%K==0:
                number+=1
        return number

solution(7,15,3)

import numpy as np
bb=np.zeros(5,)
bb



def solution (N,A):
    import numpy as np
    zero=np.zeros(N,)
    M=len(A)
    max=np.amax(zero)
    for i in range (0,M):
        if A[i]<=N:
            zero[A[i]-1]+=1
        else:
            zero=np.where(zero!=max,max,zero)
        max=np.amax(zero)
    return zero

solution(3,[0,2,1,3,4,5,6,2,0,7])

def solution(N,A):
    # write your code in Python 3.6
    zero=[0]*N
    M=len(A)
    maxint=max(zero)
    for i in range (0,M):
        if A[i]<=N:
            zero[A[i]-1]+=1
        else:
            for j in range (0,N):
                zero[j]=maxint
        maxint=max(zero)
    return zero

solution(3,[0,2,1,3,4,5,6,2,0,7])