# <stack>
# stack=[]
# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()
# print(stack[::-1])
# print(stack)

# <queue>
# from collections import deque
# 리스트를 이용해서 큐를 구현할 수 있지만 시간복잡도가 늘어나기 때문에
# 위와 같이 덱 라이브러리를 이용해서 구현하는 것이 좋다.
# queue=deque()
# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()
# print(queue) # 먼저 들어온 순서대로 출력
# queue.reverse() # 역순으로 바꾸기
# print(queue) # 나중에 들어온 원소부터 출력

# <recursive function>
# def recursive_function():
#     print("재귀함수를 호출합니다.")
#     recursive_function()
# recursive_function()

# def re_func(i):
#     if i==100:
#         return
#     print(i,'번째 재귀함수에서',i+1,'번째 재귀함수를 호출합니다.')
#     re_func(i+1)
#     print(i,'번째 재귀함수를 종료합니다.')
# re_func(1)

# <반복적으로 구현한 n!>
# def factorial_iterative(n):
#     result=1
#     for i in range(1,n+1):
#         result*=i
#     return result

# <재귀적으로 구현한 n!>
# def factorial_recursive(n):
#     if n<=1:
#         return 1
#     return factorial_recursive(n-1)*n
# print('반복적으로 구현:', factorial_iterative(5))
# print('재귀적으로 구현:', factorial_recursive(5))

# 유클리드 호제법
# 두 자연수 A,B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 한다.
# 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
# def gcd(a,b):
#     if a%b==0:
#         return b
#     else:
#         return gcd(b,a%b)
# print(gcd(192,162))

#---------------------------------------------------------------------
