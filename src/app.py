from Contas import *







#enter exit del self pedro pagnussat sabe




try:
    conta1 = ContaCorrente(1, 'Caetano', 895266, 1000, -30)
    conta2 = ContaPoupanca(2, 'Guilherme', 123456, 100, 0.1)
    conta3 = ContaInvestimento(3, 'Dalvan', 456789, 1000, 'médio')

    print(conta1)
    print(conta2)
    print(conta3)

    print('Saldo:', conta1.saldo())
    print("O banco possui", ContaBancaria.quantidade_contas, "contas.")
    print("O banco possui", ContaCorrente.quantidade_contas, "contas correntes.")
    print("O banco possui", ContaInvestimento.quantidade_contas, "contas investimento.")
    print("O banco possui", ContaPoupanca.quantidade_contas, "contas poupança.")
    print ("O rendimento em 30 dias da conta 1 é de: R$ " + str(conta1.consulta_rendimento(30)))
    print ("O rendimento em 30 dias da conta 2 é de: R$ " + str(conta1.consulta_rendimento(30)))
    print ("O rendimento em 30 dias da conta 3 é de: R$ " + str(conta1.consulta_rendimento(30)))

    #print ("Tentando depositar R$ -30 na conta 1")
    #conta1.deposito(-30)

    #print ("Tentando sacar valor negativo da conta poupança")
    #conta1.saque(-30)

    #print ("Tentando sacar valor acima do limite na conta corrente")
    #conta1.saque(2000)

    #print ("Tentando saque acima do saldo na poupança")
    #conta2.saque(10000)

    #print ("Tentando criar conta com limite positivo")
    #conta5 = ContaCorrente(1, 'Caetano', 895266, 1000, 30)

    #print ("Tentando criar conta com número inválido")
    #conta6 = ContaCorrente(100000, 'Caetano', 895266, 1000, -30)

    #print ("Tentando criar conta com nome inválido")
    #conta7 = ContaCorrente(1000, 'Caetano Brown da silva rodrigues orlenas e braganla de matos de silveira e oliveira de matos 1234567899010122121232232', 895266, 1000, -30)

    print ("Tentando criar conta com CPF inválido")
    conta8 = ContaCorrente(1000, 'Caetano', 8952430201, 1000, -30)

except ValorMonetarioNegativo as e:
    print (e)
except SaldoInsuficiente as e:
    print (e)
except SaqueAcimaDoLimite as e:
    print (e)
except LimitePrecisaSerNegativo as e:
    print (e)
except NumeroDeContaInvalido as e:
    print (e)
except NomeInvalido as e:
    print(e)
except CPFInvalido as e:
    print(e)


