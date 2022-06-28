#Crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.

import Aritmética

def main():
    op1 = Aritmética.suma(1548, 1)
    
    op2 = Aritmética.resta(1548, 1)
    
    op3 = Aritmética.multiplicación(1548, 2)
    
    op4 = Aritmética.división(3096, 2)
    
    print('El resultado de las operaciones son:', '\n' 'Suma:', op1,
          '\n''Resta:', op2, '\n' 'Multiplicación:', op3, '\n' 'División:', op4)

if __name__ == '__main__':
    main()
