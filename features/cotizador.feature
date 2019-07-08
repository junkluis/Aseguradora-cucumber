# language: es

Característica: Realizar una cotizacion

Antecedentes:
	Dado un conjunto de solicitudes
     | Cliente			| ciudad		| edad	| sexo		| estado_civil	| especial		| dependientes	|
     | Sansa Stark		| Loja			| 22	| mujer		| casado		| osteoporosis	| 0				|
     | Jofrey Baratheon	| Quito			| 16	| hombre	| soltero		| cancer		| 1				|
     | John Snow		| Cuenca		| 30	| hombre	| casado		| infarto		| 2				|
     | Catelyn Tully	| Machala		| 35	| mujer		| soltero		| diabetes		| 3				|


@Cotizacion
Escenario: El cliente solicita una cotizacion que no se encuentra entre las ciudades disponibles
    Dada la solicitud del cliente 'Sansa Stark'
    Cuando realice una cotizacion en linea,
    Entonces obtendra el mensaje: 'Saludcita no opera en la ciudad ingresada.'

@Cotizacion
Escenario: El cliente solicita una cotizacion, pero el cliente es menor de edad
    Dada la solicitud del cliente 'Jofrey Baratheon'
    Cuando realice una cotizacion en linea,
    Entonces obtendra el mensaje: 'La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.'

