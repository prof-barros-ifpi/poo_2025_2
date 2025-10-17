# main.py
from Jogador import Jogador

# Criação do objeto (instancia da classe)
j1 = Jogador("Anderson")

print("=== Versão 0 do Jogo ===")
print(j1.status())

# Simulação simples
j1.mover(5)
print(j1.status())

j1.descansar()
print(j1.status())
