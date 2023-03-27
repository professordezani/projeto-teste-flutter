# -*- coding: utf-8 -*-
"""Cópia de LP2023 - Avaliação 01 - Exercício 02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sjkVAtKmi2EQhyleQGKtbHwvqdCR5iIV

Curso de Tecnologia em Análise e Desenvolvimento de Sistemas da Faculdade de Tecnologia de São José do Rio Preto
# Avaliação de Linguagem de Programação
## Prof. Dr. Henrique Dezani

---
### SUBMISSÃO

Para submeter a sua solução, siga as etapas:
1. Faça o download do código python clicando em File -> Download -> Download.py
2. Acesse o _link_
3. Faça o login usando seu número de matrícula
4. Faça o _upload_ do Exercício (arquivo que fez o _download_ do Colab na etapa 2). 

Não se esqueça de escolher o exerício correto durante a submissão.

---
### ENUNCIADO DO EXERCÍCIO 2

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.

Examplo

Dado o valor de entrada igual a `326`, a saída esperada é:

```
3 centenas, 2 dezenas e 6 unidades
```
Formato da entrada

A entrada consiste de um número inteiro positivo `numero` menor que 1000, informado pelo usuário.

Formato da saída

Descrição, por extenso, do número.

Entrada

```
12
```

Saída

```
1 dezena e duas unidades
```
"""

# Desenvolva seu programa aqui:
numero = int(input())
centenas = 0
dezenas = 0
unidades = 0
if numero >= 100:
  centenas = numero // 100
  dezenas = (numero - (100 * centenas)) // 10
  unidades = (numero - (100 * centenas) - (10 * dezenas))
  if centenas == 1:
    print(f'{centenas} centena, {dezenas} dezenas e {unidades} unudades')
  if dezenas == 1:
    print(f'{centenas} centenas, {dezenas} dezena e {unidades} unudades')
  if unidades == 1:
    print(f'{centenas} centenas, {dezenas} dezenas e {unidades} unudade')
elif numero < 100 and numero >= 10:
  dezenas = numero // 10
  unidades = (numero - (10 * dezenas))
  if dezenas == 1:
    print(f'{dezenas} dezena e {unidades} unidades')
  if unidades == 1:
    print(f'{dezenas} dezenas e {unidades} unidade')
else:
  unidades = numero
  if unidades == 1:
    print(f'{unidades} unidade')
  else:
    print(f'{unidades} unidades')