import requests
import csv
import time

# 🔹 ضع التوكن الخاص بالبوت هنا
BOT_TOKEN = "7859907084:AAFAC4jkjJ7GWI-9P4ttVH8C7dyq_bAAozI"

# 🔹 ضع chat_id الخاص بالقناة
CHANNEL_ID = "-1002348202240"

# 🔹 تحميل الأذكار من ملف CSV
file_path = "Azkar_List.csv"  # تأكد من أن الملف موجود في نفس مسار الكود

with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # تخطي العنوان
    azkar_list = [row[0] for row in reader]

# 🔹 إرسال ذكر واحد كل دقيقة 

while True :
    
    for zikr in azkar_list:
        message = f"📿 {zikr}"

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        params = {
            "chat_id": CHANNEL_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        
        try :
            response = requests.post(url, params=params)

            if response.status_code == 200:
                print(f"✅ تم إرسال الذكر: {zikr}")
            else:
                print(f"❌ فشل في إرسال الذكر: {response.text}")

            # 🔹 الانتظار دقيقة واحدة قبل إرسال الذكر التالي
            time.sleep(3)
        
        
        except :
            pass
