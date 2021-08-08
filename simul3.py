n,m =map(int,input().split())
visit=[[0]*m for _ in range(n)]
x,y,direc=map(int,input().split())


visit[x][y]=1
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def left():
    global direc
    direc-=1
    if direc == -1:
        direc =3

cnt=1
turn=0
while True:
    left()
    nx=x+dx[direc]
    ny=y+dy[direc]
    if array[nx][ny]==0 and visit[nx][ny]==0:
        visit[nx][ny]=1
        x=nx
        y=ny
        cnt+=1
        turn=0
        continue
    else:
        turn+=1
    if turn==4:
        nx=x-dx[direc]
        ny=y-dx[direc]
        if array[nx][ny]==0:
            x=nx
            y=ny
        else:
            break
        turn=0

print(cnt)