from Banco.Contas import *
from Banco.Erros import *
from Banco.Moeda import *
import sys

# não consegui implementar isso
args = sys.argv[1:]

individuos = str('1.txt 2.txt').split()
pasta = "../individuos/"

for individuo in individuos:
    with open ((pasta+individuo), 'r', encoding='utf-8') as arquivo:
        comandos =[]
        for line in arquivo:
            linha = line.strip().split(":")
            comandos.append(linha)

        for i in range (2, len(comandos)):
            nome = comandos[0][0]
            cpf = comandos[1][1]

            # Criando contas
            if comandos[i][0] == "criar":
                if comandos[i][1] == " contaInvestimento":
                    print ("Criando conta investimento")
                    conta_inv_teste = ContaInvestimento(int(comandos[i+2][1]), nome, int(cpf), float(comandos[i+1][1]), comandos[i+3][1])
                    print (conta_inv_teste)
                elif comandos[i][1] == " contaCorrente":
                    print("Criando conta corrente")
                    conta_corr_teste = ContaCorrente(int(comandos[i+2][1]), nome, int(cpf), float(comandos[i+1][1]), float(comandos[i + 3][1]))
                    print(conta_corr_teste)
                elif comandos[i][1] == " contaPoupanca":
                    print("Criando conta poupança")
                    conta_poup_teste = ContaPoupanca(int(comandos[i + 2][1]), nome, int(cpf), float(comandos[i + 1][1]),
                                                     float(comandos[i + 3][1]))
                    print(conta_poup_teste)

            # Sacando valores
            elif comandos[i][0] == "sacar":
                saque = comandos[i][1].strip().split(" ")
                if saque[0] == "contaInvestimento":
                    print ("sacando da conta inv")
                    conta_inv_teste.saque(float(saque[2]))
                elif saque[0] == "contaPoupanca":
                    print("sacando da conta poup")
                    conta_poup_teste.saque(float(saque[2]))
                elif saque[0] == "contaCorrente":
                    print("sacando da conta corre")
                    conta_corr_teste.saque(float(saque[2]))

            # Depositando valores
            elif comandos[i][0] == "depositar":
                deposito = comandos[i][1].strip().split(" ")
                if deposito [0]  == "contaInvestimento":
                    print("depositando da conta inv")
                    conta_inv_teste.deposito(float(deposito[2]))
                elif deposito [0]  == "contaPoupanca":
                    print("depositando da conta poup")
                    conta_poup_teste.deposito(float(deposito[2]))
                elif deposito [0]  == "contaCorrente":
                    print("depositando da conta corr")
                    conta_corr_teste.deposito(float(deposito[2]))


            # Vendo saldos
            elif comandos[i][0] == "saldo":
                ver_saldo = comandos[i][1].strip()
                if ver_saldo == "contaCorrente":
                    print ("O saldo da conta corrente é: ", conta_corr_teste.saldo)
                elif ver_saldo == "contaPoupanca":
                    print ("O saldo da conta poupança é: ", conta_poup_teste.saldo)
                elif ver_saldo == "contaInvestimento":
                    print ("O saldo da conta investimento é: ", conta_inv_teste.saldo)

            # Consultando rendimentos
            elif comandos[i][0] == "rendimento":
                rendimentos = comandos[i][1].strip().split(" ")
                print ("Rendimento", rendimentos)

# criado para demonstrar alguns erros e algumas funções
try:
    conta1 = ContaCorrente(1, 'Caetano - Teste', 895266, 1000, -30)
    conta2 = ContaPoupanca(2, 'Guilherme- Teste', 123456, 100, 0.1)
    conta3 = ContaInvestimento(3, 'Roberto - Teste', 456789, 1000, 'médio')

    print(conta1)
    print(conta2)
    print(conta3)

    print("------------Contas de teste---------")
    print("O banco possui", ContaBancaria.status_contas(), "contas.")
    print("O banco possui", ContaCorrente.quantidade_contas, "contas correntes.")
    print("O banco possui", ContaInvestimento.quantidade_contas, "contas investimento.")
    print("O banco possui", ContaPoupanca.quantidade_contas, "contas poupança.")
    print ("O rendimento em 30 dias da conta 1 é de: R$ " + str(conta1.consulta_rendimento(30)))
    print ("O rendimento em 30 dias da conta 2 é de: R$ " + str(conta1.consulta_rendimento(30)))
    print ("O rendimento em 30 dias da conta 3 é de: R$ " + str(conta1.consulta_rendimento(30)))
    print ("Saque verboso", ContaBancaria.saque_verboso(conta1, 30))
    # Alguns testes de erros. Deixei para mostrar que funcionam

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

    #print ("Tentando criar conta com CPF inválido")
    #conta8 = ContaCorrente(1000, 'Caetano', -8952430201, 1000, -30)

    print("O banco possui", ContaBancaria.quantidade_contas, "contas.")



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


