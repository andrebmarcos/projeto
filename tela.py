import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #layout
        layout =[
            [sg.Text('Nome'),sg.Input()],
            [sg.Text('Idade'),sg.Input()],
            [sg.Button('Enviar Dados')]
        ]
        #Janela
        janela = sg.Window('Dados do Usuiario').layout(layout)
        #Extrair os dados da tela
        self.button, self.values = janela.read()

        def Iniciar(self):
            print (self.values)

            tela = TelaPython()
            tela.Iniciar()


TelaPython()