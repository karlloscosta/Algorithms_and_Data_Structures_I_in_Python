from conta import Conta

contabancaria=[]

contabancaria.append(Conta(titular='karllos', num=1234567)) #cria um novo cliente e adiciona a lista conta bancaria
contabancaria.append(Conta(titular='nestor', num=7654321)) #cria um novo cliente e adiciona a lista conta bancaria

contabancaria[0].deposito(9876) #realiza um deposito na conta de karllos

contabancaria[0].imprime() #imprime os dados de karllos
contabancaria[1].imprime() #imprime os dados de nestor

contabancaria[0].transferencia(contabancaria[1], 2000) #realiza uma transferencia a partir da conta de karllos com destino a de nestor

contabancaria[0].imprime() #imprime os dados atualizados da conta de karllos
contabancaria[1].imprime() #imprime os dados atualizado da consta de nestor
