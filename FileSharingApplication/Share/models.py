from django.db import models

# Create your models here.
class Fileinfo(models.Model):
    title = models.CharField(max_length=50)
    filepath = models.FileField(upload_to='Media/',null=True,verbose_name="")
    description = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title