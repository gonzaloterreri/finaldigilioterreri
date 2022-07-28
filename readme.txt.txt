


```shell
python -m pip install python
```

```shell
python -m pip install django
```

```shell
python -m pip install bootstrap5
```

```shell
python -m pip install crispyforms
```

```shell
python -m pip install pillow
```

La configuracion de email, tanto para la tienda y para contactos se debe hacer en :
ProyectoWeb\settings.py 
linea # configuración de email

EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST="smtp.office365.com"
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER="cosmefulanitoweb499@hotmail.com"
EMAIL_HOST_PASSWORD="cosme12345"

--------------------------------------------------------------------------------------


Linea 60     from_email="cosmefulanitoweb499@hotmail.com"
Linea 61    to="cosmefulanitoweb499@hotmail.com"

