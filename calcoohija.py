#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def multiplicar(self, op1, op2):
        return op1 * op2

    def dividir(self, op1, op2):
        return op1 / op2

if __name__ == "__main__":
    calculadorahija = CalculadoraHija()

    try:
        operando1 = int(sys.argv[1])
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
            pass
        else:
            result = calculadorahija.dividir(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser suma, resta, multiplica o divide')
    print(result)
