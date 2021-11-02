"""
Web Scraping -> Técnicas para extraer información de sitios de internet
xPath -> lenguaje para extraer datos de manera efectiva
--------------------------------------------------------------------------
Python

El lenguaje más especializado para hacer data science
Requests -> libreria para controlar http
BeautifulSoup -> extraer nformación de un documento html
Selenium -> controlar sitios web de manera automática
Scrapy -> recolectar datos de población local todos los dias
-------------------------------------------------------------------------
HTTP -> Hypertext Transfer Protocol
HTML
--------------------------------------------------------------------------
Robots.txt
Archivo para decirle a web scrappers que hacer y que no hacer
se encuentra en la raiz platzi.com/robots.txt
User-Agent:* -> permite cualquier User-Agent
Allow: / -> se visita todo el directorio completo
Disallow: -> no permitir
 
XML Path Language -> xtensible marquet language
expresiones regulares -> lenguaje para definir patrones
//div/span//h1[@clss="title"][1] -> extraer el primer titulo 

TIPOS DE NODOS EN XPATH
Nodos -> cada división html  de la página web

http://quotes.toscrape.com/
----------------- Expresiones xPath -------------------------------
$x('/') --> ir a la raiz
$x('/html') --> ir a html
$x('//h1') --> ver h1
$x('//h1/a/text()').map(x => x.wholeText) --> obtener texto de h1
$x('//span/..') --> seleccionar nodos por encima de span
$x('//span/@class') --> obtener atributos de una clase

-------------------- Predicados -----------------------------------
$x('/html/body/div/div[1]') -> traer el primer div de una lista
$x('/html/body/div/div[last()]') -> traer el último div
$x('//span[@class="text"]/text()') -> traer span que tengan atributo tipo texto
$x('//span[@class="text"]/text()').map (x=> x.wholeText) -> devolver los textos de las citas

--------------------- Operadores ----------------------------------
= -> igual
!= -> distinto de
$x('/html/body/div/div[position()>1]') -> traer elemenos de posición mayores a 1
and -> y
or -> o
$x('//span[@class="text" or @class="tag-item"]')
$x('//span[not(@class)]') -> span que no tiene atributo de tipo class

--------------------- wildcards -----------------------------------
para casos de incertidumbre
$x('/*') $x('/html/*')  -> traiga todos los nodos que hay después
$x('//*') -> traer todo el documento
$x('//span[@class="text"]/@*') -> traer todos los atributos
$x('/html/body//div/@*') -> todos los atributos de todos los divs que tiene body
node -> nos trae nodos y contenido
$x('//span[@class="text" and @itemprop="text"]/node() ')

---------------------- in-text search en Xpath -------------------------
$x('//small[@class="author" and starts-with(.,"A")]') -> extraer autores que empiezen con la letra A
$x('//small[@class="author" and starts-with(.,"A")]/text()').map(x=>x.wholeText)
$x('//small[@class="author" and contains(.,"Ro")]/text()').map(x=>x.wholeText)

------------------------ XPath Axes --------------------------------------
$x('/html/body/div/self::div')
$x('/html/body/div/child::div') -> traer hijos
$x('/html/body/div/descendant::div') -> traer descendencia
$x('/html/body/div/descendant-or-self::div') -> traer descendencia y nodo en si mismo

--------------------- Aplicando lo aprendido ------------------------------------------
http://books.toscrape.com/

Extraer titulos de los libros
$x('//article[@class="product_pod"]/h3/a/@title').map(x=> x.value)

Extraer precios de los libros
$x('//article[@class="product_pod"]/div[@class="product_price"]/p[@class="price_color"]/text()').map(x=> x.wholeText)

Extraer categorias
$x('//div[@class="side_categories"]/ul[@class="nav nav-list"]/li/ul/li/a/text()').map(x=> x.wholeText)

======================================== PYTHON ===========================================



"""

 