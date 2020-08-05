#Lançamento de notas de vários alunos (nome e sexo)
#cada aluno terá 3 notas (nenhuma <0 e >10)
#calcular média do aluno
# media >=7: Aprovado; media >=4 e <7: Exame; média <4: Reprovado
# Total de Alunos cadastrados;
######################################## Resultados Relativos:
# %Aprovações;
# %Exame
# %Reprovados
######################################## Resultados absolutos:
# Total aprovação feminino e masculino;
# Total exame feminino e masculino;
# Total repovação feminino masculino;
##############################################################################################

Invalida = 'OPÇÃO INVÁLIDA'
msgInforme = '\nPor favor informe S(Sim) ou N(Não): '

continuar =input('Deseja iniciar o sistema? (S/N): ').upper()
while continuar!= 'S' and continuar != 'N':
    print(Invalida)
    continuar = input(msgInforme).upper()

totalAlunos = 0
totalMasculino = 0
totalFeminino = 0
Aprovados = 0
Exame = 0
Reprovados = 0

totalAprovadoFeminino = 0
totalAprovadoMasculino = 0
totalEmExameFeminino = 0
totalEmExameMasculino = 0
totalReprovadoFeminino = 0
totalReprovadoMasculino = 0

while continuar.upper() == 'S':
    totalAlunos +=1
    nome = input('Informe o nome do aluno: ')
    sexo = input('Informe o sexo do aluno (M/F): ').upper()
    while(sexo != 'M' and sexo != 'F'):
        print(Invalida)
        sexo = input('Informe M(Masculino) ou F(Feminino): ').upper()
        if(sexo =='M'):
            totalMasculino +=1
        else:
            totalFeminino +=1

    for cont in range(1,4):
        if cont==1:
            nota1 = int(input('Informe N1: '))
            while nota1<0 or nota1>10:
                nota1=int(input('N1 inválida. Valor deve ser entre 0 e 10: '))
        elif cont==2:
            nota2 = int(input('Informe N2: '))
            while nota2<0 or nota2>10:
                nota2=int(input('N2 inválida. Valor deve ser entre 0 e 10: '))
        else:
            nota3 = int(input('Informe N3: '))
            while nota3<0 or nota3>10:
                nota3=int(input('N3 inválida. Valor deve ser entre 0 e 10: '))

    media = (nota1 + nota2 + nota3)/3
    print('\nSua média foi: ',str(media))
    if media >=7 and sexo == 'F':
        Aprovados +=1
        totalAprovadoFeminino +=1
        print('A aluna',nome.upper(),'foi APROVADA!')
    elif media >=4 and sexo == 'F':
        Exame +=1
        totalEmExameFeminino += 1
        print('A aluna',nome.upper(),'está de EXAME.')
    elif media < 4 and sexo == 'F':
        Reprovados += 1
        totalReprovadoFeminino += 1
        print('A aluna', nome.upper(), 'está de REPROVADA.')
    elif media >=7 and sexo == 'M':
        Aprovados +=1
        totalAprovadoMasculino +=1
        print('O aluno',nome.upper(),'foi APROVADO!')
    elif media >=4 and sexo == 'M':
        Exame +=1
        totalEmExameMasculino += 1
        print('O aluno',nome.upper(),'está de EXAME.')
    else:
        Reprovados +=1
        totalReprovadoMasculino += 1
        print('O aluno',nome.upper(),'está REPROVADO.')

    continuar = input('\nDeseja efetuar outro lançamento? (S/N): ')
    while continuar.upper() != 'S' and continuar.upper() != 'N':
        continuar = input('Opção inválida. Informe S(Sim) ou N(Não): ')

else:
    print(('\n FIM DOS LANÇAMENTOS \n').center(143,'#'))

print('\nTotal de Alunos cadastrados: ' +str(totalAlunos),'\n')
print((' RESULTADOS RELATIVOS ').center(60,'='))
print('\nPercentual de alunos APROVADOS:',(Aprovados*100)/totalAlunos,'%')
print('Percentual de alunos EM EXAME:',(Exame*100)/totalAlunos,'%')
print('Percentual de alunos REPROVADOS:',(Reprovados*100)/totalAlunos,'%\n')
print((' RESULTADOS ABSOLUTOS ').center(60,'='))
print('\nQuantidade de pessoas do sexo feminino APROVADAS:',totalAprovadoFeminino)
print('Quantidade de pessoas do sexo feminino EM EXAME:',totalEmExameFeminino)
print('Quantidade de pessoas do sexo feminino REPROVADAS:',totalReprovadoFeminino)
print('\nQuantidade de pessoas do sexo masculino APROVADAS:',totalAprovadoMasculino)
print('Quantidade de pessoas do sexo masculino EM EXAME:',totalEmExameMasculino)
print('Quantidade de pessoas do sexo masculino REPROVADAS:',totalReprovadoMasculino,'\n')
print(('\n FIM DO RELATÓRIO \n').center(140,'#'))