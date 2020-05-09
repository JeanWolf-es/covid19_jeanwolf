#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 19:23:18 2020

@author: jeanwolf

https://github.com/owid/covid-19-data
https://github.com/mauforonda/covid19-bolivia

http://labtecnosocial.org/iniciativas-ciudadanas-para-afrontar-el-covid-19-en-bolivia/


https://datacarpentry.org/python-ecology-lesson-es/05-merging-data/index.html
https://consultorioeconomico.blogspot.com/2020/05/las-oportunidades-de-la-digitalizacion_6.html
"""
import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np
import urllib.request

# Descargar la base de datos, y la graba. OJO Capeta Base: covid19_jeanwolf
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
file = "covid_data/owid-covid-data.csv"
r = urllib.request.urlopen(url)
f = open(file, "wb")
f.write(r.read()) 
f.close()
print("end download")

cov = pd.read_csv("covid_data/owid-covid-data.csv")

# cambiar tipo de dato por columna
cov = cov.dropna() 
cov.info() 
print("+++++++++++++++")
cov = cov.astype({
    "total_cases_per_million": "int64",
    "new_cases_per_million": "int64",
    "total_deaths_per_million": "int64",
    "new_deaths_per_million": "int64",
    "total_tests": "int64",
    "new_tests": "int64",
    "total_tests_per_thousand": "int64",
    "new_tests_per_thousand": "int64",
    }) 
cov.info() 
print("+++++++++++++++")
print("+++++++++++++++")


# pro = proyeccion de casos por dia de COVID.

# del dataset seleccionar las columnas que queremos
pro_bol = cov["iso_code"] == "BOL"
bol = cov[pro_bol]
bol.to_csv("covid_data/bol.csv")
print("Ya esta filtrados los datos y creada una nueva dataset")


# Descargar la base de datos, y la graba. OJO Capeta Base: covid19_jeanwolf
url = "https://raw.githubusercontent.com/mauforonda/covid19-bolivia/master/total.csv"
file = "covid_data/mauforonda_covid19-bolivia_total.csv"
r = urllib.request.urlopen(url)
f = open(file, "wb")
f.write(r.read()) 
f.close()
print("end download")






