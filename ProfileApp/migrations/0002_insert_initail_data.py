from __future__ import unicode_literals
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('ProfileApp', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("INSERT INTO ProfileApp_goodscategory VALUES "\
                          "('GC001', 'เครื่องประดับ', 'สินค้าสำหรับใส่ตกแต่งร่างกาย'),"\
                          "('GC002', 'เครื่องเขียน', 'สินค้าที่ใช้สำหรับเอาไว้เรียนหรือใช้ในการทำงานต่างๆ'), "\
                          "('GC003', 'เครื่องนุ่งห่ม','สินค้าสำหรับสวมใส่ นุ่งห่มร่างกาย ทั้งหญิงและชาย'),"\
                          "('GC004', 'อาหารสำเร็จรูป', 'อาหารที่ผลิตเรียบร้อยพร้อมบริโภคที่บรรจุในภาชนะพร้อมจำหน่ายได้ทันที'), "\
                          "('GC005', 'อุปกรณ์ตกแต่งห้อง', 'สินค้าที่ใช้สำหรับไว้ตกแต่งห้องให้สวยงาม');"
                          ),
        migrations.RunSQL("INSERT INTO ProfileApp_goods VALUES "\
                          "('G001', 'ถุงเท้า', 'Fashion sock', 'เดซี่',29,1000, 'ถุงเท้าแฟชั่น ผ้านิ่ม หยืดหยุ่น ใส่สบาย ขนาดสินค้า : freesize สี : คละสี', 'GC003')," \
                          "('G002', 'กำไล', 'Bearry', 'Tangan',29,200, 'สร้อยข้อมือคริสตัล สีชมพู น่ารัก วัสดุ: โลหะผสม สไตล์หวาน / น่ารัก', 'GC001')," \
                          "('G003', 'ปากกา', 'Sweet time', 'dino',12,2000, 'ปากกาหมึกเจล สีดํา ลายการ์ตูน ขนาด 0.5มม.', 'GC002')," \
                          "('G004', 'ยางลบ', 'Sweet time', 'sakura',6,2000, 'ยางลบ PVC ลายการ์ตูนซากุระ 4B แบบสร้างสรรค์ กันฝุ่น', 'GC002')," \
                          "('G005', 'โคมไฟ', 'Starlight', 'Galaxy',800,500, 'โคมไฟดาว บลูทูธ ตกแต่งห้อง เรืองแสงได้ ชาร์จ USB', 'GC005');" \
                          ),


    ]
