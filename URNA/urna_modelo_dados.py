import aroeira as ar

votante_atual = {}


def clicou(clique):
    return clique


def salva_voto(votante_atual):  # pergutar se ela entra co,o parametro ou se ela é global
    # perguntar salva o dicionario ou salva o valor de cada chave do dicionario
    with open(f'comprovantes/votos.csv', 'a') as arq:
        arq.write(
            f"{votante_atual['dep_federal']};{votante_atual['dep_estadual']};{votante_atual['senador1']};{votante_atual['senador2']};{votante_atual['governador']};{votante_atual['presidente']}\n")
        return 'VOTO SALVO COM SUCESSO'



def encontra_presidente(numero):

    with open(f'candidatos/presidente.csv', 'r') as arq:

        conteudo = arq.readlines()
        retorno = ['nome', 'partido']
        for c in conteudo:
            lista = c.split(";")

            if lista[0] == numero :

                print(lista[2])

                retorno[0] = lista[2]
                retorno[1] = lista[1]
                return retorno

        retorno[0] = 'VOTO NULO'
        retorno[1] = ''
        return retorno


def encontra_senador1(numero):

    with open(f'candidatos/senador.csv', 'r') as arq:

        conteudo = arq.readlines()
        retorno = ['nome', 'partido']
        for c in conteudo:
            lista = c.split(";")
            # print(lista)

            if lista[0] == numero:
                retorno[0] = lista[2]
                retorno[1] = lista[1]
                return retorno

        retorno[0] = 'VOTO NULO'
        retorno[1] = ''
        return retorno


def encontra_senador2(numero):

    with open(f'candidatos/senador.csv', 'r') as arq:

        conteudo = arq.readlines()
        retorno = ['nome', 'partido']
        for c in conteudo:
            lista = c.split(";")
            # print(lista)

            if lista[0] == numero:
                retorno[0] = lista[2]
                retorno[1] = lista[1]
                return retorno

        retorno[0] = 'VOTO NULO'
        retorno[1] = ''
        return retorno


def encontra_governador(numero):

    with open(f'candidatos/governador.csv', 'r') as arq:

        conteudo = arq.readlines()
        retorno = ['nome', 'partido']
        for c in conteudo:
            lista = c.split(";")
            # print(lista)

            if lista[0] == numero:
                retorno[0] = lista[2]
                retorno[1] = lista[1]
                return retorno

        retorno[0] = 'VOTO NULO'
        retorno[1] = ''
        return retorno


def encontra_dep_federal(numero):

    with open(f'candidatos/dep_federal.csv', 'r') as arq:

        conteudo = arq.readlines()
        retorno = ['nome', 'partido']
        for c in conteudo:
            lista = c.split(";")
            # print(lista)

            if lista[0] == numero:
                # print(lista[2])
                retorno[0] = lista[2]
                retorno[1] = lista[1]
                return retorno

        retorno[0] = 'VOTO NULO'
        retorno[1] = ''
        return retorno


def encontra_dep_estadual(numero):

    with open(f'candidatos/dep_estadual.csv', 'r') as arq:

        conteudo = arq.readlines()
        retorno = ['nome', 'partido']
        for c in conteudo:
            lista = c.split(";")
            # print(lista)

            if lista[0] == numero:
                retorno[0] = lista[2]
                retorno[1] = lista[1]
                return retorno

        retorno[0] = 'VOTO NULO'
        retorno[1] = ''
        return retorno


def escreve_arq(dic):

    with open(f'comprovantes/votos.csv', 'a') as arq:

        final = f"{dic['dep_federal']};{dic['dep_estadual']};{dic['senador1']};{dic['senador2']};{dic['governador']};{dic['presidente']}"
        
        
        arq.write(f'{final} \n')
