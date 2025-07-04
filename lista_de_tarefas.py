# 'Arquivo principal do código, onde se deve implementar cada funcionalidade do gerenciador
# É recomendado, o uso de múltiplos arquivos, outras classes

#afazeres: trocar o "Aperte Enter" pipipi por "1 para tarefa, 2 para lista e 3 para menu principal"

import os, datetime, json, time


'Funções ajudantes'
def clear():
    '''Limpa o terminal.'''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def listar(lista_qualquer):
    for i, lista in enumerate(lista_qualquer, 1):
            print(f'{i} - {lista}')


'Variáveis livres'
listas = list()  # guarda as listas de tarefas criadas
tarefas = list()
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
        self.prioridade = None    # sem, baixa, média, alta *
        self.repeticao = None     # não, diária, semanal, mensal, anual. *
        self.concluida = False    # True, False  *

    def cria_tarefa(self, nome, caso):
        '''Cria uma nova tarefa'''

        print('\n=> Preencha os dados a seguir. Tarefas marcadas com "OPCIONAL" podem ser puladas ao pressionar Enter.')

        self.id = len(tarefas)

        tarefas.append([])

        self.titulo = nome
        tarefas[self.id].append(self.titulo)

        self.nota = input('\n[2/7] Descrição (OPCIONAL): ')
        tarefas[self.id].append(self.nota)
        if self.nota == '':
            del self.nota
        
        self.data = input("\n[3/7] Data para finalizar a tarefa (OPCIONAL, formato dd/mm/yyyy): ")  # inserir data dd/mm/yyyy
        tarefas[self.id].append(self.data)
        if self.data == '':
            del self.data
        
        self.tags = list(input('\n[4/7] Adicione tags à lista, separando-as com vírgula e espaço (OPCIONAL, e.g. "trabalho, universidade, mc102"): ').split(", "))
        tarefas[self.id].append(self.tags)
        if self.tags == '':
            del self.tags
        
        lista_tarefas = ListaDeTarefas()

        if caso == -1:
            if len(listas) == 0:
                self.lista = lista_tarefas.cria_lista(input("\n[5/7] Nenhuma lista foi criada ainda. Crie uma lista de tarefas para associá-la a esta tarefa: "))
            else:
                print('\n[5/7] <><><><> ASSOCIAR A UMA LISTA <><><><>')

                for index, lista in enumerate(listas):
                    print(f'{index+1} - {lista}')
                print(f'{len(listas)+1} - NENHUMA DAS ANTERIORES (criar nova lista)')

                valor = input('\nSelecione a lista à qual você quer adicionar a tarefa: ')

                while True:
                    funcionou = False
                    for i in range(len(listas)):
                        if valor == str(i+1):
                            self.lista = sorted(listas)[int(valor)-1]
                            funcionou = True
                            break
                    if valor == str(len(listas)+1):
                        self.lista = lista_tarefas.cria_lista(input("\nNome da nova lista: "))
                        funcionou = True
                    if funcionou:
                        break
                    else:
                        valor = input('\nValor inválido, tente novamente: ')
        else:
            print('\n[5/7] Lista: JÁ ESCOLHIDA')
            self.lista = listas[caso]

        prioridades = input('\n[6/7] ~~~~ PRIORIDADE ~~~~\n'
                            '1 - Sem prioridade\n'
                            '2 - Baixa\n'
                            '3 - Média\n'
                            '4 - alta\n'
                            '\nEscolha um nível de prioridade para esta tarefa: ')
        while prioridades not in ('1', '2', '3', '4'):
            prioridades = input('Opção inválida. Tente novamente: ')

        match prioridades:
            case '1':
                self.prioridade = 'Sem prioridade'
            case '2':
                self.prioridade = 'Baixa'
            case '3':
                self.prioridade = 'Média '
            case '4':
                self.prioridade = 'Alta'
        
        repetir = input('\n[7/7] @@@@@ FREQUÊNCIA @@@@@\n'
                        '1 - Nenhuma\n'
                        '2 - Diária\n'
                        '3 - Semanal\n'
                        '4 - Mensal\n'
                        '5 - Anual\n'
                        '\nEscolha a frequência de repetição da tarefa: ')
        while repetir not in ('1', '2', '3', '4', '5'):
            repetir = input('Opção inválida. Tente novamente: ')
        
        match repetir:
            case '1':
                self.repeticao = 'Nenhuma'
            case '2':
                self.repeticao = 'Diária'
            case '3':
                self.repeticao = 'Semanal'
            case '4':
                self.repeticao = 'Mensal'
            case '5':
                self.repeticao = 'Anual'
        
        for i in [self.lista, self.prioridade, self.repeticao, self.concluida]:
            tarefas[self.id].append(i)
        print(tarefas)

        if caso == -1:
            input("\nTarefa criada com sucesso. Aperte Enter para retornar ao menu principal.\n")
            clear()
            print(menu_fancy)
            inicio()
        else:
            escolha = input('\nTarefa criada com sucesso. Digite [1] para retornar à lista ou [2] para retornar ao menu principal.\n-> ')
            while escolha != '1' and escolha != '2':
                escolha = input('\nOpção inválida. Tente novamente:')
            
            match escolha:
                case '1':
                    abrir_lista(caso)
                case '2':
                    clear()
                    print(menu_fancy)
                    inicio()

