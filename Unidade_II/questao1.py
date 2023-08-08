def dados_funcionarios (nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        
        while True:
            linhas = input('informe os dados do funcionario ou enter para prosseguir')
            if not linhas:
                break

        arquivo.write (linhas + '\n')
        linhas = arquivo.readlines()

        for linha in linhas:
            nova_linha = '\t'.join(linha)
            arquivo.write (nova_linha)


#EXECUÇÃO

nome_arquivo = 'arquivo.txt'
arquivo = dados_funcionarios (nome_arquivo)


