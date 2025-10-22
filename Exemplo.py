from Veiculo import Veiculo
from CarroPasseio import CarroPasseio
from CaminhaoCarga import CaminhaoCarga


if __name__ == "__main__":
    carro = CarroPasseio("Toyota", "Corolla", 2020, "CHS1234", "Prata", 45000, 4, "Gasolina")
    caminhao = CaminhaoCarga("Volvo", "FH16", 2018, "CHS9876", "Branco", 120000, 25.0, 6)

    print(" CARRO DE PASSEIO")
    carro.exibir_informacoes(True)
    carro.registrar_manutencao("Troca de óleo", 350)
    carro.calcular_depreciacao(3, 0.07)

    print("CAMINHÃO DE CARGA")
    caminhao.exibir_informacoes(True)
    caminhao.registrar_manutencao("Revisão de freios", 1200)
    caminhao.registrar_vistoria("Verificação anual", 0)