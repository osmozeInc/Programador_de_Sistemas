class Concesonaria:
    def __init__(self) -> None:
        pass

class Carros:
    def __init__(self, marca, modelo, ano, cor, placa, disponibilidade):
        self.marca = str(marca)
        self.modelo = str(modelo)
        self.ano = int(ano)
        self.cor = str(cor)
        self.placa = str(placa)
        self.disponibilidade = bool(disponibilidade)

    def C_Todos():
        pass

    def C_Alugar():
        carros_para_alugar = []
