from datetime import datetime

__author__ = 'Amine Banks'
import datetime
import re

class cuenta:
	local_iban='CAT60'
	local_cuenta='C://Users//Amine Banks//PycharmProjects//practica4//test.txt'
	local_num_cuenta='000000000'
	local_amount=0
	local_nombre='C://Users//Amine Banks//PycharmProjects//practica4//'
	local_titular=1
	local_moneda='EUR'
	local_time=0
	local_saldo=0
	def __init__(self,local_nombre,local_amount):
		with open(self.local_cuenta,mode='r',encoding='utf-8') as archivo:
			linea=archivo.readline()
		with open(self.local_cuenta,mode='w',encoding='utf-8') as archivo:
			print(linea)
			d=int(linea)
			d=d+1
			linea=str(d)
			archivo.write(linea)
		documento='.txt'
		cuenta=self.local_nombre+self.local_iban+self.local_num_cuenta+linea+documento
		print(cuenta)
		print(self.local_iban+self.local_num_cuenta+linea)
		with open(cuenta,mode='a',encoding='utf-8') as archivo:
			archivo.write(str(self.local_titular))
			archivo.write('\n')
			archivo.write(local_nombre)
			archivo.write('\n')
			archivo.write(self.local_iban)
			archivo.write((self.local_num_cuenta+linea))
			archivo.write('\n')
			self.local_time=datetime.now()
			print(self.local_time)
			archivo.write(str(self.local_time.hour))
			archivo.write(':')
			archivo.write(str(self.local_time.minute))
			archivo.write(':')
			archivo.write(str(self.local_time.second))
			archivo.write ('   ')
			archivo.write(str(self.local_time.day))
			archivo.write('/')
			archivo.write(str(self.local_time.month))
			archivo.write('/')
			archivo.write(str(self.local_time.year))
			archivo.write ('     ')
			archivo.write('ingreso')
			self.local_amount=local_amount
			archivo.write(str(self.local_amount))
			archivo.write(str(self.local_moneda))
			archivo.write('\n')
			archivo.write(str('saldo:'))
			archivo.write(str(self.local_amount))
			archivo.write(' ')
			archivo.write(str(self.local_moneda))
			archivo.write('\n')
            #return dateTime.datetime.now().strftimr("%Y-%m-$d %H:%M:%S")
	def mov(self,local_nombre):
		documento='.txt'
		cuenta=self.local_nombre+local_nombre+documento
		i=0
		with open(cuenta,mode='r',encoding='utf-8') as archivo:
			for linea in archivo:
				if (i>0):
					print(linea.rstrip())
				i=i+1
	def saldo(self,local_nombre):
		documento='.txt'
		cuenta=self.local_nombre+local_nombre+documento
		with open(cuenta,mode='r',encoding='utf-8') as archivo:
			for linea in archivo:
				if re.search('saldo:',linea):
					a=linea
			print(a)
	def ingreso (self,local_nombre,local_amount):
		documento='.txt'
		cuenta=self.local_nombre+local_nombre+documento
		with open(cuenta,mode='r',encoding='utf-8') as archivo:
			for linea in archivo:
				if re.search('saldo:',linea):
					self.local_saldo=((linea.split('saldo:'))[1].split('EUR')[0])
			print(self.local_saldo)
		with open(cuenta,mode='a',encoding='utf-8') as archivo:
			self.local_time = datetime.now()
			archivo.write(str(self.local_time.hour))
			archivo.write(':')
			archivo.write(str(self.local_time.minute))
			archivo.write(':')
			archivo.write(str(self.local_time.second))
			archivo.write ('   ')
			archivo.write(str(self.local_time.day))
			archivo.write('/')
			archivo.write(str(self.local_time.month))
			archivo.write('/')
			archivo.write(str(self.local_time.year))
			archivo.write ('     ')
			archivo.write('ingreso')
			self.local_amount=local_amount
			archivo.write(str(self.local_amount))
			archivo.write(str(self.local_moneda))
			archivo.write('\n')
			archivo.write(str('saldo:'))
			archivo.write(str(self.local_amount+int(str(self.local_saldo))))
			archivo.write(' ')
			archivo.write(str(self.local_moneda))
			archivo.write('\n')
	def retirada (self,local_nombre,local_amount):
		documento='.txt'
		cuenta=self.local_nombre+local_nombre+documento
		with open(cuenta,mode='r',encoding='utf-8') as archivo:
			for linea in archivo:
				if re.search('saldo:',linea):
					self.local_saldo=((linea.split('saldo:'))[1].split('EUR')[0])
			print(self.local_saldo)
			self.local_amount=local_amount
		if ((int(str(self.local_saldo))-self.local_amount)<0):
			print('imposible de ejecutar operación')
		else:
			with open(cuenta,mode='a',encoding='utf-8') as archivo:
				self.local_time=datetime.now()
				archivo.write(str(self.local_time.hour))
				archivo.write(':')
				archivo.write(str(self.local_time.minute))
				archivo.write(':')
				archivo.write(str(self.local_time.second))
				archivo.write ('   ')
				archivo.write(str(self.local_time.day))
				archivo.write('/')
				archivo.write(str(self.local_time.month))
				archivo.write('/')
				archivo.write(str(self.local_time.year))
				archivo.write ('     ')
				archivo.write('retirada')
				archivo.write(str('-'))
				archivo.write(str(self.local_amount))
				archivo.write(str(self.local_moneda))
				archivo.write('\n')
				archivo.write(str('saldo:'))
				archivo.write(str(int(str(self.local_saldo))-self.local_amount))
				archivo.write(' ')
				archivo.write(str(self.local_moneda))
				archivo.write('\n')
	def transfer(self,local_nombre,iban,local_amount):
		documento='.txt'
		cuenta=self.local_nombre+local_nombre+documento
		with open(cuenta,mode='r',encoding='utf-8') as archivo:
			for linea in archivo:
				if re.search('saldo:',linea):
					self.local_saldo=((linea.split('saldo:'))[1].split('EUR')[0])
			print(self.local_saldo)
			self.local_amount=local_amount
		if ((int(str(self.local_saldo))-self.local_amount)<0):
			print('imposible de ejecutar operación')
		else:
			with open(cuenta,mode='a',encoding='utf-8') as archivo:
				self.local_time=datetime.now()
				archivo.write(str(self.local_time.hour))
				archivo.write(':')
				archivo.write(str(self.local_time.minute))
				archivo.write(':')
				archivo.write(str(self.local_time.second))
				archivo.write ('   ')
				archivo.write(str(self.local_time.day))
				archivo.write('/')
				archivo.write(str(self.local_time.month))
				archivo.write('/')
				archivo.write(str(self.local_time.year))
				archivo.write ('     ')
				archivo.write('Transf')
				archivo.write(iban)
				archivo.write(str('-'))
				archivo.write(str(self.local_amount))
				archivo.write(str(self.local_moneda))
				archivo.write('\n')
				archivo.write(str('saldo:'))
				archivo.write(str(int(str(self.local_saldo))-self.local_amount))
				archivo.write(' ')
				archivo.write(str(self.local_moneda))
				archivo.write('\n')
				documento='.txt'
		cuenta=self.local_nombre+iban+documento
		with open(cuenta,mode='r',encoding='utf-8') as archivo:
			for linea in archivo:
				if re.search('saldo:',linea):
					self.local_saldo=((linea.split('saldo:'))[1].split('EUR')[0])
			print(self.local_saldo)
			self.local_amount=local_amount
		if ((int(str(self.local_saldo))-self.local_amount)<0):
			print('imposible de ejecutar operación')
		else:
			with open(cuenta,mode='a',encoding='utf-8') as archivo:
				self.local_time=datetime.now()
				archivo.write(str(self.local_time.hour))
				archivo.write(':')
				archivo.write(str(self.local_time.minute))
				archivo.write(':')
				archivo.write(str(self.local_time.second))
				archivo.write ('   ')
				archivo.write(str(self.local_time.day))
				archivo.write('/')
				archivo.write(str(self.local_time.month))
				archivo.write('/')
				archivo.write(str(self.local_time.year))
				archivo.write ('     ')
				archivo.write('Transf')
				archivo.write(local_nombre)
				archivo.write(str(self.local_amount))
				archivo.write(str(self.local_moneda))
				archivo.write('\n')
				archivo.write(str('saldo:'))
				archivo.write(str(int(str(self.local_saldo))+self.local_amount))
				archivo.write(' ')
				archivo.write(str(self.local_moneda))
				archivo.write('\n')
	def titular(self,nombre,local_nombre):
		documento = '.txt'
		cuenta=self.local_nombre+local_nombre+documento
		with open(cuenta,mode='r',encoding='utf-8') as archivo:
			datos=archivo.readlines()
		with open(cuenta,mode='w',encoding='utf-8') as archivo:
			z=1
			archivo.write('2 \n')
			archivo.write(nombre)
			archivo.write('\n')
			while (z< len(datos)):
				archivo.write(datos[z])
				z=z+1

#def menu ():
#print ("1- agregar")
#print ("2- quitar")
#print ("3- ver")
#print ("4- salir")

#while (op!=4):
# if (op=='1'):
# la sentencia para agregar
# elif (op=='2'):
# la sentencia para quitar
# elif (op=='3'):
# la sentencia para ver

# menu()
# op = raw_input("elige una opcion: ") # el bucle corta cuando pongas 4





