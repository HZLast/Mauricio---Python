n = int(input("Digite o limite de busca de primos: "))
i = 2
while i <=n:
    mult=0
    for count in range(2,i):
        if (i % count == 0):
            mult=1

if(mult==0):
    print("",i,"")
i = i + 1
