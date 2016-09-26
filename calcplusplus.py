#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import calcoohija
import csv

if __name__ == "__main__":

    c = calcoohija.CalculadoraHija()
    fichero = sys.argv[1]
    with open(fichero) as FicheroNuevo:
        datos = csv.reader(FicheroNuevo)
        for linea in datos:

            operando = linea[0]
            componentes = linea[1:]
            result = componentes[0]
            for componente in componentes[1:]:
                if operando == 'suma':
                    result = c.suma(int(result), int(componente))
                if operando == 'resta':
                    result = c.resta(int(result), int(componente))
                if operando == 'multiplica':
                    result = c.multiplicar(int(result), int(componente))
                if operando == 'divide':
                    if componente == 0:
                        result = "No se puede dividir por cero"
                    else:
                        result = c.dividir(int(result), int(componente))
            print(result)
