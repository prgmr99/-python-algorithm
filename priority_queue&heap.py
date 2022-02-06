# 우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예제
import sys
import heapq
input=sys.stdin.readline

# iterable = 반복 가능한 데이터, 객체에 적용되는 의미
def heapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h,value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n=int(input())
arr=[]

for i in range(n):
    arr.append(int(input()))
res=heapsort(arr);
for i in range(n):
    print(res[i])