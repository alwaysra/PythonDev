'''
29a+30b+31c=366
求三元一次方程
'''
a = 0
b = 0
c = 0
d = 43323

for a in range(0,d):
    for b in range(0,d):
        for c in range(0,d):
            sum=29*a+30*b+31*c
            if(sum==d):
                print(a,b,c)
print('该题无解')


