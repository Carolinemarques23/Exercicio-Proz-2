import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (1922-2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano fora do intervalo válido. Tente novamente.")
        except ValueError:
            print("Valor inválido. Tente novamente.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.date.today().year
    return ano_atual - ano_nascimento

nome = input("Digite seu nome completo: ")
ano_nascimento = obter_ano_nascimento()
idade = calcular_idade(ano_nascimento)

print(f"\nNome: {nome}")
print(f"Idade em 2022: {idade} anos")
