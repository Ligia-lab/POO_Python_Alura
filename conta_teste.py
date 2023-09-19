from conta import Conta

conta1 = Conta(112, 'Ligia', 55, 1000)
conta2 = Conta(222, 'Danilo' , 100, 1000)

print('========')
conta1.extrato()
conta2.extrato()
print('========')
conta1.deposita(100)
conta1.extrato()
print('========')

conta2.saca(20)
conta2.extrato()
print('========')
conta2.transfere(30, conta1)
conta1.extrato()
conta2.extrato()
print('========')

print(conta2.titular)
print('========')
print(Conta.codigo_banco())
cod = Conta.codigos_bancos()
print(cod['Caixa'])
print('========')