import PySimpleGUI as sg

# Criar as janelas e estilos(layout)


def janela_cadastro():
    sg.theme('DarkBlack')

cbox_layout = [[sg.Text('Nome        '), sg.Input()],
                [sg.Text('Sobrenome'), sg.Input()]]
            
cbox_layout1 = [[sg.Text('Email        '), sg.Input()],
               [sg.Text('Telefone    '), sg.Input()]]

btn_layout = [[sg.Button('Cadastrar Cliente', size=(20, 1), enable_events=True)]]
btn_layout1 = [[sg.Button('Exportar para Excel',size=(20, 1), enable_events=True)]]

layout = [[sg.Column(cbox_layout),sg.Column(btn_layout)],
          #[sg.Column(cbox_layout1)],
          [sg.Column(cbox_layout1),sg.Column(btn_layout1)],
          #[sg.Button('Exportar para Excel')],
          [sg.Text('Criado por: André Marcos')]
          ]


sg.Window('Cadastro de Clientes', layout=layout, finalize=True)

# Criar as janelas iniciais
janela = janela_cadastro

# Criar um loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    # Quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
