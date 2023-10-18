ano = int(input('Digite o ano: '))
calculo = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

if calculo:
    print(f'{ano} é bissexto.')
else:
    print(f'{ano} não é bissexto')