import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.core.window import Window


class Screen_Login(Screen):        
    def get_input_login(self, cpf, senha, departamento):
        pass   
        
class Screen_Cadastro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.departamento.bind(text=self.spinner_funcao)

    def spinner_funcao(self, instance, value):
        if value == 'Entrega':
            self.funcao.values = ['Entregador']
        elif value == 'Cozinha':
            self.funcao.values = ['Açougueiro', 'Padeiro', 'Peixero', 'Cozinheiro', 'Sommelier de vinhos']
        elif value == 'Atendimento':
            self.funcao.values = ['Operador de caixa', 'Empacotador']
        elif value == 'Estoque':
            self.funcao.values = ['Repositor', 'Estoquista']
        elif value == 'Administração':
            self.funcao.values = ['Gerente', 'Auxiliar administrativo']
        elif value == 'Auxiliar':
            self.funcao.values = ['Segurança,', 'Limpeza']
        else:
            self.funcao.values = []

    def get_input_cadastro(self, nome, cpf, numero, email, departamento, função, senha):
        pass

class Supermercado(App):
    def build(self):
        Window.size = (1280, 720)
        sm = ScreenManager()
        sm.add_widget(Screen_Login(name='login'))
        sm.add_widget(Screen_Cadastro(name='cadastro'))
        return Builder.load_file('Tela.kv')


Supermercado().run()
