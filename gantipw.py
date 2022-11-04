import re, requests, bs4
from bs4 import BeautifulSoup as parser
ses=requests.Session()

cookie = {"cookie":"cookie kamu"}
pwlama = "pw lama"
pwbaru = "pw baru"

url = ses.get("https://mbasic.facebook.com/settings/security/password/",cookies=cookie)
parsing1 = parser(url.text,"html.parser")
action1 = parsing1.find("form",{"method":"post"})["action"]
data = {
	"fb_dtsg"     : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),
	"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),
	"password_change_session_identifier" : re.search('name="password_change_session_identifier" value="(.*?)"', str(url.text)).group(1),
	"password_old": pwlama, 
	"password_new": pwbaru, 
	"password_confirm": pwbaru, 
	"save": "Simpan perubahan"}
post = ses.post("https://mbasic.facebook.com"+action1,data=data,cookies=cookie)
if "Kata Sandi Telah Diubah" in post.text:
	print(f"kata sandi telah diubah menjadi {pwbaru}")
elif "Masukkan kata sandi yang valid dan coba lagi." in post.text:
	print("kata sandi salah")
else:
	print(f"akun terkena checkpoint atau sandi salah")
