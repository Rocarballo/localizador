from django.db import models

class Colonia(models.Model):
    restuarante = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Restaurante")
    )

    horario_entrada = models.TimeField(auto_now=False, auto_now_add=False, verbose_name=("Hora inicio"))

    horario_salida = models.TimeField(auto_now=False, auto_now_add=False, verbose_name=("Hora fin"))

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
        verbose_name = "Colonia"
        verbose_name_plural = "Colonias"
        default_related_name = "Colonia"
        db_table = "colonia"
        ordering = ["-created_at"]

    def __unicode__(self):
        """Colonia"""
        return str(self.restuarante)

    def __str__(self):
        return str(self.restuarante)