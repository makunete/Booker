from django.contrib import admin

# Register your models here.
from .models import Usuarios

admin.site.register(Usuarios)

from .models import Genero

admin.site.register(Genero)

from .models import Libros

admin.site.register(Libros)