# Practica Dirigida 2

![alt text]({ED6DAF91-D4A7-4079-BF52-122A602AF191}.png)

![alt text]({8F30CF89-585B-47D3-9C38-037C231730AC}.png)

![alt text]({19404E0B-3E1C-481A-8F13-ACCABD6BFDC7}.png)

![alt text]({7F88B7CD-58EA-493D-BB5B-74B77E627A6C}.png)

![alt text]({22A95CED-5C5B-4B67-9375-518DB170ECC2}.png)


![alt text]({F185A61C-975C-4338-961F-557BEEA53919}.png)

Preguntas
¿Qué diferencias observas en el historial del repositorio después de restaurar un commit mediante reflog?

Que se eliminaron los commits posteriores al commit seleccionado, dejandome en un estado en el que al commit restaurado es el HEAD de la rama

¿Cuáles son las ventajas y desventajas de utilizar submódulos en comparación con subtrees?

Utilizar submodulos tiene como ventaja que tu no tienes que tener una copia  completa de ese repositorio sino solamente referenciarlo mientra que en un subtree necesariamente tienes que tenerlo integro en tu repositorio, ademas el submodulo tiene que ser mantenido por separado, otra ventaja del submodulo es que no se tiene que mesclar con tu repositorio principal dejando asi un acabado mas limpio, ademas de que no se vuelve dependiente de tu repositorio al tener su propio git  mientras que los subtrees al volverse parte de tu repositorio se vuelve dependiente de este, lo malo es que suele tener probleas con herramientas de CI/CD mientras que los subtrees presentan mayor compatibilidad con estas.

¿Cómo impacta la creación y gestión de hooks en el flujo de trabajo y la calidad del código?

Ayuda a poder tener un codigo mas limpio por que es como poner politicas que se deben cumplir obligatoriamente y esas politicas pueden garatizar una integridad en todos los que estan trabajando, siendo de mayor utilidad para los trabajos colaborativos pues estandariza como debe hacerse por ejemplo los commits.

¿De qué manera el uso de git bisect puede acelerar la localización de un error introducido recientemente?

Ayuda a acelerar la localizacion de errores por que automatiza la busqueda binaria entre los commits que fueron seleccionados como buenos y los malos odefectuosos, haciendo asi mas facil encontrar el commit exacto que produjo el error, mientra que revisar manualmente puede llevar mucho tiempo.

¿Qué desafíos podrías enfrentar al administrar ramas y stashes en un proyecto con múltiples colaboradores?

Los desafios a enfrentarse son que es posible que oueda crearse una desincronizacion del trabajo en curso donde los stashes pueden llegar a olvidarse.



## Ejercicios
1 . Extiende el menú de gestión de ramas para incluir la funcionalidad de renombrar ramas.

Instrucciones:

Investiga el comando git branch -m que permite renombrar una rama.
Modifica la función de "Gestión de ramas" para agregar una nueva opción (por ejemplo, "f) Renombrar una rama").
Implementa la lógica para solicitar al usuario el nombre de la rama actual y el nuevo nombre.
Verifica que, tras el cambio, la rama se renombre correctamente.
Pista: Considera cómo se comporta el cambio si la rama en uso es la que se desea renombrar.

