n,m=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if a[i]+a[j]+a[k]>m:
                continue
            if a[i]+a[j]+a[k]<=m and a[i]+a[j]+a[k]>=ans:
                ans=a[i]+a[j]+a[k] ## 위에 한 조건을 더 걸어서 i,j,k의 경우를 찾아야함
                print(i,j,k)



print(ans)
