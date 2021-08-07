n=int(input())
x,y=1,1
plans=input().split()
move=['L','R','U','D']
dx=[0,0,-1,1]
dy=[-1,1,0,0]

for plan in plans:
    for i in range(4):
        if plan==move[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y=nx,ny

           ## if nx<1 or ny<1 or nx>n or ny>n:
                ##nx,ny=x,y ## 이럴 경우에 nx, ny값 갱신 안됨.
print(x,y)