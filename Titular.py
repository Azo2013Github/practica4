__author__ = 'aminata'

import urllib
import urllib.request
import re
import collections
import os

class titular :
	local_nombre=''
	local_DNI=' '
	local_ok=0
	def __init__(self,nombre,DNI):  # crea un titular de la cuenta y le asigna un numero de cuenta para poder trabajar
		self.local_nombre=nombre
		self.local_DNI=DNI
		localizacion='c://Python33//pratica4//'
		extension='.txt'
		fichero=self.local_DNI+extension
		ficheros=os.listdir(r'c://Python33//pratica4//')
		titular=localizacion+self.local_DNI+extension
		i=0
		while (i<len(ficheros)):
			if (ficheros[i]==fichero):
				self.local_ok=1
			i=i+1
		if (self.local_ok==1):
			with open(titular,mode='a',encoding='utf-8') as archivo:
				archivo.write('n� de cuenta1')
				archivo.write('\n')
		#llamar a la funci�n crear cuenta
		else:
			with open(titular,mode='w',encoding='utf-8') as archivo:
				archivo.write(self.local_nombre)
				archivo.write('\n')
				archivo.write(self.local_DNI)
				archivo.write('\n')
				archivo.write('n� de cuenta')
				archivo.write('\n')
	def cotitular(self,nombre,DNI,DNI1): # poner mas de un titular en la misma cuenta
		self.local_nombre=nombre
		self.local_DNI=DNI
		localizacion='c://Python33//pratica4//'
		extension='.txt'
		fichero=DNI1+extension
		ficheros=os.listdir(r'c://Python33//pratica4//')
		titular=localizacion+DNI1+extension
		i=0
		while (i<len(ficheros)):
			if (ficheros[i]==fichero):
				self.local_ok=1
			i=i+1
		if (self.local_ok==1):
			with open(titular,mode='r',encoding='utf-8') as archivo:
				datos=archivo.readlines()
			titular=localizacion+self.local_DNI+extension
			with open(titular,mode='a',encoding='utf-8') as archivo:
				z=2
				archivo.write(self.local_nombre)
				archivo.write('\n')
				archivo.write(DNI)
				archivo.write('\n')
				while (z< len(datos)):
					archivo.write(datos[z])
					z=z+1


a = titular('ami', '223344556', 'EUR')
a.cotitular()