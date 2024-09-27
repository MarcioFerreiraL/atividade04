# 1. Implemente o código do slide de número 6. 

num = input('Digite um numero: ')
print(f'O numero que você digitou é o numero: {num}')
print(f'O tipo desse numero é: {type(num)}')

# 2. Implemente o código do slide de número 11. 

num = int(input('Digite um numero: '))
print(f'O numero que você digitou é o numero: {num}')
print(f'O tipo desse numero é: {type(num)}')

# 3. Implemente o código do slide de número 14. 

num1 = int(input('Digite algum numero: '))
num2 = int(input('Digite outro numero: '))
print(f'A soma dos dois numero que voce digitou é igual a: {num1 + num2}')

# 4. Solicite ao usuário seu nome e imprima uma mensagem de boas-vindas na tela. 

nome = input('Qual é o seu nome? ')
print(f'Bem-vindo, {nome}')

# 5. Peça ao usuário que digite sua idade em texto (por exemplo, "18") e converta-a em um número inteiro. 

int(input('Digite sua idade: '))

# 6. Receba um número inteiro do usuário e converta-o em um número decimal (float).

float(input('Digite algum numero: '))

# 7. Peça ao usuário para digitar dois números inteiros e exiba a soma deles. 

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
print(f'A soma dos dois numero que voce digitou é igual a: {num1 + num2}')

# 8. Receba um número decimal do usuário e calcule o seu quadrado. 

decimal = float(input('Digite um numero decimal para calcular o quadrado do mesmo: '))
print(f'O resulto é {decimal**2}')

# 9. Peça ao usuário que insira o seu ano de nascimento e, em seguida, exiba a sua idade. 

anoNasc = int(input("Qual o ano que você nasceu? "))
idade = 2024 - anoNasc
print(f"Uau! Você tem {idade} anos!")

# 10. Peça ao usuário que digite seu primeiro nome e seu sobrenome separadamente. Em seguida, concatene-os em uma única string e exiba o nome completo. 

nome = input("Qual o seu primeiro nome? ")
sobnome = input("Qual o seu sobrenome? ")
print(f"Seu nome completo é {nome+sobnome}!")

# 11. Solicite ao usuário uma sequência de números separados por espaço e exiba quantos números foram digitados. 

numeros = input("Digite uma sequencia de numeros separados por espaço: ")
print(f"Você digitou {len(numeros.split())} numeros!")

# 12. Receba o nome de um animal digitado pelo usuário e exiba uma mensagem informando qual animal foi digitado. 

animal = input("Digite o nome de alguem animal: ")
print(f"Você digitou o animal {animal}!")

# 13. Peça ao usuário que digite o seu nome e o seu sobrenome. Em seguida, exiba o nome completo invertido (sobrenome, nome). 

nome = input("Qual o seu primeiro nome? ")
sobnome = input("Qual o seu sobrenome? ")
print(f"Seu nome completo invertido é {sobnome + nome}!")

# 14. Receba uma string digitada pelo usuário e imprima o seu tamanho (número de caracteres).

string = input("Digite algo para contarmos o caracteres da palavra: ")
print(f"A palavra que voce digitou tem um total de {len(string)} caracteres!")

#  15. Solicite ao usuário um número inteiro e exiba se ele é par ou ímpar.

inteiro = int(input("Digite um numero inteiro para verificarmos se ele é impar ou par: "))
if inteiro%2 == 0:
    print(f"O numero que você digitou é par!")
else:
    print(f"O numero que você digitou é impar!")

# 16. Receba um número inteiro digitado pelo usuário e verifique se ele é positivo ou negativo. 

inteiro = int(input("Digite um numero inteiro para verificarmos se ele é positivo ou negativo: "))
if inteiro < 0:
    print(f"O numero que você digitou é negativo!")
else:
    print(f"O numero que você digitou é positivo!")

# 17. Peça ao usuário que insira dois números e exiba o maior deles. 

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um numero: "))
if num1 < num2:
    print(f"O numero {num2} é maior que o numero {num1}")
