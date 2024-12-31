from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


class PaginaInicial(Screen):
    pass


class LabelConfig(Screen):
    pass


class Lua(Screen):
    pass


class Jupiter(Screen):
    pass


class Netuno(Screen):
    pass


class Venus(Screen):
    pass


class Saturno(Screen):
    pass


class Marte(Screen):
    pass


class Plutao(Screen):
    pass


class Mercurio(Screen):
    pass


class Urano(Screen):
    pass


class Terra(Screen):
    pass


class Sobre_Nos(Screen):
    pass


class ScreenManagement(ScreenManager):

    def menu_label_Config(self):
        self.current = 'labelConfig'

    def switch_to_paginaInicial(self):
        self.current = 'paginaInicial'

    def lua(self):
        self.current = 'lua'

    def jupiter(self):
        self.current = 'jupiter'

    def netuno(self):
        self.current = 'netuno'

    def venus(self):
        self.current = 'venus'

    def saturno(self):
        self.current = 'saturno'

    def marte(self):
        self.current = 'marte'

    def plutao(self):
        self.current = 'plutao'

    def mercurio(self):
        self.current = 'mercurio'

    def urano(self):
        self.current = 'urano'

    def terra(self):
        self.current = 'terra'

    def sobre_nos(self):
        self.current = 'sobre_nos'


class Principal(App):
    Window.size = 1244, 700

    def build(self):
        self.root = ScreenManagement()
        return self.root


Principal().run()
