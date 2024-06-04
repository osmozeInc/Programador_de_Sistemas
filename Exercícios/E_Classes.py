class Carros:
    def __init__(self, marca, modelo, aluguel) -> None:
        self.marca = marca
        self.modelo = modelo
        self.aluguel = aluguel

class Gerenciar_Carros:
    def __init__(self):
        self.__todos_os_carros = []
        self.carros_para_alugar = []

    def C_Adicionar(self, marca, modelo, aluguel):
        carro = Carros(marca, modelo, aluguel)
        self.__todos_os_carros.append(carro)

    def C_Alugar(self):
        for carro in self.__todos_os_carros:
            if carro.aluguel:
                self.carros_para_alugar.append(carro)

class Cliente:
    def __init__(self, gerenciador) -> None:
        self.gerenciador = gerenciador

    def Alugar(self):
        self.gerenciador.C_Alugar()
        print("Carros disponíveis para serem alugados:")
        for carro in self.gerenciador.carros_para_alugar:
            print(carro.marca, carro.modelo)

# Criar uma instância de Gerenciar_Carros
gerenciador = Gerenciar_Carros()

# Adicionar carros
gerenciador.C_Adicionar('Toyota', 'Corolla', True)
gerenciador.C_Adicionar('Honda', 'Civic', False)
gerenciador.C_Adicionar('Ford', 'Focus', True)
gerenciador.C_Adicionar('Chevrolet', 'Cruze', False)
gerenciador.C_Adicionar('Volkswagen', 'Golf', True)
gerenciador.C_Adicionar('BMW', 'X1', False)
gerenciador.C_Adicionar('Audi', 'A4', True)
gerenciador.C_Adicionar('Mercedes-Benz', 'C-Class', False)
gerenciador.C_Adicionar('Hyundai', 'Elantra', True)
gerenciador.C_Adicionar('Kia', 'Sportage', False)

# Criar uma instância de Cliente e chamar o método Alugar
cliente = Cliente(gerenciador)
cliente.Alugar()
