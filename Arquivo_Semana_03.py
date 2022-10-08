#!/usr/bin/env python3

#Contagem do número de itens em uma lista usando o len
tuple = ("Jan.", "Fev.", "Mar.", "Abr.", "Mai.", "Jun.", "Jul.", "Ago.", "Set.", "Out.", "Nov.", "Dez.")
print(len(tuple))

#Verificando o que a função rstrip faz
txt = '               texugo                        '
print("De todos os animais,", txt, "é o meu favorito.")
print("De todos os animais,", txt.rstrip(), "é o meu favorito.")

#Testando o rjust()
txt2 = "Dragão de komodo"
print(txt2.rjust(10) + ".")
txt2 = "Dragão de komodo".rjust(20)
print(txt2 + ".")

#Testando o ljust para ver no que dá
txt3 = "Alligator"
print(txt3.ljust(10) + ".")

#Tentando imprimir mais de uma variável por vez no python
Max = 10
Min = 2
print(Max, Min)

#Testando escrever usando caracteres de espaço em um texto.
print("Os tuatara possuem odontoides no pré-maxilar\ne dentes no palatino\ne seu crânio diápsido não apresenta modificações.")
print("Lagartos se alongaram na cauda,\renquanto serpentes se alongaram no corpo.")
print("Serpentes possuem mais de 120 vértebras cloacais\tpodendo chegar até 400.")
