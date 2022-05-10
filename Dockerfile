FROM python:3.9

WORKDIR /usr/src/app

# Agrega codigo de python
ADD ManagerTasks .

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
RUN python manage.py makemigrations

RUN python manage.py migrate

# --insecure cuando no se han configurado el servidor de archivos estaticos
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ] 
#CMD [ "gunicorn", "tusalvavidas.wsgi", "--bind", "0.0.0.0:8000" ]