from django.db import models

class Restaurante(models.Model):
    restuarante = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Restaurante")
    )

    horario = models.CharField(
        null=True, blank=True, max_length=50, verbose_name=("Horario")
    )

    zona = models.CharField(null=True, blank=True, max_length=50, verbose_name=("Zona"))

    colonia = models.CharField(
        null=True, blank=True, max_length=50, verbose_name=("Colonia")
    )

    # pais = models.CharField(null=True, blank=True, max_length=50, verbose_name=("Pais"))

    descripcion = models.CharField(
        null=True, blank=True, max_length=50, verbose_name=("Descripción")
    )

    updated_at = models.DateTimeField(auto_now=True, verbose_name=("actualizacion"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("Creación"))

    class Meta:
        verbose_name = "Restaurante"
        verbose_name_plural = "Restaurantes"
        default_related_name = "Restaurante"
        db_table = "restaurate"
        ordering = ["-created_at"]

    def __unicode__(self):
        """Restaurante"""
        return str(self.restuarante)

    def __str__(self):
        return str(self.restuarante)