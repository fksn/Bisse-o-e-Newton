from sympy import *

def bissecao(f, a, b, erro, max_iter):
    # Definir X como um simbolo nas equações
    x = symbols('x')

    # Tranformar expressoes f em lambda function
    f = lambdify(x, f)

    if f(a)*f(b) > 0:
        print("Defina outro intervalo.")
        return None
    print("   a   |   c   |   b   |     f(a)    |    f(c)    |    f(a)*f(c)  ")

    # Rodar quantas vezes foi definido
    for n in range(0, max_iter):
        # Realizar calculo de c
        c = (a + b) / 2

        # Realizar calculo de f(a) e de f(c)
        f_a = f(a)
        f_c = f(c)
        f_ac = f_a*f_c
        print("{:.5f}".format(a), "{:.5f}".format(c), "{:.5f}".format(b), "{:.10f}".format(f_a), "{:.10f}".format(f_c), "{:.10f}".format(f_ac))

        # Verifica se condição de parada foi atingido
        if f_c == 0 or b - a < erro:
            return c
        else:
            # Verifica qual vai ser o valor de a e de b
            if f_ac < 0:
                b = c
            else:
                a = c

    print('Número máximo de iterações foi atingido.')
    return None


def newton(f, a, b, erro, max_iter):
    # Definir X como um simbolo nas equações
    x = symbols('x')

    # Tranformar f em f' e f''
    df = diff(f, x)
    d3f = diff(df, x)

    # Tranformar expressoes f, df e d3f em lambda functions
    f = lambdify(x, f)
    df = lambdify(x, df)
    d3f = lambdify(x, d3f)

    # Verifica propriedade de f(a)*f(b) < 0
    if f(a)*f(b) >= 0:
        print("Não cumpre requisito de f(a)*f(b) < 0")
        return None
    else:
        # Verifica se a ou b podem ser utilizados como X0
        x = a
        if f(x)*d3f(x)<=0:
            x = b
            if f(x) * d3f(x) <= 0:
                print("Escolha outros valores para a, b.")
                return None

    print("     x_k    |   f(x_k)   |   f'(x_k)  |f(x_k)/f'(x_k)|abs(x_k - x_(k-1))")

    # Rodar quantas vezes foi definido
    for n in range(0, max_iter):
        # Calcula f(x), f'(x) e verifica se é igual a 0
        fx = f(x)
        dfr = df(x)

        if dfr == 0:
            print("df(x) = 0, resultado não encontrado.")
            return None

        # Calcula o valor do proximo X
        x1 = x - (fx/dfr)

        print("{:.10f}".format(x), "{:.10f}".format(fx), "{:.10f}".format(dfr), "{:.10f}".format(fx/dfr), "{:.10f}".format(abs(x-x1)))

        # Verifica criterio de parada
        if abs(x1-x) < erro:
            return x1

        x = x1
    print('Número máximo de iterações foi atingido.')
    return None

def ajuda():
    print("x**2 = x^2")
    print("exp(2) = e^2")
    print("log(x) = ln(x)")


def princ(op):
    f = input("Digite a função: ")
    f1 = plot(f, show=False)
    f1.ylim = (-20, 20)
    f1.show()
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    erro = float(input("Digite o valor do erro: "))
    if op == '1':
        epsilon = bissecao(f, a, b, erro, max_iter=50)
    else:
        epsilon = newton(f, a, b, erro, max_iter=50)
    if epsilon != None:
        print("\nEpsilon = ", epsilon)

choice = '1'
while choice == '1':
    print("[1] Digite 1 para utilizar Método da Bisseção.")
    print("[2] Digite 2 para utilizar Método de Newton")
    print("[3] Digite 3 para ajuda com caracteres de input")
    op = input("Opção desejada: ")
    if op == '3':
        ajuda()
    else:
        princ(op)

    print("\n[1] Digite 1 para realizar outra operação.")
    print("[2] Digite 2 para sair.")
    choice = input("Opção desejada: ")
