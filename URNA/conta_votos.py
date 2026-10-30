

dep_federal = {'nulo': 0, 'branco': 0}
dep_estadual = {'nulo': 0, 'branco': 0}
senador = {'nulo': 0, 'branco': 0}
governador = {'nulo': 0, 'branco': 0}
presidente = {'nulo': 0, 'branco': 0}

lista_todos = [dep_federal, dep_estadual, senador, governador, presidente]


def final_dep_federal():

    with open(f'candidatos/dep_federal.csv', 'r') as arq:

        conteudo = arq.readlines()

        for c in conteudo:
            lista = c.split(";")

            dep_federal[lista[0]] = 0


def conta_votos_dep_federal():
    with open(f'comprovantes/votos.csv', 'r') as arq:
        conteudo = arq.readlines()
        for c in conteudo:
            lista = c.split(";")
            lista = [item.rstrip(' \n') for item in lista]
            if lista[0] == 'nulo':
                dep_federal['nulo'] += 1

            elif lista[0] == 'branco':
                dep_federal['branco'] += 1

            else:
                dep_federal[lista[0]] += 1

        print(f'este é o dep federal {dep_federal}')

# .........................


def final_dep_estadual():

    with open(f'candidatos/dep_estadual.csv', 'r') as arq:

        conteudo = arq.readlines()

        for c in conteudo:
            lista = c.split(";")

            dep_estadual[lista[0]] = 0


def conta_votos_dep_estadual():
    with open(f'comprovantes/votos.csv', 'r') as arq:
        conteudo = arq.readlines()
        for c in conteudo:
            lista = c.split(";")
            lista = [item.rstrip(' \n') for item in lista]

            if lista[1] == 'nulo':
                dep_estadual['nulo'] += 1

            elif lista[1] == 'branco':
                dep_estadual['branco'] += 1

            else:
                dep_estadual[lista[1]] += 1

        print(f'este é o deputado estadual {dep_estadual}')


def final_senador():

    with open(f'candidatos/senador.csv', 'r') as arq:

        conteudo = arq.readlines()

        for c in conteudo:
            lista = c.split(";")

            lista = [item.rstrip('\n') for item in lista]

            senador[lista[0]] = 0


def conta_votos_senador():
    with open(f'comprovantes/votos.csv', 'r') as arq:
        conteudo = arq.readlines()
        for c in conteudo:
            lista = c.split(";")

            lista = [item.rstrip('\n') for item in lista]

            if "" in senador:
                del senador[""]

            if lista[2] == 'nulo':
                senador['nulo'] += 1

            elif lista[2] == 'branco':
                senador['branco'] += 1

            else:
                senador[lista[2]] += 1

        print(f'este é do senador{senador}')


def final_governador():

    with open(f'candidatos/governador.csv', 'r') as arq:

        conteudo = arq.readlines()

        for c in conteudo:
            lista = c.split(";")

            governador[lista[0]] = 0


def conta_votos_governador():
    with open(f'comprovantes/votos.csv', 'r') as arq:
        conteudo = arq.readlines()
        for c in conteudo:
            lista = c.split(";")
            lista = [item.rstrip(' \n') for item in lista]
            if lista[4] == 'nulo':
                governador['nulo'] += 1

            elif lista[4] == 'branco':
                governador['branco'] += 1

            else:
                governador[lista[4]] += 1

        print(f'este é do governador{governador}')


def final_presidente():

    with open(f'candidatos/presidente.csv', 'r') as arq:

        conteudo = arq.readlines()

        for c in conteudo:
            lista = c.split(";")

            presidente[lista[0]] = 0


def conta_votos_presidente():
    with open(f'comprovantes/votos.csv', 'r') as arq:
        conteudo = arq.readlines()
        for c in conteudo:
            lista = c.split(";")
            # TIRA O /N PQ DAVA ERRO NA HORA DA COMPARACAO
            lista = [item.rstrip(' \n') for item in lista]

            if lista[5] == 'nulo':
                presidente['nulo'] += 1

            elif lista[5] == 'branco':
                presidente['branco'] += 1

            else:
                presidente[lista[5]] += 1

        print(f'este é do presidente{presidente}')


def relatorio_final():

    with open(f'comprovantes/relatorio.html', 'w') as arq:
        arq.write(f'<b><h3>DEPUTADOS FEDERAIS:</h3></b>{dep_federal} <br>')
        arq.write(f'<b><h3>DEPUTADOS ESTADUAIS:</h3></b>{dep_estadual} <br>')

        arq.write(f'<b><h3>SENADORES:</h3></b>{senador} <br>')
        arq.write(f'<b><h3>GOVERNADORES:</h3></b>{governador} <br>')
        arq.write(f'<b><h3>PRESIDENTE:</h3></b>{presidente} <br>')


def main():
    final_dep_federal()
    conta_votos_dep_federal()

    (final_dep_estadual())
    conta_votos_dep_estadual()

    (final_senador())
    conta_votos_senador()

    (final_governador())
    conta_votos_governador()

    (final_presidente())
    conta_votos_presidente()

    relatorio_final()


main()
