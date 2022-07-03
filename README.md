# ATACK_RSA_TYPE1
Lo primero que realizamos fue crear un valor entero  dentro del [0,n> para de esta manera sea coprimo con n. Luego calculamos c’ que tiene por fórmula cxe mod n, donde usamos el algoritmo de EXPMOD(Exponenciación modular) para xe, ya que las propiedades de mod nos permiten modular de esta manera (((c%n)*EXPMOD(x,e,n))%n).

Para hallar d necesitábamos de fi(n) para lo cual empleamos un algoritmo que nos retornara factores primos de n, ya con estos factores primos pudimos hallar fi(n) para poder hallar m’ (c’d mod n). Y finalmente hallar n multiplicando m’ * x’.

Como verificación usamos cifrado al m con la clave pública dada por el ejercicio y devuelva lo cifrado al principio.

		
