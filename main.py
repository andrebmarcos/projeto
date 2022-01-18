from ast import Break
import PySimpleGUI as sg


class criar_janela_inicial:
    def __init__(self):
        sg.theme('darkBlue4')
        linha = [
        [sg.Checkbox(''), sg.Input('')]
        ]
        # layout
        layout = [
        [sg.Frame('Tarefas', layout=linha, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]

        return sg.Window('Todo List', layout=layout, finalize=True)
        # Janela
    janela = criar_janela_inicial()

        # Extrair os dados da tela
    while True:
        event, values = janela.read()
if event == sg.WIN_CLOSED:
break
if event == 'Nova Tarefa':
       janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])
elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()