from django.db import models

# Create your models here.
class Champion(models.Model):
    cname = models.CharField(primary_key=True, max_length=10)
    cimg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'champion'


class Itembuild(models.Model):
    pnum = models.ForeignKey('Pos', models.DO_NOTHING, db_column='pnum')
    item1 = models.CharField(max_length=30, blank=True, null=True)
    item2 = models.CharField(max_length=30, blank=True, null=True)
    item3 = models.CharField(max_length=30, blank=True, null=True)
    pick = models.CharField(max_length=10, blank=True, null=True)
    user = models.CharField(max_length=10, blank=True, null=True)
    win = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itembuild'


class Lun(models.Model):
    pnum = models.ForeignKey('Pos', models.DO_NOTHING, db_column='pnum')
    rimg1 = models.CharField(max_length=30, blank=True, null=True)
    rimg2 = models.CharField(max_length=30, blank=True, null=True)
    rimg3 = models.CharField(max_length=30, blank=True, null=True)
    rimg4 = models.CharField(max_length=30, blank=True, null=True)
    rimg5 = models.CharField(max_length=30, blank=True, null=True)
    rimg6 = models.CharField(max_length=30, blank=True, null=True)
    rimg7 = models.CharField(max_length=30, blank=True, null=True)
    rimg8 = models.CharField(max_length=30, blank=True, null=True)
    rimg9 = models.CharField(max_length=30, blank=True, null=True)
    rimg10 = models.CharField(max_length=30, blank=True, null=True)
    rimg11 = models.CharField(max_length=30, blank=True, null=True)
    pick = models.CharField(max_length=10, blank=True, null=True)
    user = models.CharField(max_length=10, blank=True, null=True)
    win = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lun'


class Pos(models.Model):
    cirum = models.ForeignKey(Champion, models.DO_NOTHING, db_column='cirum')
    pname = models.CharField(max_length=5, blank=True, null=True)
    pno = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pos'


class Shoes(models.Model):
    pnum = models.ForeignKey(Pos, models.DO_NOTHING, db_column='pnum')
    item1 = models.CharField(max_length=30, blank=True, null=True)
    pick = models.CharField(max_length=10, blank=True, null=True)
    user = models.CharField(max_length=10, blank=True, null=True)
    win = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shoes'


class Skill(models.Model):
    pnum = models.ForeignKey(Pos, models.DO_NOTHING, db_column='pnum')
    pimg = models.TextField(blank=True, null=True)
    sk1img = models.TextField(blank=True, null=True)
    s2img = models.TextField(blank=True, null=True)
    s3img = models.TextField(blank=True, null=True)
    s4img = models.TextField(blank=True, null=True)
    s1 = models.CharField(max_length=2, blank=True, null=True)
    s2 = models.CharField(max_length=2, blank=True, null=True)
    s3 = models.CharField(max_length=2, blank=True, null=True)
    s4 = models.CharField(max_length=2, blank=True, null=True)
    s5 = models.CharField(max_length=2, blank=True, null=True)
    s6 = models.CharField(max_length=2, blank=True, null=True)
    s7 = models.CharField(max_length=2, blank=True, null=True)
    s8 = models.CharField(max_length=2, blank=True, null=True)
    s9 = models.CharField(max_length=2, blank=True, null=True)
    s10 = models.CharField(max_length=2, blank=True, null=True)
    s11 = models.CharField(max_length=2, blank=True, null=True)
    s12 = models.CharField(max_length=2, blank=True, null=True)
    s13 = models.CharField(max_length=2, blank=True, null=True)
    s14 = models.CharField(max_length=2, blank=True, null=True)
    s15 = models.CharField(max_length=2, blank=True, null=True)
    pick = models.CharField(max_length=10, blank=True, null=True)
    user = models.CharField(max_length=10, blank=True, null=True)
    win = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill'


class Spell(models.Model):
    pnum = models.ForeignKey(Pos, models.DO_NOTHING, db_column='pnum')
    sp1img = models.TextField(blank=True, null=True)
    sp2img = models.TextField(blank=True, null=True)
    pick = models.CharField(max_length=10, blank=True, null=True)
    user = models.CharField(max_length=10, blank=True, null=True)
    win = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spell'


class Startitems(models.Model):
    pnum = models.ForeignKey(Pos, models.DO_NOTHING, db_column='pnum')
    item1 = models.CharField(max_length=30, blank=True, null=True)
    item2 = models.CharField(max_length=30, blank=True, null=True)
    pick = models.CharField(max_length=10, blank=True, null=True)
    user = models.CharField(max_length=10, blank=True, null=True)
    win = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'startitems'
