from django.db import models

# Create your models here.
# class BoardTab(models.Model):
#     name = models.CharField(max_length = 20)
#     passwd = models.CharField(max_length = 20)
#     mail = models.CharField(max_length = 30)
#     title = models.CharField(max_length = 100)
#     cont = models.TextField()
#     bip = models.GenericIPAddressField()
#     bdate = models.DateTimeField()
#     readcnt = models.IntegerField()
#     gnum = models.IntegerField()
#     onum = models.IntegerField()
#     nested = models.IntegerField()
#     
#     
class Boardtab(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    passwd = models.CharField(max_length=20, blank=True, null=True)
    mail = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    cont = models.TextField(blank=True, null=True)
    bip = models.CharField(max_length=20, blank=True, null=True)
    bdate = models.DateField(blank=True, null=True)
    readcnt = models.IntegerField(blank=True, null=True)
    gnum = models.IntegerField(blank=True, null=True)
    onum = models.IntegerField(blank=True, null=True)
    nested = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boardtab'