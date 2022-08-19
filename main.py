
#kütüphane ekleme!

from tkinter import *
from tkinter import messagebox
import tkinter as tk
import webbrowser


# Pencere oluşturma!

pencerebir = Tk()
pencerebir.title("Limeliz")
pencerebir.config(bg="black")
pencerebir.state("zoomed")
pencerebir.resizable(False,False)
bg = PhotoImage(file ="wallpaperbetter (1366x768) k.png")
label = tk.Label(pencerebir,image=bg)
label.place(x=0,y=0)



#Giriş Yapma Fonksiyonları
def girişyapmak():
    controlbir = cb1.get()
    controliki = cb2.get()
    controlkullanıcı = kullanıcıgirdi.get()
    controlşifre = şifregirdi.get()

    with open("kullanıcı.py", "r") as r:
        r.seek(0)
        kulcontrol = (r.read())

    with open("şifre.py", "r") as o:
        o.seek(0)
        şifcontrol = (o.read())

    if (controlbir == 1) and (controliki == 1):

        if (controlkullanıcı == kulcontrol) and (controlşifre == şifcontrol):
            webyazı =tk.Label(pencerebir,text="Web Siteleri :",fg="black",bg="white",font="Times 15")
            webyazı.place(x=350,y=0)
            twityazı =tk.Label(pencerebir,text="Twitter Siteleri:",fg="black",bg="white",font="Times 15")
            twityazı.place(x=1008,y=0)
            canlıyazı =tk.Label(pencerebir,text="Canlı Yayın Siteleri:",fg="black",bg="white",font="Times 15")
            canlıyazı.place(x=1000,y=450)


            def but1k ():
                webbrowser.open("https://rt.pornhub.com")
            but1=tk.Button(pencerebir,text="1)PornHub           ",fg="black",bg="white",font="Times 11",command=but1k)
            but1.place(x=500,y=0)


            def but2k ():
                webbrowser.open("https://www.redtube.com")
            but2=tk.Button(pencerebir,text="2)RedTube           ",fg="black",bg="white",font="Times 11",command=but2k)
            but2.place(x=500,y=36)


            def but3k ():
                webbrowser.open("https://www.xnxx.com")
            but3=tk.Button(pencerebir,text="3)XnXX               ",fg="black",bg="white",font="Times 11",command=but3k)
            but3.place(x=500,y=72)


            def but4k ():
                webbrowser.open("https://www.forhertube.com")
            but4=tk.Button(pencerebir,text="4)ForherTube       ",fg="black",bg="white",font="Times 11",command=but4k)
            but4.place(x=500,y=108)


            def but5k ():
                webbrowser.open("https://www.xvideos.com")
            but5=tk.Button(pencerebir,text="5)Xvideos            ",fg="black",bg="white",font="Times 11",command=but5k)
            but5.place(x=500,y=144)


            def but6k ():
                webbrowser.open("https://vagina.nl")
            but6=tk.Button(pencerebir,text="6)Vagina.Nl         ",fg="black",bg="white",font="Times 11",command=but6k)
            but6.place(x=500,y=180)


            def but7k ():
                webbrowser.open("http://www.doeda.com/one/")
            but7=tk.Button(pencerebir,text="7)Doeda              ",fg="black",bg="white",font="Times 11",command=but7k)
            but7.place(x=500,y=216)


            def but8k ():
                webbrowser.open("http://maheir.com")
            but8=tk.Button(pencerebir,text="8)Maheir             ",fg="black",bg="white",font="Times 11",command=but8k)
            but8.place(x=500,y=252)


            def but9k ():
                webbrowser.open("http://www.badtv.net/seks/")
            but9=tk.Button(pencerebir,text="9)BadTv              ",fg="black",bg="white",font="Times 11",command=but9k)
            but9.place(x=500,y=288)


            def but10k ():
                webbrowser.open("https://7dak.com")
            but10=tk.Button(pencerebir,text="10)7DaK             ",fg="black",bg="white",font="Times 11",command=but10k)
            but10.place(x=500,y=326)


            def but11k ():
                webbrowser.open("https://hdabla.net")
            but11=tk.Button(pencerebir,text="11)HdAbla           ",fg="black",bg="white",font="Times 11",command=but11k)
            but11.place(x=500,y=362)


            def but12k ():
                webbrowser.open("https://ru.xhamster.com")
            but12=tk.Button(pencerebir,text="12)XhamsTer       ",fg="black",bg="white",font="Times 11",command=but12k)
            but12.place(x=500,y=398)


            def but13k ():
                webbrowser.open("https://www.youporn.com")
            but13=tk.Button(pencerebir,text="13)YouPorn         ",fg="black",bg="white",font="Times 11",command=but13k)
            but13.place(x=500,y=434)


            def but14k ():
                webbrowser.open("http://www.kasut.org/opentr/")
            but14=tk.Button(pencerebir,text="14)Kasut.Org       ",fg="black",bg="white",font="Times 11",command=but14k)
            but14.place(x=500,y=470)


            def but15k ():
                webbrowser.open("http://www.sex4.tv")
            but15=tk.Button(pencerebir,text="15)Sex4Tv           ",fg="black",bg="white",font="Times 11",command=but15k)
            but15.place(x=500,y=506)


            def but16k ():
                webbrowser.open("https://www.evooli.com")
            but16=tk.Button(pencerebir,text="16)Evooli             ",fg="black",bg="white",font="Times 11",command=but16k)
            but16.place(x=500,y=542)


            def but17k ():
                webbrowser.open("https://liebelib.net")
            but17=tk.Button(pencerebir,text="17)Liebelib           ",fg="black",bg="white",font="Times 11",command=but17k)
            but17.place(x=500,y=578)


            def but18k ():
                webbrowser.open("http://www.upslut.com")
            but18=tk.Button(pencerebir,text="18)Upslot             ",fg="black",bg="white",font="Times 11",command=but18k)
            but18.place(x=500,y=614)


            def but19k ():
                webbrowser.open("https://www.xxxps.net")
            but19=tk.Button(pencerebir,text="19)xxxPs              ",fg="black",bg="white",font="Times 11",command=but19k)
            but19.place(x=500,y=650)


            def but20k ():
                webbrowser.open("https://pornotub.mobi")
            but20=tk.Button(pencerebir,text="20)Pornotub          ",fg="black",bg="white",font="Times 11",command=but20k)
            but20.place(x=500,y=686)


            def bu1k ():
                webbrowser.open("https://kompoz2.com")
            bu1=tk.Button(pencerebir,text="21)Kompoz2            ",fg="black",bg="white",font="Times 11",command=bu1k)
            bu1.place(x=700,y=0)


            def bu2k ():
                webbrowser.open("https://www.porn.com")
            bu2=tk.Button(pencerebir,text="22)Porn                   ",fg="black",bg="white",font="Times 11",command=bu2k)
            bu2.place(x=700,y=36)


            def bu3k ():
                webbrowser.open("https://xxxhd93.com")
            bu3=tk.Button(pencerebir,text="23)xxxHD93            ",fg="black",bg="white",font="Times 11",command=bu3k)
            bu3.place(x=700,y=72)


            def bu4k ():
                webbrowser.open("https://www.pornsos.com")
            bu4=tk.Button(pencerebir,text="24)Pornsos               ",fg="black",bg="white",font="Times 11",command=bu4k)
            bu4.place(x=700,y=108)


            def bu5k ():
                webbrowser.open("https://hqtube.xxx")
            bu5=tk.Button(pencerebir,text="25)HqTube.xxx        ",fg="black",bg="white",font="Times 11",command=bu5k)
            bu5.place(x=700,y=144)


            def bu6k ():
                webbrowser.open("https://see.xxx")
            bu6=tk.Button(pencerebir,text="26)See.xxx               ",fg="black",bg="white",font="Times 11",command=bu6k)
            bu6.place(x=700,y=180)


            def bu7k ():
                webbrowser.open("https://thematureporn.net")
            bu7=tk.Button(pencerebir,text="27)theMatureporn     ",fg="black",bg="white",font="Times 11",command=bu7k)
            bu7.place(x=700,y=216)


            def bu8k ():
                webbrowser.open("https://tr.spankbang.com")
            bu8=tk.Button(pencerebir,text="28)SpankBang          ",fg="black",bg="white",font="Times 11",command=bu8k)
            bu8.place(x=700,y=252)


            def bu9k ():
                webbrowser.open("https://www.faphub.tv")
            bu9=tk.Button(pencerebir,text="29)FapHub               ",fg="black",bg="white",font="Times 11",command=bu9k)
            bu9.place(x=700,y=288)


            def bu10k ():
                webbrowser.open("https://www.24video.porn/videos/")
            bu10=tk.Button(pencerebir,text="30)24Video               ",fg="black",bg="white",font="Times 11",command=bu10k)
            bu10.place(x=700,y=326)


            def bu11k ():
                webbrowser.open("https://beeg.com")
            bu11=tk.Button(pencerebir,text="31)Beeg                   ",fg="black",bg="white",font="Times 11",command=bu11k)
            bu11.place(x=700,y=362)


            def bu12k ():
                webbrowser.open("https://vtrahe.fun/videos/")
            bu12=tk.Button(pencerebir,text="32)VtRahe               ",fg="black",bg="white",font="Times 11",command=bu12k)
            bu12.place(x=700,y=398)


            def bu13k ():
                webbrowser.open("https://sslkn.me")
            bu13=tk.Button(pencerebir,text="33)SosalKino            ",fg="black",bg="white",font="Times 11",command=bu13k)
            bu13.place(x=700,y=434)


            def bu14k ():
                webbrowser.open("https://prostoporno.tube")
            bu14=tk.Button(pencerebir,text="34)ProstoPorno         ",fg="black",bg="white",font="Times 11",command=bu14k)
            bu14.place(x=700,y=470)


            def bu15k ():
                webbrowser.open("https://dt.pornk.top/sex/")
            bu15=tk.Button(pencerebir,text="35)PornK                  ",fg="black",bg="white",font="Times 11",command=bu15k)
            bu15.place(x=700,y=506)


            def bu16k ():
                webbrowser.open("https://www.porno.limo/videos/")
            bu16=tk.Button(pencerebir,text="36)PornoLimo           ",fg="black",bg="white",font="Times 11",command=bu16k)
            bu16.place(x=700,y=542)


            def bu17k ():
                webbrowser.open("https://www.poimru.org")
            bu17=tk.Button(pencerebir,text="37)Poimru                 ",fg="black",bg="white",font="Times 11",command=bu17k)
            bu17.place(x=700,y=578)


            def bu18k ():
                webbrowser.open("https://xhdporno.me")
            bu18=tk.Button(pencerebir,text="38)Xhdorno               ",fg="black",bg="white",font="Times 11",command=bu18k)
            bu18.place(x=700,y=614)


            def bu19k ():
                webbrowser.open("https://javur.com")
            bu19=tk.Button(pencerebir,text="39)Javur                   ",fg="black",bg="white",font="Times 11",command=bu19k)
            bu19.place(x=700,y=650)


            def bu20k ():
                webbrowser.open("https://www.tiava.com/tr/")
            bu20=tk.Button(pencerebir,text="40)Tiava                   ",fg="black",bg="white",font="Times 11",command=bu20k)
            bu20.place(x=700,y=686)


            def bt1k ():
                webbrowser.open("https://twitter.com/dailypornvidzzz")
            bt1=tk.Button(pencerebir,text="Daily Porn Vids     ",fg="black",bg="white",font="Times 11",command=bt1k)
            bt1.place(x=920,y=50)


            def bt2k ():
                webbrowser.open("https://twitter.com/kizinsexgunlugu")
            bt2=tk.Button(pencerebir,text="1 Kızın Sex Günlüğü ",fg="black",bg="white",font="Times 11",command=bt2k)
            bt2.place(x=1120,y=50)


            def bt3k ():
                webbrowser.open("https://twitter.com/NisaBayat")
            bt3=tk.Button(pencerebir,text="Nisa Türk Porno    ",fg="black",bg="white",font="Times 11",command=bt3k)
            bt3.place(x=920,y=90)


            def bt4k ():
                webbrowser.open("https://twitter.com/cathenna11")
            bt4=tk.Button(pencerebir,text="HD Porno               ",fg="black",bg="white",font="Times 11",command=bt4k)
            bt4.place(x=1120,y=90)


            def bt5k ():
                webbrowser.open("https://twitter.com/pantyouofficial")
            bt5=tk.Button(pencerebir,text="Tiktok +18             ",fg="black",bg="white",font="Times 11",command=bt5k)
            bt5.place(x=920,y=130)


            def bt6k ():
                webbrowser.open("https://twitter.com/elifturkporno")
            bt6=tk.Button(pencerebir,text="Elif Türk Porno        ",fg="black",bg="white",font="Times 11",command=bt6k)
            bt6.place(x=1120,y=130)


            def bt7k ():
                webbrowser.open("https://twitter.com/PornB4u")
            bt7=tk.Button(pencerebir,text="CCtv Porn             ",fg="black",bg="white",font="Times 11",command=bt7k)
            bt7.place(x=920,y=170)


            def bt8k ():
                webbrowser.open("https://twitter.com/kizpornosex")
            bt8=tk.Button(pencerebir,text="Kız Porno                ",fg="black",bg="white",font="Times 11",command=bt8k)
            bt8.place(x=1120,y=170)


            def bt9k ():
                webbrowser.open("https://twitter.com/turkcepornvideo")
            bt9=tk.Button(pencerebir,text="Türkçe Porn Video",fg="black",bg="white",font="Times 11",command=bt9k)
            bt9.place(x=920,y=210)


            def bt10k ():
                webbrowser.open("https://twitter.com/pornoicerik")
            bt10=tk.Button(pencerebir,text="Porno Türk              ",fg="black",bg="white",font="Times 11",command=bt10k)
            bt10.place(x=1120,y=210)


            def bt11k ():
                webbrowser.open("https://twitter.com/scope_porno")
            bt11=tk.Button(pencerebir,text="Türk ifşa               ",fg="black",bg="white",font="Times 11",command=bt11k)
            bt11.place(x=920,y=250)


            def bt12k ():
                webbrowser.open("https://twitter.com/turkvesex")
            bt12=tk.Button(pencerebir,text="Türk Sex                 ",fg="black",bg="white",font="Times 11",command=bt12k)
            bt12.place(x=1120,y=250)


            def bc1k ():
                webbrowser.open("https://tr.xhamsterlive.com")
            bc1=tk.Button(pencerebir,text="XhamsterLive        ",fg="black",bg="white",font="Times 11",command=bc1k)
            bc1.place(x=920,y=500)


            def bc2k ():
                webbrowser.open("https://ukr.bongacams.com")
            bc2=tk.Button(pencerebir,text="BongaCams           ",fg="black",bg="white",font="Times 11",command=bc2k)
            bc2.place(x=1120,y=500)


            def bc3k ():
                webbrowser.open("https://trylivecam.com")
            bc3=tk.Button(pencerebir,text="TryliveCam             ",fg="black",bg="white",font="Times 11",command=bc3k)
            bc3.place(x=920,y=550)


            def bc4k ():
                webbrowser.open("https://chaturbate.com")
            bc4=tk.Button(pencerebir,text="ChatTurtabe            ",fg="black",bg="white",font="Times 11",command=bc4k)
            bc4.place(x=1120,y=550)


        elif (controlkullanıcı !=kulcontrol) and (controlşifre == şifcontrol):
            messagebox.showerror(title ="Başarısız",message="Kullanıcı veya şifre hatalı girildi! Lütfen kontrol ederek tekrar deneyiniz")


        elif (controlkullanıcı == kulcontrol) and (controlşifre != şifcontrol):
            messagebox.showerror(title="Başarısız",message="Kullanıcı veya şifre hatalı girildi! Lütfen kontrol ederek tekrar deneyiniz")


        else:
            messagebox.showerror(title="Başarısız",message="Kullanıcı adı ve şifre doğru  değil!")



    elif (controlbir != 1) and (controliki == 1):
        messagebox.showerror(title="Uyarı!",message="Giriş için 18 yaşından büyük olduğunuzu onaylamanız gerekmektedir!")


    elif (controlbir == 1) and (controliki != 1):
        messagebox.showerror(title="Uyarı!",message="Giriş için kullanıcı kullanım koşullarını kabul etmeniz gerekmektedir!")


    else:
        messagebox.showerror(title="Uyarı",message="Giriş için kullanım koşullarını ve yaş sınırlamasını kabul etmeniz gerekmektedir!")


