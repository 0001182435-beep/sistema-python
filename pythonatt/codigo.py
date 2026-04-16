def calcular_media():
    nota1 = float(input("digite sua primeira nota: "))
    nota2 = float(input("digite sua segunda nota: "))
    nota3 = float(input("digite sua terceira nota: "))
    
    media = (nota1 + nota2 + nota3) / 2  
    
    if media >= 7:
        print("aprovado")
    elif media >= 5:
        print("recuperação")
    else:
        print("reprovado")
    
    print("sua média foi: " + media) 

calcular_media

calcular_media()