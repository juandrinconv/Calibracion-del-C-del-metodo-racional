# 1. Descripción general
Para empezar, este es un código que calibra el parámetro C (coeficiente de escorrentía) del método racional. Cabe mencionar que, evidentemente, hay que tener valores del caudal observado para realizar la calibración de dicho parámetro.

Por otro lado, no es ocioso mencionar que, como es el método racional, se obtiene el valor del caudal pico para el evento de lluvia tratado, es decir, solo se obtiene el valor de un solo caudal para la intensidad correspondiente.

En otro orden de ideas, las unidades en las cuales se deben introducir las variables requeridas en este código se encuentran en el código mismo, por ende, se recomienda revisar el código antes de usarlo.

Para acabar, en este respositorio se anexa una hoja de cálculo en excel donde se determina la gráfica de intensidad-duración mediante el suministro de un hietograma (evento de lluvia). Cabe destacar, que con el tiempo de concentración de la cuenca calculado por diversos métodos, sale el valor del parámetro de la intensidad a utilizar en este código.

# 2. Versión de Python utilizada 
Python 3.12.4

# 3. Librerías utilizadas
scipy   1.14.1
numpy   2.2.0 (no se utilizó en el código, pero se instaló en el entorno virtual)

# 4. Información para cuando se vaya a clonar el repositorio
Este repositorio se subió con el entorno virtual por defecto de Python, por ende, no es necesario crear por separado dicho entorno antes de clonar el repositorio, sino que simplemente, después de clonar el repositorio, se instalan todas las dependencias en el entorno virtual [apartado (3)].
