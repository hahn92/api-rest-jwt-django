# api-rest-jwt-django
REST API en Django

Administrador de tareas simple:

- Los usuarios se pueden autenticar (JWT)
- Las tareas son privadas. Solo las puede administrar su dueño
- Los usuarios pueden agregar, editar, eliminar y marcar como completa/incompleta las tareas
- El listado de tareas es paginado
- Busquedas por descripción
- test unitarios


Ejecuta con docker-compose:

Ejecutar:
-  docker-compose up -d

Detener:
-  docker-compose down


-----------

- Se incluyen las colexiones de Postman para consumo de los APIs


---------- Archivo de configuracion de variables de entorno .env

- archivo con la configuracion de las variables de entorno, se incluye un archivo de ejemplo "example.env"

---------- Ajustes para debug en .vscode

.vscode/launch.json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Docker: Python - Django",
            "type": "docker",
            "request": "launch",
            "env": {
                "PYTHONPATH": "src",
                "DEBUG": "True",
                "MEDIA": "False",
                "DATABASE": "False",
                "ALLOWED_HOSTS": "localhost",
                "SECRET_KEY": "django-insecure-l&kgmclk8fmpv37nio8ltkpz$3=h6@18==49f*=cf0hpsmm7js",
                "DATABASE_HOST": "db",
                "DATABASE_NAME": "task_manager",
                "DATABASE_USER": "postgres",
                "DATABASE_PASSWORD": "root",
                "ACCESS_TOKEN_LIFETIME": "15",
                "REFRESH_TOKEN_LIFETIME": "3",
                "SLIDING_TOKEN_LIFETIME": "60",
                "SLIDING_TOKEN_REFRESH_LIFETIME": "3",
                "LANGUAGE_CODE": "es-co",
                "TIME_ZONE": "America/Bogota",
                "LANG": "es_CO.UTF-8",
                "LANGUAGE": "es_CO.UTF-8", 
                "LC_ALL": "es_CO.UTF-8"
            },
            "preLaunchTask": "docker-run: debug",
            "python": {
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}",
                        "remoteRoot": "/app"
                    }
                ],
                "projectType": "django"
            }
        }
    ]
}


.vscode/tasks.json
{
	"version": "2.0.0",
	"tasks": [
		{
			"type": "docker-build",
			"label": "docker-build",
			"platform": "python",
			"dockerBuild": {
				"tag": "pruebaelenas:latest",
				"dockerfile": "${workspaceFolder}/Dockerfile",
				"context": "${workspaceFolder}",
				"pull": true
			}
		},
		{
			"type": "docker-run",
			"label": "docker-run: debug",
			"dependsOn": [
				"docker-build"
			],
			"python": {
				"args": [
					"runserver",
					"0.0.0.0:8000",
					"--nothreading",
					"--noreload"
				],
				"file": "manage.py"
			}
		}
	]
}