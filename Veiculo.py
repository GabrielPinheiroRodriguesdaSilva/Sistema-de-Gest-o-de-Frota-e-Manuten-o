class Veiculo:
    def __init__(self,marca: str, modelo: str, ano_fabricacao: int, chassi: str, cor: str, quilometragem: float):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.chassi = chassi
        self.cor = cor
        self.quilometragem = quilometragem
   
    def registrar_manutencao(self, tipo: str, custo: float):
        print(f"A manutenção do tipo '{tipo}' teve um custo de R${custo:.2f}.")
    
    def exibir_informacoes(self, detalhado: bool = False):
        if detalhado:
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Ano de Fabricação: {self.ano_fabricacao}")
            print(f"Chassi: {self.chassi}")
            print(f"Cor: {self.cor}")
            print(f"Quilometragem: {self.quilometragem} km")
        else:
            print(f"{self.marca} {self.modelo} - {self.quilometragem} km")
        