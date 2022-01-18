import PySimpleGUI as sg
# Criando Layout
def criar_janela_inicial():
    sg.theme('darkBlue4')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]

    return sg.Window('Todo List', layout=layout, finalize=True)
    # Criando janela
    #janela = criar_janela_inicial()
    # criar as regras dessa janela
   # while True:
    #    event, values = janela.read()
    #if event == sg.WIN_CLOSED:
     #   break
    #if event == 'Nova Tarefa':
     #  janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])
    #elif event == 'Resetar':
      #  janela.close()
       # janela = criar_janela_inicial()