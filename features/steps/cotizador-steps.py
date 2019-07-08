import sys
sys.path.append("..")

from behave import given, when, then
from modulos.cotizador import *


def before_scenario(context, scenario):
	context = {}


@given("un conjunto de solicitudes")
def obtener_solicitudes(context):
	lista_solicitudes = []
	for row in context.table:
		solicitud = {}
		solicitud["cliente"] = row['Cliente']
		solicitud["info"] = [ row['ciudad'],
							  row['edad'],
							  row['sexo'],
							  row['estado_civil'],
							  row['especial'],
							  row['dependientes'] ]

		lista_solicitudes.append(solicitud)

	context.solicitudes = lista_solicitudes


@given("la solicitud del cliente '{cliente}'")
def seleccionar_cliente(context, cliente):
	for solicitud in context.solicitudes:
		if(solicitud['cliente'] == cliente):
			context.cliente = solicitud
		

@when("realice una cotizacion en linea,")
def calcular_cotizacion(context):
	cliente_info = context.cliente["info"]
	context.mensaje = cotizar_seguro( cliente_info[0],
									int(cliente_info[1]),
									cliente_info[2],
									cliente_info[3],
									cliente_info[4],
									int(cliente_info[5]) )


@then("obtendra el mensaje: '{msj}'")
def mesaje_alerta_ciudad(context, msj):
	print(context.mensaje)
	print(msj)
	assert context.mensaje == msj
