# -*- coding: utf-8 -*-
"""LP2023 - Avaliação 01 - Exercício 01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q3HtXEbC0QPav5nlKGnhgzfiPmWl51Q5

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
### ENUNCIADO DO EXERCÍCIO 1

Faça um programa que leia o salário bruto de uma pessoa e calcule o total do seu salário no referido mês, sabendo-se que são descontados de maneira sequencial 8% para o INSS, 11% para o Imposto de Renda (IR) e 5% para o sindicato.

Examplo

Dado o valor de entrada igual a `1000`, tem-se os descontos de `80`de INSS, `101.20` de IR e `40.94` de sindicato. Sendo assim, o salário líquido é de:

```
777.86
```
Formato da entrada

A entrada consiste de um número float positivo `valor`, informado pelo usuário.

Formato da saída

Imprima o salário final após os descontos.

Entrada

```
1000
```

Saída

```
777.86
```
"""

# Desenvolva seu programa aqui:
sind = 0
inss = 0
ir = 0
salario_bruto = float(input())
inss = salario_bruto - (salario_bruto * 0.08)
ir = inss - (inss * 0.11)
sind = ir - (ir * 0.05)
print(f'{sind}')

