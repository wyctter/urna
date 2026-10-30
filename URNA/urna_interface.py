
import aroeira as ar
import urna_modelo_dados as ur
import subprocess
import conta_votos as cv


# 1= DEP FEDERAL; 2= DEP ESTADUAL; 3= SENADOR1; 4=SENADOR2; 5=GOVERNADOR, 6=PRESIDENTE
# Início Variáveis Globais---------------------------------------------------------------------------------------
# mostra quantos retangulo tem que colocar na tela em cada momento
digitos_cargo_atual = 4  # 4:depferal,5depestadual,3sen1,
digito_global = 1

ordem = {'dep_federal': False, 'dep_estadual': False, 'senador1': False,
         'senador2': False, 'governador': False, 'presidente': False}

votante_atual = {'dep_federal': 'branco', 'dep_estadual': 'branco  ',
                 'senador1': 'branco', 'senador2': 'branco', 'governador': 'branco', 'presidente': 'branco'}
# Fim Variáveis Globais------------------------------------------------------------------------------------------


tela = ar.Tela("Urna Eletrônica", 1500, 1200, cor_fundo="preto")

fundo = ar.Imagem(ar.Ponto(-20, -250),
                  "Imagens/fundo_urna.png", altura=1200, largura=1400)
tela.adicionar(fundo)

# objetos de digitos de candidatos + obgetos globais da tela -----------------------------------------------------------------
digito_provisoirio = ''

foto_candidato = ar.Imagem(
    ar.Ponto(680, 150), f"foto/.jpg", altura=200)
tela.adicionar(foto_candidato)

foto_vice = ar.Imagem(
    ar.Ponto(720, 360), f"foto/.jpg", altura=150)
tela.adicionar(foto_vice)

numero1 = ar.Texto(ar.Ponto(200, 260), digito_provisoirio,
                   tamanho=50, cor="Preto", negrito=True)
tela.adicionar(numero1)
numero2 = ar.Texto(ar.Ponto(265, 260), digito_provisoirio,
                   tamanho=50, cor="Preto", negrito=True)
tela.adicionar(numero2)
numero3 = ar.Texto(ar.Ponto(330, 260), digito_provisoirio,
                   tamanho=50, cor="Preto", negrito=True)
tela.adicionar(numero3)
numero4 = ar.Texto(ar.Ponto(395, 260), digito_provisoirio,
                   tamanho=50, cor="Preto", negrito=True)
tela.adicionar(numero4)
numero5 = ar.Texto(ar.Ponto(460, 260), digito_provisoirio,
                   tamanho=50, cor="Preto", negrito=True)
tela.adicionar(numero5)

voto_branco = ar.Texto(ar.Ponto(190, 260), "",
                       tamanho=55, cor="Preto", negrito=True)
tela.adicionar(voto_branco)

nome_oficial = ''
partido_oficial = ''
seu_voto_para = ar.Texto(ar.Ponto(80, 145), "", tamanho=22, cor="Preto")
tela.adicionar(seu_voto_para)

cargo = ar.Texto(ar.Ponto(180, 190), "", tamanho=38, cor="Preto", negrito=True)
tela.adicionar(cargo)

numero = ar.Texto(ar.Ponto(80, 280), "", tamanho=22, cor="Preto")
tela.adicionar(numero)

nome = ar.Texto(ar.Ponto(80, 360), '', tamanho=22, cor="Preto")
tela.adicionar(nome)

nome_candidato = ar.Texto(ar.Ponto(165, 350), nome_oficial,
                          tamanho=34, cor="Preto", negrito=True)
tela.adicionar(nome_candidato)


partido = ar.Texto(ar.Ponto(80, 410), '', tamanho=22, cor="Preto")
tela.adicionar(partido)

partido_candidato = ar.Texto(
    ar.Ponto(165, 400), partido_oficial, tamanho=32, cor="Preto", negrito=True)
tela.adicionar(partido_candidato)

aperte = ar.Texto(ar.Ponto(80, 450), '', tamanho=22, cor="Preto")
tela.adicionar(aperte)

aperte_verde = ar.Texto(ar.Ponto(112, 485), '', tamanho=22, cor="Preto")
tela.adicionar(aperte_verde)

