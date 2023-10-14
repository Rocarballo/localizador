# localizador

Tener en cuanta tener instalado python, pip  y la base de datos MYSQL

PASO 1: Istalar las librerias
#instalar dependencias desde el archivo que se adjunta en el repo
pip install -r requirements.txt

PASO 2; Generar las migraciones ejectutando los siguientes comandos
python manage.py makemigrations
python manage.py migrate

PASO 3; Crear un superusuario, completando lo que require al ejectur el comando
python manage.py createsuperuser

PASO 4: Levantar el proyecto local
python manage.py runserver


# Omitir estas instalaciones 

$ pip install mysqlclienta$ brew install mysql pkg-config
$ pip install mysqlclient
$ pip install django-daterangefilter
$pip install django-liststyle==0.2b
credenciales
admin
1234
