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
listas = list()  # guarda as listas de tarefas criadas
identificadores_ldt = list() # ids das listas de tarefas

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

        self.Titulo = input('Titulo da tarefa:\n')
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
        listas.append(nome)
        identificação = nome.split(sep=' ')
        numero_id = ''
        for palavra in identificação:
            numero_id += str(ord(palavra[0]))
        self.id = numero_id


# Funções de implementações
def ver_listas_de_tarefas():
    '''Acessa as listas de tarefas'''
    clear()
    if listas != []:
        for i, lista in enumerate(listas, 1):
            print(f'{i} - {lista}')
        entrada = input()
        # # #

    else:
        print('nenhuma lista encontrada, gostaria de criar uma nova?')
        entrada = input('[s] [n]\n')

        while True:
            if entrada == 's' or entrada == 'sim':
                clear()

                lista_tarefas = ListaDeTarefas()
                nome = input('insira o titulo da lista:\n')
                clear()
                lista_tarefas.cria_lista(nome)
                break


            elif entrada == 'n' or entrada == 'não' or entrada == 'nao':
                break

            else:
                entrada = input('resposta invalida, por favor digite apenas "s" ou "n" \n')
        inicio()


def inicio():
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
