from time import sleep
import os

def Solar():
    while True:
        welcome = int(input('''
          |================================================|   
          |              B E M - V I N D O                 | 
          |================================================| 
          |                                                | 
          |         [ 1 ] SISTEMA SOLAR                    | 
          |         [ 2 ] Sobre nos                        | 
          |         [ 0 ] Sair                             | 
          |================================================|      
              
          Sua Escolha :  '''))
        print()
        print('AGUARDE.....')
        sleep(2)
        print()
        if welcome == 1:
            s_solar()

        elif welcome == 2:
            sobre()

        elif welcome == 0:
            print('''
            
                OBRIGADO POR USAR NOSSO PROJETO EM DESENVOLVIMENTO
                _AUTOR_: CORTEZ
            
            ''')
            break


def s_solar():
    while True:
        solar = int(input('''
        
            |================================================|
            |       S I S T E M A        S O L A R           |
            |================================================|
            |                                                |
            |   [ 1 ] SOL               [ 7 ] MARTE          |
            |   [ 2 ] LUA               [ 8 ] PLUTÃO         |
            |   [ 3 ] JÚPITER           [ 9 ] MERCÚRIO       |
            |   [ 4 ] NETUNO            [ 10 ] URANO         |
            |   [ 5 ] VÊNUS             [ 11 ] TERRA         |
            |   [ 6 ] SATURNO                                |
            |================================================|
            
            Escolha :   '''))
        print('Buscando...')
        os.system('cls')
        print('LOADING...')
        sleep(2)
        print()
        if solar == 1:
            print('''
                            |=================================|
                            |             S O L               |
                            |=================================|
                            | Estrela                         |
                            | Diâmetro: 1.392.000 km          |
                            | Temperatura: 6.000 °C           |
                            | Distância da Terra: 149.597.870 |
                            |=================================|                   

                        ''')
            verificar = str(input('DESEJA CONTINUAR [S/N]: '))
            os.system('cls')
            if verificar == 's':
                continue
            elif verificar == 'n':
                break

        elif solar == 2:
            print('''
                          |===================================|
                          |             L U A                 |
                          |===================================|
                          | SATÉLITE DA TERRA                 |
                          | Diâmetro: 3.473 km                |
                          | Temperatura: de 120 °C a -100 °C  |
                          | Distância do Sol: 152.369.000 km  |
                          | Distância da Terra: 405.530 km    |
                          |===================================|                   
    
                                    ''')
            verificar = str(input('DESEJA CONTINUAR [S/N]: '))
            os.system('cls')
            if verificar == 's':
                continue
            elif verificar == 'n':
                break

        elif solar == 3:
            print('''
                    
                          |=========================================================|
                          |                      JÚPITER                            |
                          |=========================================================|
                          | Planeta                                                 |
                          | Diâmetro: 142.984 km                                    |
                          | Distância do Sol: 778.000.000 km                        |
                          | Temperatura: - 153 °C                                   |
                          | Duração do Dia: 9,84 Horas Terrestres                   |
                          | Duração do Ano: 11,86 Anos Terrestres                   |
                          | Satélites: 12 entre eles: Calixto,Europa,Ganimedes e IO |
                          |=========================================================|                 
            ''')
            verificar = str(input('DESEJA CONTINUAR [S/N]: '))
            os.system('cls')
            if verificar == 's':
                continue
            elif verificar == 'n':
                break

        elif solar == 4:
            print('''
                          |=========================================================|
                          |                       NETUNO                            |
                          |=========================================================|
                          | Planeta                                                 |
                          | Diâmetro: 49.528  km                                    |
                          | Distância do Sol: 4.497.000.000 km                      |
                          | Temperatura: - 225 °C                                   |
                          | Duração do Dia: 19,2 Horas Terrestres                   |
                          | Duração do Ano: 164,79 Anos Terrestres                  |
                          | Satélites: 2 Nereida e Tritão                           |
                          |=========================================================|      
            ''')
            verificar = str(input('DESEJA CONTINUAR [S/N]: '))
            os.system('cls')
            if verificar == 's':
                continue
            elif verificar == 'n':
                break

        elif solar == 5:
            print('''
                          |=========================================================|
                          |                       VÊNUS                             |
                          |=========================================================|
                          | Planeta                                                 |
                          | Diâmetro: 12.102  km                                    |
                          | Distância do Sol: 108.000.000 km                        |
                          | Temperatura: - 457 °C                                   |
                          | Duração do Dia: 243,01 Horas Terrestres                 |
                          | Duração do Ano: 224,7 Dias Terrestres                   |
                          | Satélites: Não Tem                                      |
                          |=========================================================|                   
            ''')
            verificar = str(input('DESEJA CONTINUAR [S/N]: '))
            os.system('cls')
            if verificar == 's':
                continue
            elif verificar == 'n':
                break

        elif solar == 6:
            print('''
            
                          |=========================================================|
                          |                       SATURNO                           |
                          |=========================================================|
                          | Planeta                                                 |
                          | Diâmetro: 102.660  km                                   |
                          | Distância do Sol: 1.427.000.000 km                      |
                          | Temperatura: - 185 °C                                   |
                          | Duração do Dia: 10,23 Horas Terrestres                  |
                          | Duração do Ano: 29,46 Anos Terrestres                   |
                          | Satélites: 15 Entre Eles: Titã, Mimas e Encélado        |
                          |=========================================================|                  
            ''')
            verificar = str(input('DESEJA CONTINUAR [S/N]: '))
            os.system('cls')
            if verificar == 's':
                continue
            elif verificar == 'n':
                break

        elif solar == 7:
            print('''
                          |=========================================================|
                          |                       MARTE                             |
                          |=========================================================|
                          | Planeta                                                 |
                          | Diâmetro: 6.786 km                                      |
                          | Distância do Sol: 228.000.000 km                        |
                          | Temperatura: De -137 a 37 °C                            |
                          | Duração do Dia: 24,623 Horas Terrestres                 |
                          | Duração do Ano: 1,88 Anos Terrestres                    |
                          | Satélites: 2 Fobos e Delmos                             |
                          |=========================================================|                                
            ''')
            verificar = str(input('DESEJA CONTINUAR [S/N]: '))
            os.system('cls')
            if verificar == 's':
                continue
            elif verificar == 'n':
                break

        elif solar == 8:
            print('''
                          |=========================================================|
                          |                       PLUTÃO                            |
                          |=========================================================|
                          | Planeta                                                 |
                          | Diâmetro: 2.300 km                                      |
                          | Distância do Sol: 5.900.000.000 km                      |
                          | Temperatura: -236 °C                                    |
                          | Duração do Dia: 6,39 Horas Terrestres                   |
                          | Duração do Ano: 248,54 Anos Terrestres                  |
                          | Satélites: 1 Caronte                                    |
                          |=========================================================|            
            ''')
            verificar = str(input('DESEJA CONTINUAR [S/N]: '))
            os.system('cls')
            if verificar == 's':
                continue
            elif verificar == 'n':
                break

        elif solar == 9:
            print('''
                          |=========================================================|
                          |                       MERCÚRIO                          |
                          |=========================================================|
                          | Planeta                                                 |
                          | Diâmetro: 4.878 km                                      |
                          | Distância do Sol: 58.000.000 km                         |
                          | Temperatura: De -173 a 427 °C                           |
                          | Duração do Dia: 58,65 Horas Terrestres                  |
                          | Duração do Ano: 87,97 Anos Terrestres                   |
                          | Satélites: Não Tem                                      |
                          |=========================================================|          
            ''')
            verificar = str(input('DESEJA CONTINUAR [S/N]: '))
            os.system('cls')
            if verificar == 's':
                continue
            elif verificar == 'n':
                break

        elif solar == 10:
            print('''
                          |=========================================================|
                          |                       URANO                             |
                          |=========================================================|
                          | Planeta                                                 |
                          | Diâmetro: 51.118 km                                     |
                          | Distância do Sol: 2.870.000.000 km                      |
                          | Temperatura: -214 °C                                    |
                          | Duração do Dia: 17,9 Horas Terrestres                   |
                          | Duração do Ano: 84,01 Anos Terrestres                   |
                          | Satélites: 15 Entre Eles: Titânia,Oberon,Miranda e Ariel|
                          |=========================================================|      
            ''')
            verificar = str(input('DESEJA CONTINUAR [S/N]: '))
            os.system('cls')
            if verificar == 's':
                continue
            elif verificar == 'n':
                break

        elif solar == 11:
            print(''' 
                          |=========================================================|
                          |                       TERRA                             |
                          |=========================================================|
                          | Planeta                                                 |
                          | Diâmetro: 12.756 km                                     |
                          | Distância do Sol: 150.000.000 km                        |
                          | Temperatura: -70 A 55 °C                                |
                          | Duração do Dia: 23,92 Horas Terrestres                  |
                          | Duração do Ano: 365,25 Anos Terrestres                  |
                          | Satélites: Lua                                          |
                          | Idade: Aproximadamente 4,6 Bilhões de Anos              |
                          |=========================================================|        
            ''')
            verificar = str(input('DESEJA CONTINUAR [S/N]: '))
            os.system('cls')
            if verificar == 's':
                continue
            elif verificar == 'n':
                break


def sobre():
    while True:
        print('Sistema Desenvolvido por: CORTEZ')
        sleep(2)
        print()
        print('Versão 0.1')
        sleep(1)
        print()
        print('Sistema Basico Sobre Astronomia')
        sleep(1)
        print()
        print('Desenvolvido em Python')
        sleep(1)
        print()
        print('Novas Versões em Breve.....')
        print()

        verificar = str(input('PRECIONE [S] PARA VOLTAR: '))
        os.system('cls')
        if verificar == 's':
            break


Solar()
