# Exemplo 1: apenas 1 centro de custo
area1   = "Financeiro"
centro1 = "ABC"

match centro1:
    case _:
        print(f"A área {area1} possui o centro de custo {centro1}")


# Exemplo 2: 3 centros de custo (sem lista)
area2    = "Marketing"
centroA  = "ABC"
centroB  = "XYZ"
centroC  = "HJG"

match centroA:
    case _:
        print(f"A área {area2} possui os centros de custo abaixo:")
        # Vamos usar um for com índice e if/elif para imprimir cada variável
        for i in range(3):
            if i == 0:
                print(centroA)
            elif i == 1:
                print(centroB)
            else:  # i == 2
                print(centroC)