#Kullanıcı şifre yazıları

kullanıcıyazısı =tk.Label(pencerebir,text="Kullanıcı :",fg="white",bg="black",font="Times 17")
kullanıcıyazısı.place(x=120,y=200)


şifreyazısı =tk.Label(pencerebir,text="Şifre :",fg="white",bg="black",font="Times 17")
şifreyazısı.place(x=120,y=260)


#Kullanıcı şifre girdileri

kullanıcıgirdi =tk.Entry(pencerebir,show="*",bg="grey")
kullanıcıgirdi.place(x=230,y=207)


şifregirdi =tk.Entry(pencerebir,show="*",bg="grey")
şifregirdi.place(x=230,y=266)


#Onay butonu oluşturma

girişbutonu =tk.Button(pencerebir,text="           Giriş Yap          ",fg="white",bg="black",activebackground="white",command=girişyapmak)
girişbutonu.place(x=234,y=390)



#18 yaş doğrulama ve kullanıjm koşulları
cb1 = IntVar()
doğrulama18 =Checkbutton(pencerebir, text = "18 Yaşından büyük olduğumu onaylıyorum.",variable= cb1, onvalue = 1, 
offvalue = 0, height=0, width =35,fg="grey",bg="black",activebackground="black",activeforeground="black")
doğrulama18.place(x=110,y=310)


cb2 = IntVar()
kullanımkoşul =Checkbutton(pencerebir, text="Kullanım koşullarını kabul ediyorum.",variable= cb2,onvalue = 1, 
offvalue = 0,height=0, width=35,fg="grey",bg="black",activebackground="black",activeforeground="black")

kullanımkoşul.place(x=91,y=340)

pencerebir.mainloop()
