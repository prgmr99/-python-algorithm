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
# <DFS> Depth_First Search
# 깊이 우선 탐색: 깊은 부분을 우선적으로 탐색하는 알고리즘
# 스택 자료구조(혹은 재귀함수)를 이용한다.
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면
# 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

# 예제 1
# def dfs(graph,v,visited):
#     visited[v]=True
#     print(v,end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph,i,visited)

# graph=[
#     [],
#     [2,3,8], 1(인덱스도 1로 맞춤)번 노드가 연결된 노드
#     [1,7],   2번 노드가 연결된 노드
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
# visited=[False]*9
# dfs(graph,1,visited)

# <BFS> Breadth_First Search
# 너비 우선 탐색: 가까운 노드부터 우선적으로 탐색하는 알고리즘
# 큐 자료구조 이용
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 
# 모두 큐에 삽입하고 방문 처리한다.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

# 예제 1
# from collections import deque
# def bfs(graph,start,visited):
#     queue=deque([start])
#     visited[start]=True
#     while queue:
#         v=queue.popleft()
#         print(v,end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i]=True
                
# graph=[
#     [],
#     [2,3,8], 
#     [1,7],  
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# visited=[False]*9
# bfs(graph,1,visited)

# <문제 1>
# 해설
# def dfs(x,y):
#     if x<=-1 or x>=n or y<=-1 or y>=m:
#         return False
#     if graph[x][y]==0:
#         graph[x][y]==1  # 이렇게 해야 다음 노드로 이동하고 이번 노드에 다시 왔을 때 한번 더 실행하지 않는다.
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         return True
#     return False

# n,m=map(int,input().split())
# graph=[]
# for i in range(n):
#     graph.append(list(map(int,input())))

# result=0
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j)==True:
#             result+=1   # 해당 노드에 처음 방문했을 때만 값 추가.
# print(result)
# 여기서는 인덱스와 노드 번호를 맞출 필요가 없었다.
# dfs함수를 계속 실행하면서 중복됐던 것들은 모두 False로 변하고 마지막에
# 중복이 되지 않은 것만 True를 반환해 결국 한 덩어리가 result+=1을 하는 꼴이 된다.

# <문제 2>
