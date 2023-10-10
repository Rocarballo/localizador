from django.contrib import admin
from restaurante.models import Restaurante
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter


# Funcion para exportar datos a formatos(excel, html, json)
# Permite genera un reporte de los datos seleccionados
class Exportar(resources.ModelResource):
    class Meta:
        model = Restaurante


@admin.register(Restaurante)
class RestauranteAdin(ImportExportActionModelAdmin, admin.ModelAdmin):
    # Campos a mostrar en la vista de bodequero
    list_display = ["restuarante", "horario", "zona", "colonia", "descripcion"]

    # Filtro que me permite generar reporte por fechas
    list_filter = ("horario", "zona", ("created_at", DateRangeFilter))

    # Funcion que me permite export a los diferentes formatos
    resource_class = Exportar

    # Encabezado el sitio
    date_hierarchy = "created_at"

    list_editable = ["horario", "descripcion"]

    # Funcion que permite buscar por los atributos
    search_fields = ["restuarante", "horario", "descripcion"]
