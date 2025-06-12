# MC102 - Projeto 03: Gerenciador de Tarefas

📌 Objetivo
Neste projeto, vamos desenvolver um Gerenciador de Tarefas em Python para treinar
organização de código, manipulação de arquivos, tratamento de datas e interação com o
usuário via terminal, além de colocar em prática os conhecimentos adquiridos durante a
disciplina.
📋 O que é um Gerenciador de Tarefas?
Um gerenciador de tarefas é um sistema que permite organizar e acompanhar afazeres
pessoais ou profissionais. Seu principal objetivo é facilitar o planejamento do dia a dia,
permitindo ao usuário registrar tarefas, atribuir prazos, definir prioridades, classificá-las com
tags e acompanhar o andamento de cada uma — desde a criação até a sua conclusão.
Exemplos bastante conhecidos são Microsoft To Do, Trello, Evernote e o Google Keep.
Exemplo do que o programa deve permitir:
● Criar uma tarefa como “Estudar para a prova”, com data e prioridade;
● Marcar como concluída quando finalizada;
● Ver tarefas por listas, por tags ou por período (semanais, hoje, etc.);
● Ver somente as tarefas não concluídas ou somente as concluídas.
⚙️ Especificações Funcionais e Critério de Correção
O seu programa deverá conter as especificações listadas abaixo. Ao lado esquerdo de cada
especificação, está entre parênteses, quando aplicável, o número de pontos associados ao
correto funcionamento deste item para a nota do trabalho.
● O sistema funcionará no terminal. Isso significa que você irá mostrar informações
para o usuário e esperará que ele interaja com o sistema escolhendo uma opção em
um menu. A interação pode ser em relação às informações apresentadas (veja mais
abaixo) ou fazer alguma outra ação como obter outras informações. Assim, você
deve pensar em menus de opções a serem apresentados para o usuário e esses
menus podem ser diferentes dependendo de que funcionalidade/parte do programa
está sendo usada.
● Classes: O projeto terá duas classes principais: Tarefa e ListaDeTarefas. Segue o
detalhamento de cada uma delas. Os campos marcados como “opcional” devem ser
implementados, porém, o usuário pode ou não os adicionar ao registrar uma nova
tarefa/lista.
a. Tarefa
i. ID: Um número inteiro identificador para a tarefa (obrigatório) que é
definido internamente pelo sistema, nunca pelo usuário;
ii. Título: String descrevendo a tarefa (obrigatório);
iii. Nota: String com uma descrição mais detalhada ou anotações sobre
a tarefa (opcional);

iv. Data: Data para a conclusão da tarefa (opcional, impressa/lida no
formato dia, mês e ano, por exemplo, 04/06/2025 corresponde a 04
de Junho de 2025 — este formato é chamado de DD/MM/AAAA);
v. Tags: Lista de strings que podem ser usadas para categorizar ou
filtrar tarefas (ex: “universidade”, “trabalho”, “pessoal”, opcional no
sentido que a lista pode ser vazia);
vi. Lista de Tarefas Associada: indica a qual “Lista de Tarefas” esta
tarefa pertence. Pode ser o ID da “lista de tarefas mãe”, mas ao ser
impresso para o usuário deve se mostrar o título da lista, nunca o ID
(que não tem significado algum para o usuário). Toda tarefa tem que
estar em alguma lista (obrigatório);
vii. Prioridade: Define a urgência da tarefa. Valores possíveis: “Sem
Prioridade”, “Baixa”, “Média” e “Alta” (obrigatório);
viii. Repetição: Define a frequência com que a tarefa se repete. Valores
possíveis: “Nenhuma”, “Diária”, “Semanal”, “Mensal”, “Anual”
(obrigatório); e
ix. Concluída: Um valor Booleano (True/False) indicando se a tarefa foi
finalizada (obrigatório).

