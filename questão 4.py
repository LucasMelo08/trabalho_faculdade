class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumenta_salario(self, porcentagem=None):
        if porcentagem is None:
            porcentagem = 5
        self.salario *= 1 + (porcentagem / 100)

    def __str__(self):
        return f"Nome: {self.nome} | Salário: R${self.salario:.2f}"


class Gerente(Funcionario):
    def aumenta_salario(self, porcentagem=None):
        if porcentagem is None:
            porcentagem = 10
        super().aumenta_salario(porcentagem)


class Programador(Funcionario):
    def aumenta_salario(self, porcentagem=None):
        if porcentagem is None:
            porcentagem = 20
        super().aumenta_salario(porcentagem)

f1 = Funcionario("João", 1000)
f2 = Gerente("Maria", 1000)
f3 = Programador("Ana", 1000)

f1.aumenta_salario()
f2.aumenta_salario()
f3.aumenta_salario()

print(f1)
print(f2)
print(f3)