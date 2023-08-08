#definindo função que lê o arquivo
def ler_arquivo(nome_arquivo):
    lista = [] #lista em branco para receber as sublistas
    try:#try except para testar se ha erros
        with open(nome_arquivo, 'r') as arquivo:#with as -> ja fecha automaticamente o arquivo aberto
            linhas = arquivo.readlines() #cria uma lista com cada linha do arquivo aberto
            for linha in linhas: #estrutura for para acessar cada linha do arquivo
                campos_lista = linha.strip().split('\t')#transforma cada linha em um sublista dividindo no \t, antes verifica se ha espaços no inicio e no final
                lista.append(campos_lista)#adiciona as sublistas a lista antes declarada 
        return lista#retorna lista
    except FileNotFoundError as erro: #caso não encotre o arquivo retorna um erro
        print(erro)
#função que soma os salarios de cada departamento        
def soma_salarios(lista):
    #inicia as somas com zero
    soma_Dep_A = 0
    soma_Dep_B = 0
    soma_Dep_C = 0
    #passa por cada sublista 
    for sublista in lista:
        if len(sublista) >= 4: #verifica se a sublista possui os 4 campos de texto (Funcional, Nome, Dep, Salario)
            departamento = sublista[2] #atribui o departamento a var departamento
            salario = float(sublista[3])#atribui o salario a variavel salario convertendo em um float
            #estrutura if elif para checar a qual departamento o funcionario pertence e efetuar a soma
            if departamento == 'A':
                soma_Dep_A += salario
            elif departamento == 'B':
                soma_Dep_B += salario
            elif departamento == 'C':
                soma_Dep_C += salario

    return soma_Dep_A, soma_Dep_B, soma_Dep_C #retrona os gastos de cada departamento
#função  que imprime o relatório, recebe como argumento a lista de funcionarios, soma dos salarios, e o departamento
def imprime(lista, soma, dep):
    print(f"Folha de pagamento do departamento {dep}:")
    print("FUNCIONAL\t\tNOME\t\t\tDEPARTAMENTO\t\tSALARIO")
    for funcionario in lista:
        if len(funcionario) >= 4 and funcionario[2] == dep:  #Verifica se o funcionário pertence ao Departamento digitado
            print('\t\t\t'.join(funcionario))#agrupa a lista em uma string separando com a formatação \t\t\t
    print (f"VALOR TOTAL GASTO: R$ {soma}\n")
# EXECUÇÃO=
nome_arquivo = 'arq.txt'
arquivo = ler_arquivo(nome_arquivo)
soma_Dep_A, soma_Dep_B, soma_Dep_C = soma_salarios(arquivo)

imprime(arquivo, soma_Dep_A, 'A')
imprime(arquivo, soma_Dep_B, 'B')
imprime(arquivo, soma_Dep_C, 'C')
total = soma_Dep_A+soma_Dep_B+soma_Dep_C
print(f"AS DESPESAS TOTAIS SÃO R$:{total}")
