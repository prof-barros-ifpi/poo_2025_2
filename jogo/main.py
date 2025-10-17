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

j2 = Jogador("Goku")
j3 = Jogador("Vegeta")

j2.mover(10)
j3.mover(30)

print(j2.status())
print(j3.status())

j2.atacar(j3)
