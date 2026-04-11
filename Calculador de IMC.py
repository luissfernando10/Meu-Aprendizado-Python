"""
programa : Calculador de Massa Corporal
Autor : [Luis Fernando Garcia Martins]
Descrição : Utilizamos os dados de seu peso e sua altura para conseguir o resultado da sua IMC (Indíce De Massa Corporal)
"""
# Coleta De Dados 
nome = input ("Qual é o seu nome ")
idade = input ("Qual sua idade? ")
peso = float (input ("Qual seu peso "))
altura = float (input ("Qual a sua altura "))

#Cálculo Do IMC
# Para calcular irei utilizar a seguinte fórmula: O peso dividido pela a altura ao quadrado !
imc = peso / (altura ** 2)

#Exibição com f-string (formatando para duas casas decimais)
print (f"OLá,{nome}, obrigado por aguardar !")
print (f"Olá {nome} seu IMC é {imc :.2f} ")

"""
Done//

"""