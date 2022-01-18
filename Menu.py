ans=True

def decimal_a_binario(numero_decimal):
	numero_binario = 0
	multiplicador = 1
	while numero_decimal != 0:
		numero_binario = numero_binario + numero_decimal % 2 * multiplicador
		numero_decimal //= 2
		multiplicador *= 10
	return numero_binario

def binario_a_decimal(numero_binario):
	numero_decimal = 0 
	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion
	return numero_decimal

def decimal_a_octal(decimal):
	octal = ''
	while decimal > 0:
		residuo = decimal % 8
		octal = str(residuo) + octal
		decimal = int(decimal / 8)
	return octal

def octal_a_decimal(octal):
	decimal = 0
	posicion = 0
	octal = octal[::-1]
	for digito in octal:
		valor_entero = int(digito)
		numero_elevado = int(8 ** posicion)
		equivalencia = int(numero_elevado * valor_entero)
		decimal += equivalencia
		posicion += 1
	return decimal

def obtener_caracter_hexadecimal(valor):
	valor = str(valor)
	equivalencias = {
		'10': 'a',
		'11': 'b',
		'12': 'c',
		'13': 'd',
		'14': 'e',
		'15': 'f',
	}
	if valor in equivalencias:
		return equivalencias[valor]
	else:
		return valor

def decimal_a_hexadecimal(decimal):
	hexadecimal = ''
	while decimal > 0:
		residuo = decimal % 16
		verdadero_caracter = obtener_caracter_hexadecimal(residuo)
		hexadecimal = verdadero_caracter + hexadecimal
		decimal = int(decimal / 16)
	return hexadecimal

def obtener_valor_real(caracter_hexadecimal):
	equivalencias = {
		'f': 15,
		'e': 14,
		'd': 13,
		'c': 12,
		'b': 11,
		'a': 10,
	}
	if caracter_hexadecimal in equivalencias:
		return equivalencias[caracter_hexadecimal]
	else:
		return int(caracter_hexadecimal)

def hexadecimal_a_decimal(hexadecimal):
	hexadecimal = hexadecimal.lower()
	hexadecimal = hexadecimal[::-1]
	decimal = 0
	posicion = 0
	for digito in hexadecimal:
		valor = obtener_valor_real(digito)
		elevado = 16 ** posicion
		equivalencia = elevado * valor
		decimal += equivalencia
		posicion += 1
	return decimal

embResP = '\n ----------RESULTADO----------\n'
embResF = '\n -----------------------------'

try:
	while ans:
		print ('''
	   1.Binario => decimal
	   2.Binario => hexadecimal
	   3.Binario => octal
	   4.Decimal => binario
	   5.Decimal => hexadecimal
	   6.Decimal => octal
	   7.Hexadecimal => binario
	   8.Hexadecimal => decimal
	   9.Hexadecimal => octal
	   10.Octal => binario
	   11.Octal => decimal
	   12.Octal => hexadecimal
	   13.Salir/Cerrar
		''')
		ans= input('Elige tu operacion: ') 
		if ans=='1':
			b8 = input ('Ingrese un número binario => decimal: ')
			print(embResP + f'El binario {b8} es {int(binario_a_decimal(b8))} en decimal' + embResF)
		elif ans=='2':
			b3 = input ('Ingrese un número binario => hexadecimal: ')
			print(embResP + f'El binario {b3} es {hex(int(b3,2))} en hexadecimal' + embResF)
		elif ans=='3':
			b1 =  input ('Ingrese un número binario: ') 
			print(embResP + f'El binario {b1} es {oct(int(b1,2))} en octal' + embResF) 
		elif ans=='4':
			b7 = int(input ('Ingrese un número decimal => binario: '))
			print(embResP + f'El decimal {b7} es {int(decimal_a_binario(b7))} en binario' + embResF)
		elif ans=='5':
			b11 = int(input ('Ingrese un número decimal => hexadecimal: '))
			print(embResP + f'El decimal {b11} es {(decimal_a_hexadecimal(b11))} en hexadecimal' + embResF)
		elif ans=='6':
			b9 = int(input ('Ingrese un número decimal => octal: '))
			print(embResP + f'El decimal {b9} es {int(decimal_a_octal(b9))} en octal' + embResF)
		elif ans=='7':
			b4 = input ('Ingrese un número hexadecimal => binario: ')
			print(embResP + f'El hexadecimal {b4} es {bin(int(b4,16))} en octal' + embResF)
		elif ans=='8':
			b12 = input ('Ingresa un número hexadecimal => decimal: ')
			print(embResP + f'El hexadecimal {b12} es {int(hexadecimal_a_decimal(b12))} en decimal' + embResF)
		elif ans=='9':
			b6 = input ('Ingrese un número hexadecimal => octal: ')
			print(embResP + f'El hexadecimal {b6} es {oct(int(b6,16))} en octal' + embResF)
		elif ans=='10':
			b2 = input ('Introduzca un número octal => binario: ')
			print(embResP + f'El octal {b2} es {bin(int(b2,8))} en binario' + embResF)
		elif ans=='11':
			b10 = input ('Ingrese un número octal => decimal: ')
			print(embResP + f'El octal {b10} es {(octal_a_decimal(b10))} en decimal' + embResF)
		elif ans=='12':
			b5 = input ('Ingrese un número octal => hexadecimal: ')
			print(embResP + f'El octal {b5} es {hex(int(b5,8))} en hexadecimal' + embResF)
		elif ans=='13':
			print('\n Gracias \n')
			break 
		elif ans !='':
			print('\n El numero escogido es incorrecto | La operacon no es valida \n')
except:
	print(embResP + 'Oops! Algo salio mal comprueba los valores y vuelve a intentarlo' + embResF)
	pass