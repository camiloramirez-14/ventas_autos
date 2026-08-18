## Que es la app y donde esta desplegada ?
la siguiente app ha sido desplegada desde el servidor render y fue creada con el fin de proporcionar a nuestros clientes de herramienta interactivas que permitan conocer las caracteristicas de nuestros vehiculos disponibles en la tienda
## Que herramientas ofrece?
La app proporciona botones interactivos que permiten la creacion de un histograma que muestra el kilometraje de cada uno de los vehiculos disponibles; ademas se cuenta con un segundo boton interactivo que permite la generacion de un segundo grafico de dispersion en el cual se comparan los precios y el kilometraje de cada uno de nuestros vehiculos
## que le proporciona al cliente final? 
Proporciona a nuestros clientes de la informacion adecuada para la eleccion del vehiculo que mas se adecue a sus necesidades actuales.
## Estructura
el proyecto cuenta con dos carpetas en las que se puede aprecir un archivo notebook en cual se realiza una analisis exploratori del dataframe base en el que se ilustran los precios de diferentes vehiculos, asi como, su caracteristicas mas importantes, tambien se cuenta con un archivo requirements.txt en el que se exponen las librerias necesarias para el desarrollo de la pagina web, y lo mas importante que es el archivo app.py en el que se ejecuta las herramientas necesaria para desplegar la pagina web a traves del servidor render, todos estos archivos se encuentran ubicados en un repositoria en GitHub.
## librerias utilizadas
Las librerias implementadas para el desarrollo del proyecto fueron pandas, streamlit para el despligue de la pagina en el servidor render y la liberia plotly_express para el diseño de un grafico de dispersion y un histograma. 

## Comando utilizado para instalar dependencias
pip install -r requirements.txt

## comando utilizado para ejecutar la app localmente
streamlit run app.py

## URL de la app 
https://ventas-autos-5c1z.onrender.com/