N=int(input())
grid=[]
for i in range(0,N):
    lists=[int(i) for i in input().split()]
    grid.append(lists)
count=0
sum1=0
sum2=0
j1=0
j2=N-1
while(count<N):
    sum1=sum1+grid[count][j1]
    sum2=sum2+grid[count][j2]
    count+=1
    j1+=1
    j2-=1
print(abs(sum1-sum2))