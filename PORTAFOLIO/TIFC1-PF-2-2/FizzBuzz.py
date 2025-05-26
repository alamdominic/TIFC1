
for i in range(1000):
    if i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz")
    elif i % 5==0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# miLista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# listaFinal = []
# for i in miLista:
#     if i % 3 == 0 and i % 5 ==0:
#         listaFinal.append("FizzBuzz")
#     elif i % 5==0:
#         listaFinal.append("Buzz")
#     elif i % 3 == 0:
#         listaFinal.append("Fizz")
#     else:
#         listaFinal.append(i)
# print(f'Lista final: {listaFinal}')

    """Descripción del Código – FizzBuzz
Este script implementa la lógica del desafío clásico FizzBuzz. 
Su propósito es recorrer un rango de números y aplicar condiciones específicas basadas en divisibilidad:
Primer bloque:
Recorre los números del 0 al 999 e imprime:
"FizzBuzz" si el número es divisible por 3 y 5.
"Buzz" si es divisible solo por 5.
"Fizz" si es divisible solo por 3.
El número original si no cumple ninguna de las condiciones.
Segundo bloque (comentado):
Aplica la misma lógica a una lista predefinida (miLista) y guarda los resultados en listaFinal, en lugar de imprimirlos. 
Esto permite reutilizar o procesar los resultados posteriormente.
    """