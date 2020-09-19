from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.db.models import *


class Student(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=4)
    sex = models.CharField(max_length=2)
    address = models.CharField(max_length=50)
    birthday = models.DateTimeField()


    class Meta:
        managed = False
        db_table = 'student'


class Test(models.Model):
    name = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class Post(models.Model):
    author = models.CharField(max_length=15, null=False)
    title = models.CharField(max_length=200,)
    text = models.TextField(default='')
    create_data = models.DateTimeField(default=timezone.now)
    publiced_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publiced_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class User(models.Model):
    user_id = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20, default='')

    class Meta:
        db_table = 'users'

class Items(models.Model):
    id = models.BigAutoField(primary_key=True)
    index = models.BigIntegerField(blank=True, null=True)
    item_code = models.BigIntegerField(unique=True)
    item_name = models.CharField(max_length=600, blank=True, null=True)
    item_nick_name = models.CharField(max_length=350, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    pb = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'

    def __str__(self):
        return self.item_code

class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    index = models.BigIntegerField(blank=True, null=True)
    item_code = models.BigIntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=600, blank=True, null=True)
    item_nick_name = models.CharField(max_length=350, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    box_num = models.IntegerField(blank=True, null=True)
    ea_num = models.IntegerField(blank=True, null=True)
    kg_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'

class OrderPaper(models.Model):
    index = models.IntegerField(blank=True, null=True)
    no = models.IntegerField(db_column='No', blank=True, null=True)  # Field name made lowercase.
    item_code = models.BigIntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=500, blank=True, null=True)
    due_date = models.DateTimeField()
    con = models.CharField(max_length=10, blank=True, null=True)
    item_kind = models.CharField(max_length=5, blank=True, null=True)
    soter = models.CharField(max_length=5, blank=True, null=True)
    input = models.IntegerField(blank=True, null=True)
    zone = models.CharField(max_length=5, blank=True, null=True)
    bus_num = models.CharField(max_length=5, blank=True, null=True)
    order_part = models.CharField(max_length=5, blank=True, null=True)
    cmpy_code = models.CharField(max_length=20, blank=True, null=True)
    cmpy_name = models.CharField(max_length=300, blank=True, null=True)
    order_value = models.IntegerField(blank=True, null=True)
    ordered_value = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=5, blank=True, null=True)
    unit_price = models.IntegerField(blank=True, null=True)
    order_price = models.IntegerField(blank=True, null=True)
    delivery_part = models.CharField(max_length=5, blank=True, null=True)
    ett = models.CharField(max_length=300, blank=True, null=True)
    ordered_num = models.BigIntegerField(blank=True, null=True)
    ordered_item_num = models.IntegerField(db_column='ordered_ITEM_num', blank=True, null=True)  # Field name made lowercase.
    order_num = models.BigIntegerField(blank=True, null=True)
    order_item_num = models.IntegerField(db_column='order_ITEM_num', blank=True, null=True)  # Field name made lowercase.
    delivery_cmpy = models.CharField(max_length=5, blank=True, null=True)
    delivery_num = models.CharField(max_length=5, blank=True, null=True)
    factory_num = models.CharField(max_length=5, blank=True, null=True)
    subdivision = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_paper'

