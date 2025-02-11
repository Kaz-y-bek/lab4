# #1
# def generator(N):
#     for i in range(1, N + 1):
#         yield i ** 2 
# n = int(input())
# gen = generator(n)
# for i in gen:
#     print(i)

# # 2
# n = int(input())
# a=[]
# def gena(n):
    
#     for i in range(1,n+1):
#         if(i % 2 == 0):
#             a.append(i)
#         yield a
# gen = gena(n)
# for _ in gen:
#     pass
# print(a)

# #3
# def gena(n):
#     for num in range(1,n + 1):
#         if num % 3 == 0 and num % 4 == 0:
#             yield num 

# n = int(input())
# gen = gena(n)
# print(list(gen))

# #4
# def square(a, b):
#     for num in range(a, b + 1):
#         yield num ** 2

# a = int(input())
# b = int(input())
# for i in square(a, b):
#     print(i)

#5
def gen(n):
    while n >= 0:
        yield n
        n -= 1 
n = int(input())
for num in gen(n):
    print(num)