from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.PositiveBigIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields