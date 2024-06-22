# Instalación
Para ejecutar este proyecto, necesitarás tener instalado Python y algunos paquetes específicos. A continuación se detallan los pasos para configurar el entorno adecuadamente.

## Paso 1: Clonar el Repositorio
```
git clone https://github.com/alexjmz2077/Concurso2024.git
```

```
cd Concurso2024
```

## Paso 2: Configurar el Entorno Virtual (recomendado)
Crea un entorno virtual usando conda para aislar las dependencias del proyecto:
```
conda create --name nombre-del-entorno python=3.12
```

```
conda activate nombre-del-entorno
```


## Paso 3: Instalar Dependencias
Instala los paquetes requeridos para ejecutar el proyecto:
```
conda install -c conda-forge django=5.0.6 djangorestframework=3.15.1 sqlparse=0.5.0
```

```
pip install mysqlclient==2.2.4
```

## Paso 4: Ejecutar Migraciones de Django
Antes de iniciar el servidor, ejecuta las migraciones de Django para configurar la base de datos:
```
python manage.py migrate
```

## Paso 5: Iniciar el Servidor
Finalmente, inicia el servidor de desarrollo de Django:
```
python manage.py runserver
```
El proyecto ahora debería estar corriendo en http://localhost:8000.

## Detalles de los Paquetes Instalados
Asegúrate de tener instaladas las siguientes versiones de los paquetes:

- django: 5.0.6
* djangorestframework: 3.15.1
+ sqlparse: 0.5.0
- mysqlclient: 2.2.4

## Problemas Comunes
Si encuentras algún problema durante la instalación o ejecución del proyecto, verifica que tengas las versiones correctas de Python y los paquetes mencionados.
