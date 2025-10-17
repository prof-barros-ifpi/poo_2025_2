# jogador.py
class Jogador:
    """
    Classe que representa o jogador do jogo.
    Demonstra os conceitos de:
    - Classe
    - Atributos
    - Métodos
    - Construtor
    """

    def __init__(self, nome):
        # Construtor - inicializa o estado do objeto
        self.nome = nome
        self.energia = 100
        self.posicao = 0

    def mover(self, passos):
        """Move o jogador para frente ou para trás"""
        self.posicao += passos
        self.energia -= abs(passos) * 2

    def status(self):
        """Exibe o estado atual do jogador"""
        return f"Jogador: {self.nome} | Posição: {self.posicao} | Energia: {self.energia}"

    def descansar(self):
        """Recupera parte da energia"""
        self.energia = min(self.energia + 10, 100)

    #Resposta dos exercícios práticos em sala Versão 0

    def atacar(self, outro_jogador):
        print("Kamehamehaaaaaa........")
        outro_jogador.energia = outro_jogador.energia - 10
        

