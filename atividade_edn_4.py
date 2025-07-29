#=================================
# ATIVIDADE PRÁTICA 04 - EDN
#=================================

def calculadora_basica():
    print("\n=== Calculadora Básica ===")
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: Divisão por zero.")
                return
            resultado = num1 / num2
        else:
            print("Operação inválida.")
            return

        print(f"Resultado: {resultado}")
    except ValueError:
        print("Por favor, digite números válidos.")

def media_notas():
    print("\n=== Cálculo de Média ===")
    try:
        n = int(input("Quantos alunos? "))
        total = 0
        for i in range(n):
            nota = float(input(f"Nota do aluno {i+1}: "))
            total += nota
        media = total / n
        print(f"Média da turma: {media:.2f}")
    except ValueError:
        print("Erro: insira valores numéricos válidos.")

def verificador_senha():
    print("\n=== Verificador de Segurança de Senha ===")
    senha = input("Digite a senha: ")
    erros = []
    if len(senha) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")
    if not any(char.isdigit() for char in senha):
        erros.append("A senha deve conter pelo menos um número.")

    if erros:
        for erro in erros:
            print(f"- {erro}")
    else:
        print("Senha válida!")

def analise_pares_impares():
    print("\n=== Analisador de Números Pares e Ímpares ===")
    try:
        pares = 0
        impares = 0
        while True:
            entrada = input("Digite um número (ou 'sair' para finalizar): ")
            if entrada.lower() == 'sair':
                break
            numero = int(entrada)
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
        print(f"Total de números pares: {pares}")
        print(f"Total de números ímpares: {impares}")
    except ValueError:
        print("Por favor, digite apenas números ou 'sair'.")

def menu_principal():
    while True:
        print("\n" + "="*35)
        print("Opções:")
        print("1 - Calculadora Básica")
        print("2 - Média de Notas")
        print("3 - Verificador de Senha")
        print("4 - Analisador de Pares e Ímpares")
        print("5 - Sair")
        print("="*35)

        try:
            opcao = int(input("Escolha uma opção (1-5): "))

            if opcao == 1:
                calculadora_basica()
            elif opcao == 2:
                media_notas()
            elif opcao == 3:
                verificador_senha()
            elif opcao == 4:
                analise_pares_impares()
            elif opcao == 5:
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite uma opção numérica válida.")

if __name__ == "__main__":
    menu_principal()
