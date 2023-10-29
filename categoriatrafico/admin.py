from django.contrib import admin
from categoriatrafico.models import CategoriaTrafico


# Register your models here.
@admin.register(CategoriaTrafico)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ["name"]

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

