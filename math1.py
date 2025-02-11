#1
# import math
# a=float(input())
# print((a * math.pi)/180)

# #2
# h=int(input())
# a=int(input())
# b=int(input())
# area=((a+b)/2)*h
# print(area)

# #3
# import math
# def areap(n, s):
#     area = (n * s**2) / (4 * math.tan(math.pi / n))
#     return area
# n = int(input())
# s = int(input())
# print(int(areap(n, s)))

#4
h=int(input())
a=int(input())
def area(a,h):
    area=a * h
    return area
print(area(a,h))