# coding: utf-8

from menu import Menu
from utilities import valida_nif, tipo_de_nif, calc_check_digit_nif, \
                    nif_aleatorio

if __name__ == '__main__':
    options = []
    options.append('Obter check-digit')
    options.append('Validar NIF')
    options.append('Tipificação do NIF')
    options.append('NIF aleatório')
    menu = Menu('Menu Principal', options)
    op = 0
    while op != menu.exit():
        op = menu.run()
        print()

        # Obter Check-digit
        if op == 1:
            nif = input('Indique o NIF com 8 posições: ')
            print()

            if len(nif) != 8:
                print('Tamanho inválido.')
                print()
            else:
                cd = calc_check_digit_nif(nif)
                print('Check digit é %s' % cd)
                nif_completo = nif + cd
                print('NIF completo é %s' % nif_completo)

        # Validar NIF
        elif op == 2:
            nif = input('Indique o NIF com 9 posições: ')
            print()
            r = valida_nif(nif)
            if ( r == '' ):
                print('NIF é válido.')
            else:
                print(r)

        # Tipificação do NIF
        elif op == 3:
            nif = input('Indique o NIF com 9 posições: ')
            print()
            r = valida_nif(nif)

            if r == '':
                t = tipo_de_nif(nif)
                print(t)
            else:
                print(r)

        # NIF aleatório
        elif op == 4:
            prefix = input('Indique um prefixo ou deixe em branco: ')
            print()

            if len(prefix) > 0:
                nif_completo = nif_aleatorio(prefix)
                if nif_completo == '':
                    print('NIF inválido.')
                else:
                    print('NIF %s' % nif_completo)
            else:
                nif_completo = nif_aleatorio()
                print('NIF %s' % nif_completo)
