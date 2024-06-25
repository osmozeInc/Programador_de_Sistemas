import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.core.window import Window


class Banco_de_Dados:
    def __init__(self):
        self.conexao = sqlite3.connect('Supermercado.db')
        self.cursor = self.conexao.cursor()

    def Cadastro_db(self, nome, cpf, numero, email, departamento, função, senha):
        pass

class Screen_Login(Screen):        
    def get_input_login(self, cpf, senha, departamento):
        pass   
        
class Screen_Cadastro(Screen, Banco_de_Dados):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        banco = Banco_de_Dados()
    
    def informacoes_de_cadastro(self, nome, cpf, ddd, numero, email, departamento, função, senha, ConfirmSenha):
        pass

    def spinner_funcao(self, departamento, value):
        if value == 'Entrega':
            self.ids.cargo.values = ('Entregador',)
        elif value == 'Cozinha':
            self.ids.cargo.values = ('Açougueiro', 'Padeiro', 'Peixero', 'Cozinheiro', 'Sommelier de vinhos')
        elif value == 'Atendimento':
            self.ids.cargo.values = ('Operador de caixa', 'Empacotador')
        elif value == 'Estoque':
            self.ids.cargo.values = ('Repositor', 'Estoquista')
        elif value == 'Administração':
            self.ids.cargo.values = ('Gerente', 'Auxiliar administrativo')
        elif value == 'Auxiliar':
            self.ids.cargo.values = ('Segurança,', 'Limpeza')
        else:
            self.ids.cargo.values = ()


class Screen_Gerencia(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Supermercado(App):
    def build(self):
        Window.size = (1280, 720)
        sm = ScreenManager()
        sm.add_widget(Screen_Login(name='login'))
        sm.add_widget(Screen_Cadastro(name='cadastro'))
        sm.add_widget(Screen_Gerencia(name='gerencia'))
        return Builder.load_file('Tela.kv')

banco = Banco_de_Dados()
Supermercado().run()
