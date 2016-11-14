import sys
import csv
import Stemmer
import operator

stemmer = Stemmer.Stemmer('spanish')

def getMention(set_data):
	mention = ''
	if 'la' in set_data:
		mention = 'base de datos'
	elif 'olap' in set_data:
		mention = 'sistemas de informacion'
	elif 'ipv4' in set_data:
		mention = 'tecnologias en comunicaciones y redes de computadoras'
	elif '80211' in set_data:
		mention = 'tecnologias en comunicaciones y redes de computadoras'
	elif 'bluetooth' in set_data:
		mention = 'tecnologias en comunicaciones y redes de computadoras'
	elif 'ipv6' in set_data:
		mention = 'tecnologias en comunicaciones y redes de computadoras'
	elif 'postgr' in set_data:
		mention = 'aplicaciones internet'
	elif 'organizacional' in set_data:
		mention = 'sistemas de informacion'
	elif 'trabaj' in set_data:
		mention = 'sistemas de informacion'
	elif 'inalambr' in set_data:
		mention = 'tecnologias en comunicaciones y redes de computadoras'
	elif 'segur' in set_data:
		mention = 'tecnologias en comunicaciones y redes de computadoras'
	elif 'el' in set_data:
		mention = 'base de datos'
	elif 'lom' in set_data:
		mention = 'base de datos'
	elif 'xml' in set_data:
		mention = 'base de datos'
	elif 'cienci' in set_data:
		mention = 'base de datos'
	elif 'proyect' in set_data:
		mention = 'base de datos'
	elif 'on' in set_data:
		mention = 'aplicaciones internet'
	elif 'mvc' in set_data:
		mention = 'base de datos'
	elif 'control' in set_data:
		mention = 'tecnologias en comunicaciones y redes de computadoras'
	elif 'rails' in set_data:
		mention = 'aplicaciones internet'
	elif 'gener' in set_data:
		mention = 'aplicaciones internet'
	elif 'electron' in set_data:
		mention = 'tecnologias en comunicaciones y redes de computadoras'
	elif 'javascript' in set_data:
		mention = 'aplicaciones internet'
	elif 'servici' in set_data:
		mention = 'aplicaciones internet'
	elif 'clinic' in set_data:
		mention = 'aplicaciones internet'
	elif 'sms' in set_data:
		mention = 'aplicaciones internet'
	else:
		mention = 'inteligencia artificial'
	return mention


with open('In/Datos_Proyecto_Clasificar.txt', 'r', encoding='utf-8') as file:
	for row in file:
		row = row.replace(',', '')
		row = row.replace('.', '')
		row = row.replace('-', '')
		row = row.replace('(', '')
		row = row.replace(')', '')
		row = row.replace('[', '')
		row = row.replace(']', '')
		data = set(stemmer.stemWords(row.split(' ')))
		print(getMention(data))