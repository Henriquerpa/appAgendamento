import PySimpleGUI as sg

# Definir as opções para os filtros
opcoes_filtro1 = ['Opção 1', 'Opção 2', 'Opção 3']
opcoes_filtro2 = ['Opção A', 'Opção B', 'Opção C']
opcoes_filtro3 = ['Opção X', 'Opção Y', 'Opção Z']
opcoes_filtro4 = ['Opção I', 'Opção II', 'Opção III']

# Definir o layout da janela
layout = [
    [sg.Text('Filtro 1:'), sg.Combo(opcoes_filtro1, default_value='Opção 1')],
    [sg.Text('Filtro 2:'), sg.Combo(opcoes_filtro2, default_value='Opção A')],
    [sg.Text('Filtro 3:'), sg.Combo(opcoes_filtro3, default_value='Opção X')],
    [sg.Text('Filtro 4:'), sg.Combo(opcoes_filtro4, default_value='Opção I')],
    [sg.Button('Filtrar')]
]

# Criar a janela
window = sg.Window('Exemplo de Filtros', layout)

# Loop para ler os eventos da janela
while True:
    event, values = window.read()

    # Verificar se o usuário fechou a janela
    if event == sg.WINDOW_CLOSED:
        break

    # Verificar se o botão "Filtrar" foi clicado
    if event == 'Filtrar':
        filtro1 = values[0]
        filtro2 = values[1]
        filtro3 = values[2]
        filtro4 = values[3]

        # Aplicar os filtros (realizar a lógica desejada)
        # ...
        # Aqui você pode adicionar a lógica para aplicar os filtros nos dados do seu programa

# Fechar a janela
window.close()
