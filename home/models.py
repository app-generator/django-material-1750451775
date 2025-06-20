# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Asociacion(models.Model):

    #__Asociacion_FIELDS__
    id_asociacion = models.IntegerField(null=True, blank=True)
    nombre_asociacion = models.TextField(max_length=255, null=True, blank=True)
    siglas = models.TextField(max_length=255, null=True, blank=True)
    longitud = models.TextField(max_length=255, null=True, blank=True)
    latitud = models.TextField(max_length=255, null=True, blank=True)

    #__Asociacion_FIELDS__END

    class Meta:
        verbose_name        = _("Asociacion")
        verbose_name_plural = _("Asociacion")


class Patrocinadores(models.Model):

    #__Patrocinadores_FIELDS__
    id_patrocinador = models.IntegerField(null=True, blank=True)
    nombre_patrocindador = models.TextField(max_length=255, null=True, blank=True)

    #__Patrocinadores_FIELDS__END

    class Meta:
        verbose_name        = _("Patrocinadores")
        verbose_name_plural = _("Patrocinadores")


class Especies(models.Model):

    #__Especies_FIELDS__
    id_especie = models.IntegerField(null=True, blank=True)
    nombre_cientifico = models.TextField(max_length=255, null=True, blank=True)
    nombre_comun = models.TextField(max_length=255, null=True, blank=True)
    orden = models.TextField(max_length=255, null=True, blank=True)
    familia = models.TextField(max_length=255, null=True, blank=True)
    genero = models.TextField(max_length=255, null=True, blank=True)
    especie = models.TextField(max_length=255, null=True, blank=True)
    estado_conservacion = models.TextField(max_length=255, null=True, blank=True)
    habito = models.TextField(max_length=255, null=True, blank=True)
    tipo_bosque = models.TextField(max_length=255, null=True, blank=True)
    nativa = models.BooleanField()
    localizacion = models.TextField(max_length=255, null=True, blank=True)

    #__Especies_FIELDS__END

    class Meta:
        verbose_name        = _("Especies")
        verbose_name_plural = _("Especies")


class Vivero(models.Model):

    #__Vivero_FIELDS__
    id_inventario = models.IntegerField(null=True, blank=True)
    id_asociacion = models.ForeignKey(Asociacion, on_delete=models.CASCADE)
    tipo_vivero = models.TextField(max_length=255, null=True, blank=True)
    nombre_vivero = models.TextField(max_length=255, null=True, blank=True)
    infraestructura = models.TextField(max_length=255, null=True, blank=True)
    ubicacion = models.TextField(max_length=255, null=True, blank=True)

    #__Vivero_FIELDS__END

    class Meta:
        verbose_name        = _("Vivero")
        verbose_name_plural = _("Vivero")


class Vivero_Especie(models.Model):

    #__Vivero_Especie_FIELDS__
    id_vivero_especie = models.IntegerField(null=True, blank=True)
    id_vivero = models.ForeignKey(vivero, on_delete=models.CASCADE)
    id_especie = models.ForeignKey(Especies, on_delete=models.CASCADE)
    cantidad_0_15cm = models.IntegerField(null=True, blank=True)
    fecha_embolsa_0_15cm = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fecha_entrega_0_15cm date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    cantidad_15_30cm = models.IntegerField(null=True, blank=True)
    fecha_embolsa_15_30cm = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fecha_entrega_15_30cm = models.DateTimeField(blank=True, null=True, default=timezone.now)
    cantidad_30_50cm = models.IntegerField(null=True, blank=True)
    fecha_embolsa_30_50cm = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fecha_entrega_30_50cm = models.DateTimeField(blank=True, null=True, default=timezone.now)
    cantidad_mayor_50cm = models.IntegerField(null=True, blank=True)
    fecha_embolsa_mayor_50cm = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fecha_entrega_mayor_50cm = models.DateTimeField(blank=True, null=True, default=timezone.now)
    edad_minima_entrega = models.DateTimeField(blank=True, null=True, default=timezone.now)
    tipo_propagacion = models.TextField(max_length=255, null=True, blank=True)

    #__Vivero_Especie_FIELDS__END

    class Meta:
        verbose_name        = _("Vivero_Especie")
        verbose_name_plural = _("Vivero_Especie")



#__MODELS__END
