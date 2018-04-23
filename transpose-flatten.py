import numpy
array = numpy.array([input().split() for y in range(int(input().split()[0]))], int)
print(numpy.transpose(array))
print(array.flatten())