aperte_laranja = ar.Texto(ar.Ponto(95, 515), '', tamanho=22, cor="Preto")
tela.adicionar(aperte_laranja)

campo1 = ar.Imagem(ar.Ponto(180, 255), "retangulo.png", altura=85)
campo2 = ar.Imagem(ar.Ponto(245, 255), "retangulo.png", altura=85)
campo3 = ar.Imagem(ar.Ponto(310, 255), "retangulo.png", altura=85)
campo4 = ar.Imagem(ar.Ponto(375, 255), "retangulo.png", altura=85)
campo5 = ar.Imagem(ar.Ponto(440, 255), "retangulo.png", altura=85)
tela.adicionar(campo1)
tela.adicionar(campo2)
tela.adicionar(campo3)
tela.adicionar(campo4)
tela.adicionar(campo5)
campo1.visivel = False
campo2.visivel = False
campo3.visivel = False
campo4.visivel = False
campo5.visivel = False


mensagem_fim = ar.Texto(ar.Ponto(320, 230), '',
                        tamanho=150, cor="Preto", negrito=True)
tela.adicionar(mensagem_fim)
# Fim de Objetos globais -----------------------------------------------------------------------------------------------------


def coloca_objetos_gerais(digito_global2):
    if mensagem_fim.conteudo == '':
        global digito_global
        digito_global = digito_global2

        seu_voto_para.conteudo = "SEU VOTO PARA"
        numero.conteudo = "Número:"
        nome.conteudo = 'Nome:'
        partido.conteudo = 'Partido: '
        aperte.conteudo = 'Aperte a tecla: '
        aperte_verde.conteudo = 'VERDE para CONFIRMAR '
        aperte_laranja.conteudo = 'LARANJA para CORRIGIR '
        nome_candidato.conteudo = ''

        partido_candidato.conteudo = ''

        numero1.conteudo = ''
        numero2.conteudo = ''
        numero3.conteudo = ''
        numero4.conteudo = ''
        numero5.conteudo = ''
        if voto_branco.conteudo != '':  # aqui zera o voto em branco
            voto_branco.conteudo = ''

        if digito_global == 6:  # testando pra ver quais retangulos tem que aparecer
            campo1.visivel = True
            campo2.visivel = True
            campo3.visivel = False
            campo4.visivel = False
            campo5.visivel = False
            cargo.conteudo = "PRESIDENTE"

        elif digito_global == 5:  # testando pra ver quais retangulos tem que aparecer
            campo1.visivel = True
            campo2.visivel = True
            campo3.visivel = False
            campo4.visivel = False
            campo5.visivel = False
            cargo.conteudo = "GOVERNADOR"

        elif digito_global == 4:
            campo1.visivel = True
            campo2.visivel = True
            campo3.visivel = True
            campo4.visivel = False
            campo5.visivel = False
            cargo.conteudo = "SENADOR 2 "

        elif digito_global == 3:
            campo1.visivel = True
            campo2.visivel = True
            campo3.visivel = True
            campo4.visivel = False
            campo5.visivel = False
            cargo.conteudo = "SENADOR 1"
        elif digito_global == 1:
            campo1.visivel = True
            campo2.visivel = True
            campo3.visivel = True
            campo4.visivel = True
            campo5.visivel = False
            cargo.conteudo = "DEPUTADO FEDERAL"

        elif digito_global == 2:
            campo1.visivel = True
            campo2.visivel = True
            campo3.visivel = True
            campo4.visivel = True
            campo5.visivel = True
            cargo.conteudo = "DEPUTADO ESTADUAL"

        coloca_foto('')
        coloca_vice('')


def branco():  # Botão Branco: tira tudo da tela e coloca a mensagem de voto em branco
    if mensagem_fim.conteudo == '':
        seu_voto_para.conteudo = ""
        cargo.conteudo = ""
        numero.conteudo = ""
        nome.conteudo = ""
        nome_candidato.conteudo = ""
        partido.conteudo = ""
        partido_candidato.conteudo = ""
        coloca_vice('')

        campo1.visivel = False
        campo2.visivel = False
        campo3.visivel = False
        campo4.visivel = False
        campo5.visivel = False

        numero1.conteudo = ''
        numero2.conteudo = ''
        numero3.conteudo = ''
        numero4.conteudo = ''
        numero5.conteudo = ''

        voto_branco.conteudo = "VOTO EM BRANCO"
        foto_candidato.visivel = False