class ListaDeTarefas():
    def __init__(self):
        self.id   = str()   # identificador da lista*
        self.titulo = str()   # título da lista *
        self.tarefas = list()   # lista de objetos Tarefas na lista *


    def cria_lista(self, nome):
        '''Cria uma nova lista de tarefas'''

        global listas

        while nome == '':
            nome = input('A lista precisa ter um nome. Tente novamente: ')
        while nome in listas:
            nome = input('Esta lista já existe. Tente novamente: ')
        
        self.titulo = nome
        
        listas.append(nome)
        listas.sort()
        self.id = str(listas.index(nome) + 1)

        return nome


# Funções de implementações
def ver_listas_de_tarefas():
    '''Acessa as listas de tarefas'''
    clear()
    lista_tarefas = ListaDeTarefas()
    print('X------------------X\n| LISTA DE TAREFAS |\nX------------------X')

    while True:
        if listas != []:
            listar(listas)

            if len(listas) == 1:
                placeholder = '[1]'
            else:
                placeholder = f'[1-{len(listas)}]'
            
            print(f'\nOPÇÕES: {placeholder} Acessar e/ou editar uma lista. [O] Criar uma nova lista. [X] Voltar ao menu principal.')
            entrada = input('\n-> ').lower()


            while True:
                for i, lista in enumerate(listas):
                    if str(i+1) == str(entrada):
                        abrir_lista(i)
                    
                if entrada == 'o' or entrada == '0':
                    lista_tarefas.cria_lista(input('\nInsira o título da lista: '))
                    print("\nLista criada com sucesso. Sumário de listas atualizado:")
                    break
                elif entrada == 'x' or entrada == '-1':
                    clear()
                    print(menu_fancy)
                    inicio()
                else:
                    entrada = input('Opção inválida. Tente novamente: ')

            # # #

        else:
            entrada = input('\nNenhuma lista foi encontrada, gostaria de criar uma nova?\n1 - Sim\n2 - Não (retorna ao menu principal)\n\n=> ').lower()

            while True:
                if entrada == 's' or entrada == 'sim' or entrada == '1' or entrada == '':
                    lista_tarefas.cria_lista(input('\nInsira o título da lista: '))
                    print('\nLista criada com sucesso. Sumário de listas atualizado:')
                    break


                elif entrada == 'n' or entrada == 'não' or entrada == 'nao' or entrada == '2' or entrada == '':
                    clear()
                    print(menu_fancy)
                    inicio()
                    break

                else:
                    entrada = input('Resposta inválida. Tente novamente: ')


