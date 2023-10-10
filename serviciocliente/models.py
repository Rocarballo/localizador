from django.db import models
CHOICES= (
('GUATEMALA', 'GUATEMALA'),
('EL SALVADOR', 'EL SALVADOR'),
('HONDURAS', 'HONDURAS'),
('NICARAGUA', 'NICARAGUA'),
('COSTA RICA', 'COSTA RICA'),
('PANAMA', 'PANAMA'),
)

class ServicioCliente(models.Model):
    telefono = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Télefono")
    )

    checkin = models.CharField(
        null=True, blank=True, max_length=50, verbose_name=("Agregado")
    )

    restaurante = models.CharField(null=True, blank=True, max_length=50, verbose_name=("Restaurante"))

    cliente = models.CharField(
        null=True, blank=True, max_length=100, verbose_name=("Cliente")
    )

    pais = models.CharField(max_length=50, choices=CHOICES, default=None,blank=True, null=True, verbose_name=("País"))

    estado = models.BooleanField(default=True, verbose_name=("Estado"))

    updated_at = models.DateTimeField(auto_now=True, verbose_name=("actualizacion"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("Creación"))

    class Meta:
        verbose_name = "Servicio al Cliente"
        verbose_name_plural = "Servicio Clientes"
        default_related_name = "ServicioCliente"
        db_table = "ServicioCliente"
        ordering = ["-created_at"]
    
    def delete(self):
        self.estado = False
        self.save()

    def __unicode__(self):
        """ServicioCliente"""
        return str(self.restuarante)

    def __str__(self):
        return str(self.cliente)