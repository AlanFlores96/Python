from math import factorial


def primo(numero: int) -> bool:
    if (factorial(numero-1)+1)%numero==0:
        return True
    else:
        return False


def run():
    # numero=int(input("Escribe un núnero natural y te dire si es número primo: "))
    numero = 5
    if primo(numero):
        print(str(numero)+" es primo")
    else:
        print(str(numero)+" no es primo")


if __name__=="__main__":
    run()