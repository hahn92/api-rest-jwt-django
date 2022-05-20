# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Instala dependencias del sistema operativo
# POSTGIS Development Libraries
RUN apt-get update && apt-get install -y libgdal-dev 

RUN apt-get install -y build-essential libpq-dev

# Instala dependencias de python
RUN apt-get install python3-psycopg2

# Cliente posgrest
RUN apt-get install -y postgresql-client 

# Set timezone and locales
RUN apt-get install -y locales && \
    sed -i 's/^# *\(es_CO.UTF-8\)/\1/' /etc/locale.gen && locale-gen

# Instalacion de dependencias de python
RUN pip install --upgrade pip setuptools wheel

RUN pip install psycopg2-binary --no-binary psycopg2-binary

WORKDIR /usr/src/app

# copiamos unica las dependencias de python al inicio antes de agregar todo el codigo
COPY ManagerTasks/requirements.txt .

RUN pip3 install -r requirements.txt

# Agrega codigo de python
COPY ManagerTasks/ .

# Actualizar base de datos
#RUN python manage.py makemigrations

#RUN python manage.py migrate

# --insecure cuando no se han configurado el servidor de archivos estaticos
#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ] 

# Producction mode
#CMD [ "gunicorn", "ManagerTasks.wsgi", "--bind", "0.0.0.0:8000" ]

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ManagerTasks.wsgi"]
