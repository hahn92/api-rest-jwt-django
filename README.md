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

---------- Ajustes para debug en .vscode

.vscode/launch.json
{
    "configurations": [
        {
            "name": "Docker: Python - Django",
            "type": "docker",
            "request": "launch",
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
                "tag": "dockerdebuggingdjango:latest",
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
                "file": "./manage.py"
            }
        }
    ]
}