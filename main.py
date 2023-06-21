import PySimpleGUI as sg
import layouts.telas as lt

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

#_____________________________________________________________________________________
NOME_APLCATIVO = 'Agendamento'
THEME = 'DarkTeal12'

#_____________________________________________________________________________________

class WindowPattern:
    def __init__(self):
        self.theme = sg.theme(THEME)
        pass


class MenuPrincipal(WindowPattern):
    def __init__(self):
        super().__init__()

        window = sg.Window(NOME_APLCATIVO,layout= lt.telaInicial()).finalize()
        window.maximize()

        while True:
            event, self.value = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == 'Status Agendamento':
                window.disable()
                StatusAgendamento()
                window.enable()
                window.bring_to_front()


class StatusAgendamento(WindowPattern):
    def __init__(self):
        super().__init__()

        window = sg.Window(NOME_APLCATIVO,layout= lt.statusAgendamento()).finalize()
        window.maximize()
        while True:
            event, self.value = window.read()

            if event == 'Fechar':
                window.disable()
                MenuPrincipal()
                window.enable()
                window.bring_to_front()


            if event == sg.WIN_CLOSED:
                break

           



    