# Teclado ------------------------------------------------------------------------------------
def pre_load():

    tamanho_tecla = 100
    eixo_ylinha1 = 180

    coluna1 = 920
    coluna2 = 1028
    coluna3 = 1133

    tecla1 = ar.Imagem(ar.Ponto(coluna1, eixo_ylinha1),
                       "Imagens/botoes/renomeia/1.png", altura=tamanho_tecla)
    tela.adicionar(tecla1)

    tecla2 = ar.Imagem(ar.Ponto(coluna2, eixo_ylinha1),
                       "Imagens/botoes/renomeia/2.png", altura=tamanho_tecla)
    tela.adicionar(tecla2)

    tecla3 = ar.Imagem(ar.Ponto(coluna3, eixo_ylinha1),
                       "Imagens/botoes/renomeia/3.png", altura=tamanho_tecla)
    tela.adicionar(tecla3)

    # =================

    eixo_ylinha2 = 260

    tecla4 = ar.Imagem(ar.Ponto(coluna1, eixo_ylinha2),
                       "Imagens/botoes/renomeia/4.png", altura=tamanho_tecla)
    tela.adicionar(tecla4)

    tecla5 = ar.Imagem(ar.Ponto(coluna2, eixo_ylinha2),
                       "Imagens/botoes/renomeia/5.png", altura=tamanho_tecla)
    tela.adicionar(tecla5)

    tecla6 = ar.Imagem(ar.Ponto(coluna3, eixo_ylinha2),
                       "Imagens/botoes/renomeia/6.png", altura=tamanho_tecla)
    tela.adicionar(tecla6)

    # =================

    eixo_ylinha3 = 340

    tecla7 = ar.Imagem(ar.Ponto(coluna1, eixo_ylinha3),
                       "Imagens/botoes/renomeia/7.png", altura=tamanho_tecla, )
    tela.adicionar(tecla7)

    tecla8 = ar.Imagem(ar.Ponto(coluna2, eixo_ylinha3),
                       "Imagens/botoes/renomeia/8.png", altura=tamanho_tecla)
    tela.adicionar(tecla8)

    tecla9 = ar.Imagem(ar.Ponto(coluna3, eixo_ylinha3),
                       "Imagens/botoes/renomeia/9.png", altura=tamanho_tecla)
    tela.adicionar(tecla9)

    # =====================

    tecla0 = ar.Imagem(ar.Ponto(coluna2, 420),
                       "Imagens/botoes/renomeia/0.png", altura=tamanho_tecla)
    tela.adicionar(tecla0)

    # ====================

    teclabranco = ar.Imagem(
        ar.Ponto(900, 493), "Imagens/botoes/renomeia/11.png", altura=115)
    tela.adicionar(teclabranco)

    teclaamarela = ar.Imagem(
        ar.Ponto(1017, 493), "Imagens/botoes/renomeia/12.png", altura=115)
    tela.adicionar(teclaamarela)

    teclaverde = ar.Imagem(ar.Ponto(1125, 474),
                           "Imagens/botoes/renomeia/13.png", altura=135)
    tela.adicionar(teclaverde)
# Final Teclado -----------------------------------------------------------------------------------------------------------------


''' NAO DEU CERTO PISCAR
def pisca_retangulo():

    if numero1.conteudo != '':  # TEMOS Q VER ISSO AQUI NAO VI DAR TENPO
        campo1.visivel = True
    elif numero2.conteudo != '':
        campo2.visivel = True
    elif numero3.conteudo != '':
        campo3.visivel = True
    elif numero4.conteudo != '':
        campo4.visivel = True
    elif numero5.conteudo != '':
        campo5.visivel = True

    if numero.conteudo == '':  # TEMOS Q VER ISSO AQUI NAO VI DAR TENPO
        campo1.visivel = not campo1.visivel
    elif numero2.conteudo == '':
        campo2.visivel = not campo2.visivel
    elif numero3.conteudo == '':
        campo3.visivel = not campo3.visivel
    elif numero4.conteudo == '':
        campo4.visivel = not campo4.visivel
    elif numero5.conteudo == '':
        campo4.visivel = not campo4.visivel
'''


