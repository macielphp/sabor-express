import os

restaurantes = [{'nome':'Praça', 'categoria': 'Arabe', 'ativo':False},
                {'nome':'Panni', 'categoria': 'Espano', 'ativo':True},
                {'nome':'Canto', 'categoria': 'Grego', 'ativo':False}]
def exibir_nome_do_programa():
    print('Sabor Express\n')
def exibir_opcoes():
    print('1. Cadastrar restaurante.')
    print('2. Listar restaurante.')
    print('3. Ativar restaurante.')
    print('4. Sair.')

def finalizar__app():
    exibir_subtitulo('Finalizar app\n')
def voltar_ao_menu_principal():
    input('Digite uma tecla oara voltar para o menu principal: ')
    main()
def opcao_invalida():
    print('Opção inválida.\n')
    voltar_ao_menu_principal()
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja começar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'Ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante: {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante.')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']: 
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_ao_menu_principal()
def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

     
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')
        
    voltar_ao_menu_principal()
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            print('Cadastrar novo restaurante')
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Lista de restaurantes: ')
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar__app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()