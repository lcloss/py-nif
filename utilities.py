# coding: utf-8
import re
from random import randint, choice

def valida_nif(nif):
    erro = ''
    if (len(nif) != 9):
        erro = 'O número tem tamanho inválido. Repita, por favor.'

    else:
        p = re.compile('[0-9]+')
        if (p.match(nif) == False):
            erro = 'Número inválido. Aceite de 0 a 9. Repita, por favor.'

        else:
            if nif[:1] == '0':
                erro = 'Número inválido. Primeiro dígito não pode ser zeros. Repita, por favor.'

            elif nif[:1] == '4':
                if nif[1:2] not in ('5'):
                    erro = 'Tipo de NIF inválido.'

            elif nif[:1] == '7':
                if nif[1:2] not in ('0', '1', '2', '7', '9'):
                    erro = 'Tipo de NIF inválido.'

            elif nif[:1] == '9':
                if nif[1:2] not in ('0', '1', '8', '9'):
                    erro = 'Tipo de NIF inválido.'

        cd = calc_check_digit_nif(nif)

        if nif[8:9] != cd:
            erro = 'NIF com check-digit inválido.'

    return erro

def tipo_de_nif(nif):
    if len(nif) < 1 or len(nif) > 9:
        return ''

    tipo = ''

    if (nif[:1] == '1' or nif[:1] == '2' or nif[:1] == '3'):
        tipo = 'NIF de Pessoa Singular'

    elif nif[:1] == '4':
        if len(nif) < 2:
            tipo = ''
        else:
            if nif[1:2] == '5':
                tipo = 'NIF de Pessoa Singular Não Residente'
            else:
                tipo = ''

    elif nif[:1] == '5':
        tipo = 'NIF de Pessoa Colectiva'

    elif nif[:1] == '6':
        tipo = 'NIF de Administração Pública'

    elif nif[:1] == '7':
        if len(nif) < 2:
            tipo = ''
        else:
            if nif[1:2] == '0':
                tipo = 'NIF de Herança Indivisa'

            elif nif[1:2] == '1':
                tipo = 'NIF de Pessoa Coletiva Não Residente'

            elif nif[1:2] == '2':
                tipo = 'NIF de Fundos de Investimento'

            elif nif[1:2] == '7':
                tipo = 'NIF de Atribuição Oficiosa'

            elif nif[1:2] == '9':
                tipo = 'NIF de Regime Excepcional'

            else:
                tipo = ''

    elif nif[:1] == '8':
        tipo = 'NIF de Empresário em Nome Individual (extinto)'

    elif nif[:1] == '9':
        if len(nif) < 2:
            tipo = ''
        else:
            if nif[1:2] == '0' or nif[1:2] == '1':
                tipo = 'NIF de Condomínios e Sociedade Irregulares'

            elif nif[1:2] == '8':
                tipo = 'NIF de Não Residentes'

            elif nif[1:2] == '9':
                tipo = 'NIF de Sociedades Civis'

            else:
                tipo = ''

    return tipo

def calc_check_digit_nif(nif):
    if len(nif) < 8 or len(nif) > 9:
        return ''

    control = 0
    for i in range(8):
        control += ((9 - i) * int(nif[i:i+1]))

    cd = 11 - (control % 11)
    if (cd  > 9):
        cd = 9

    return str(cd)

def nif_aleatorio(prefix=''):
    if prefix == '':
        prefix = str(randint(2,9))

    if prefix == '4':
        prefix += '5'

    elif prefix == '7':
        prefix += str(choice('01279'))

    elif prefix == '9':
        prefix += str(choice('0189'))

    tipo = tipo_de_nif(prefix)

    if tipo == '':
        return ''

    q = 8 - len(prefix)

    rest = ''
    while len(rest) < q:
        rest += str(randint(0,9))

    pre_nif = prefix + rest

    cd = calc_check_digit_nif(pre_nif)
    nif_completo = pre_nif + cd

    return nif_completo