def abrir_lista(i):
    exemplo_tarefa = Tarefas()
    clear()

    lista = listas[i]
    print(f'()*********{'*'*len(lista)}()\n|| LISTA: {lista} ||\n()*********{'*'*len(lista)}()\n')

    correspondencias = []

    for tarefa in tarefas:
        if tarefa[4] == lista:
            correspondencias.append(tarefa)
    
    if len(correspondencias) != 0:
        print(f'TAREFAS CORRESPONDENTES: {len(correspondencias)}')
        for ordem, tarefa in enumerate(correspondencias):
            print('=================================')
            print(  f'---TAREFA {ordem+1}: {tarefa[0]}---\n'
                    f'Prazo: {tarefa[2]}\n'
                    f'Prioridade: {tarefa[5]}\n'
                    f'Frequência: {tarefa[6]}'
                    f'STATUS: {('Concluída' if tarefa[7] == True else 'Pendente')}'
            )
        
        if len(correspondencias) == 1:
            placeholder = '[1]'
        else:
            placeholder = f'[1-{len(listas)}]'

        print(f'\n\nOPÇÕES: {placeholder} Abrir tarefa | [C] Criar tarefa | [E] Editar lista | [V] Voltar à lista de tarefas | [X] Menu principal')
        escolha = input('=> ').lower()

        for x in range(len(correspondencias)):
            if str(x) == escolha:
                abrir_tarefa(correspondencias[x])
            
            while escolha not in ['c', 'e', 'v', 'x']:
                escolha = input("Opção inválida. Tente novamente:")

            match escolha:
                case 'c':
                    clear()
                    exemplo_tarefa.cria_tarefa(input('O=-----+-----=O\n| NOVA TAREFA |\nO=-----+-----=O\n\n[1/7] Nome da tarefa: '), i)
                case 'e':
                    editar_lista(i)
                case 'v':
                    ver_listas_de_tarefas()
                case 'x':
                    clear()
                    print(menu_fancy)
                    inicio()


    else:
        entrada = input("Esta lista está vazia.\n\nOPÇÕES: [C] Criar tarefa - [E] Editar lista - [V] Voltar à lista de tarefas - [X] Menu principal\n-> ").lower()

        while entrada not in ['c', 'e', 'v', 'x']:
            entrada = input("Opção inválida. Tente novamente:")

        match entrada:
            case 'c':
                clear()
                exemplo_tarefa.cria_tarefa(input('O=-----+-----=O\n| NOVA TAREFA |\nO=-----+-----=O\n\n[1/7] Nome da tarefa: '), i)
            case 'e':
                editar_lista(i)
            case 'v':
                ver_listas_de_tarefas()
            case 'x':
                clear()
                print(menu_fancy)
                inicio()


def editar_lista(i):
    clear()
    escolha = input(f'----- editar lista {listas[i]} -----\n[1] Renomear\n[2] Deletar\n[3] Retornar\n\n=> ')

    counter = 0
    for tarefa in tarefas:
        if tarefa[4] == listas[i]:
            counter += 1
    
    while escolha not in ['1', '2', '3']:
        escolha = input('Opção inexistente. Tente novamente: ')
    
    match escolha:
        case '1':
            novo_nome = input('Insira um novo nome: ')
            while novo_nome in listas:
                if novo_nome != listas[i]:
                    novo_nome = input("Esta lista já existe. Tente novamente: ")
                else:
                    novo_nome = input("Este já é o nome da lista! Tente novamente:")
            
            listas[i] = novo_nome
            clear()
            editar_lista(i)
        
        case '2':
            if len(listas) == 1:
                print('\nNão é possível executar essa ação, pois esta é a única lista existente.')
                escolha = input('=>')
            else:
                print(f'\nAVISO: Ao deletar esta lista, TODAS as tarefas ({counter}) inseridas nesta lista serão deletadas. Você quer mesmo fazer isso?')
                print('\n[O] Confirmar (NÃO SERÁ POSSÍVEL RECUPERAR O CONTEÚDO DELETADO\n[X])\n[X] Retornar')

                escolha_final = input('-> ').lower()
                if escolha_final == '0':
                    escolha_final = 'o'

                while escolha_final not in ['o', 'x']:
                    escolha_final = input('Opção inválida. Tente novamente: ')
                
                match escolha_final:
                    case 'o':
                        for tarefa in tarefas:
                            if tarefa[4] == listas[i]:
                                tarefas.remove(tarefa)
                        listas.remove(listas[i])

                        print("Tarefa finalizada. Pressione [1] para retornar ao menu de listas ou [2] para retornar ao menu principal.")

                        pos_escolha = input('-> ')

                        while pos_escolha not in ['1', '2']:
                            pos_escolha = input('Escolha inválida. Tente novamente: ')
                        
                        match pos_escolha:
                            case '1':
                                ver_listas_de_tarefas()
                            case '2':
                                clear()
                                print(menu_fancy)
                                inicio()
                    case 'x':
                        clear()
                        editar_lista(i)
        
        case '3':
            abrir_lista(i)

