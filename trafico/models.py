from django.db import models

from categoriatrafico.models import CategoriaTrafico
CHOICES= (
('GUATEMALA', 'GUATEMALA'),
('EL SALVADOR', 'EL SALVADOR'),
('HONDURAS', 'HONDURAS'),
('NICARAGUA', 'NICARAGUA'),
('COSTA RICA', 'COSTA RICA'),
('PANAMA', 'PANAMA'),
)

class Trafico(models.Model):
    
    categoria = models.ForeignKey(CategoriaTrafico, on_delete=models.CASCADE, null=True, verbose_name='Categoria')
    telefono = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Télefono")
    )

    restaurante = models.CharField(null=True, blank=True, max_length=50, verbose_name=("Restaurante"))

    cliente = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Cliente")
    )

    pais = models.CharField(max_length=50, choices=CHOICES, default=None,blank=True, null=True, verbose_name=("País"))
    
    comentario = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Comentario")
    )

    usuario = models.CharField(max_length=50, default=None,blank=True, null=True, verbose_name=("Encargado"))

    estado = models.BooleanField(default=True, verbose_name=("Estado"))
    
    updated_at = models.DateTimeField(auto_now=True, verbose_name=("actualizacion"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("Creación"))

    class Meta:
        verbose_name = "Tráfico"
        verbose_name_plural = "Tráfico"
        default_related_name = "Tráfico"
        db_table = "trafico"
        ordering = ["-created_at"]
    
    def delete(self):
        self.estado = False
        self.save()

    def __unicode__(self):
        """Trafico"""
        return str(self.restuarante)

    def __str__(self):
        return str(self.cliente)