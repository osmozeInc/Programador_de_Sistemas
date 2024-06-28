import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.core.window import Window
import dados


class Banco_de_Dados:
    def __init__(self):
        self.conexao = sqlite3.connect('Supermercado.db')
        self.cursor = self.conexao.cursor()

    def Criar_tabelas(self):
        pass

    def Cadastro_db(self, nome, cpf, numero, email, departamento, função, senha):
        nome_db = nome


class Supermercado(App):
    def build(self):
        Window.size = (1280, 720)
        sm = ScreenManager()
        sm.add_widget(Screen_Login(name='login'))
        sm.add_widget(Screen_Cadastro(name='cadastro'))
        return Builder.load_file('Tela.kv')


class Screen_Login(Screen):        
    def get_input_login(self, cpf, senha, departamento):
        pass   


class Screen_Cadastro(Screen, Banco_de_Dados):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        banco = Banco_de_Dados()
    
    def informacoes_de_cadastro(self, nome, cpf, ddd, numero, email, departamento, função, senha, ConfirmSenha):
        Verific = []
        Verific[0], nome_db = Dados.Dados_de_cadastro.VerificNome(nome)
        if Verific == 'Erro': self.ids.nome_cad_error.text = 'Nome inválido'
        Verific[1], cpf_db = Dados.Dados_de_cadastro.VerificCPF(cpf)
        if Verific == 'Erro': self.ids.cpf_cad_error.text = 'CPF inválido'
        Verific[2], ddd_db = Dados.Dados_de_cadastro.VerificDDD(ddd)
        if Verific == 'Erro': self.ids.ddd_cad_error.text = 'DDD inválido'
        Verific[3], numero_db = Dados.Dados_de_cadastro.VerificNumero(numero)
        if Verific == 'Erro': self.ids.numero_cad_error.text = 'Número inválido'
        Verific[4], email_db = Dados.Dados_de_cadastro.VerificEmail(email)
        if Verific == 'Erro': self.ids.email_cad_error.text = 'Email inválido'
        Verific[5], departamento_db = Dados.Dados_de_cadastro.VerificDepartamento(departamento)
        if Verific == 'Erro': self.ids.departamento_cad_error.text = 'Departamento inválido'
        Verific[6], função_db = Dados.Dados_de_cadastro.VerificCargo(função)
        if Verific == 'Erro': self.ids.cargo_cad_error.text = 'Função inválida'
        Verific[7], senha_db = Dados.Dados_de_cadastro.VerificSenha(senha)
        if Verific == 'Erro': self.ids.senha_cad_error.text = 'Senha inválida'
        Verific[8], ConfirmSenha_db = Dados.Dados_de_cadastro.VerificConfirmSenha(ConfirmSenha)
        if Verific == 'Erro': self.ids.ConfirmSenha_cad_error.text = 'Confirmar senha inválida'

        for verific in Verific:
            if verific == 'Erro':
                pass

    

    def spinner_funcao(self, departamento, value):
        if value == 'Entrega':
            self.ids.cargo_cad.values = ('Entregador',)
        elif value == 'Cozinha':
            self.ids.cargo_cad.values = ('Açougueiro', 'Padeiro', 'Peixero', 'Cozinheiro', 'Sommelier de vinhos')
        elif value == 'Atendimento':
            self.ids.cargo_cad.values = ('Operador de caixa', 'Empacotador')
        elif value == 'Estoque':
            self.ids.cargo_cad.values = ('Repositor', 'Estoquista')
        elif value == 'Administração':
            self.ids.cargo_cad.values = ('Gerente', 'Auxiliar administrativo')
        elif value == 'Auxiliar':
            self.ids.cargo_cad.values = ('Segurança,', 'Limpeza')
        else:
            self.ids.cargo_cad.values = ()


banco = Banco_de_Dados()
Supermercado().run()
