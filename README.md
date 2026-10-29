Corrida Noturna da Ponte Estaiada

Este repositório apresenta um sistema desenvolvido em Python para a disciplina de Programação I, do curso de Engenharia de Software do Centro Universitário Santo Agostinho (UNIFSA).

O projeto simula o gerenciamento de uma corrida de rua, permitindo cadastrar participantes, registrar seus resultados e acompanhar a classificação das provas de 5 km e 10 km.

O desenvolvimento foi realizado em dupla e dividido em duas etapas.

Como executar

O programa foi desenvolvido em Python 3 e funciona pelo terminal, sem necessidade de bibliotecas externas.

Após baixar o repositório, a execução é feita pelo comando:

python corrida.py

O sistema apresenta um menu com as funcionalidades disponíveis, permitindo realizar diferentes operações durante a mesma execução.

Funcionalidades

Etapa 1 — Inscrição e resultados

A primeira etapa concentrou-se nas operações básicas do sistema:

Cadastro de corredores com validação de idade, distância e lote.

Cálculo do valor da inscrição, incluindo acréscimos e descontos.

Geração de códigos de identificação dos participantes.

Classificação dos atletas por faixa etária.

Conversão do tempo de corrida para segundos.

Cálculo do pace e verificação dos limites de premiação.

Etapa 2 — Gerenciamento da corrida

Na segunda etapa, o sistema foi ampliado para trabalhar com vários corredores e seus respectivos resultados.

Nível essencial

Armazenamento dos participantes em dicionários organizados em uma lista.

Listagem dos inscritos e busca por código.

Registro de tempos para corredores cadastrados.

Tratamento de códigos inexistentes.

Nível intermediário

Controle de códigos repetidos utilizando set.

Contagem de participantes por categoria.

Organização dos limites de premiação em uma tupla.

Utilização de list comprehensions para consultar corredores com tempo registrado e corredores premiados.

Nível avançado

Classificação geral dos corredores por distância e tempo.

Pódio com os três melhores participantes de cada categoria e distância.

Relatório final com quantidade de inscritos, arrecadação, tempo médio e corredor mais rápido de cada prova.

Exemplo de utilização

Após o cadastro e o registro dos tempos, o sistema pode apresentar uma classificação semelhante a esta:

Classificação geral: 5 km
1º - MARIA SOUSA
Tempo: 00:19:30
2º - JOÃO SILVA
Tempo: 00:21:00
3º - PEDRO LIMA
Tempo: 00:23:15

Os corredores são organizados do menor para o maior tempo, considerando apenas aqueles que possuem resultado registrado.

Decisões de implementação

Cada corredor é representado por um dicionário, enquanto uma lista reúne todos os participantes cadastrados.

Para evitar códigos repetidos, foi utilizado um set. Quando dois participantes geram o mesmo código inicial, o sistema acrescenta uma numeração ao código seguinte, como JOASIL25--2.

Os tempos são armazenados no formato HH:MM:SS e também em segundos, facilitando os cálculos e a organização das classificações.

As funções foram separadas de acordo com suas responsabilidades, permitindo reaproveitar os cálculos desenvolvidos na primeira etapa.

Integrantes

O projeto foi desenvolvido por dois integrantes do curso de Engenharia de Software:

Integrante 1: [Nome completo] — [Perfil do GitHub]

Integrante 2: [Nome completo] — [Perfil do GitHub]

Versões

v1.0: implementação das funcionalidades iniciais de inscrição e resultado.

v2.0: ampliação do sistema para gerenciar múltiplos corredores, classificações, pódios e relatórios.
