' Sistema de notas UVV '


# main
def main():
        
        print                   ("Bem vindo!")
        nome_aluno              = input("Digite o seu nome por favor: ")
        print                   ("Olá", nome_aluno + "!")
        
        resultado_aops          = notas_aops()
        resultado_prova_regular = nota_prova_regular()
        print                   ("Resultado nas AOPs: ", resultado_aops)
        print                   ("Resultado na Prova Regular: ", resultado_prova_regular)

        status_do_aluno         = analise_das_notas(resultado_aops, resultado_prova_regular, nome_aluno)
        
        

# notas das aops
def notas_aops():
    
        
    aop_1 = float(input("Digite a nota da AOP 1: "))

    while aop_1 < 0 or aop_1 > 1:

        print   ("Valor inválido, digite novamente...")
        aop_1   = float(input("Digite a nota da AOP 1: "))
    
    aop_2 = float(input("Digite a nota da AOP 2: "))
    
    while aop_2 < 0 or aop_2 > 2:
        
        print   ("Valor inválido, digite novamente...")
        aop_2   = float(input("Digite a nota da AOP 2: "))
    

    aop_3 = float(input("Digite a nota da AOP 3: "))
    
    while aop_3 < 0 or aop_3 > 1:
        
        print   ("Valor inválido, digite novamente...")
        aop_3   = float(input("Digite a nota da AOP 3: "))
    

    total_aops  = aop_1 + aop_2 + aop_3
    print       ("Soma das AOPs:", round(total_aops, 1))
    return      total_aops

# prova regular
def nota_prova_regular():
    
    prova_regular = float(input("Digite a nota da prova regular: "))

    
    if prova_regular >= 0 and prova_regular <= 6:
        
        print   ("Nota da prova regular:", round(prova_regular, 1))
        return  prova_regular
    
    else:
        
        while prova_regular < 0 or prova_regular > 6:
            
            print           ("Nota inválida, tente novamente...")
            prova_regular   = float(input("Digite a nota da prova regular: "))
            
            if prova_regular >= 0 and prova_regular <= 6:
                
                print       ("Nota na prova regular:", round(prova_regular, 1))
                return      prova_regular
                break
            
            else:
                
                continue


# analise das notas e status do aluno
def analise_das_notas(resultado_aops, resultado_prova_regular, nome_aluno):
    
    x = resultado_aops
    y = resultado_prova_regular
    z = x + y
    
    if z >= 7:
        
        print   (nome_aluno, "- Aprovado Direto")
    
    if z < 3:
        
        print   (nome_aluno, "- Reprovado Direto")

    if z >= 3 and z < 7:
        
        print   (nome_aluno, "- Em Recuperacao")

        nota_prova_recuperacao = float(input("Digite a nota na prova de recuperacao: "))
        
        while nota_prova_recuperacao < 0 or nota_prova_recuperacao > 10:
            
            print                   ("Nota invalida, digite novamente...")
            nota_prova_recuperacao  = float(input("Digite a nota na prova de recuperacao: "))
        
        
        resultado_geral = (x + y + nota_prova_recuperacao) / 2
        
        if resultado_geral >= 5:

            print(nome_aluno, "- Aprovado na Recuperacao")
        
        else:

            print(nome_aluno, "- Reprovado na Recuperacao")


main()
