# Historial de modificaciones:

- Se ha actualizado el archivo "/apps/category/moldels.py" añadiendo el campo "description".
- En dicho archivo, se ha configurado "description" como "TextField" con "blank=True" y "null=True" para que pueda ser un campo sin limite de longitud y para que se pueda dejarlo vacío.

- Se ha actualizado el archivo "/apps/category/serializers.py" añadiendo "description" a los "fields" para que se pueda serializar correctamente.

- Se ha creado el archivo /core/.env
- Se ha modificado el archivo /core/settings.py . Aunque no se ha requerido de forma explicita y directa, me ha parecido importante organizar y ocultar ciertos datos utilizando variables de entorno. Considero que esta modificación facilita la configuración del proyecto, haciéndola más dinámica y segura. Consecuentemente, se ha actualizado el archivo .env.

- Se ha creado un archivo /core/.env.exemple con los campos actualmente presentes en el archivo .env

- Se ha modificado el endpoint (presente en /apps/category/views.py) que retorna todas las categorías registrada para que también retorne el campo "description" añadido en el modelo "category".
- El archivo "/apps/category/urls.py" tenía la linea 7 configurada como "path('categories', ListCategoriesView.as_view()),"
Inicialmente llegué a pensar que fuera un error, dado que estaba intentando acceder a las categorias con una ruta similar a la definida para los posts del blog ("/api/blog/"). Aunque después me di cuenta que no era un error, igualmente me pareció más limpio y coherente modificar ese archivo para que las rutas sean similares ("/api/blog/" devuelve los posts y "/api/category/" devuelve las categorias).

-

Psycopg2 para Mac y Linux:
sudo apt install python3-dev libpq-dev

Cuando se instalan los requerimientos si usa python 3.10 da un error y hay que poner en requirements.txt quitar "backports.zoneinfo==0.2.1" y poner : " backports.zoneinfo==0.2.1;python_version<"3.9" " porque da un error con la version mas actual.