def adiciona_dados(dados):
    nome_candidato.conteudo = dados[0]
    partido_candidato.conteudo = dados[1]
    # print('ta aqui')


def fim():
    digito_global = 1
    branco()
    aperte.conteudo = ''
    aperte_verde.conteudo = ''
    aperte_laranja.conteudo = ''
    voto_branco.conteudo = ''
    '''fim = ar.Texto(ar.Ponto(320, 230), 'FIM',
                   tamanho=150, cor="Preto", negrito=True)
    tela.adicionar(fim)'''
    mensagem_fim.conteudo = 'FIM'
    if (votante_atual['senador1'] == votante_atual['senador2']) and votante_atual['senador1'] != 'branco' :
        votante_atual['senador2'] = 'nulo'
    ur.escreve_arq(votante_atual)
    subprocess.Popen(["aplay", "confirma-urna.wav"])


def confirma():  # ESSA MANDA NA ORDEM DA URNA, PURO GAMBIARRA!
    global digito_global
    subprocess.Popen(["aplay", "confirma_curto.wav"])  # cada etapa fz barulho
    if ordem['dep_federal'] == False:
        numero_concatenado = numero1.conteudo + \
            numero2.conteudo+numero3.conteudo+numero4.conteudo
        votante_atual['dep_federal'] = numero_concatenado

        if voto_branco.conteudo == "VOTO EM BRANCO":
            votante_atual['dep_federal'] = 'branco'

        # VERIFICA SE A PESSOA NAO DIGITOU MENOS QUE A QTD DE NUMEROS
        elif len(numero_concatenado) != 4 and voto_branco.conteudo != "VOTO EM BRANCO":

            votante_atual['dep_federal'] = 'nulo'

        retorno = ur.encontra_dep_federal(numero_concatenado)
        if retorno == ['VOTO NULO', ''] and voto_branco.conteudo != "VOTO EM BRANCO":
            votante_atual['dep_federal'] = 'nulo'

        ordem['dep_federal'] = True

        digito_global = 2
        return coloca_objetos_gerais(digito_global)

    elif ordem['dep_estadual'] == False:

        numero_concatenado = numero1.conteudo + \
            numero2.conteudo+numero3.conteudo+numero4.conteudo+numero5.conteudo
        votante_atual['dep_estadual'] = numero_concatenado

        if voto_branco.conteudo == "VOTO EM BRANCO":
            votante_atual['dep_estadual'] = 'branco'

        elif len(numero_concatenado) != 5 and voto_branco.conteudo != "VOTO EM BRANCO":
            votante_atual['dep_estadual'] = 'nulo'

        retorno = ur.encontra_dep_estadual(numero_concatenado)
        if retorno == ['VOTO NULO', ''] and voto_branco.conteudo != "VOTO EM BRANCO":
            votante_atual['dep_estadual'] = 'nulo'

        ordem['dep_estadual'] = True
        digito_global = 3
        return coloca_objetos_gerais(digito_global)

    elif ordem['senador1'] == False:

        numero_concatenado = numero1.conteudo + \
            numero2.conteudo+numero3.conteudo
        votante_atual['senador1'] = numero_concatenado

        if voto_branco.conteudo == "VOTO EM BRANCO":
            votante_atual['senador1'] = 'branco'

        elif len(numero_concatenado) != 3 and voto_branco.conteudo != "VOTO EM BRANCO":
            votante_atual['senador1'] = 'nulo'

        retorno = ur.encontra_senador1(numero_concatenado)
        if retorno == ['VOTO NULO', '']:
            votante_atual['senador1'] = 'nulo'

        ordem['senador1'] = True
        digito_global = 4
        return coloca_objetos_gerais(digito_global)

    elif ordem['senador2'] == False:

        numero_concatenado = numero1.conteudo + \
            numero2.conteudo+numero3.conteudo
        votante_atual['senador2'] = numero_concatenado

        if voto_branco.conteudo == "VOTO EM BRANCO":
            votante_atual['senador2'] = 'branco'

        elif len(numero_concatenado) != 3 and voto_branco.conteudo != "VOTO EM BRANCO":
            votante_atual['senador2'] = 'nulo'

        retorno = ur.encontra_senador2(numero_concatenado)
        if retorno == ['VOTO NULO', ''] and voto_branco.conteudo != "VOTO EM BRANCO":
            votante_atual['senador2'] = 'nulo'

        ordem['senador2'] = True
        digito_global = 5
        return coloca_objetos_gerais(digito_global)

    elif ordem['governador'] == False:

        numero_concatenado = numero1.conteudo + numero2.conteudo
        votante_atual['governador'] = numero_concatenado

        if voto_branco.conteudo == "VOTO EM BRANCO":
            votante_atual['governador'] = 'branco'

        elif len(numero_concatenado) != 2 and voto_branco.conteudo != "VOTO EM BRANCO":
            votante_atual['governador'] = 'nulo'

        retorno = ur.encontra_governador(numero_concatenado)

        if retorno == ['VOTO NULO', ''] and voto_branco.conteudo != "VOTO EM BRANCO":
            votante_atual['governador'] = 'nulo'

        ordem['governador'] = True
        digito_global = 6
        return coloca_objetos_gerais(digito_global)

    elif ordem['presidente'] == False:

        numero_concatenado = numero1.conteudo + numero2.conteudo
        votante_atual['presidente'] = numero_concatenado

        if voto_branco.conteudo == "VOTO EM BRANCO":
            votante_atual['presidente'] = 'branco'

        elif len(numero_concatenado) != 2 and voto_branco.conteudo != "VOTO EM BRANCO":
            votante_atual['presidente'] = 'nulo'

        retorno = ur.encontra_presidente(numero_concatenado)

        if retorno == ['VOTO NULO', ''] and voto_branco.conteudo != "VOTO EM BRANCO":
            votante_atual['presidente'] = 'nulo'

        ordem['presidente'] = True
        digito_global = 0  # acabou chamar um FUNCAO FIM()
        return fim()
