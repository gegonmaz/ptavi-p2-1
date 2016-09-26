#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys  #Cuando importamos funcionalidad de otro usuario 
                    #-+-+ funciones para interactuar-+-

import calcoohija
import csv

if __name__ == "__main__":

    archivo = open('operaciones.txt','r')
    lista = archivo.readlines()
    c = calcoohija.CalculadoraHija()   

    for linea in lista:
        operando = linea.split(',')[0]
        componentes = linea.split(',')[1:]
        result = componentes[0]
        
        for componente in componentes[1:]:
            if operando == 'suma':
                result = c.suma(int(result) , int(componente))
            if operando == 'resta':
                result = c.resta(int(result), int(componente))
            if operando == 'multiplica':
                result = c.multiplicar(int(result) ,int(componente))
            if operando == 'divide':
                
                if componente == 0:
                    result = "No se puede dividir por cero"
                else:
                    result = c.dividir(int(result) , int(componente))
                 
        print(result)
        
        