def abrir_tarefa(selecionado):
    clear()

    tarefa = Tarefas()
    tarefa.id = tarefas.index(selecionado)

    tarefa.titulo = selecionado[0]
    tarefa.nota = selecionado[1]
    tarefa.data = selecionado[2]
    tarefa.tags = selecionado[3]
    tarefa.lista = selecionado[4]
    tarefa.prioridade = selecionado[5]
    tarefa.repeticao = selecionado[6]
    tarefa.concluida = selecionado[7]

    if not tarefa.nota:
        tarefa.nota == '[vazio]'
    if not tarefa.data:
        tarefa.data == '[vazio]'

    print(  f'======= TAREFA: {tarefa.titulo.upper()} =======\n'
            f'[a] Resumo:              {tarefa.nota}\n\n'
            f'[b] Prazo para entrega:  {tarefa.data}\n'
            f'[c] Etiquetas:           {', '.join(tarefa.tags)}\n'
            f'[d] Pertence à lista:    {tarefa.lista}\n'
            f'[e] Prioridade:          {tarefa.prioridade}\n'
            f'[f] Período:             {tarefa.repeticao}')
    
    if not tarefa.concluida:
        print(f'[*] Status:          EM ANDAMENTO\n\n')
    else:
        print(f'[*] Status:          CONCLUÍDO\n\n')
    
    print('-- MENU DE OPÇÕES:\n'
          '[a-f] Editar atributo\n'
          '[R] Renomear\n'
          '[*]/[0] Marcar como concluído\n'
          '[!] Deletar tarefa (NÃO PODE SER DESFEITO)\n'
          '[L] Retornar à lista correspondente\n'
          '[X] Menu principal\n\n')
    
    escolha = input('=> ').lower()
    if escolha == '0' or escolha == 'o':
        escolha = '*'

    if escolha not in ['a', 'b', 'c', 'd', 'e', 'f', 'r', '*', '!', 'l', 'x']:
        escolha = ('Opção inválida. Tente novamente: ')
    
    match escolha:
        case 'a':
            'oi'
        case 'b':
            'oi'
        case 'c':
            'oi'
        case 'd':
            'oi'
        case 'e':
            'oi'
        case 'f':
            'oi'
        case 'r':
            'oi'
        case '*':
            tarefas[tarefa.id][7] == True
            abrir_tarefa(selecionado)
        case '!':
            print('AVISO: ESTA AÇÃO NÃO PODE SER DESFEITA. TODAS AS INFORMAÇÕES DELETADAS SERÃO PERMANENTEMENTE EXCLUÍDAS. PROSSEGUIR?\n'
                  '[O] Sim\n'
                  '[X] Não (retornar à tarefa)\n')
            escolha_final = input('=> ').lower()

            while escolha_final not in ['o', 'x']:
                escolha_final = input('Opção inválida. Tente novamente; ')
            
            match escolha_final:
                case 'o':
                    lista_original = tarefa.lista
                    tarefa.remove(selecionado)
                    pos_escolha = input('Ação concluída. Pressione [1] Para retornar à lista da tarefa deletada ou [2] para retornar ao menu principal.\n=>')

                    while pos_escolha not in ['1', '2']:
                        pos_escolha = input('Opção inválida. Tente novamente: ')
                    
                    match pos_escolha:
                        case '1':
                            abrir_lista(listas.index(lista_original))
                        case '2':
                            clear()
                            print(menu_fancy)
                            inicio()
                case 'x':
                    abrir_tarefa(selecionado)
        case 'l':
            abrir_lista(listas.index(tarefa.lista))
        case 'x':
            clear()
            print(menu_fancy)
            inicio()

def inicio():
    entrada = input('1 - Ver listas de tarefas\n'
                    '2 - Ver tarefas pendentes\n'
                    '3 - Ver tarefas concluidas\n'
                    '4 - Criar uma nova tarefa\n'
                    '5 - Sair\n\n'
                    'Escolha uma opção: '
                    )
    
    lista_tarefas = ListaDeTarefas()

    while entrada not in ('1', '2', '3', '4', '5'):
            entrada = input('\nOpção inválida. Tente novamente: ')

    match entrada:
        case '1':
            ver_listas_de_tarefas()

        case '2':
            'a'     # implementar

        case '3':
            'a'     # implementar

        case '4':
            tarefa = Tarefas()
            clear()
            nome = input('O=-----+-----=O\n| NOVA TAREFA |\nO=-----+-----=O\n\n' '[1/7] Nome da tarefa: ')
            while nome == '':
                nome = input("A tarefa precisa ter um nome. Tente novamente: ")
            tarefa.cria_tarefa(nome, -1)
        case '5':
            exit(0)


menu_fancy = 'X<><><><><><><><><><><><>X\n' '=|=|= MENU PRINCIPAL =|=|=\n' 'X<><><><><><><><><><><><>X\n'

print(menu_fancy)
inicio()