elif num1 > num2:
    print(f"O numero {num1} é maior que o numero {num2}")
else:
    print(f"O numero {num2} e o numero {num1} são iguais!")

# 18. Receba a altura e o peso de uma pessoa digitados pelo usuário. Em seguida, calcule o seu índice de massa corporal (IMC) utilizando a fórmula: IMC = peso / (altura * altura) e exiba o resultado.

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura * altura)
print(f"Seu IMC é {imc}")

# 19. Peça ao usuário que digite o seu nome e verifique se ele contém mais de 5 caracteres utilizando a função. 

nome = input("Digite seu nome: ")
if len(nome) > 5:
    print("Seu nome tem mais de 5 caracteres!")
elif len(nome) < 5:
    print("Seu nome tem menos de 5 caracteres!")
else:
    print("Seu nome tem 5 caracteres!")

# 20. Solicite ao usuário que insira o seu estado civil e exiba uma mensagem apropriada (por exemplo: "Você é casado(a)", "Você é solteiro(a)", etc.). 

estdCivil = input("Digite seu estado civil: ")
if estdCivil.lower == 'solteiro':
    print("Você é solteiro(a)!")
elif estdCivil.lower == 'casado':
    print("Você é casado(a)!")
elif estdCivil.lower == 'divorciado':
    print("Você é divorciado(a)!")
else:
    print("Erro. Digite algo valido. Ex: Solteiro, Casado ou Divorciado")

# 21. Receba a base e a altura de um retângulo digitados pelo usuário. Em seguida, calcule a sua área e exiba o resultado. 

altura = float(input("Digite a altura de retangulo: "))
largura = float(input("Digite um largura de retangulo: "))
area = altura * largura
print(f"O retangulo tem {area}m²!")

# 22. Peça ao usuário que digite a sua cidade e verifique se ela começa com a letra "S" (ou outra letra de sua escolha). 

cidade = input("Digite o nome de uma cidade: ")
if cidade[0] == "s" or cidade[0] == "S":
    print(f"A cidade que você digitou o nome, começa com 'S'!")
else:
    print(f"A cidade que você digitou o nome, não começa com 'S'!")

# 23. Solicite ao usuário que insira dois números decimais e calcule o resto da divisão entre eles.

dec1 = float(input("Digite um numero decimal: "))
dec2 = float(input("Digite um numero decimal: "))
print(f"O resto da divisão de {dec1} e {dec2} é {dec1%dec2}")

# 24. Solicite ao usuário um número decimal e converta-o em um número inteiro. 

inteiro = float(input("Digite um numero decimal: "))
print(f"O numero inteiro do decimal que você digitou é: {round(inteiro)}")

# 25. Receba uma string contendo um número inteiro e some 10 a esse número, convertendo-o novamente para uma string antes de exibi-lo. 

numero = int(input("Digite um numero: "))
numero = numero+10
numero = str(numero)
print(f"O numero que você digitou + 10 é {numero}")

# 26. Solicite ao usuário que digite uma data no formato "dd/mm/aaaa" e extraia o dia, o mês e o ano separadamente, convertendo-os em números inteiros. 

data = input("Digite uma data: (dd/mm/aaaa) ")
data = data.split("/")
print(f"Dia: {int(data[0])}, Mês: {int(data[1])}, Ano: {int(data[2])}")


# 27. Receba o nome de uma cidade do usuário e concatene-o com o nome do estado para formar uma mensagem completa, como "Você mora em [cidade], [estado].". 

cidade = (input("Digite o nome da sua cidade: "))
print(f"Você mora em {cidade}, PE")

# 28. Solicite ao usuário que insira seu ano de nascimento e concatene-o com uma mensagem de boas-vindas, como "Bem-vindo ao nosso programa, nascido em [ano de nascimento]!". 

anoNasc = int(input("Digite o ano que voce nasceu: "))
print(f"Bem-vindo ao nosso programa, nascido em {anoNasc}!")

