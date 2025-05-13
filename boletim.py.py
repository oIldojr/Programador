frequencia = int (input("digite a frequencia"))

if frequencia <= 6:
    print("reprovado")

else:    
        n1 = float(input("digite sua primeira nota"))
        n2 = float(input("digite sua segunda nota"))
        n3 = float(input("digite sua terceira nota"))
        n4 = float(input("digite sua quarta nota"))
        media = (n1 + n2 + n3 + n4)/4

        if media < 5 or frequencia <=6:
            print("reprovado")      

        if media >= 7 and frequencia >= 7: 
            print("aprovado!")

        if media < 7 and media > 5:
            print("recuperação")        
'
     