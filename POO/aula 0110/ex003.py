# Exercício 3: Sistema de Cadastro de Idade
# Crie uma função `cadastrar_idade()` que solicita a idade de um usuário. Se o usuário inserir
# um valor negativo ou maior que 120, uma exceção personalizada `IdadeInvalidaError` deve
# ser levantada e tratada. O sistema deve continuar solicitando uma idade válida até que o
# usuário forneça uma entrada correta.

class IdadeInvalidaError(Exception):
    pass

def cadastrar_idade():
    while True: 
        try:
            idade = int(input('insira a idade: '))
            if idade < 0 or idade > 120: 
                raise IdadeInvalidaError('ERRO: Idade invalida, digite a idade novamente')
            return idade
        except IdadeInvalidaError as i:
            print(i)

idade = cadastrar_idade()
print(f"idade: {idade}")
