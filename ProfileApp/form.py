from django import forms

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