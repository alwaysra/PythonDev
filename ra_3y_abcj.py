a=0
b=0
c=0
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            if((a*100+b*10+c)+(a*100+a*10+c)==(b*100+c*10+c)):
                print(a,b,c)