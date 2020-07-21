# QuadradoMagicoEsburacado
Solução do puzzle "Quadrado mágico esburacado"

O Quadrado Mágico “esburacado”

#Vi o puzzle a seguir, e parecia interessante. Por falta de um nome melhor, chamá-lo-ei de “quadrado mágico esburacado”.

![](https://ideiasesquecidas.files.wordpress.com/2020/07/puzzlequadradoesburacado.jpeg)

Se o leitor quiser tentar resolver, aviso que há spoilers à frente.

Como eu já tinha feito uma rotina que resolve quadrados mágicos de qualquer tamanho, achei que poderia aproveitar algum padrão já existente.

![](https://ideiasesquecidas.files.wordpress.com/2020/05/quadrado13-1.png?w=524)

Vide https://asgunzi.github.io/QuadradoMagicoD3/index.html

Entretanto, não foi possível partir para uma solução que utilizasse quadrados mágicos comuns. E também não consegui chegar numa fórmula matemática fechada, que deve uma solução.

O jeito foi apelar para os computadores. Mesmo assim, não é tarefa fácil.

O jeito “força bruta” pura chega a 20! (fatorial) combinações. Isso dá o número astronômico de 2,4*10^18 combinações. Computador algum no mundo consegue resolver. Uma “força bruta” refinada.

O que fiz foi usar a estrutura do problema para diminuir drasticamente o número de combinações.

![](https://ideiasesquecidas.files.wordpress.com/2020/07/buraco01.jpg)
Imagine fatiar o problema. Resolver somente a primeira linha.

![](https://ideiasesquecidas.files.wordpress.com/2020/07/buraco02.jpg)

Se olhar só para a primeira linha, há 20 números possíveis, e a combinação de 4 delas tem que dar 42.

O Python tem algumas rotinas de combinações e permutações que vêm bem a calhar. Elas geram todas as combinações possíveis.

#Passo 0:
comb = itertools.combinations(setNumbers,4)
 
for c in comb:
    if sum(c)==42:
       #Faz alguma coisa
Esse código vai descartar uma combinação errada (digamos, [1,2,3,4]) e vai ficar com uma combinação correta (ex. [1, 2, 20,19]).

Dada essa combinação correta, ainda assim há todas as permutações possíveis dela (ex. [1,20, 19, 2]) a checar.

permut1 = list(itertools.permutations(c)) #Código para gerar permutações

Isso dá comb(20,4)*permut(4) = 116 mil

Para cada combinação possível da primeira linha, agora vamos tentar encaixar a primeira coluna:

![](https://ideiasesquecidas.files.wordpress.com/2020/07/buraco03.jpg)


São três espaços vazios, para encaixar 16 números (ou seja, 20 iniciais – 4 da primeira linha). A soma da coluna tem que dar 42.

O resto do procedimento é igual. Dá comb(16,3)*permut(3) = 3360.

Uma nota importante. Das 116 mil, somente uma fração preenche o critério da soma ser 42. Portanto, esses 3360 testes não são aplicados aos 116 mil, somente ao que passou. Ainda assim, dá um número enorme, mas dessa forma, vamos restringindo o problema.

A seguir, tento preencher a diagonal. Isso porque ela tem só duas casas vazias. É um espaço menor de busca de combinações, mais fácil. Vamos restringindo o problema aos poucos.

![](https://ideiasesquecidas.files.wordpress.com/2020/07/buraco04.jpg)


A seguir, a segunda coluna.
![](https://ideiasesquecidas.files.wordpress.com/2020/07/buraco05.jpg)


E assim, sucessivamente.
![](https://ideiasesquecidas.files.wordpress.com/2020/07/buraco06.jpg)



Com isso, a rotina chegou à diversas soluções:

6	9	10	0	17
0	20	2	13	7
18	5	0	16	3
14	8	19	1	0
4	0	11	12	15
Ou:

1	2	19	0	20
0	18	12	3	9
11	16	0	10	5
17	6	4	15	0
13	0	7	14	8
Ou:

2	4	17	0	19
0	20	5	8	9
10	15	0	16	1
18	3	14	7	0
12	0	6	11	13
Na verdade, a rotina mostrou mais de 30 mil soluções (tinha várias permutações simples das soluções mostradas, e até repetidas).

Mesmo não tendo a elegância de ter solução única, é um desafio computacional interessante.

Download do código (em Python): https://github.com/asgunzi/QuadradoMagicoEsburacado

Veja também:

https://ideiasesquecidas.com/laboratorio-de-matematica/
