from Veiculo import Veiculo

class CarroPasseio(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, numero_portas, tipo_combustivel):
        super().__init__(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self._numero_portas = numero_portas
        self._tipo_combustivel = tipo_combustivel

    def calcular_depreciacao(self, anos_uso, taxa_extra):
        depreciacao = anos_uso * taxa_extra
        print(f"Depreciação estimada: {depreciacao * 100:.1f}%")

    def exibir_informacoes(self, detalhado=False):
        super().exibir_informacoes(detalhado)
        if detalhado:
            print(f"Número de portas: {self._numero_portas}")
            print(f"Tipo de combustível: {self._tipo_combustivel}")
