'''32a+30b+31c=366'''
flag = False
a = 0
b = 0
c = 0

for a in range(0,366):
    for b in range(0,366):
        for c in range(0,366):
            sum=29*a+30*b+31*c
            if(sum==366):
                print(a,b,c)



