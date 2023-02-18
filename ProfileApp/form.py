from django import forms
from .models import *

class ProductForm(forms.Form):
    BRAND_LIST = [("Sanrio", "Sanrio"), ("Midori", "Midori"), ("M&G", "M&G"), ("Mizuchol", "Mizuchol"),
                  ("Ownory", "Ownory"), ]
    TYPE_LIST = [('เครื่องเขียน', 'เครื่องเขียน'), ('เครื่องประดับ', 'เครื่องประดับ')]
    pdNumber = forms.CharField(max_length = 13, label="รหัสสินค้า",required = True,
                                widget=forms.TextInput(attrs={'size':'15','class' : 'form form-control'}))

    pdName = forms.CharField(max_length=255, label="ชื่อสินค้า", required=True,
                                widget=forms.TextInput(attrs={'size': '55','class' : 'form form-control'}))
    pdBrand = forms.CharField(max_length=100,label="ยี่ห้อสินค้า",required=True,
                              widget=forms.Select(choices=BRAND_LIST,attrs={'class':'form form-select'}))

    pdType = forms.CharField(max_length=100,label="ประเภทสินค้า",required=True,
                             widget=forms.RadioSelect(choices=TYPE_LIST,attrs={'class':'form  '}))

    pdPrice = forms.FloatField(max_value = 100000.00, label="ราคาต่อหน่วย", required=True,
                                widget=forms.NumberInput(attrs={'size': '10','class' : 'form form-control'}))

    pdPriceSale = forms.FloatField(max_value=100000.00, label="ราคาขาย", required=True,
                               widget=forms.NumberInput(attrs={'size': '10', 'class': 'form form-control'}))


    pdAmount = forms.IntegerField( max_value = 1000,label="จำนวนที่มีในคลัง",required=True,
                                widget=forms.NumberInput(attrs={'size': '10','class' : 'form form-control'}))

    pdSaleAmount = forms.IntegerField(max_value=1000, label="จำนวนที่ขายไป",required=True,
                                widget=forms.NumberInput(attrs={'size': '10','class' : 'form form-control'}))

class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('goodscategory', 'gid', 'name', 'brand', 'model', 'price', 'net', 'property')
        widgets = {
            'goodscategory': forms.Select(attrs={'class': 'form-control'}),
            'gid': forms.TextInput(attrs={'class': 'form-control','maxlength' : '13'}),
            'name': forms.TextInput(attrs={'class': 'form-control','maxlength' : '100'}),
            'brand': forms.TextInput(attrs={'class': 'form-control','maxlength' : '100'}),
            'model': forms.TextInput(attrs={'class': 'form-control','maxlength' : '100'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'net': forms.NumberInput(attrs={'class': 'form-control'}),
            'property': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),

        }
        labels = {
            'goodscategory': 'ประเภทสินค้า',
            'gid': 'รหัสสินค้า',
            'name': 'ชื่อสินค้า',
            'brand': 'ยี่ห้อ',
            'model': 'รุ่น',
            'price': 'ราคา',
            'net': 'จำนวนคงเหลือ',
            'property': 'ข้อมูลเพิ่มเติม',
        }

    def updateForm(self):
        self.fields['gid'].widget.attrs['readonly'] = True


class CustomerForm(forms.ModelForm):
    class Meta:
        gender_choices = [('ชาย','เพศชาย'), ('หญิง','เพศหญิง')]
        model = Customer
        fields = ('cid', 'name', 'surname', 'address', 'telephone', 'gender', 'career', 'password')
        widgets = {'cid': forms.TextInput(attrs={'class': 'form-control','maxlength' : '13'}),
                   'name': forms.TextInput(attrs={'class': 'form-control','maxlength' : '100'}),
                   'surname': forms.TextInput(attrs={'class': 'form-control','maxlength' : '100'}),
                   'address': forms.Textarea(attrs={'class': 'form-control'}),
                   'telephone': forms.TextInput(attrs={'class': 'form-control','maxlength' : '10'}),
                   'gender': forms.RadioSelect(choices=gender_choices),
                   'career': forms.TextInput(attrs={'class': 'form-control','maxlength' : '100'}),
                   'password': forms.PasswordInput(attrs={'class': 'form-control','maxlength' : '32'})
                   }
        labels = {
            'cid' : 'รหัสลูกค้า',
            'name' : 'ชื่อ',
            'surname' : 'นามสกุล',
            'address' : 'ที่อยู่',
            'telephone' : 'เบอร์โทร',
            'gender' : 'เพศ',
            'career' : 'อาชีพ',
            'password' : 'รหัสผ่าน',
        }
    def updateForm(self):
        self.fields['password'].widget= forms.HiddenInput()
        self.fields['cid'].widget.attrs['readonly'] = True