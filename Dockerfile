# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# Agrega codigo de python
ADD ManagerTasks/ .

#Instala dependencias del sistema operativo
# POSTGIS Development Libraries
RUN apt-get update && apt-get install -y libgdal-dev 

RUN apt-get install -y build-essential libpq-dev

# Cliente posgrest
RUN apt-get install -y postgresql-client 

RUN apt-get install python3-psycopg2

# Set timezone and locales
RUN apt-get install -y locales && \
    sed -i 's/^# *\(es_CO.UTF-8\)/\1/' /etc/locale.gen && locale-gen

# Instalacion de dependencias de python
RUN pip install --upgrade pip setuptools wheel

RUN pip install psycopg2-binary --no-binary psycopg2-binary

RUN pip3 install -r requirements.txt

# Actualizar base de datos
#RUN python manage.py makemigrations

#RUN python manage.py migrate

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
#USER appuser


# --insecure cuando no se han configurado el servidor de archivos estaticos
#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ] 

# Producction mode
#CMD [ "gunicorn", "ManagerTasks.wsgi", "--bind", "0.0.0.0:8000" ]

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi"]
