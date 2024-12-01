matriz_carga = []
marcas_carga = []
kilo = []

matriz_pipa = []
marcas_pipa = []
litro = []

print('-=' * 25)
print('Sistema de Gestão de Caminhões')
print('-=' * 25)

while True:

    print()
    print('''        [1] \033[34mCadastrar Caminhões\033[m
        [2] \033[34mCadastrar Carga/Volume\033[m
        [3] \033[34mAnalisar Dados\033[m
        [4] \033[34mExibir Dados Específicos\033[m
        [5] \033[34mAlterar Dados\033[m
        [6] \033[34mSair\033[m''')
    print()

    try:
        escolha = int(input('Digite sua Escolha: '))
        if not 0 <= escolha <= 6:
            print('\033[31mPor favor, digite sua escolha em relação ao menu abaixo.\033[m')

        if escolha == 6:
            print('\033[31mSaindo do sistema...\033[m')
            break
        
        if escolha == 1:
            while True:
                print()
                print('''[1] \033[34mCaminhões de Carga\033[m
[2] \033[34mCaminhões Pipa\033[m
[3] \033[34mVoltar ao menu principal\033[m''')
                print()

                escolha_1 = int(input('Digite sua escolha: '))

                if escolha_1 == 3:
                    break
            
                elif escolha_1 == 1:
                    while True:
                        try:
                            caminhoes_carga = str(input('Digite o nome da \033[34mmarca do caminhão de carga\033[m [digite "S" para sair]: ')).upper()

                            if caminhoes_carga == "S":
                                break
                            else:
                                if caminhoes_carga in marcas_carga:
                                    print('\033[31mMarca já cadastrada! Por favor, tente novamente.\033[m')
                                else:
                                    marcas_carga.append(caminhoes_carga)
                                    print('\033[32mMarca cadastrada com sucesso!\033[m')
                        
                        except ValueError:
                            print('Erro: Por favor, digite um nome válido.')

                elif escolha_1 == 2:
                    while True:
                        try:
                            caminhoes_pipa = str(input('Digite o nome da \033[34mmarca do caminhão pipa\033[34m [digite "S" para sair]: ')).upper()

                            if caminhoes_pipa == 'S':
                                break
                            else:
                                if caminhoes_pipa in marcas_pipa:
                                    print('\033[31mMarca já cadastrada! Por favor, tente novamente.\033[m')   
                                else:
                                    marcas_pipa.append(caminhoes_pipa)
                                    print('\033[32mMarca cadastrada com sucesso!\033[m')
                        except ValueError:
                            print('Erro: Por favor, digite um nome válido.')

        if escolha == 2:
            print() 
            print('''[1] \033[34mCastrar Toneladas: Caminhões de Carga\033[m
[2] \033[34mCadastrar Litros: Caminhões Pipa\033[m
[3] \033[34mVoltar ao menu principal\033[m''')
            print()
                
            escolha_2 = int(input('Digite sua escolha: '))

            if escolha_2 == 3:
                break

            if escolha_2 == 1:    
                print('-=' * 40)

                while True:
                    try:
                        kilos = float(input('Digite o número de \033[34mtonelada dos caminhões\033[34m [ou "0" para sair]: '))

                        if kilos == 0:
                            break
                        else:
                            if kilos in kilo:
                                print('\033[31mPeso já cadastrado! Por favor, tente novamente.\033[m')
                            else:
                                kilo.append(kilos)
                                print('\033[32mPeso cadastrado com sucesso!\033[m')
                    except ValueError:
                        print('Erro: Por favor, digite um número válido.')

                print(kilo)
                print('-=' * 40)

                for dados1 in marcas_carga:
                    for dados2 in kilo:
                        while True:
                            try:
                                valores = float(input(f'Qual o valor do caminhão carga de marca \033[32m{dados1}\033[m de peso \033[32m{dados2}\033[m: '))
                                break
                            except ValueError:
                                print('\033[31mErro: Por favor, digite um número válido.\033[m')
                        matriz_carga.append([dados1, dados2, valores])
                        print('\033[32mValores cadastrados com sucesso!\033[m')
                        if len(matriz_carga) == 0:
                            print('\033[31mErro: Não foi possível cadastrar peso pois não foi cadastrado o modelo do caminhão de carga. Por favor, cadastre o modelo e tente novamente.\033[m')
                        
                    print('-' * 60)

            if escolha_2 == 2:
                print('-=' * 40)

                while True:
                    try:
                        litros = float(input('Digite o número de \033[34mLitros dos caminhões\033[34m [ou "0" para sair]: '))

                        if litros == 0:
                            break
                        else:
                            if litros in litro:
                                print('\033[31mLitro já cadastrado! Por favor, tente novamente.\033[m')
                            else:
                                litro.append(litros)
                                print('\033[32mLitros cadastrados com sucesso!\033[m')
                    except ValueError:
                        print('\033[31mErro: Por favor, digite um número válido.\033[m')

                print(litro)
                print('-=' * 40)

                for dados1 in marcas_pipa:
                    for dados2 in litro:
                        while True:
                            try:
                                valores = float(input(f'Qual o valor do caminhão pipa de marca \033[32m{dados1}\033[m de peso \033[32m{dados2}\033[m: '))
                                break
                            except ValueError:
                                print('\033[31mErro: Por favor, digite um nome válido.\033[m')
                        matriz_pipa.append([dados1, dados2, valores])
                        print('\033[32mValores cadastrados com sucesso!\033[m')
                        if len(matriz_pipa) == 0:
                            print('\033[31mErro: Não foi possível cadastrar peso pois não foi cadastrado o modelo do caminhão de carga. Por favor, cadastre o modelo e tente novamente.\033[m')
                    print('-' * 60)

        if escolha == 3:
            print()
            print('''[1] \033[34mAnalisar dados de: Caminhões de Carga\033[m
[2] \033[34mAnalisar dados de: Caminhões Pipa\033[m
[3] \033[34mVoltar ao menu principal\033[m''')
            print()
            
            escolha_3 = int(input('Digite sua escolha: '))

            if escolha_3 == 3:
                break

            if escolha_3 == 1:
                print('-=' * 60)

                print(f'{"ID":<20}{"Marca":<20}{"Capacidade de Carga (TL)":<35}{"Valor por Tonelada (R$)":<20}')

                for indice, dados in enumerate(matriz_carga):
                    print(f'{indice:<20}{dados[0]:<20}{dados[1]:<35}{dados[2]:<20}')

                print()
                if len(matriz_carga) == 0:
                    print('\033[31mNão há valores a analisar pois nenhum modelo foi cadastrado. Por favor, cadastre um modelo e tente novamente.\033[m')
            
            elif escolha_3 == 2:
                print('-=' * 60)

                print(f'{"ID":<20}{"Marca":<20}{"Capacidade de Litros (L)":<35}{"Valor por Metro Cúbico (m^3) (R$)":<20}')

                for indice, dados in enumerate(matriz_pipa):
                    print(f'{indice:<20}{dados[0]:<20}{dados[1]:<35}{dados[2]:<20}')

                print()
                if len(matriz_pipa) == 0:
                    print('\033[31mNão há valores a analisar pois nenhum modelo foi cadastrado. Por favor, cadastre um modelo e tente novamente.\033[m')

        if escolha == 4:
            print()
            print('''[1] \033[34mCaminhões de Carga\033[m
[2] \033[34mCaminhões Pipa\033[m
[3] \033[34mVoltar ao menu principal\033[m''')
            print()
            
            escolha_4 = int(input('Digite sua escolha: '))

            if escolha_4 == 3:
                break

            if escolha_4 == 1:

                print('-=' * 50)
                print(f'{"ID":<20}{"Marca":<20}{"Capacidade de Carga (TL)":<35}{"Valor por Tonelada (R$)":<20}')

                for indice, dados in enumerate(matriz_carga):
                    print(f'{indice:<20}{dados[0]:<20}{dados[1]:<35}{dados[2]:<20}')
                print('-=' * 50)

                while True:
                    try:
                        if len(matriz_carga) == 0:
                            print('\033[31mNão há modelos para analisar especificamente pois nenhum modelo foi cadastrado. Por favor, cadastre um modelo e tente novamente.\033[m')
                            break

                        analisar = int(input('Digite o \033[32mID\033[m a analisar: '))
                        if 0 <= analisar < len(matriz_carga):
                            dados = matriz_carga[analisar]
                            print('=' * 25)
                            print(f'Marca: \033[32m{dados[0]}\033[m\nPeso: \033[32m{dados[1]} Toneladas\033[m\nValor(TL): R$\033[32m{dados[2]:.2f}\033[m')
                            print('=' * 25)
                        else:
                            print(f'\033[31mErro: ID {analisar} não existe!\033[m')
                            continue
                        
                        ir = str(input('Quer continuar analisando? [S/N]: ')).upper()
                        while ir not in 'SN':
                            ir = str(input('Por favor, Digite um \033[31m"S"\033[m ou \033[31m"N"\033[m para continuar: ')).upper()
                        if ir == 'N':
                            break

                    except ValueError:
                        print('\033[31mErro: Por favor, digite um número válido.\033[m')

            elif escolha_4 == 2:
                print('-=' * 50)
                print(f'{"ID":<20}{"Marca":<20}{"Capacidade de Litros (L)":<35}{"Valor por Metro Cúbico (m^3) (R$)":<20}')

                for indice, dados in enumerate(matriz_pipa):
                    print(f'{indice:<20}{dados[0]:<20}{dados[1]:<35}{dados[2]:<20}')
                print('-=' * 50)

                while True:
                    try:
                        if len(matriz_pipa) == 0:
                            print('\033[31mNão há modelos para analisar especificamente pois nenhum modelo foi cadastrado. Por favor, cadastre um modelo e tente novamente.\033[m')
                            break

                        analisar = int(input('Digite o ID a analisar: '))
                        if 0 <= analisar < len(matriz_pipa):
                            dados = matriz_pipa[analisar]
                            print('=' * 25)
                            print(f'Marca: \033[32m{dados[0]}\033[m\nLitro: \033[32m{dados[1]} m^3\033[m\nValor(TL): R$\033[32m{dados[2]:.2f}\033[m')
                            print('=' * 25)
                        else:
                            print(f'\033[31mErro: ID {analisar} não existe!\033[m')
                            continue

                        ir = str(input('Quer continuar analisando? [S/N]: ')).upper()
                        while ir not in 'SN':
                            ir = str(input('Por favor, digite \033[31m"S"\033[m ou \033[31m"N"\033[m para continuar: ')).upper()
                        if ir == 'N':
                            break

                    except ValueError:
                        print('\033[31mErro: Por favor, digite um número válido.\033[m')

        if escolha == 5:
            print()
            print('''[1] \033[34mCaminhões de Carga\033[m
[2] \033[34mCaminhões Pipa\033[m
[3] \033[34mVoltar ao menu principal\033[m''')
            print()
            
            escolha_5 = int(input('Digite sua escolha: '))

            if escolha_5 == 3:
                break

            if escolha_5 == 1:

                print('-=' * 50)
                print(f'{"ID":<20}{"Marca":<20}{"Capacidade de Carga (TL)":<35}{"Valor por Tonelada (R$)":<20}')

                for indice, dados in enumerate(matriz_carga):
                    print(f'{indice:<20}{dados[0]:<20}{dados[1]:<35}{dados[2]:<20}')
                print('-=' * 50)
            
                while True:
                    try:
                        if len(matriz_carga) == 0:
                            print('\033[31mNão é possível alterar dados pois nenhum modelo foi cadastrado. Por favor, cadastre um modelo e tente novamente.\033[m')
                            break
                        print('=' * 25)
                        mudar = int(input('Digite o \033[32mID\033[m da matriz a ser alterada: '))
                        print('=' * 25)
                        if 0 <= mudar < len(matriz_carga):
                            matriz_carga[mudar][2] = float(input('Digite o novo valor: R$'))
                            print('\033[32mValor alterado com sucesso!\033[m')
                        else:
                            print(f'\033[31mErro: ID {mudar} não existe!\033[m')
                            continue
                    except ValueError:
                        print('\033[31mPor favor, Digite um número válido.\033[34m')

                    print('=' * 25)

                    ir = str(input('Quer continuar alterando? [S/N]: ')).upper()
                    while ir not in 'SN':
                        ir = str(input('Por favor, digite \033[31m"S"\033[m ou \033[31m"N"\033[m para continuar: ')).upper()
                    if ir == 'N':
                        break
                    else:
                        continue

            elif escolha_5 == 2:
                print('-=' * 50)
                print(f'{"ID":<20}{"Marca":<20}{"Capacidade de Litros (L)":<35}{"Valor por Metro Cúbico (m^3) (R$)":<20}')

                for indice, dados in enumerate(matriz_pipa):
                    print(f'{indice:<20}{dados[0]:<20}{dados[1]:<35}{dados[2]:<20}')
                print('-=' * 50)

                while True:
                    try:
                        if len(matriz_pipa) == 0:
                            print('\033[31mNão é possível alterar dados pois nenhum modelo foi cadastrado. Por favor, cadastre um modelo e tente novamente.\033[m')
                            break
                        print('=' * 25)
                        mudar = int(input('Digite o \033[32mID\033[m da matriz a ser alterada: '))
                        print('=' * 25)
                        if 0 <= mudar < len(matriz_pipa):
                            matriz_pipa[mudar][2] = float(input('Digite o novo valor: R$'))
                            print('\033[32mValor alterado com sucesso!\033[m')
                        else:
                            print(f'\033[31mErro: ID {mudar} não existe!\033[m')
                            continue
                    except ValueError:
                        print('\033[31mPor favor, Digite um número válido.\033[34m')

                    print('=' * 25)
                    ir = str(input('Quer continuar alterando? [S/N]: ')).upper()
                    while ir not in 'SN':
                        ir = str(input('Por favor, digite \033[31m"S"\033[m ou \033[31m"N"\033[m para continuar: ')).upper()
                    if ir == 'N':
                        break
                    else:
                        continue

        print('-+' * 70)
    except ValueError:
        print('\033[31mPor favor, digite um número válido.\033[m')