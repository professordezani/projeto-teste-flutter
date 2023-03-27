# -*- coding: utf-8 -*-
"""Cópia de LP2023 - Avaliação 01 - Exercício 02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TbJRktkGi8SBC4yTMtzs40IHc4TwdJf-

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
n = int(input())
centena = n // 100
resto = n % 100
dezena = resto // 10
unidade = n % 10

if centena > 1 and dezena > 1 and unidade > 1:
  print(f'{centena} centenas, {dezena} dezenas e {unidade} unidades')

if centena == 1 and dezena == 1 and unidade == 1:
  print(f'{centena} centena, {dezena} dezena e {unidade} unidade')

if centena == 1 and dezena > 1 and unidade > 1:
  print(f'{centena} centena, {dezena} dezenas e {unidade} unidades')

if centena > 1 and dezena == 1 and unidade > 1:
  print(f'{centena} centena, {dezena} dezena e {unidade} unidades')

if centena > 1 and dezena > 1 and unidade == 1:
  print(f'{centena} centena, {dezena} dezena e {unidade} unidade')

if centena == 0 and dezena == 1 and unidade == 1:
  print(f'{dezena} dezena e {unidade} unidade')

if centena == 1 and dezena == 0 and unidade == 1:
  print(f'{centena} centena e {unidade} unidade')

if centena == 1 and dezena == 1 and unidade == 0:
  print(f'{centena} centena e {dezena} dezena')

if centena == 0 and dezena > 1 and unidade > 1:
  print(f'{dezena} dezenas e {unidade} unidades')

if centena == 0 and dezena == 1 and unidade == 1:
  print(f'{dezena} dezena e {unidade} unidade')

if centena > 1 and dezena == 0 and unidade > 1:
  print(f'{centena} centenas, e {unidade} unidades')

if centena == 1 and dezena == 0 and unidade == 1:
  print(f'{centena} centena e {unidade} unidade')

if centena > 1 and dezena > 1 and unidade == 0:
  print(f'{centena} centenase e {dezena} dezenas')

if centena == 1 and dezena == 1 and unidade == 0:
  print(f'{centena} centena e {dezena} dezenas')

if dezena == 1 and unidade > 1:
  print(f'{dezena} dezena e {unidade} unidades')