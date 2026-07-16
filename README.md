# Projeto de Cálculo Numérico

## Aluno

**João Gabriel de Paula Silva**

Email: joao.paula@discente.ufma.br

Disciplina: Cálculo Numérico


---

## Sobre o projeto

Este projeto foi desenvolvido como parte da Avaliação da disciplina de Cálculo Numérico.

O objetivo é implementar, sem utilizar bibliotecas numéricas prontas, os principais métodos estudados durante a disciplina, utilizando apenas a linguagem Python e estruturas nativas da linguagem.

Todos os algoritmos foram implementados manualmente com base nos conceitos matemáticos apresentados em sala de aula.

---

## Métodos implementados

### Interpolação

* Interpolação de Lagrange
* Interpolação de Newton (Diferenças Divididas)
* Interpolação de Gregory-Newton
* Spline Linear
* Spline Cúbica Natural

---

### Ajuste de Curvas

* Método dos Mínimos Quadrados (MMQ)

  * Ajuste Linear
  * Previsão de valores

---

### Integração Numérica

* Regra dos Trapézios (Repetida)
* Regra de Simpson 1/3
* Regra de Simpson 3/8 (Newton-Cotes)
* Quadratura de Gauss (2 pontos)

---

### Descrição dos arquivos

| Arquivo           | Descrição                                         |
|-------------------| ------------------------------------------------- |
| `main.py`         | Menu principal e execução dos algoritmos          |
| `exemplos.py`     | Dados utilizados em cada exercício                |
| `interpolacao.py` | Métodos de interpolação                           |
| `splines.py`      | Implementação das Splines Linear e Cúbica Natural |
| `mmq.py`          | Ajuste Linear por Mínimos Quadrados               |
| `integracao.py`   | Métodos de integração numérica                    |
| `utils.py`        | Funções auxiliares                                |

---

## Menu do sistema

Ao executar o programa será exibido o seguinte menu:

```
1  - Interpolação de Lagrange
2  - Interpolação de Newton
3  - Gregory-Newton
4  - Spline Linear
5  - Spline Cúbica Natural
6  - Ajuste Linear (MMQ)
7  - Regra dos Trapézios
8  - Regra de Simpson 1/3
9  - Regra de Simpson 3/8
10 - Quadratura de Gauss
0  - Sair
```

Cada opção executa automaticamente o exercício correspondente utilizando os dados fornecidos nas descrição do projeto.

---

## Tecnologias utilizadas

* Python 3

---

## Conceitos aplicados

Durante o desenvolvimento deste projeto foram utilizados conceitos de:

* Interpolação polinomial
* Diferenças divididas
* Diferenças progressivas
* Splines
* Ajuste de curvas
* Integração numérica
* Organização modular de código
* Estruturas de repetição
* Funções
* Listas
* Manipulação de matrizes utilizando listas

---

