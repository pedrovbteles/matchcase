dia = int(input("Insira um dia da semana: "))
match dia:
    case 'Domingo' | 'Sábado':
        print("Fim de semana")
    case _:
        print("Dia de semana")