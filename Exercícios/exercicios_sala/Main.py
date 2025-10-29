from Conta import Conta
c1 = Conta(1000.00, "1234")
c2 = Conta(300.0,"098-66")

c1.exibir_informacoes() #Saldo = 1000.0 
#c2.exibir_informacoes()

print("Ocorreu um saque")
c1.sacar(350.00)
print("Valores após o saque:")

c1.exibir_informacoes() # Saldo = 650.0


print("Ocorreu outro saque")
c1.sacar(670.00)
print("Valores após o segundo saque:")

c1.exibir_informacoes() # saldo = -20
