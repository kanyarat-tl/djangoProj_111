from django.shortcuts import render

# Create your views here.
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
