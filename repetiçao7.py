thanos = 150
zomiaranha = 110
a=100
contagem=0
for i in range(a):
    zomiaranha+=3
    thanos+=2
    contagem += 1
    if zomiaranha>thanos:
        break
print("o homem aranha será maior depois de",contagem,"anos")