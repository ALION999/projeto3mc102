# 'Arquivo principal do código, onde se deve implementar cada funcionalidade do gerenciador
# É permitido, e recomendado, o uso de múltiplos arquivos, outras classes,
# funções e bibliotecas nativas (como os, datetime, etc.). 

# Bibliotecas que exigem instalação via pip não são permitidas.

import datetime
import os

# Funções ajudantes
def clear():
    'limpa o terminal'
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Variáveis livres

 #  identificadores_ldt = open('listas.txt', 'at+') # ids das listas de tarefas

identificadores_tarefas = dict()  # id : título


# define as classes obrigatorias do projeto, propriedades marcadas com * são obrigatórias de serem definidas ao serem criadas
class Tarefas():
    def __init__(self):
        self.id = None            # numero identificador da tarefa *
        self.titulo  = None       # *
        self.nota  = None         # descrição da tarefa
        self.data  = None         # data para a conclusão da tarefa
        self.tags  = None         #
        self.lista   = None       # *
        self.prioridade = None    # sem, baixa, media, alta *
        self.repeticao = None     # não, diaria, semanal, mensal, anual. *
        self.concluida = False    # True, False  *

    def cria_tarefa(self, nome: str):
        'cria uma nova tarefa'

        self.Titulo = nome
        self.nota = input('descrição: (opcional, enter para continuar)\n')
        if self.nota == '':
            del self.nota
        self.data = input()  # inserir data dd/mm/yyyy + horario hh/mm


class ListaDeTarefas():
    def __init__(self):
        self.id   = str()   # identificador da lista*
        self.titulo = str()   # titulo da lista *
        self.tarefas = list()   # lista de objetos Tarefas na lista *

    def cria_lista(self, nome: str):
        'Cria uma nova lista de tarefas'

        while nome.strip() == '':
            nome = input('insira o título da lista:\n')

        self.titulo = nome
        identificação = nome.split()
        numero_id = ''
        for palavra in identificação:
            numero_id += str(ord(palavra[0]))
        self.id = numero_id
        with open('listas.txt', 'at+') as file:
            file.write(f'{self.id}\n')


# Funções de implementações
def ver_listas_de_tarefas():
    'Acessa as listas de tarefas'
    clear()
    with open('listas.txt', 'r+') as file:
        file.seek(0)
        listas_criadas = file.read().split()

    if listas_criadas != []:

        for i, lista in enumerate(listas_criadas, 1):
            print(f'{i} - {lista}')

        print(f'{len(listas_criadas) + 1} - Criar nova lista')
        print(f'{len(listas_criadas) + 2} - Voltar\n')
        entrada = input()

        if entrada == str(len(listas_criadas) + 1):
            while True:
                
                clear()
                lista_tarefas = ListaDeTarefas()
                nome = input('insira o titulo da lista:\n')
                clear()
                lista_tarefas.cria_lista(nome)
                break
            ver_listas_de_tarefas()

        elif entrada == str(len(listas_criadas) + 2):
            inicio()


    else:
        print('nenhuma lista encontrada, gostaria de criar uma nova?')

        while True:
            entrada = input('1- sim\n2- não\n')
            if entrada == '1':
                clear()
                lista_tarefas = ListaDeTarefas()
                nome = input('insira o titulo da lista:\n')
                clear()
                lista_tarefas.cria_lista(nome)
                ver_listas_de_tarefas()

            elif entrada == '2':
                inicio()



# Função principal
def inicio():
    clear()
    entrada = input('1 - ver listas de tarefas\n'
                    '2 - ver tarefas pendentes\n'
                    '3 - ver tarefas concluidas\n'
                    '4 - criar nova tarefa\n\n'
                    )


    match entrada:
        case '1':
            return 'listadetarefas'

        case '2':
            return 'pendentes'    # implementar

        case '3':
            return 'concluidas'     # implementar

        case '4':
            return 'novatarefa'

        case _:
            entrada = input('opção invalida, tente novamente\n')
            return 'inicio'

escolha = inicio()

while True:
    match escolha:
        case 'inicio':
            escolha = inicio()
        case 'listadetarefas':
            escolha = ver_listas_de_tarefas()
        #case 'pendentes': ##
            escolha = tarefas_pendentes()
        #case 'concluidas':
            escolha = tarefas_concluidas()