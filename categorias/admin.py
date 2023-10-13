from django.contrib import admin
from categorias.models import Categoria

# Register your models here.
@admin.register(Categoria)
class RestauranteAdmin(admin.ModelAdmin):
        list_display = [ "name" ]