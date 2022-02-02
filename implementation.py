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
#     if nx<1 or ny<1 or nx>x or ny>n:
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
#             if k%10==3 or k//10==3 or j%10==3 or j//10==3 or i%10==3 or i//10==3:
#                 cnt+=1
# print(cnt)

