from django.db import models

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