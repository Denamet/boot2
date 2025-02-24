import requests
import time
import schedule
import os
import csv


# 🔹 بيانات تيليجرام
BOT_TOKEN = "7859907084:AAFAC4jkjJ7GWI-9P4ttVH8C7dyq_bAAozI"
CHANNEL_ID = "-1002348202240"

# 🔹 مجلد تخزين ملفات الأذكار



def load_zeker(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = file.read()

        return reader.split("#######")
    



# 🔹 دالة لإرسال ذكر معين إلى القناة
def send_zekr(zekr):
    message = f"📿 {zekr}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    
    try :
        response = requests.post(url, params=params)
        
        if response.status_code == 200:
            print(f"✅ تم إرسال الذكر: {zekr}")
        else:
            print(f"❌ فشل في إرسال الذكر: {response.text}")
    except :
        pass



def send_morning_azkar():
    for zekr in load_zeker("file_one.txt") :
        send_zekr(zekr.strip())
        time.sleep(10)

def send_evening_azkar():
   for zekr in load_zeker("file_two.txt") :
        send_zekr(zekr.strip())
        time.sleep(10)

def send_sleep_azkar():
   for zekr in load_zeker("file_three.txt") :
        send_zekr(zekr.strip())
        time.sleep(10)



def send_fajr_azkar():
     for zekr in load_zeker("file_5.txt") :
        send_zekr(zekr.strip())
        time.sleep(10)

def send_duhr_azkar():
   for zekr in load_zeker("file_four.txt") :
        send_zekr(zekr.strip())
        time.sleep(10)


def send_asr_azkar():
    for zekr in load_zeker("file_four.txt") :
        send_zekr(zekr.strip())
        time.sleep(10)


def send_maghrib_azkar():
     for zekr in load_zeker("file_5.txt") :
        send_zekr(zekr.strip())
        time.sleep(10)

def send_isha_azkar():
      for zekr in load_zeker("file_four.txt") :
        send_zekr(zekr.strip())
        time.sleep(10)



time1 = "07:33"

# # 🔹 جدولة الأوقات لتشغيلها تلقائيًا
schedule.every().day.at("06:00").do(send_morning_azkar)   # أذكار الصباح
schedule.every().day.at("05:30").do(send_fajr_azkar)      # بعد الفجر
schedule.every().day.at("12:30").do(send_duhr_azkar)      # بعد الظهر
schedule.every().day.at("15:35").do(send_asr_azkar)       # بعد العصر
schedule.every().day.at("18:30").do(send_maghrib_azkar)   # بعد المغرب
schedule.every().day.at("20:00").do(send_isha_azkar)      # بعد العشاء
schedule.every().day.at("16:30").do(send_evening_azkar)   # أذكار المساء
schedule.every().day.at("21:00").do(send_sleep_azkar)   # اذكار النوم


# schedule.every().day.at(time1).do(send_morning_azkar)   # أذكار الصباح
# schedule.every().day.at(time1).do(send_fajr_azkar)      # بعد الفجر
# schedule.every().day.at(time1).do(send_duhr_azkar)      # بعد الظهر
# schedule.every().day.at(time1).do(send_asr_azkar)       # بعد العصر
# schedule.every().day.at(time1).do(send_maghrib_azkar)   # بعد المغرب
# schedule.every().day.at(time1).do(send_isha_azkar)      # بعد العشاء
# schedule.every().day.at(time1).do(send_evening_azkar)   # أذكار المساء
# schedule.every().day.at(time1).do(send_sleep_azkar)   # اذكار النوم



while True:
    schedule.run_pending()
    time.sleep(30)  # الانتظار نصف دقيقة قبل فحص الجدولة مرة أخرى
