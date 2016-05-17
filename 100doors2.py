doors = [0]*101

for i in range(1,101):
    for j in range (0,101,i):
        doors[j]+=1

for i in range(len(doors)):
    if doors[i]%2 == 1:
        print(i)
