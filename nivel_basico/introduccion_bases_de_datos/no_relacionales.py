"""
clasificacion:

clave - valor: 
    - Gran cantidad de información con campo id, rapidas
        las consultas son dificiles
        dynamoDB, cassandra
Basadas en documentos:
    - documentos json y xml, 
        MongoDB, Firestore, no responde bien a querys
basadas en grafos:
    - entidades multiconectadas, utiles en inteligencia
        artificial,
        neo4j, titan db
en memoria:
    - sumamente rapidas, tienen limites y son volatiles
        Memcached, Redis
optimizadas para busqueda:
    - sirven para hacer querys complejos en cuestiones 
        rapidas de tiempo,
        BigQuery, Elasticsearch 

-------------------------------------------------------------------
        Firestore - basadas en documentos - servicio administrado

Jerarquía de datos en Firestore:
    - Base de datos
        - Coleccion 
            - Documentos 


                                Firebase

Top level collections -> colecciones que se tienen de inmediato 


"""