# =========== mapeamento de botoes


def clicou(ponto):
    global digito_global
    # print(f"Clique em x={ponto.x}, y={ponto.y}")
    if mensagem_fim.conteudo == '':  # Aqui para não bugar depois de acabar
        if ponto.x > 970 and ponto.x < 1054 and ponto.y > 200 and ponto.y < 261:
            # print("clicou no 1")

            return preencher('1', digito_global)

        elif ponto.x > 1076 and ponto.x < 1160 and ponto.y > 199 and ponto.y < 260:
            # print("clicou no 2")

            return preencher('2', digito_global)

        elif ponto.x > 1183 and ponto.x < 1265 and ponto.y > 200 and ponto.y < 260:
            # print("clicou no 3")

            return preencher('3', digito_global)

        elif ponto.x > 970 and ponto.x < 1052 and ponto.y > 280 and ponto.y < 339:
            # print("clicou no 4")

            return preencher('4', digito_global)

        elif ponto.x > 1077 and ponto.x < 1160 and ponto.y > 280 and ponto.y < 341:
            # print("clicou no 5")

            return preencher('5', digito_global)

        elif ponto.x > 1182 and ponto.x < 1266 and ponto.y > 280 and ponto.y < 341:
            # print("clicou no 6")

            return preencher('6', digito_global)

        elif ponto.x > 968 and ponto.x < 1052 and ponto.y > 359 and ponto.y < 419:
            # print("clicou no 7")

            return preencher('7', digito_global)

        elif ponto.x > 1076 and ponto.x < 1160 and ponto.y > 361 and ponto.y < 421:
            # print("clicou no 8")

            return preencher('8', digito_global)

        elif ponto.x > 1183 and ponto.x < 1265 and ponto.y > 361 and ponto.y < 421:
            # print("clicou no 9")

            return preencher('9', digito_global)

        elif ponto.x > 1077 and ponto.x < 1160 and ponto.y > 440 and ponto.y < 500:
            # print("clicou no 0")

            return preencher('0', digito_global)

        elif ponto.x > 952 and ponto.x < 1053 and ponto.y > 515 and ponto.y < 583:
            # print("clicou no Branco")

            return branco()

        elif ponto.x > 1070 and ponto.x < 1170 and ponto.y > 515 and ponto.y < 583:
            # print("clicou no Corrige")

            return coloca_objetos_gerais(digito_global)

        elif ponto.x > 1188 and ponto.x < 1303 and ponto.y > 494 and ponto.y < 581:
            # print("clicou no Confirma")

            return confirma()


