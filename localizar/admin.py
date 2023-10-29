from django.contrib import admin
from localizar.models import Regiones, Localizar
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from liststyle.admin import ListStyleAdminMixin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
@admin.register(Regiones)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ["name"]
    date_hierarchy = "created_at"

    def render_change_form(
        self, request, context, add=False, change=False, form_url="", obj=None
    ):
        context.update(
            {
                "show_delete": False,  # Here
                # 'show_save': False,
                "show_save_and_continue": False,
            }
        )
        return super().render_change_form(request, context, add, change, form_url, obj)


class Exportar(resources.ModelResource):
    class Meta:
        model = Localizar

@admin.register(Localizar)
class LocalizarAdmin(ImportExportActionModelAdmin, admin.ModelAdmin, ListStyleAdminMixin):
    list_display = [
        "zona",
        "callei",
        "callf",
        "avenidai",
        "avenidaf",
        "tienda",
        "area",
        "horario_entrada",
        "comentario",
    ]

    search_fields = ["zona", "area", "tienda"]
    list_filter = ("area", ("created_at", DateRangeFilter))

    def changelist_view(self, request, extra_context=None):
        response = super(LocalizarAdmin, self).changelist_view(request, extra_context)
        filtered_query_set = response.context_data["cl"].queryset
        currencies_count = filtered_query_set.all()
        extra_context = {"coloniasgt": currencies_count}
        response.context_data.update(extra_context)

        return response

    def render_change_form(
        self, request, context, add=False, change=False, form_url="", obj=None
    ):
        context.update(
            {
                "show_delete": False,  # Here
                # 'show_save': False,
                "show_save_and_continue": False,
            }
        )
        return super().render_change_form(request, context, add, change, form_url, obj)

    change_list_template = "admin/viewlocalizador.html"