# 29. Receba um número inteiro e uma string do usuário. Em seguida, concatene-os em uma única string, separando-os com um espaço. 

inteiro = int(input("Digite um numero: "))
string = (input("Digite uma frase qualquer para juntar com o numero que voce digitou acima: "))
inteiro = str(inteiro)
print(f"{inteiro+', '+string}")

# 30. Receba o nome de um produto digitado pelo usuário e concatene-o com o preço do produto, adicionando o símbolo de moeda da sua escolha. 

produto = input("Digite o nome de um produto e o preço separando-os por um espaço: ").split()
print(f"O produto {produto[0]} custa R${produto[1]}.")


# 31. Receba um número inteiro do usuário e concatene-o com uma mensagem, informando o dobro desse número.

num = int(input("Digite um numero : "))
print(f"Você digitou o numero {num} e o dobro dele é {num*2}")

# 32. Receba uma string contendo um endereço de e-mail e concatene-a com uma mensagem de agradecimento personalizada. 

email = (input("Digite seu endereço de email: "))
print(f"Obrigado por digitar seu email, {email}!")

# 33. Receba dois números inteiros do usuário e exiba a soma, a diferença, o produto e o quociente (divisão inteira) entre eles. 

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
print(f"A soma {num1+num2}, a diferença {num1-num2}, o produto {num1*num2} e o quociente {num1/num2} entre eles.")

# 34. Peça ao usuário para digitar a base e a altura de um triângulo. Em seguida, calcule e exiba a área do triângulo. 

altura = int(input("Digite a altura de um triângulo: "))
base = int(input("Digite a base de um triângulo: "))
print(f"A area do triangulo é {(altura*base) / 2}m²")

# 35. Receba o raio de uma circunferência digitado pelo usuário e calcule o seu perímetro (2 * π * raio).

raio = int(input("Digite o raio de uma circuferencia: "))
import math
print(f"O perimetro da circunferencia é {2 * math.pi + raio:.2f}m²")

# 36. Receba a base e a altura de um retângulo digitados pelo usuário. Em seguida, calcule e exiba o perímetro do retângulo. 

altura = int(input("Digite a altura de um retangulo: "))
base = int(input("Digite a base de um retangulo: "))
print(f"A area do retangulo é {(altura*base)}m²")

# 37. Solicite ao usuário que insira três números decimais. Em seguida, calcule e exiba a média aritmética desses números. 

dec1 = float(input("Digite um numero decimal: "))
dec2 = float(input("Digite um numero decimal: "))
dec3 = float(input("Digite um numero decimal: "))
print(f"A media aritmetica dos numero que você digitou é {(dec1+dec2+dec3)/3}")

# 38. Peça ao usuário para digitar a sua idade e, em seguida, informe quantos meses e quantos dias ele já viveu (considerando um ano com 365 dias). 

idade = int(input("Digite sua idade: "))
print(f"Você viveu {idade*12} meses e um total de {idade*365} de dias")

# 39. Receba um valor em reais e a cotação do dólar digitados pelo usuário. Em seguida, converta o valor para dólares e exiba o resultado. 

reais = float(input("Digite um valor em reais para converter em dolares: "))
dolar = reais / 5.44
print(f"O valor R${reais} convertidos para dolares valem U${dolar}")

# 40. Solicite ao usuário para digitar um número decimal e arredonde-o para o inteiro mais próximo.

dec = float(input("Digite um numero decimal: "))
print(f"O numero inteiro mais proximo de {dec} é {round(dec)}")

# 41. Receba três números inteiros digitados pelo usuário e exiba o resultado da operação (n1 + n2) * n3. 

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite um numero: "))
print(f"({num1}'+'{num2}) * {num3} = {(num1 + num2) * num3}")

# 42. Peça ao usuário que digite uma temperatura em graus Celsius e a converta para Fahrenheit usando a fórmula: Fahrenheit = (Celsius * 9/5) + 32.

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} graus Celsius é igual a {fahrenheit} graus Fahrenheit.")