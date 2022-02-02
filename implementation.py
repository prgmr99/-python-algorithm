#문제 1
# 내 풀이
# n=int(input())
# plan=list(map(str,input().split()))
# x,y=1,1
# for i in range(len(plan)):
#     if plan[i]=='R':
#         if y>=n:
#             continue
#         y+=1
#     elif plan[i]=='L':
#         if y<=1:
#             continue
#         y-=1
#     elif plan[i]=='U':
#         if x<=1:
#             continue
#         x-=1
#     elif plan[i]=='D':
#         if x>=n:
#             continue
#         x+=1
# print(x,y)

# 해설
# n=int(input())
# x,y=1,1
# plans=input().split()

# dx=[0,0,-1,1]
# dy=[-1,1,0,0]
# move_types=['L','R','U','D']

# for plan in plans:
#     for i in range(len(move_types)):
#         if plan==move_types[i]:
#             nx=x+dx[i]
#             ny=y+dy[i]
#     if nx<1 or ny<1 or nx>n or ny>n:
#         continue
#     x,y=nx,ny
# print(x,y)

# <문제 2>
# 내 풀이
# n=int(input())
# cnt=0
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             if k%10==3 or k//10==3 or j%10==3 or j//10==3 or i%10==3 or i//10==3:  # c++에서는 이렇게 사용 -> 문자열로 변경이 어렵기 때문
#                 cnt+=1
# print(cnt)

# 해설
# h=int(input())
# count=0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i)+str(j)+str(k): # 내가 두 개의 조건으로 사용한 것을 문자열로 바꿔 하나의 조건으로 만듬
#                 count+=1
# print(count)

# <문제 3>
# 내 풀이
# coord=input()
# dx=[2,2,1,1,-1,-1,-2,-2]
# dy=[-1,1,-2,2,-2,2,-1,1]
# temp_y=ord(coord[0])-96
# cnt=0
# for i in range(8):
#     ny=temp_y+dy[i]
#     nx=int(coord[1])+dx[i]
#     if ny<1 or nx<1 or nx>8 or ny>8:
#         continue
#     cnt+=1
# print(cnt)

# 해설
# input_data=input()
# row=int(input_data[1])
# column=int(ord(input_data[0]))-int(ord('a'))+1

# steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# result=0
# for step in steps:
#     next_row=row+step[0]
#     next_column=column+step[1]
#     if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
#         result+=1
# print(result)

# <문제 3>
# 내 풀이
# str1=input()
# num=0
# s=0
# l=[]
# for i in range(len(str1)):
#     if str1[i]>='A' and str1[i]<='Z':
#         l.append(str1)
#     else:
#         num=int(str1[i])
#         s+=num
# l.sort()
# print(l+str(s))
# I don't know

# 해설
data=input()
result=[]
value=0
# 문자를 하나씩 확인하며
for x in data:
    if x.isalpha():
        # 알파벳인 경우 결과 리스트에 삽입
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value+=int(x)    
# 알파벳을 오름차순으로 정렬
result.sort()
# 숫자가 하나라도 존재하는 경우, 가장 뒤에 삽입
if value!=0:
    result.append(str(value))
print(''.join(result)) # ''.join(list)는 리스트에 문자열로 변경이 가능하다.

# 잊고 있던 함수가 많다.
# 한 번씩 봐주고 상기시키는 것이 중요하다.
# 리스트와 문자열은 유사하다.