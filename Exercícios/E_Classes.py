class Carros:
    def __init__(self) -> None:
        pass

class Gerenciar_Carros:
    def __init__(self, marca, modelo, ano, cor, placa, disponibilidade, aluguel, venda):
        self.marca = str(marca)
        self.modelo = str(modelo)
        self.ano = int(ano)
        self.cor = str(cor)
        self.placa = str(placa)
        self.disponibilidade = bool(disponibilidade)
        self.aluguel = bool(aluguel)
        self.venda = bool(venda)

    __todos_os_carros = []
    __carros_para_alugar = []

    def C_Adicionar(self, marca, modelo, ano, cor, placa, disponibilidade, aluguel, venda):
        carro = self(marca, modelo, ano, cor, placa, disponibilidade, aluguel, venda)
        self.__todos_os_carros.append(carro)

    def C_Alugar(self):
        for carro in self.__todos_os_carros:
            if Gerenciar_Carros.aluguel == True:
                self.__carros_para_alugar.append(carro)

Gerenciar_Carros.C_Adicionar('Toyota', 'Corolla', 2020, 'Branco', 'ABC-1234', True, False, True)
Gerenciar_Carros.C_Adicionar('Honda', 'Civic', 2019, 'Preto', 'XYZ-5678', False, True, False)
