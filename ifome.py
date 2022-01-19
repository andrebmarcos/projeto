import PySimpleGUI as sg

#Criar as janelas e estilos(layout)
def janela_login():
    sg.theme('HotDogStand')
    layout =[
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)
def janela_pedido():
    sg.theme('HotDogStand')
    layout =[
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Calabresa',key='pizza1'), sg.Checkbox('Pizza Portuguesa',key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)
#Criari as janelas iniciais
janela1, janela2 = janela_login(), None
#Criar um loop de leitura de eventos
while True:
    window,event,values = sg.read_all_windows()
    #Quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    #Quabndo queremos ir para proxima janela
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide
        janela1.un_hide()
    if window == janela2 and event == 'Fazer Pedido':
        if values ['pizza1'] == True and values ['pizza2']== True:
            sg.popup('Foram solicitados uma pizza de Calabresa e uma pizza Portuguesa')
        elif values ['pizza1'] == True:
            sg.popup('Foram solicitados uma pizza de Calabresa')
        elif values ['pizza2'] == True:
            sg.popup('Foram solicitados uma pizza Portuguesa')
    #Quando queremos voltar oara janela anterior
#Lógica de oque deve acontecer ai clicar nos botões