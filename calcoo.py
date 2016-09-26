#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys #Cuando importamos funcionalidad de otro usuario 
                    #-+-+ funciones para interactuar-+-

class Calculadora():

    def suma(self, op1, op2):
        return op1 + op2
    def resta(self, op1, op2):
        return op1 - op2

#class CalculadoraMejor(Calculadora):
   # def resta(self, op1, op2):
   # return op1 -op2

if __name__ == "__main__":
    #calculadora = CalculadoraMejor()
   
    #resultado = Calculadora.suma(3, 5)

    #print(resultado)

    try: # nos aseguramos que los argumentos que le pasamos sean solo enteros, 
         #para no tener luego problemas como por ejemplo del tipo 3 suma a
        operando1 = int(sys.argv[1]) # argumento que le pasa el sistema Posicion 
                                     #0 nombre programa, pos. 1 1er argumento, 
                                     #pos 2 suma, pos. 3 segundo argumento.
        operando2 = int(sys.argv[3])

    except ValueError:
       sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = Calculadora().suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = Calculadora().resta(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar, restar')

    print(result)
