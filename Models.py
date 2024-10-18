from django.db import models
from django.db import models
from django.contrib.auth.models import User

class employee(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True ,blank=True)
    ename=models.CharField(max_length=200)
    eage=models.BigIntegerField()
    edateofbirth=models.DateField(max_length=200)
    eeducation=models.CharField(max_length=200)
    etype=models.TextField(max_length=100)
    eimage=models.ImageField(upload_to="eimage",null=True,blank=True)

    def save(self, *args, **kwargs):
        # Make sure you're not setting `eimage` to a string
        if isinstance(self.eimage, str):
            raise ValueError("eimage must be a file object, not a string.")
        super().save(*args, **kwargs)
# Create your models here.