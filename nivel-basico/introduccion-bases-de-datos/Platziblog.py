"""
 _______________________________     
|USUARIOS                       | 
|id: int (pk)                   |
|login:VARCHAR(30) NN           |       
|passwd: varchar(32) NN         |--|-|---|--|
|nickname: varchar(40) NN       |    |      |
|email: varchar(40) NN Unique   |    |      |   
|_______________________________|    |      |    
                                     |      |
 _______________________________     |      |   
|POST                           |    |      |
|id: int (pk)                   |    |      |
|titulo:VARCHAR(150)            |    |      |
|Fecha publ: timestamp          |>---|      |
|contenido: text                |           |
|estatus:char(8)                |---|--|    | >-----------------------------|    
|    check(activo:inactivo)     |      |    |                               |
|usuario_id:Int (fk)            |>--|  |    |                               |
|Categoria_id:Int (fk)          |   |  |    |                               |
|_______________________________|   |  |    |                               |    
                                    |  |    |                               |
 _______________________________    |  |    |                               |
|Comentarios                    |   |  |    |                               |
|id: int (pk)                   |   |  |    |                               |
|comentario:TEXT                |>--)--)----|                               |
|usuario_id:Int (fk)            |>--)--|                                    |
|post_id:Int (fk)               |   |                                       |
|_______________________________|   |                                       |    
                                    |                                       |        
 _______________________________    |                                       |        
|Categorias                     |   |                                       |
|id: int (pk)                   |   |                                       |        
|Categoria:VARCHAR(30)          |-|-|                                       |       
|_______________________________|                                           |
                                                                            |
 _______________________________                            ________________|______________ 
|Etiquetas                      |                          |Post Etiquetas                 |
|id: int (pk)                   |>-----------------------|-|post_id: int (fk,pk)           |  
|nombre_etiqueta:VARCHAR(30)    |                          |etiqueta_id: int (fk,pk)       |    
|_______________________________|                          |_______________________________|   


"""