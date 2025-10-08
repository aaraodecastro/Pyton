#diferenca = lambda a,b: a-b
#print(diferenca(1,2))
from functools import reduce

#produto = lambda a,b: a*b
#print(produto(4,2))
#quadrado = lambda a: a**2
#print(quadrado(9))

numero = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#dobro = list(map(lambda x:x*2,numero))
#print(dobro)

#sucessor = list(map(lambda x:x+1,numero))
#print(sucessor)

#antecessor = list(map(lambda x:x-1,numero))
#print(antecessor)

#maluquice = list(map(lambda x:x*5+1,numero))
#print(maluquice)

#pares = list(filter(lambda x : x%2==0 ,numero))
#print(pares)

#positivos = list(filter(lambda x:x>0,numero))
#print(positivos)

#impares = list(filter(lambda x : x%2 != 0,numero))
#print(impares)

#negativo = list(filter(lambda x : x<0,numero))
#print(negativo)

#doidera = list(filter(lambda x: x%3==0 and x%5==0,numero))
#print(doidera)

total = reduce(lambda acumulador,n:acumulador+n,numero,0)
print(total)
               
