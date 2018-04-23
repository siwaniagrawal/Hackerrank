import numpy
n,m=map(int,input().strip().split())
a=numpy.array([input().strip().split() for _ in range(n)],int)
b=numpy.array([input().strip().split() for _ in range(n)],int)
c=numpy.array(numpy.divide(a,b),int)
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(c)
print(numpy.mod(a,b))
print(numpy.power(a,b))

