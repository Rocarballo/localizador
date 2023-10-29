from django.db import models

# Create your models here.
class Regiones(models.Model):
    name = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Nombre de la región")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=("actualizacion"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("Creación"))
    
    estado = models.BooleanField(default=True, verbose_name=("Estado"))

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"
        default_related_name = "Región"
        db_table = "region"
        ordering = ["-created_at"]

    def __unicode__(self):
        """Regiones"""
        return str(self.name)

    def __str__(self):
        return str(self.name)
    
class Localizar(models.Model):
    zona = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Zona")
    )
    
    callei = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Calle i")
    )
    callf = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Calle f")
    )
    avenidai = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Avenida i")
    )
    avenidaf = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Avenida f")
    )
    tienda = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Tienda")
    )
    area = models.ForeignKey(Regiones, on_delete=models.CASCADE, null=True, verbose_name='Area')
    
    horario_entrada = models.TimeField(auto_now=False, auto_now_add=False, verbose_name=("Horario"))
    
    comentario = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Comentario")
    )
    
    estado = models.BooleanField(default=True, verbose_name=("Estado"))
    
    updated_at = models.DateTimeField(auto_now=True, verbose_name=("actualizacion"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("Creación"))

    class Meta:
        verbose_name = "Localizador"
        verbose_name_plural = "Localizador"
        default_related_name = "Localizador"
        db_table = "localizador"
        ordering = ["-created_at"]

    def __unicode__(self):
        """Localizador"""
        return str(self.zona)

    def __str__(self):
        return str(self.zona)