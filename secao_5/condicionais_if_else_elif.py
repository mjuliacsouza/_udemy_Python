"""
Estruturas condicionais
if, else, elif
"""

idade = int(input("Qual a sua idade? "))

'''
# Estrutura condicional if, em C

if(idade <10){
    printf("Menor de idade");
}else if(idade == 18){
    printf("Tem 18 anos.")
}else{
    printf("É Maior de idade.")
}
'''

'''
# Estrutura condicional if, em Java

if(idade <10){
    System.out.println("Menor de idade");
}else if(idade == 18){
    System.out.println("Tem 18 anos.")
}else{
    System.out.println("É Maior de idade.")
}
'''

if idade < 18:
    print("Menor de idade. Bebêzinho...")
elif idade == 18:
    print("Tem 18 anos! Parabéns, é o começo do fim!")
else:
    print("Maior de idade. Como vc é velha!")
