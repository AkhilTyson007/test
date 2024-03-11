from django.db import models

# Create your models here.
        
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    pub_date = models.DateField()
    product_type = models.CharField(max_length=10)  
    image = models.ImageField( upload_to='shop/images/',null=True)
    video = models.FileField(upload_to='shop/videos/', null=True)
    
    def __str__(self):
        return str(self.product_id)+" ("+str(self.pub_date)+')' 


