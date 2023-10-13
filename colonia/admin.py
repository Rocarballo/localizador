from datetime import datetime
from django.contrib import admin
from colonia.models import Colonia
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from django.utils.html import format_html
from liststyle import ListStyleAdminMixin

# Funcion para exportar datos a formatos(excel, html, json)
# Permite genera un reporte de los datos seleccionados
class Exportar(resources.ModelResource):
    class Meta:
        model = Colonia


@admin.register(Colonia)
class RestauranteAdmin(ImportExportActionModelAdmin, admin.ModelAdmin, ListStyleAdminMixin):
    # Campos a mostrar en la vista de bodequero
    list_display = [
        "restuarante", 
        "horario_entrada", 
        "horario_salida", 
        "colonia", 
        "descripcion"
    ]
    change_list_template = 'admin/view.html'
    def changelist_view(self, request, extra_context=None):
        response = super(RestauranteAdmin, self).changelist_view(request, extra_context)
        filtered_query_set = response.context_data["cl"].queryset
        datetime_str = '20::00::00'
        time_object = datetime.strptime(datetime_str, '%H::%M::%S').time()
        
        datetime_str2 = '22::00::00'
        time_object2 = datetime.strptime(datetime_str2, '%H::%M::%S').time()
        
        datetime_str3 = '23::00::00'
        time_object3 = datetime.strptime(datetime_str3, '%H::%M::%S').time()
        
        
        currencies_count = filtered_query_set.all()
        extra_context = {
             'coloniasgt': currencies_count,
             'vientehoras': time_object,
             'vientehoras2': time_object2,
             'vientehoras3': time_object3,
        }
        response.context_data.update(extra_context)

        return response
    # Filtro que me permite generar reporte por fechas
    list_filter = ( "zona", ("created_at", DateRangeFilter))

    # Funcion que me permite export a los diferentes formatos
    resource_class = Exportar

    # Encabezado el sitio
    date_hierarchy = "created_at"

    # list_editable = [ "descripcion"]

    # Funcion que permite buscar por los atributos
    search_fields = ["restuarante", "descripcion", "colonia"]

    def get_row_css(self, obj, index):
        if obj.restaurante == 'Mi restaurante':
            return 'red'
        return 'red'