b. ListaDeTarefas
i. ID da Lista: Identificador numérico para cada lista, similar ao ID da
tarefa (obrigatório);
ii. Título: Nome da lista de tarefas (ex: “Trabalhos MC102”, “Compras
de Supermercado”, obrigatório);
iii. Tarefas: Lista contendo as tarefas que pertencem a esta lista
(obrigatório, mas a lista pode ser vazia).

● (0,25 ponto) Adição de novas tarefas: O gerenciador deve permitir que o usuário
crie novas tarefas, inserindo todos os campos (ou pulando os opcionais), exceto o ID
que é determinado pelo sistema (e deve ser único).
● (0,25 ponto) Adição de novas listas de tarefas: O gerenciador deve permitir que o
usuário crie novas listas de tarefas, inicialmente vazia. Não deve ser possível criar
duas listas com exatamente o mesmo nome e isso deve ser informado ao usuário
caso ele tente fazer.
● (0,25 ponto) Edição das tarefas: O usuário pode editar qualquer campo (exceto
ID) da tarefa selecionada. Ao editar em qual lista de tarefas esta tarefa está, o seu
sistema precisa garantir que tal lista exista. Uma opção é imprimir os nomes de listas
existentes juntamente com o ID e solicitar para ele escolher o ID, mas existem
outras formas possíveis também.
● (0,25 ponto) Edição das listas de tarefas: Deve ser possível editar o título da listas
de tarefas desde que isso não gere duas listas com o mesmo nome.
● (0,5 ponto) Remoção das tarefas: O gerenciador deve permitir ao listar tarefas
(veja mais abaixo) que o usuário possa remover (apagar) uma tarefa do sistema.
● (0,5 ponto) Remoção das listas de tarefas: O gerenciador deve permitir que o
usuário apague uma lista de tarefas, o que implica também na remoção de todas as
tarefas daquela lista. Você deve informar ao usuário que todas as tarefas da lista
serão removidas e pedir que ele confirme ou cancele a remoção. O usuário não
pode apagar as listas até ficar sem nenhuma, pois ele não teria onde adicionar as
novas tarefas. Caso ele tente fazer isso, você deve informá-lo que não é possível.

● (2 pontos) Conclusão das tarefas: O usuário pode marcar uma tarefa como
concluída. Isso deve ser possível de fazer em qualquer um dos momentos que o
usuário está visualizando a tarefa. Se a tarefa apresenta alguma repetição, uma
nova tarefa deverá ser gerada com a data atualizada (ex: “estudar inglês” deverá ser
feita uma vez por semana, após concluir, deverá ser recriada com sua data ajustada
para a semana seguinte, somando 7 dias a partir da data de término).
● (0,5 ponto) Busca por tarefas: Deve ser possível o usuário buscar por tarefas.
Digita-se um termo (string) e todas as tarefas que contém esse texto no título, nota
ou tags deverão ser mostradas. O usuário deverá ser capaz editar, remover ou
marcar como concluídas estas tarefas.
● (0,5 ponto) Ver tarefas concluídas: Deve ser possível ver todas as tarefas
concluídas e o usuário pode escolher desmarcar alguma delas, remover uma, ou
remover todas as tarefas concluídas.
● (2 pontos no total, veja abaixo) Visualização das tarefas: Há vários tipos de
visualizações que devem ser possíveis ao usuário:
a. O usuário pode ver as tarefas de uma determinada “tag”, de uma
determinada lista ou de todas as listas ao mesmo tempo, das seguintes
formas:
i. todas as tarefas
ii. apenas as tarefas com data até hoje (incluindo atrasadas),
iii. apenas as tarefas com data até em 7 dias (incluindo atrasadas),
iv. apenas tarefas não concluídas.
b. Quando visualizar as tarefas, elas estarão por padrão ordenadas por data
(aquelas que não apresentam ficam no final), e se houver mais de uma tarefa
num mesmo dia, o desempate será pela prioridade e por lista (se também
tiverem a mesma prioridade).
c. Deve ser possível também visualizar as tarefas ordenadas por prioridade,
desempatadas por data e por lista.
d. Cada ponto do item (a) vale 0,5 ponto, sendo 0,25 ponto para a ordenação
do item (b) e 0,25 ponto para a ordenação do item (c).

