from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

from serviciocliente.models import ServicioCliente


# Funcion para exportar datos a formatos(excel, html, json)
# Permite genera un reporte de los datos seleccionados
class Exportar(resources.ModelResource):
    class Meta:
        model = ServicioCliente


@admin.register(ServicioCliente)
class ServicioClienteAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    # Campos a mostrar en la vista de bodequero
    list_display = ["telefono", "checkin", "restaurante", "pais", "estado"]

    # Filtro que me permite generar reporte por fechas
    list_filter = ("checkin", "pais", "estado", ("created_at", DateRangeFilter))

    # Funcion que me permite export a los diferentes formatos
    resource_class = Exportar

    # Encabezado el sitio
    date_hierarchy = "created_at"

    list_editable = ["checkin", "restaurante"]

    # Funcion que permite buscar por los atributos
    search_fields = ["telefono", "checkin", "restaurante"]