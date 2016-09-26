#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys  #Cuando importamos funcionalidad de otro usuario 
                    #-+-+ funciones para interactuar-+-

import calcoo

class CalculadoraHija(calcoo.Calculadora):
    
    #def __init__(self, op1, op2):
    #Metodo de inicializacion
   
    def multiplicar(self, op1, op2):
        return op1 * op2

    def dividir(self, op1, op2):
        
        return op1 / op2


if __name__ == "__main__":
    calculadorahija = CalculadoraHija()
    try: # nos aseguramos que los argumentos que le pasamos sean solo enteros, 
         #para no tener luego problemas como por ejemplo del tipo 3 suma a
        operando1 = int(sys.argv[1]) # argumento que le pasa el sistema Posicion 
                                     #0 nombre programa, pos. 1 1er argumento, 
                                     #pos 2 suma, pos. 3 segundo argumento.
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = calculadorahija.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calculadorahija.resta(operando1, operando2)
    elif sys.argv[2] == "multiplica":
            result = calculadorahija.multiplicar(operando1, operando2)
    elif sys.argv[2] == "divide":
        if operando2 == 0:
            result = "No se puede dividir por cero"
        else: 
            result = calculadorahija.dividir(operando1, operando2)        
         
    else:
        sys.exit('Operación sólo puede ser suma, resta, multiplica o divide')
print(result)
