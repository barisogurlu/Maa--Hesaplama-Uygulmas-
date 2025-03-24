import tkinter
from tkinter import *
PhotoImage
root = tkinter.Tk()  # PENCERE  DEĞİŞKEN İSMİ
root.title("MAAŞ HESAPLAMA PROGRAMI")  # PENCERE BAŞLIK
root.configure(bg="brown")  # PENCERE RENGİ
root.geometry("900x560")  # PENCERE BOYUT


# ŞİRKET İÇERİSİNDE 100 ADET ÇALIŞAN BULUNMAKTADIR
# 1  ADET YÖNETİCİ (MANAGER) BULUNMAKTADIR,GÜNLÜK ALACAĞI MAAŞ:3000
# 10 ADET YÖNETİCİ ASİSTANI(ADMİNİSTRATİVE ASSİSTANT) BULUNMAKTADIR,GÜNLÜK ALINACAK MAAŞ:2300
# 40 ADET TEKNİK PERSONEL(TECHNİCAL STAFF) BULUNMAKTADIR,GÜNLÜK ALINACAK MAAŞ:1750
# 15 ADET PROJE YÖNETİCİSİ(PROJECT MANAGER) BULUNMAKTADIR,GÜNLÜK ALICAĞI MAAŞ:1400
# 24 ADET PROJE YÜRÜTÜCÜSÜ(PROJECT COORDİNATOR) BULUNMKATADIR,GÜNLÜK ALACAĞI MAAŞ:1000
# 10 ADET TEMİZLİK GÖREVLİSİ(CLEANİNG STAFF) BULUNMKATADIR:800

