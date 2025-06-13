# 'Arquivo principal do código, onde se deve implementar cada funcionalidade do gerenciador
# É permitido, e recomendado, o uso de múltiplos arquivos, outras classes,
# funções e bibliotecas nativas (como os, datetime, etc.). 

# Bibliotecas que exigem instalação via pip não são permitidas.

import os
import datetime

'Funções ajudantes'
def clear():
    '''limpa o terminal'''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


'variaveis livres'

identificadores_ldt = open('listas.txt', 'at+') # ids das listas de tarefas

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

    def cria_tarefa(self, nome):
        '''Cria uma nova tarefa'''

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

    def cria_lista(self, nome):
        '''Cria uma nova lista de tarefas'''
        self.titulo = nome
        identificação = nome.split()
        numero_id = ''
        for palavra in identificação:
            numero_id += str(ord(palavra[0]))
        self.id = numero_id

        identificadores_ldt.seek(0)
        identificadores_ldt.read()
        identificadores_ldt.write(self.id)


# Funções de implementações
def ver_listas_de_tarefas():
    '''Acessa as listas de tarefas'''
    clear()
    identificadores_ldt.seek(0)
    listas_criadas = identificadores_ldt.read().split()
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
        entrada = input('1- sim\n2- não')

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
            ver_listas_de_tarefas()

        case '2':
            'a'     # implementar

        case '3':
            'a'     # implementar

        case '4':
            tarefa = Tarefas()
            nome = input('Nome da tarefa:\n')
            tarefa.cria_tarefa(nome)

inicio()
