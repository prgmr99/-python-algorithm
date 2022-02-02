# n=1260
# count=0

# array=[500,100,50,10]
# for coin in array:
#     count+=n//coin
#     n%=coin
# print(count)

# <문제 1>
# 내 풀이 - 잘 안됨
# n,k=map(int,input().split())
# cnt=0
# while n%k!=0:
#     n-=1
#     cnt+=1
# while True:
#     n/=k
#     cnt+=1
#     if n==1:
#         break
# print(cnt)

# 해설
# n,k=map(int, input().split())
# result=0
# while True:
#     target=(n//k)*k # 이걸 떠올린다고?
#     result+=(n-target)
#     n=target
#     if n<k:
#         break
#     result+=1
#     n//=k
# result+=(n-1) # 예를 들어 2가 남았을 때 2로 나누면 0이니까 1을 뺀다.
# print(result)
# 매번 n을 확인해서 k로 나누어 떨어지는 아닌지 확인하는 방법으로 간단하게 작성할 수도 있다
# n,k가 10만 이하의 수이기 때문에
# 다만, 위와 같이 작성을 하면 반복문이 한번 반복이 될 때마다 n이 기하급수적으로 감소한다.

#<문제 2>
# 내 풀이
# str=input()
# result=0
# for i in str:
#     if i=='0' or i=='1':
#         result+=int(i)
#     else:
#         if (i-1)=='0' or (i-1)=='1':
#             result+=int(i-1)
#         result*=int(i)
# print(result)

# 해설
# data=input()
# result=int(data[0])
# for i in range(1,len(data)):
#     num=int(data[i])
#     if num<=1 or result<=1:
#         result+=num
#     else:
#         result*=num
# print(result)

#<문제 3>
n=int(input())
data=list(map(int,input().split()))
data.sort()
result=0
count=0
for i in data:
    count+=1
    if count>=i:
        result+=1
        count=0
print(result)
