# n=1260
# count=0

# array=[500,100,50,10]
# for coin in array:
#     count+=n//coin
#     n%=coin
# print(count)

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

n,k=map(int, input().split())
result=0
while True:
    target=(n//k)*k # 이걸 떠올린다고?
    result+=(n-target)
    n=target
    if n<k:
        break
    result+=1
    n//=k
result+=(n-1) # 예를 들어 2가 남았을 때 2로 나누면 0이니까 1을 뺀다.
print(result)