# NOT:MAAŞLAR GÜN HESABI VERİLMEKTEDİR
# MAAŞ HESAPLARI:SİGORTA HESAPLAMA,EK MESAİ HESAPLAMA
def salary_calculation():
    username = str(username_entery.get())
    passaword = str(password_entery.get())
    if username == "admin":
        if passaword == "123":
            print("GİRİŞ BAŞARILI ")
            group = int(departmen_entry.get())
            name_surname = str(personel_name_entry.get())
            print("-------------------------------------------")

            def manger_wage(numberofdaysworked, dailynetsalary, overtime, insurance):
                print(((numberofdaysworked + overtime) * dailynetsalary) - insurance)

            def administrative_assistant(numberofdaysworked2, dailynetsalary2, overtime2, insurance2):
                print(((numberofdaysworked2 + overtime2) * dailynetsalary2) - insurance2)

            def technical_staff(numberofdaysworked3, dailynetsalary3, overtime3, insurance3):
                print(((numberofdaysworked3 + overtime3) * dailynetsalary3) - insurance3)

            def project_manager(numberofdaysworked4, dailynetsalary4, overtime4, insurance4):
                print(((numberofdaysworked4 + overtime4) * dailynetsalary4) - insurance4)

            def project_coordinator(numberofdaysworked5, dailynetsalary5, overtime5, insurance5):
                print(((numberofdaysworked5 + overtime5) * dailynetsalary5) - insurance5)

            def cleaning_staff(numberofdaysworked6, dailynetsalary6, overtime6, insurance6):
                print(((numberofdaysworked6 + overtime6) * dailynetsalary6) - insurance6)

            if group == 1:
                print("YÖNETİCİ BİRİMİNİ SEÇTİNİZ")
                print("--------------------------------------------")
                print(name_surname, ",BİRİMİ:YÖNETİCİ")
                print("--------------------------------------------")
                numberofdaysworked = float(daily_net_salary_entry.get())
                print(name_surname, ",ÇALIŞTIĞI TOPLAM GÜN SAYISI=", numberofdaysworked)
                print("--------------------------------------------")
                dailynetsalary = 3000
                print(name_surname, ",GÜNLÜK MAAŞI=", dailynetsalary, "TL")
                print("--------------------------------------------")
                overtime = float(overtimepersonel_entry.get())
                print(name_surname, ",YAPTIĞI EK MESAİ=", overtime, "GÜN")
                print("--------------------------------------------")
                insurance = ((numberofdaysworked + overtime) * dailynetsalary) * 0.32
                print(name_surname, ",ÖDENECEK TOPLAM SİGORTA=", insurance, "TL")
                print("--------------------------------------------")
                print(name_surname, ",ADLI ŞİRKET PERSONELİNE ÖDENECEK TUTAR:")
                manger_wage(numberofdaysworked, dailynetsalary, overtime, insurance)

            elif group == 2:
                print("YÖNETİCİ ASİSTANI BİRİMİNİ SEÇTİNİZ")
                print("--------------------------------------------")
                print(name_surname, ",BİRİMİ:YÖNETİCİ ASİSTANI")
                print("--------------------------------------------")
                numberofdaysworked2 = float(daily_net_salary_entry.get())
                print(name_surname, ",ÇALIŞTIĞI TOPLAM GÜN SAYISI=", numberofdaysworked2)
                print("--------------------------------------------")
                dailynetsalary2 = 2300
                print(name_surname, ",GÜNLÜK MAAŞI=", dailynetsalary2, "TL")
                print("--------------------------------------------")
                overtime2 = float(overtimepersonel_entry.get())
                print(name_surname, ",YAPTIĞI EK MESAİ=", overtime2, "GÜN")
                insurance2 = ((numberofdaysworked2 + overtime2) * dailynetsalary2) * 0.32
                print(name_surname, ",ÖDENECEK TOPLAM SİGORTA=", insurance2, "TL")
                print("--------------------------------------------")
                print(name_surname, ",ADLI ŞİRKET PERSONELİNE ÖDENECEK TUTAR:")
                administrative_assistant(numberofdaysworked2, dailynetsalary2, overtime2, insurance2)

            elif group == 3:
                print("TEKNİK PERSONEL BİRİMİNİ SEÇTİNİZ")
                print("--------------------------------------------")
                print(name_surname, ",BİRİMİ:TEKNİK PERSONEL")
                print("--------------------------------------------")
                numberofdaysworked3 = float(daily_net_salary_entry.get())
                print(name_surname, ",ÇALIŞTIĞI TOPLAM GÜN SAYISI=", numberofdaysworked3)
                print("--------------------------------------------")
                dailynetsalary3 = 1750
                print(name_surname, ",GÜNLÜK MAAŞI=", dailynetsalary3, "TL")
                print("--------------------------------------------")
                overtime3 = float(overtimepersonel_entry.get())
                print(name_surname, ",YAPTIĞI EK MESAİ=", overtime3, "GÜN")
                print("--------------------------------------------")
                insurance3 = ((numberofdaysworked3 + overtime3) * dailynetsalary3) * 0.32
                print(name_surname, ",ÖDENECEK TOPLAM SİGORTA=", insurance3, "TL")
                print("--------------------------------------------")
                print(name_surname, ",ADLI ŞİRKET  PERSONELİNE ÖDENECEK TUTAR:")
                technical_staff(numberofdaysworked3, dailynetsalary3, overtime3, insurance3)

            elif group == 4:
                print("PROJE YÖNETİCİSİ BİRİMİNİ SEÇTİNİZ ")
                print("--------------------------------------------")
                print(name_surname, ",BİRİMİ:PROJE YÖNETİCİSİ")
                print("--------------------------------------------")
                numberofdaysworked4 = float(daily_net_salary_entry.get())
                print(name_surname, ",ÇALIŞTIĞI TOPLAM GÜN SAYISI=", numberofdaysworked4)
                print("--------------------------------------------")
                dailynetsalary4 = 1400
                print(name_surname, ",GÜNLÜK MAAŞI=", dailynetsalary4, "TL")
                print("--------------------------------------------")
                overtime4 = float(overtimepersonel_entry.get())
                print(name_surname, ",YAPTIĞI EK MESAİ=", overtime4, "GÜN")
                print("--------------------------------------------")
                insurance4 = ((numberofdaysworked4 + overtime4) * dailynetsalary4) * 0.32
                print(name_surname, ",ÖDENECEK TOPLAM SİGORTA=", insurance4, "TL")
                print("--------------------------------------------")
                print(name_surname, ",ADLI ŞİRKET PERSONELİNE ÖDENECEK TUTAR:")
                project_manager(numberofdaysworked4, dailynetsalary4, overtime4, insurance4)

            elif group == 5:
                print("PROJE YÜRÜTÜCÜSÜ BİRİMİNİ SEÇTİNİZ")
                print("--------------------------------------------")
                print(name_surname, ",BİRİMİ:PROJE YÜRÜTÜCÜSÜ")
                print("--------------------------------------------")
                numberofdaysworked5 = float(daily_net_salary_entry.get())
                print(name_surname, ",ÇALIŞTIĞI TOPLAM GÜN SAYISI=", numberofdaysworked5)
                print("--------------------------------------------")
                dailynetsalary5 = 1000
                print(name_surname, ",GÜNLÜK MAAŞI=", dailynetsalary5, "TL")
                print("--------------------------------------------")
                overtime5 = float(overtimepersonel_entry.get())
                print(name_surname, ",YAPTIĞI EK MESAİ=", overtime5, "GÜN")
                print("--------------------------------------------")
                insurance5 = ((numberofdaysworked5 + overtime5) * dailynetsalary5) * 0.32
                print(name_surname, ",ÖDENECEK TOPLAM SİGORTA=", insurance5, "TL")
                print("--------------------------------------------")
                print(name_surname, ",ADLI ŞİRKET PERSONELİNE ÖDENECEK TUTAR:")
                project_coordinator(numberofdaysworked5, dailynetsalary5, overtime5, insurance5)

            elif group == 6:
                print("TEMİZLİK GÖREVLİSİ BİRİMİNİ SEÇTİNİZ")
                print("-------------------------------------------")
                print(name_surname, ",BİRİMİ:TEMİZLİK GÖREVLİSİ")
                print("--------------------------------------------")
                numberofdaysworked6 = float(daily_net_salary_entry.get())
                print(name_surname, ",ÇALIŞTIĞI TOPLAM GÜN SAYISI=", numberofdaysworked6)
                print("--------------------------------------------")
                dailynetsalary6 = 800
                print(name_surname, ",GÜNLÜK MAAŞI=", dailynetsalary6, "TL")
                print("--------------------------------------------")
                overtime6 = float(overtimepersonel_entry.get())
                print(name_surname, ",YAPTIĞI EK MESAİ=", overtime6, "GÜN")
                print("--------------------------------------------")
                insurance6 = ((numberofdaysworked6 + overtime6) * dailynetsalary6) * 0.32
                print(name_surname, ",ÖDENECEK TOPLAM SİGORTA=", insurance6, "TL")
                print("--------------------------------------------")
                print(name_surname, ",ADLI ŞİRKET PERSONELİNE ÖDENECEK TUTAR:")
                cleaning_staff(numberofdaysworked6, dailynetsalary6, overtime6, insurance6)

            else:
                print("YANLIŞ VEYA HATALI TUŞLAMA YAPTINIZ ")
        else:
            print("GİRİŞ BAŞARISIZ")
    else:
        print("HATALI GİRİŞ")


