# -*- coding: utf-8 -*-
"""LP2023 - Avaliação 01 - Exercício 03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L3wjvDx9SvknAXPnkGSp7X37M3_2O7IU

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
### ENUNCIADO DO EXERCÍCIO 3

Faça um programa que mostre os `n` termos da Série a seguir:
`S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m`

Examplo

Dado o valor de entrada igual a `4`, a saída esperada é uma string, conforme apresentado abaixo:

```
1/1 + 2/3 + 3/5 + 4/7
```
Formato da entrada

A entrada consiste de um número inteiro positivo `n` informado pelo usuário.

Formato da saída

Série da soma das frações

Entrada

```
6
```

Saída

```
1/1 + 2/3 + 3/5 + 4/7 + 5/9 + 6/11
```
"""

# Desenvolva seu programa aqui:
numero = int(input('numero inteiro '))
fraçao = 0
numero2 = 1

for numero2 in range(1,numero*2,2):
  fraçao += 1
  print(f"{fraçao}/{numero2} ")