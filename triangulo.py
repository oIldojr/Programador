v1= float(input("distancia A"))
v2= float(input("distancia B"))
v3= float(input("Distancia C"))

if v1 + v2 > v3 and  v1 + v3 > v2 and v2 + v3 > v1:
    print("pode formar um triângulo")

else:
    print("não pode formar um triângulo")