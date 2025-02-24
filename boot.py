import requests

# ضع التوكن الخاص بالبوت هنا
BOT_TOKEN = "7859907084:AAFAC4jkjJ7GWI-9P4ttVH8C7dyq_bAAozI"


CHANNEL_ID = "-1002348202240"



# message = "مرحبًا، هذه رسالة تجريبية من كود بايثون!"


url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

# البيانات المرسلة
params = {
    "chat_id": CHANNEL_ID,
    # "text": message,
    "photo": "https://i.pinimg.com/736x/68/35/52/6835526bd7cca2d5392b82b621689866.jpg"  , 
    "caption": "سبحان الله وبحمده سبحان الله العظيم"
 

}

# إرسال الطلب
response = requests.post(url, params=params)

# طباعة النتيجة
if response.status_code == 200:
    print("✅ تم إرسال الرسالة بنجاح!")
else:
    print(f"❌ فشل في الإرسال! {response.text}")


https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNfYe4GlFQPecYD3bw0k0E_Sl02Tp941aHNw&s