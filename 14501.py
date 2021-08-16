n=int(input())
t=[0]*(n+1)
p=[0]*(n+1)
for i in range(1,n+1):
    t[i],p[i]=map(int,input().split())
ans=0

def go(day,sum):
    global ans
    if day==n+1:
        ans=max(ans,sum)
        return ##n+1이 되었으면 거기서 마치고 종료하기 위해서 return을 써줌. 안 그러면 index 넘어감
    if day>n+1:
        return
    go(day+1,sum)
    go(day+t[day],sum+p[day])

go(1,0)
print(ans)
