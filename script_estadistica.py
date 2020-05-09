#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:00:20 2020

@author: jeanwolf

Script para hacer estadisticas.
Dar formato a las columnas
Estadiscas por columna
moda de la columna

"""

import pandas as pd

d = pd.read_csv("covid_data/prome.csv")
d = d.dropna() 
d.info()
print("+++++++++++++++")
d = d.astype({"log": "int64", "dif": "int64",})
d.info()

print(d)
print(d["log"].describe())
print("la moda:", d["log"].mode())
print("++++++++++++++")

print(d["dif"].describe())
print("la moda:", d["dif"].mode())