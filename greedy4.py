n,k=map(int,input().split())
result=0
while True:
    target=(n//k)*k
    result+=(n-target)
    n=target
    n//=k
    result+=1
    if n<k:
        break
result+=(n-1)
print(result)
## 이 알고리즘에서 순서가 바뀌어도 논리만 맞으면 답은 맞는다.##