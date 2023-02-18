from django.shortcuts import render,HttpResponse,redirect,get_object_or_404

# Create your views here.
from .form import *
from .models import *


def home(request):
    return render(request,'home.html')
def MyHistory(request):
    return render(request,'myHistory.html')
def MyEducation(request):
    return render(request,'education.html')
def MyInterests(request):
    return render(request,'interests.html')
def MyProducts(request):
    return render(request,'product.html')
def MyRoleModel(request):
    return render(request,'roleModel.html')
def showMyData(request):
    IdNumber = "65342310111-0"
    fullName = "กัลยรัตน์ ไตรลิน"
    nickname = "เอ็มมี่"
    age = '21 ปี'
    birthday = "10 กันยายน 2544"
    sex = 'หญิง'
    bloodType = "B"
    animalLike = "แกะ ,แมว ,แรคคูน"
    occupation = "นักศึกษา"
    tel = "096-8491387"

    Product1 = ["ปากกาเจลหมึกดำ",10.00,'images/Products/Product1.jpg']
    Product2 = ["กระเป๋าเครื่องเขียนอนิเมะ", 49.00,'images/Products/Product2.jpg']
    Product3 = ["ยางลบผลไม้", 5.00,'images/Products/Product3.jpg']
    Product4 = ["กำไลโลมา", 39.00,'images/Products/Product4.jpg']
    Product5 = ["ยางลบแบบยาว", 7.00,'images/Products/Product5.jpg']
    Product6 = ["ถุงเท้าข้อสั้น", 19.00,'images/Products/Product6.jpg']
    Product7 = ["กิ๊บติดผม", 5.00,'images/Products/Product7.jpg']
    Product8 = ["ยางมัดผม", 2.00,'images/Products/Product8.jpg']
    Product9 = ["ไม้บรรทัดเหล็ก", 10.00,'images/Products/Product9.jpg']
    Product10 = ["เครื่องเหลาดินสอ", 79.00,'images/Products/Product10.jpg']
    myproduct = [Product1,Product2,Product3,Product4,Product5,Product6,Product7,Product8,Product9,Product10,]
    mydata = {'IdNumber': IdNumber, 'fullName': fullName,'nickname': nickname, 'age': age, 'birthday': birthday, 'sex': sex,
              'bloodType': bloodType, 'animalLike': animalLike,'occupation':occupation, 'tel': tel,
              'myproduct':myproduct}
    return  render(request,'showMyData.html',mydata)
lstOurProduct = []
def listProduct(requset):
    context = {'products':lstOurProduct}
    return render(requset,"listProduct.html",context)
def inputProduct(requset) :
    if requset.method == "POST":
        form = ProductForm(requset.POST)
        if form.is_valid() :
            form = form.cleaned_data
            pdNumber = form.get('pdNumber')
            pdName = form.get('pdName')
            pdBrand = form.get('pdBrand')
            pdType = form.get('pdType')
            pdPrice = float(form.get('pdPrice'))
            pdAmount = form.get('pdAmount')
            pdSaleAmount = form.get('pdSaleAmount')
            pdPriceSale = form.get('pdPriceSale')
            product= Product(pdNumber,pdName,pdBrand,pdType,pdPrice,pdPriceSale,pdAmount,pdSaleAmount)
            lstOurProduct.append(product)
            return redirect('listProduct')

        else:
            form =ProductForm(form)
    else:
        form =ProductForm()
    context = {'form':form,"CHECK":requset.method}
    return render(requset,'inputProduct.html',context)

def showGoodsList(request):
    goods = Goods.objects.all().order_by("gid")
    context = {'goods':goods}
    return render(request, 'GoodsAndCus/showGoodsList.html', context)
def showGoodsOne(request,gid):
    goods = Goods.objects.get(gid=gid)
    context = {'goods':goods}
    return render(request, 'GoodsAndCus/showGoodOne.html', context)
def showCustomerList(request):
    customer = Customer.objects.all().order_by('cid')
    context = {'Customers':customer}
    return render(request, 'GoodsAndCus/showCustomerList.html', context)
def showCustomerOne(request,cid):
    customer = Customer.objects.get(cid=cid)
    context = {'customer':customer}
    return render(request, 'GoodsAndCus/showCustomerOne.html', context)
def newGoods(request):
    if request.method == "POST":
        form = GoodsForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('showGoodsList')
        else:
            form = GoodsForm(form)
    else:
        form = GoodsForm()
    context = {'form': form}
    return render(request,'GoodsAndCus/newGoods.html',context)
def updateGoods(request,gid):
    goods = get_object_or_404(Goods,gid = gid)
    if request.method == "POST":
        form = GoodsForm(data=request.POST or None, instance=goods)
        if form.is_valid() :
            form.save()
            return redirect('showGoodsList')
    else:
        form = GoodsForm(instance=goods)
        form.updateForm()
        context = {'form': form,'gid':gid}
        return render(request,'GoodsAndCus/updateGoods.html',context)
def deleteGoods(request,gid):
    goods = Goods.objects.get(gid=gid)
    if request.method == "POST":
        goods.delete()
        return redirect('showGoodsList')
    context = {'goods': goods}
    return render(request,'GoodsAndCus/deleteGoods.html',context)
def newCustomer(request):
    if request.method == "POST":
        form = CustomerForm(data = request.POST)
        print(form.is_valid)
        if form.is_valid():
            form.save()
            return redirect('showCustomerList')
        else:
            form = CustomerForm(form)
    else:
        form = CustomerForm()
    context = {'form': form}
    return render(request,'GoodsAndCus/newCustomer.html',context)
def updateCustomer(request,cid):
    customer = get_object_or_404(Customer, cid=cid)
    if request.method == "POST":
        form = CustomerForm(data=request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('showCustomerList')
    else:
        form = CustomerForm(instance=customer)
        form.updateForm()
        context = {'form': form, 'cid': cid}
        return render(request, 'GoodsAndCus/updateCustomer.html',context)
def deleteCustomer(request,cid):
    customer = Customer.objects.get(cid=cid)
    if request.method == "POST":
        customer.delete()
        return redirect('showCustomerList')
    context = {'customer': customer}
    return render(request,'GoodsAndCus/deleteCustomer.html',context)