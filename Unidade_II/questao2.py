def recebe_notas (nome_arquivo):

    with open(nome_arquivo, 'a') as arquivo:

        while True:
            linhas = input('informe o nome e as notas de um aluno ou enter para prosseguir')
            if not linhas:
                break
            arquivo.write(linhas + '\n')

            linhas = arquivo.readlines()
            for linha in linhas:
                nova_linha = '\t'.join(linha)
                arquivo.write(nova_linha)

#execução

arquivo = 'alunos.txt'
nome_arquivo = recebe_notas (arquivo)