def coloca_foto(numero_candidato=''):
    if numero_candidato == '':
        foto_candidato.caminho = f"fotos_presidente/.jpg"
        foto_candidato.visivel = False

        return False

    if digito_global == 6:

        foto_candidato.caminho = f"fotos_presidente/{numero_candidato}.jpg"
        foto_candidato.visivel = True
        # print('entrei aqui')
        # print(numero_candidato)
        return coloca_vice(numero_candidato)

    else:
        foto_candidato.caminho = f"fotos_outros/{numero_candidato}.jpg"
        foto_candidato.visivel = True
        return coloca_vice(numero_candidato)


def coloca_vice(numero_candidato):
    if numero_candidato == '':
        foto_vice.caminho = f"fotos_presidente/.jpg"
        foto_vice.visivel = False

    if digito_global == 6:

        foto_vice.caminho = f"fotos_presidente/{numero_candidato}v.jpg"
        foto_vice.visivel = True
    else:
        foto_vice.caminho = f"fotos_outros/{numero_candidato}v.jpg"
        foto_vice.visivel = True
        return True


def preencher(digito, digito_global):

    if voto_branco.conteudo == '':  # duplicada do clicou, trocar depois
        if numero1.conteudo == '':
            numero1.conteudo = digito  # todos
            # print('estamos aqui1')
        elif numero2.conteudo == '':  # todos
            numero2.conteudo = digito
            if digito_global == 5:
                print(adiciona_dados(ur.encontra_governador(
                    numero1.conteudo+numero2.conteudo)))
                coloca_foto(numero1.conteudo+numero2.conteudo)

            if digito_global == 6:
                print(adiciona_dados(ur.encontra_presidente(
                    numero1.conteudo+numero2.conteudo)))
                coloca_foto(numero1.conteudo+numero2.conteudo)

            # print('estamos aqui2')
        elif numero3.conteudo == '' and digito_global <= 4:  # aquiso cabe,1,2,3,4
            numero3.conteudo = digito
            if digito_global == 3:
                print(adiciona_dados(ur.encontra_senador1(numero1.conteudo +
                      numero2.conteudo+numero3.conteudo)))
                coloca_foto(numero1.conteudo+numero2.conteudo+numero3.conteudo)

            elif digito_global == 4:  # SENADOR2

                if numero1.conteudo + numero2.conteudo+numero3.conteudo == votante_atual['senador1']:
                    coloca_foto('')
                    votante_atual['senador2'] = 'nulo'
                    nome_candidato.conteudo = 'VOTO NULO'
                    # print(votante_atual['senador2'])
                else:
                    print(adiciona_dados(ur.encontra_senador2(numero1.conteudo +
                                                              numero2.conteudo+numero3.conteudo)))
                    coloca_foto(numero1.conteudo +
                                numero2.conteudo+numero3.conteudo)

        elif numero4.conteudo == '' and digito_global <= 2:  # aq so cabe 1 e 2
            numero4.conteudo = digito
            if digito_global == 1:
                print(adiciona_dados(ur.encontra_dep_federal(
                    numero1.conteudo+numero2.conteudo+numero3.conteudo+numero4.conteudo)))
                coloca_foto(numero1.conteudo+numero2.conteudo +
                            numero3.conteudo+numero4.conteudo)
            # print('estamos aqui4')
        elif numero5.conteudo == '' and digito_global == 2:  # aq so cabe 2
            numero5.conteudo = digito  # 2
            print(adiciona_dados(ur.encontra_dep_estadual(numero1.conteudo+numero2.conteudo +
                  numero3.conteudo+numero4.conteudo+numero5.conteudo)))
            coloca_foto(numero1.conteudo+numero2.conteudo +
                        numero3.conteudo+numero4.conteudo+numero5.conteudo)
            # print('estamos aqui5')


def clicou_fim(tecla):
    if tecla == 'Escape':
        cv.main()
        tela.fechar()


def main():
    pre_load()
    coloca_objetos_gerais(digito_global)


main()
tela.ao_clicar(clicou)
tela.ao_pressionar_tecla(clicou_fim)
tela.executar(tela_cheia=True)
