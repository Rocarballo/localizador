from django.db import models

class CategoriaTrafico(models.Model):
    name = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Nombre")
    )

    updated_at = models.DateTimeField(auto_now=True, verbose_name=("actualizacion"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("Creación"))

    class Meta:
        verbose_name = "Categoría de tráfico"
        verbose_name_plural = "Categoría de tráfico"
        default_related_name = "Categoría de tráfico"
        db_table = "categoriatrafico"
        ordering = ["-created_at"]

    def __unicode__(self):
        """Categoria trafico"""
        return str(self.name)

    def __str__(self):
        return str(self.name)