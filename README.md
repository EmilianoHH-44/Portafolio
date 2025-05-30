
# Portafolio de inversión con Python

El proposito del proyecto es la automatizar la creación de  portfolios de inversión, mediente un modelo CAPM, y procesos de técnicas de optimización lineal, considerando restricciones como la prohibición de ventas en corto y una beta objetivo, con Python.

Este proyecto nace de despues de una clase de Portafolios de inversión, nos dimos cuenta que los procesos de creación de un portafolio en excel requieren más tiempo y son procesos que se pueden optimizar.

Por lo que decidimos crear un programa para la elaboración de un portafolio.


## Contenidos 

- Titulo y descripción
- Inspiración
- Contenido
- Instrucciones
- Caracteristicas
- Código
- Instalación
- Licencia
- Creadores
## Ejemplos
![APPSCREENSHOT]("C:\Users\emili\Downloads\WhatsApp Image 2025-05-30 at 11.08.34 AM.jpeg")
## Características 

En nuestro programa 
Las fechas de las acciones comienzan en: 2000-01-01
Terminan en: 2025-05-01

Tomamos la tasa de retorno de: s&p
La tasa libre de riesgo es: 0.05

Tenemos restricciones en el programa como:
el total invertido debe ser 100%
no se permite short-selling
 βobjetivo​=1.0

Se utilizan:
Pesos optimos
Rendimiento esperado
Riesgo sistémico total (beta)
Sharpe Ratio
## Instalación

1. Descarga el programa de VSCode
2. Copia el código en el programa
3. Agrega: acciones seleccionadas, benchmark, tasa libre de riesgo, fecha de inicio y fin.
4. Ejecuta
## Instrucciones

Selección de Acciones:

1. Selecciona al menos 10 acciones de tu interés.
2. Obtén el ticker de cada acción.
3. Asigna los tickers de tu elección en el código.
4. Selecciona tu tasa libre de riesgo, y asignala en el código, en "rf = 0.05".
5. Selecciona un índice cómo tu benchmark, y asignala en el código, en data_benchmark = yf.download('^XXXXX', start=start), si quieres el S&P dejalo sin modificar.
6. Modifica la fecha de inicio , según el tiempo de cotización de tus acciones.
7. Modifica la fecha de fin al momento que ejecutes el código.

Nota: Usa VSCode para ejecutar el código.

## Instalación

1. Descarga el programa de VSCode
2. Copia el código en el programa
3. Agrega: acciones seleccionadas, benchmark, tasa libre de riesgo, fecha de inicio y fin.
4. Ejecuta
## Tecnología

Python
VSCode
Yahoo Finances

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Creadores

**Hecho con amor por:** 

Isai Saldivar Ayala
Gabriela Ponce Diego
Ximena Torres Martínez
Emiliano Hernandez Hernandez
