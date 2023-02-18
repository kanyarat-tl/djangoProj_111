from django.db import models
import datetime

# Create your models here.
class Product :
    def __init__(self,pdNumber,pdName,pdBrand,pdType,pdPrice,pdPriceSale,pdAmount,pdSaleAmount):
        self.pdNumber = pdNumber
        self.pdName = pdName
        self.pdBrand = pdBrand
        self.pdType = pdType
        self.pdPrice = pdPrice
        self.pdPriceSale = pdPriceSale
        self.pdAmount = pdAmount
        self.pdSaleAmount = pdSaleAmount
        self.setTotal()
        self.setSaleTotal()
        self.setBalance()
    def setTotal(self):
        self.total = self.pdPrice * self.pdAmount
    def setSaleTotal(self):
        self.saleTotal = self.pdPriceSale * self.pdSaleAmount
    def setBalance(self):
        self.balance = self.pdAmount - self.pdSaleAmount
    def __str__(self):
        return "pdNumber:{},pdName:{},pdPrice:{},pdProfit:{},pdAmount:{},pdVat:{}" \
               "pdSaleProfit:{},saleTotal:{},taxPrice:{},salePrice:{}"\
            .format(self.pdNumber,self.pdName,self.pdBrand,self.pdType,
                    self.pdPrice,self.pdPriceSale,self.pdAmount,self.pdSaleAmount,self.total,self.saleTotal,self.balance)


class GoodsCategory(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    gc_name = models.CharField(max_length=100, null=False)
    desc = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.id + ' : ' + self.gc_name


class Goods(models.Model):
    goodscategory = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, default=None)
    gid = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    brand = models.CharField(max_length=100, )
    model = models.CharField(max_length=100, )
    price = models.FloatField(default=0.00)
    net = models.IntegerField(default=0)
    property = models.TextField()


class Customer(models.Model):
    cid = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False)
    address = models.TextField(default="")
    telephone = models.CharField(max_length=10, default="")
    gender = models.CharField(max_length=10, default="")
    career = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=32, null=False)


class Order(models.Model):
    oid = models.CharField(max_length=13, primary_key=True)
    date = models.DateField(default=datetime.date.today())
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    status = models.CharField(max_length=100, default="Start", null=False)


class OrderDetail(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, default=None)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)