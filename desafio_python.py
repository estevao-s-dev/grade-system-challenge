' Sistema de notas UVV '
# libs
import time

# main
def main():
        
        print("Bem vindo!")
        nome_aluno = input("Digite o seu nome por favor: ")
        print("Olá", nome_aluno + "!")
        
        notas_aops()
        nota_prova_regular()
        analise_das_notas()

# soma de notas das aops
def notas_aops():
    
    # adicionar condições caso a nota tenha valor invalido
    aop_1 = input("Digite a nota da AOP 1: ")
    aop_2 = input("Digite a nota da AOP 2: ")
    aop_3 = input("Digite a nota da AOP 3: ")
    total_aop = float(aop_1) + float(aop_2) + float(aop_3)
    
    if total_aop >= 0 and total_aop <= 4:
        
        print("Soma das AOPs:", round(total_aop, 1))
    
    else:

        while total_aop > 4 or total_aop < 0:
    
            print("Soma de notas inválida. Tente novamente...")
            aop_1 = input("Digite a nota da AOP 1: ")
            aop_2 = input("Digite a nota da AOP 2: ")
            aop_3 = input("Digite a nota da AOP 3: ")
            total_aop = float(aop_1) + float(aop_2) + float(aop_3)
        

        
            if total_aop >= 0 and total_aop <= 4:
                
                print("Soma das AOPs:", round(total_aop, 1))
                break

            else:
                
                continue


def nota_prova_regular():
    
    prova_regular = float(input("Digite a nota da prova regular: "))
    
    if prova_regular >= 0 and prova_regular <= 6:
        
        print("Nota da prova regular:", round(prova_regular, 1))
    
    else:
        
        while prova_regular < 0 or prova_regular > 6:
            
            print("Nota inválida, tente novamente...")
            prova_regular = float(input("Digite a nota da prova regular: "))
            
            if prova_regular >= 0 and prova_regular <= 6:
                
                print("Nota na prova regular:", round(prova_regular, 1))
                break
            
            else:
                
                continue

# analise das notas e situacao do aluno
def analise_das_notas():

    def situacao_do_aluno():


main()
