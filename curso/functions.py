def calcular_renta_4(renta): 
    if renta > 0:
        if ( renta <= 10000 ):
            print('5%')
            print('El valor a pagar es ', renta*0.05)
            valor = renta * 0.05
            print(f'El valor a pagar es {valor}')

        elif ( renta <= 20000):
            valor = renta * 0.15
            print('15%')
            print(f'El valor a pagar es {valor}')

        elif ( renta <= 35000):
            valor = renta * 0.20
            print('20%')
            print(f'El valor a pagar es {valor}')    

        elif ( renta <= 60000):
            valor = renta * 0.30
            print('30%')
            print(f'El valor a pagar es {valor}')  

        else: 
            valor = renta * 0.45
            print('45%')
            print(f'El valor a pagar es {valor}')  

    elif renta == 0:
        print('No puedes cobrar cero :( ')

    else:
        print('Introduce un valor mayor de cero!!')



def func_hola_world(nombre: str):
    print(f'hello world {nombre}')


def suma_valores(a: float, b : float) -> float:
    print(a+b)
    return a+b