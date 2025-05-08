from biblioteca import ContaBancaria

conta = ContaBancaria("12345-6", "João Silva")
conta.ativar_conta()
conta.depositar(500)
conta.verificar_saldo()
conta.sacar(200)
conta.verificar_saldo()
conta.desativar_conta()
conta.sacar(300)
conta.sacar(300)
conta.desativar_conta()
