from django.db import models
from .utils import Shortened_Code
from .forms import ValidateURL

# Create your models here.
MYURL = 'http://127.0.0.1:8000/'

class URLShortenModel(models.Model):
    original_url = models.CharField(max_length=150, validators=[ValidateURL])
    short_code = models.CharField(max_length=100, blank=True, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if self.short_code is None or self.short_code == '':
            self.short_code = Shortened_Code(self)
        super().save(*args, **kwargs)
        

    def __str__(self):
        return self.original_url

    def get_short_url(self):
        return MYURL+self.short_code