Label(root, text="", bg="brown", height="1").pack()
Label(root, text="PERSONEL MAAŞ HESAPLAMA SİSTEMİ", background="white", font="verdana 30 ").pack()  # PENCERE ANA BAŞLIK
# KULLANICIYI  YÖNLENDİREN  GÖREVİ OLMAYAN TERİMLER
Label(root, text="---------------------------DEPARTMANLAR---------------------------").place(x=200, y=100)
Label(root, text="1)YÖNETİCİ").place(x=290, y=130)
Label(root, text="2)YÖNETİCİ ASİSTANI").place(x=290, y=160)
Label(root, text="3)TEKNİK PERSONEL").place(x=290, y=190)
Label(root, text="4)PROJE YÖNETİCİSİ").place(x=290, y=220)
Label(root, text="5)PROJE YÜRÜTÜCÜSÜ").place(x=290, y=250)
Label(root, text="6)TEMİZLİK GÖREVLİSİ").place(x=290, y=280)
Label(root, text="KULLANICI ADINIZI GİRİNİZ :").place(x=80, y=320)
Label(root, text="KULLANICI ŞİFRENİZİ GİRİNİZ :").place(x=80, y=350)
Label(root, text=" DEPARTMAN SEÇİNİZ :").place(x=80, y=380)
Label(root, text="PERSONEL İSMİ GİRİNİZ :").place(x=80, y=410)
Label(text="ÇALIŞILAN TOPLAM GÜN SAYISI :").place(x=80, y=440)
Label(root, text="YAPTIĞI EK MESAİ VARSA GİRİNİZ").place(x=80, y=470)
Label(root, text="PERSONEL RESİM").place(x=680, y=295)
##image = PhotoImage(file="C:\\Users\\EXCALIBUR\\Desktop\\Ekran görüntüsü 2024-01-01 191144.png")  # FOTOĞRAF
##Label = tkinter.Label(root, image=image)      ##kodun çalışması için dosya yolu yorumlandı
##Label.place(x=650, y=120)
# KULLANICIDAN VERİ ALMAK İÇİN KULLANILAN ALAN
username_entery = tkinter.Entry(root, width="50")  # KULLANICI ADI GİRİŞ
username_entery.place(x=275, y=320)
# -------------------------------------------------------------------------------------------------
password_entery = tkinter.Entry(root, show="*", width="50")  # KULLANICI ŞİFRE
password_entery.place(x=275, y=350)
# ------------------------------------------------------------------------------------------------
departmen_entry = tkinter.Entry(root, width="50")  # DEPARTMAN SEÇME
departmen_entry.place(x=275, y=380)
# ---------------------------------------------------------------------------------------------------------
personel_name_entry = tkinter.Entry(root, width="50")  # PERSONEL İSMİ
personel_name_entry.place(x=275, y=410)
# ---------------------------------------------------------------------------------------------------------
daily_net_salary_entry = tkinter.Entry(root, width="50")  # PERSONELİN TOPLAM ÇALIŞTIĞI GÜN SAYISI
daily_net_salary_entry.place(x=275, y=440)
# ----------------------------------------------------------------------------------------------------------
overtimepersonel_entry = tkinter.Entry(root, width="50")  # YAPTIĞI EK MESAİ
overtimepersonel_entry.place(x=275, y=470)
# --------------------------------------------------------------------------------------------------------------
loginButton = tkinter.Button(root, text="HESAPLA", bg="green", fg="white", height="2", width="10",
                             command=salary_calculation)  # HESAPLAMA FONKSİYONU
loginButton.place(x=380, y=500)

root.mainloop()  # PENCERE SON
