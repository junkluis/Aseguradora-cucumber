# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modulos import cotizador

#from modulos import ventas
#from modulos import banco


cliente = { "nombre": "Luis Zuniga",
			"ciudad": "Guayaquil",
			"edad": 24, "sexo": "hombre",
			"estado_civil": "casado",
			"especial": "osteoporosis",
			"dependientes": 0 }
cartera = 40

if __name__ == "__main__":
	print("Venta de Seguros")
	print("----------------")
	print("1. Realizar cotizacion")
	cotizacion = cotizador.cotizar_seguro(  cliente["ciudad"],
											cliente["edad"] ,
											cliente["sexo"] ,
											cliente["estado_civil"] ,
											cliente["especial"] ,
											cliente["dependientes"] )
	print(cotizacion)

	valor_cotizado = cotizador.obtener_cuota_total(  cliente["edad"] ,
													 cliente["sexo"] ,
													 cliente["estado_civil"] ,
													 cliente["especial"] ,
													 cliente["dependientes"]  )
	'''
	print("----------------")
	print("2. Realizar retiro")

	cuenta_ahorros = {"tipo":"ahorro", "monto":999}
	cuenta_corriente = {"tipo":"ahorro", "monto":999}

	cuenta_ahorros, cartera, msg = banco.realizar_retiro(cuenta_ahorros, cartera, -0)
	print(msg)


	print("----------------")
	print("3. Realizar compra")
	
	venta = ventas.comprar_seguro(cartera, valor_cotizado, cliente["edad"], cliente["dependientes"])
	print(venta[0])
	'''
	