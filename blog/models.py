from django.db import models
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    tittle = models.CharField(max_length=500)
    head0 = models.CharField(max_length=500,default="")
    head1 = models.CharField(max_length=500,default="")
    head2 = models.CharField(max_length=500,default="")
    chead0 = models.CharField(max_length=5000,default="")
    chead1 = models.CharField(max_length=5000,default="")
    chead2 = models.CharField(max_length=5000,default="")
    thumbnail = models.ImageField(upload_to='lol/images',default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.tittle