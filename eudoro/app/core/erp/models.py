from datetime import datetime

from django.db import models
from django.forms import model_to_dict

from config.settings import MEDIA_URL, STATIC_URL
from core.erp.choices import gender_choices
from core.models import BaseModel


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True, db_column='cat_name')
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripcion',
                                   db_column='cat_description')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'categories'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True, db_column='pro_name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría', db_column='cat_id')
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen',
                              db_column='pro_image')
    stock = models.IntegerField(default=0, verbose_name='Stock', db_column='pro_stock')
    pvp = models.DecimalField(default=0.0, max_digits=9, decimal_places=2, verbose_name='Precio de Venta',
                              db_column='pro_pvp')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = '{} / {}'.format(self.name, self.category.name)
        item['category'] = self.category.toJSON()
        item['image'] = self.get_image()
        item['pvp'] = format(self.pvp, '.2f')
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'products'
        ordering = ['id']


class Customer(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres', db_column='cst_names')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos', db_column='cst_surnames')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni', db_column='cst_dni')
    date_birthday = models.DateField(default=datetime.now, verbose_name='Fecha de Nacimiento',
                                     db_column='cst_date_birthday')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Direccion', db_column='cst_address')
    gender = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo',
                              db_column='cst_gender')

    def __str__(self):
        return self.names

    def get_full_name(self):
        return '{} {} / {}'.format(self.names, self.surnames, self.dni)

    def toJSON(self):
        item = model_to_dict(self)
        item['gender'] = {'id': self.gender, 'name': self.get_gender_display()}
        item['date_birthday'] = self.date_birthday.strftime('%Y-%m-%d')
        item['full_name'] = self.get_full_name()
        return item

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        db_table = 'customers'
        ordering = ['id']


class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now, db_column='sal_date_joined')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, db_column='sal_subtotal')
    igv = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, db_column='sal_igv')
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, db_column='sal_total')

    def __str__(self):
        return self.customer.names

    def toJSON(self):
        item = model_to_dict(self)
        item['customer'] = self.customer.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['igv'] = format(self.igv, '.2f')
        item['total'] = format(self.total, '.2f')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['detail'] = [i.toJSON() for i in self.saledetail_set.all()]
        return item

    def delete(self, using=None, keep_parents=False):
        for det in self.saledetail_set.all():
            det.product.stock += det.quantity
            det.product.save()
        super(Sale, self).delete()

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
        db_table = 'sales'
        ordering = ['id']


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, db_column='sal_id')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='pro_id')
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, db_column='sld_price')
    quantity = models.IntegerField(default=0, db_column='sld_quantity')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, db_column='sld_subtotal')

    def __str__(self):
        return self.product.name

    def toJSON(self):
        item = model_to_dict(self, exclude=['sale'])
        item['product'] = self.product.toJSON()
        item['price'] = format(self.price, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item

    class Meta:
        verbose_name = 'Sale Detail'
        verbose_name_plural = 'Sales Details'
        db_table = 'sales_details'
        ordering = ['id']