● (3 pontos) Manipulação de arquivos: O programa deve manipular arquivos,
carregando as tarefas existentes no início e salvando as alterações após cada
modificação. Para facilitar a avaliação, o sistema deve ser entregue com diversas
tarefas e listas predefinidas no sistema, isto é, salva em um ou mais arquivos de
acordo com a forma que o sistema armazena os dados.
📋 Requisitos
O programa principal, lista_de_tarefas.py, é o ponto de execução do sistema (isto é, nós
executaremos o seu software digitando python lista_de_tarefas.py). O Gerenciador de
Tarefas deve, obrigatoriamente, conter no mínimo as classes Tarefa e ListaDeTarefas,
caso contrário o projeto terá nota zero. É permitido, e recomendado, o uso de múltiplos
arquivos, outras classes, funções e bibliotecas nativas (como os, datetime, etc.). Bibliotecas
que exigem instalação via pip não são permitidas.
TURMA W: GRUPO DE ATÉ 2 PESSOAS;

É fundamental aplicar os conceitos aprendidos em aula e seguir boas práticas de
programação, como a escolha de nomes de variáveis significativas e a elaboração de
docstrings, até mesmo para que seja fácil programar e trabalhar em grupo.
Pode-se, opcionalmente, utilizar o projeto também como uma forma de treinar os conceitos
de teste com pytest, de type hinting com mypy, e de formatação de código com o flake8.
Não há nota para estes aspectos, mas é uma forma de treinar os conceitos vistos em aula.
🗂 Entrega
Deverá ser entregue um único arquivo chamado RA1_RA2_RA3_RA4.zip onde RAi é o RA
do i-ésimo aluno. Dentro dele deve haver:
● README.pdf: Este arquivo deverá conter a explicação de todas as funcionalidades
que o seu Gerenciador de Tarefas possui, além de mostrar como utilizar o seu
programa com alguns exemplos simples e screenshots. Também deve conter, no
início, o nome e RA de todos os alunos do grupo.
● lista_de_tarefas.py: O arquivo principal do seu software.
● Outros arquivos .py que você criar para organizar o código do seu software
(recomendado)
● Arquivo(s) referente(s) com várias tarefas e listas de tarefas salvas para que o seu
software ao rodar já tenha esses conteúdos salvos.
💡 Dicas
● Vocês podem implementar outras funcionalidades, apesar disso não valer nota.
● Os IDs são gerados pelo seu software, não pelo usuário e podem ajudar a tornar
mais fácil tarefas como edição e remoção.
● Vocês podem criar outros campos para tarefas, tanto para adicionar novas
funcionalidades (ex: horário, local, link_do_meet, etc.), quanto para facilitar a
programação de vocês.
● Para a manipulação das datas, vocês podem utilizar a biblioteca datetime,
principalmente as classes date e timedelta. Aqui está a documentação para
consultarem: datetime.
● Mesmo que você possa criar o seu próprio formato para ler e escrever no arquivo,
recomendamos que você utilize json, um formato para arquivos de texto que permite
o uso de dicionários e listas. É parte do trabalho o que é o json e como usar no
Python, mas é algo bem tranquilo (e é o que esperamos que a maioria vá fazer).
Porém, deixamos algumas dicas para não ter problemas:
○ Nem todo objeto pode ser transformado para json. Um exemplo é o set.
Porém, dicionários, listas, strings, inteiros e floats podem ser transformados
para json.
○ Um objeto da classe date do datetime não pode ser transformado para json
diretamente. Sugerimos converter ele para uma string no padrão iso (ex:
2025-06-04 representa 04 de Junho de 2025) usando o método isoformat()
da classe date (ex: data.isoformat onde data é a sua variável que armazena
a data). E você pode converter uma string no padrão iso para um objeto da
classe date escrevendo date.fromisoformat(string).
