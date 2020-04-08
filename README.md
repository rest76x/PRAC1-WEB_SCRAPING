# Pràctica 1: Web scraping

## Descripció

Aquesta pràctica s’ha realitzat sota el context de l’assignatura _Tipologia i cicle de vida de les dades_, pertanyent al Máster en ciència de dades de la universitat Oberta de Catalunya. Consisteix en aplicar tècniques de _web scraping_, mitjançant el llenguatge de programació python per extreure així dades de la web _www.aco.es_ y generar un _dataset_. Ens basem en el fet que som una de les empreses dominants del mercat i volem fer un anàlisi de mercat amb el competidor principal, per això extrèiem tota la informació disponible en la pagina web del competidor per poder classificar els seus productes en relació amb els nostres i fer una comparació en quant a preus i propietats.

## Miembros del equipo

La actividad ha sido realizada de manera individual por **Xavier Parramon Boada**.

## Ficheros del código fuente

* **src/main.py**: punto de entrada al programa. Inicia el proceso de scraping.
* **src/scraper.py**: contiene la implementación de la clase _AccidentsScraper_ cuyos métodos generan el conjunto de datos a partir de la base de datos online [PlaneCrashInfo](http://www.planecrashinfo.com/database.htm).
* **src/reason_classifier.py**: contiene la implementación de la clase que se encarga de asignar una causa a un resumen de accidente dado. Para ello, utiliza la librería *TextBlob*.

## Recursos

1. Lawson, R. (2015). _Web Scraping with Python_. Packt Publishing Ltd. Chapter 2. Scraping the Data.
2. Mitchel, R. (2015). _Web Scraping with Python: Collecting Data from the Modern Web_. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.
