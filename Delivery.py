from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from fpdf import FPDF 
from PIL import ImageTk , Image
import tkinter  as tk 
from tkcalendar import DateEntry
import datetime as dt
from tkinter import filedialog
import os
from tkcalendar import Calendar
def Resize_Image(image, maxsize):
    r1 = image.size[0]/maxsize[0] # width ratio
    r2 = image.size[1]/maxsize[1] # height ratio
    ratio = max(r1, r2)
    newsize = (int(image.size[0]/ratio), int(image.size[1]/ratio))
    image = image.resize(newsize, Image.ANTIALIAS)
    return image

monthes=["يناير","فبراير","مارس","ابريل","مايو","يونيو","يوليو","اغسطس","سبتمبر","اكتوبر","نوفمبر","ديسمبر"]
years= [2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040]
class Deliver:

    def __init__(self,root) :
        self.root = root 
         # declaring string variable 
        self.x = dt.datetime.now()
        self.daa=StringVar()
        self.kaa=StringVar()
        self.namm=StringVar()
        self.dayy=StringVar()
        self.mon=StringVar()
        self.year=StringVar()
        self.store = StringVar()
        self.haff=StringVar()
        self.hass=StringVar()
        self.id=StringVar()
        self.date=StringVar()
        self.trr=StringVar()
        self.mad=StringVar()
        self.name=StringVar()
        self.sel=tk.StringVar()
        self.today=StringVar()
        self.idd=StringVar()
        self.ideg= StringVar()
        self.addre=StringVar()
        self.phon=StringVar()
        self.namo = StringVar()
        self.key = False
        self.keyy= False
        #-------------------------------------------
        self.reset()
        #--------------------------------------------
        self.root.title("Deliver system")
        self.root.geometry("1550x800+0+0")
        Labe1= Label(self.root,text="علــــي الســـريـــع",bd=2,bg="teal",fg="white",relief=RIDGE,pady=5,padx=4,font=("times new roman",32,""))
        Labe1.pack(side=TOP,fill=X,ipady=14)
        # Create an object of tkinter ImageTk
       
        x = 0
        y = 15

        dataframerighttop= Frame(self.root,relief=RIDGE,bg="white")
        dataframerighttop.place(x=1045,y=115,height=100,width=220,)
        lab01=Label(dataframerighttop,text= "اختــار الشهــر",fg='white',bg="teal",font=("arial",14,"bold"))
        lab01.pack(side=TOP,fill=X,ipady=14)
        self.comb2=ttk.Combobox(dataframerighttop,width=30,font=("arial",14,""),state="readonly",justify="center")
        self.comb2.pack(side=TOP,fill=X,ipady=14)
        self.comb2['values']=monthes

        dataframerighttop2= Frame(self.root,relief=RIDGE,bg="white")
        dataframerighttop2.place(x=800,y=115,height=100,width=220,)
        lab01=Label(dataframerighttop2,text="اختــار السنـة",fg='white',bg="teal",font=("arial",14,"bold"))
        lab01.pack(side=TOP,fill=X,ipady=14)
        self.comb3=ttk.Combobox(dataframerighttop2,width=30,font=("arial",14,""),state="readonly",justify="center")
        self.comb3.pack(side=TOP,fill=X,ipady=14)
        self.comb3['values']=years    

        dataframeright= Frame(self.root,relief=RIDGE,bg="white")
        dataframeright.place(x=1290,y=115,height=100,width=220,)
        lab01=Label(dataframeright,text="اختـــار السائـق",fg='white',bg="teal",font=("arial",14,"bold"))
        lab01.pack(side=TOP,fill=X,ipady=14)
        self.comb1=ttk.Combobox(dataframeright,width=30,font=("arial",14,""),state="readonly",justify="center")
        self.comb1.pack(side=TOP,fill=X,ipady=14)
        # self.comb1.current(0)
        dataframeright1= Frame(self.root,relief=RIDGE,bg="white")
        dataframeright1.place(x=800,y=240,height=260+y,width=710,)
       
        lab2=Label(dataframeright1,text="الاضـــافــات",fg="white",bg="darkgreen",font=("times new roman",14,"bold"))
        lab2.pack(side=TOP,fill=X,ipady=14)
        lab3=Label(dataframeright1,text="قيمة الداخلــــي بالجنية",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab3.place(x=535+x,y=60+y) 
        entr1=Entry(dataframeright1,textvariable=self.daa,font=("arial",14,""),relief=RIDGE,borderwidth=2,width=12)
        entr1.place(x=360+x,y=60+y) 
        lab4=Label(dataframeright1,text="قيمة الخارجـــي بالجنية",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab4.place(x=535+x,y=105+y) 
        entr2=Entry(dataframeright1,textvariable=self.kaa,font=("arial",14,""),relief=RIDGE,borderwidth=2,width=12)
        entr2.place(x=360+x,y=105+y)
        lab7=Label(dataframeright1,text="قيمة الحـــافــز بالجنية",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab7.place(x=190+x,y=60+y) 
        entr3=Entry(dataframeright1,font=("arial",14,""),textvariable=self.haff,relief=RIDGE,borderwidth=2,width=12)
        entr3.place(x=14+x,y=60+y) 
        lab8=Label(dataframeright1,text="قيمة الخــصــم بالجنية",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab8.place(x=190+x,y=105+y) 
        entr4=Entry(dataframeright1,textvariable=self.hass,font=("arial",14,""),relief=RIDGE,borderwidth=2,width=12)
        entr4.place(x=14+x,y=105+y)
        
        lab9=Label(dataframeright1,text="المدفوع اليوم",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab9.place(x=215+x,y=155+y) 
        entr41=Entry(dataframeright1,textvariable=self.mad,font=("arial",14,""),relief=RIDGE,borderwidth=2,width=12)
        entr41.place(x=14+x,y=155+y)
        
        lab10=Label(dataframeright1,text="التـاريـخ",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab10.place(x=570+x,y=155+y) 
        #datetime---------------------------------------------
        
        self.noww=dt.datetime.now()
        #-----------------------------------------------------
        
        self.cal=DateEntry(dataframeright1, date_pattern='dd/mm/yy',textvariable=self.sel,year =int(self.noww.strftime("%y")), month = int(self.noww.strftime("%m")),
        			day = int(self.noww.strftime("%d")))
        self.cal.place(x=360+x,y=155+y)             
        
        buttadd7=Button(dataframeright1,text="اضــافــة",font=("arial",14,"bold"),fg="white",width=20,bg="darkgreen",command=self.iadd)
        buttadd7.place(x=350,y=220)
        buttadd6=Button(dataframeright1,text="تعديــل",font=("arial",14,"bold"),fg="white",width=10,bg="darkblue",command=self.update)
        buttadd6.place(x=150,y=220) 
        buttadd5=Button(dataframeright1,text="حـذف",font=("arial",14,"bold"),fg="white",width=10,bg="darkred",command=self.delete)
        buttadd5.place(x=10,y=220) 

        self.sel.trace("w",self.reset)

        dataframeright3= Frame(self.root,relief=RIDGE,bg="white")
        dataframeright3.place(x=800,y=540,height=230,width=710,)
        lab11=Label(dataframeright3,text="اضــافة سائــق",fg="white",bg="darkgreen",font=("times new roman",14,"bold"))
        lab11.pack(side=TOP,fill=X,ipady=14)
        lab12=Label(dataframeright3,text="الاســم",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab12.place(x=550,y=60+y) 
        entr11=Entry(dataframeright3,textvariable=self.name,font=("arial",14,""),relief=RIDGE,borderwidth=2,width=12)
        entr11.place(x=360,y=60+y) 
        lab13=Label(dataframeright3,text="رقم الهـــاتف",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab13.place(x=550,y=105+y) 
        entr12=Entry(dataframeright3,textvariable=self.phon,font=("arial",14,""),relief=RIDGE,borderwidth=2,width=12)
        entr12.place(x=360,y=105+y)
        lab14=Label(dataframeright3,text="رقم البطاقــة",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab14.place(x=190,y=60+y) 
        entr13=Entry(dataframeright3,font=("arial",14,""),textvariable=self.ideg,relief=RIDGE,borderwidth=2,width=12)
        entr13.place(x=14,y=60+y) 
        lab15=Label(dataframeright3,text="لوحة المركبة",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab15.place(x=190,y=105+y) 
        entr14=Entry(dataframeright3,textvariable=self.idd,font=("arial",14,""),relief=RIDGE,borderwidth=2,width=12)
        entr14.place(x=14,y=105+y)
        buttadd2=Button(dataframeright3,text="اضــافــة",font=("arial",14,"bold"),fg="white",width=20,bg="darkgreen",command=self.iaddinfo)
        buttadd2.place(x=350,y=160+y)
        buttadd3=Button(dataframeright3,text="تعديــل",font=("arial",14,"bold"),fg="white",width=10,bg="darkblue",command=self.updateinfo)
        buttadd3.place(x=100,y=160+y)

        dataframeleft= Frame(self.root,relief=RIDGE,bg="white")
        dataframeleft.place(x=25,y=115,width=750,height=340)
        lab1=Label(dataframeleft,textvariable=self.namm,fg="white",bg="teal",font=("times new roman",14,"bold"))
        lab1.pack(side=TOP,fill=X,ipady=14)
        scx=ttk.Scrollbar(dataframeleft,orient=HORIZONTAL)
        scx.pack(side=BOTTOM,fill=X)
        scy=ttk.Scrollbar(dataframeleft,orient=VERTICAL)
        scy.pack(side=RIGHT,fill=Y)
        self.orders=ttk.Treeview(dataframeleft,columns=("ta","da","kha","ha","has","tot","mad","mot",),xscrollcommand=scx.set,yscrollcommand=scy.set)        
        scx.config(command=self.orders.xview)
        scy.config(command=self.orders.yview)

        self.orders.heading("ta",text="التــاريــخ")
        self.orders.heading("da",text="الداخلــي")
        self.orders.heading("kha",text="الخارجــي")
        self.orders.heading("ha",text="قيمة الحافز بالجنية")
        self.orders.heading("has",text="قيمة الخصم بالجنية")
        self.orders.heading("tot",text="المجموع")
        self.orders.heading("mad",text="المدفوع")
        self.orders.heading("mot",text="المتبقي")
        self.orders["show"] = "headings"
        self.orders.pack(fill=BOTH,expand=1)
        self.orders.column( "da",width=110,anchor=CENTER)
        self.orders.column( "ta",width=110,anchor=CENTER)
        self.orders.column("kha",width=110,anchor=CENTER)
        self.orders.column( "ha",width=130,anchor=CENTER)
        self.orders.column("has",width=130,anchor=CENTER)
        self.orders.column("tot",width=110,anchor=CENTER)
        self.orders.column("mad",width=110,anchor=CENTER)
        self.orders.column("mot",width=110,anchor=CENTER)

        self.orders.bind("<ButtonRelease-1>",self.getdate)
        self.rr=self.comb1.get()
      
        self.id.set(self.rr)
        self.namm.set(self.rr)

        self.comb1.unbind_class("TCombobox", "<MouseWheel>")

        self.comb1.bind("<<ComboboxSelected>>",self.ref)
        self.comb2.bind("<<ComboboxSelected>>",self.fetchdata)
        self.comb3.bind("<<ComboboxSelected>>",self.fetchdata)
        
        style = ttk.Style()
        style.configure("Treeview.Heading", font = ("",14,""))

        #   frame left two ----------------------------------------------------------
        dataframeleft2= Frame(self.root,relief=RIDGE,bg="white")
        dataframeleft2.place(x=25,y=460,width=750,height=55)
        
        self.work=ttk.Treeview(dataframeleft2,columns=("id","name","ideg","phone",))
        self.work.heading("id",text="لوحة المركبة")
        self.work.heading("name",text="الاســم")
        self.work.heading("ideg",text="رقم البطاقــة")
        self.work.heading("phone",text="رقم الهاتــف")
        
        self.work["show"]="headings"
        self.work.pack(fill=BOTH,expand=1)
        self.work.column( "id",width=50,anchor=CENTER)
        self.work.column( "name",width=50,anchor=CENTER)
        self.work.column( "ideg",width=110,anchor=CENTER)
        self.work.column("phone",width=110,anchor=CENTER)
        self.work.bind("<ButtonRelease-1>",self.getdateinfo)
        self.comb3.set(int(self.noww.strftime("%Y")))
        self.comb2.set(monthes[int(self.noww.strftime("%m"))-1])
        
    # fatora ----------------------------------------------------------
        t= 0
        yy = 0
        dataframeleft3= Frame(self.root,relief=RIDGE,bg="white")
        dataframeleft3.place(x=25,y=540,height=230,width=750,)
        lab11=Label(dataframeleft3,text="استخراج فـاتورة شهرية",fg="white",bg="darkgreen",font=("times new roman",14,"bold"))
        lab11.pack(side=TOP,fill=X,ipady=14)
        lab12=Label(dataframeleft3,text="اختار السائـق",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab12.place(x=550+t,y=60+y) 
        self.comb4=ttk.Combobox(dataframeleft3,width=12,font=("arial",14,""),state="readonly",justify="center")
        self.comb4.place(x=360+t,y=60+y)
       
        lab17=Label(dataframeleft3,text="مكان التخزين",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab17.place(x=550,y=105+y) 
        lab18=Label(dataframeleft3,textvariable=self.store,bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab18.place(x=90,y=105+y) 
        
        lab14=Label(dataframeleft3,text="الشـهر",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab14.place(x=260+t,y=60+y)
        
        self.comb5=ttk.Combobox(dataframeleft3,width=12,font=("arial",14,""),state="readonly",justify="center")
        self.comb5.set("")
        self.comb5.place(x=90+t,y=60+y)
        self.comb5['values']=monthes
        self.comb5.set(monthes[int(self.noww.strftime("%m"))-1])

        buttadd4=Button(dataframeleft3,text="اختار مكان التخزيـن",font=("arial",14,"bold"),fg="white",width=10,bg="darkblue",command=self.openpath)
        buttadd4.place(x=100,y=160+y)

        buttadd2=Button(dataframeleft3,text="حفــظ الفـاتــورة",font=("arial",14,"bold"),fg="white",width=20,bg="darkgreen")
        buttadd2.place(x=350,y=160+y)

        self.fechcom()
        self.fetchdata()
        self.fetchdataaa()

        
    #--------------------------------------------
    # create table workers (id varchar(255) not null,name varchar(255) unique null,ideg BigINT NULL, phone varchar(11));
    #--------------------------------------------
    def openpath(self):
        filename = filedialog.askdirectory(initialdir=os.getcwdb(),title='اختــار مكان تخزين الفاتورة',)
       
        self.store.set(str(filename))
    def ref(self,arg):
        self.orders.delete(*self.orders.get_children())
        # self.getid()
        self.fetchdata()
        self.fetchdataaa()
        
        self.rr=self.comb1.get()
        # self.id.set(self.rr)
        self.namm.set(self.rr)
    def reset(self,*args):
        self.mad.set(0)
        self.daa.set(0)
        self.kaa.set(0)
        self.hass.set(0)
        self.haff.set(0)
        self.key=False
        self.keyy=False
    def iaddinfo(self):
            if len(self.ideg.get()) == 14 or self.ideg.get() == "0" :
                if str(self.name.get())!="workers":
                    if len(self.phon.get())==11 or len(self.phon.get())==10 or self.phon.get()== "0": 
                        try:
                                conn=mysql.connector.connect(
                                host = "localhost",database="nader", 
                                username ="root",
                                password = "nader01227546543N",)
                                mycursor = conn.cursor()
                                newname = ""
                                for i in str(self.name.get()):
                                    if i == ' ':
                                        newname+='_'
                                    else:
                                        newname+=i

                                strr ="create table nader.{} (ta DATE UNIQUE NULL ,daa DOUBLE NULL,kaa DOUBLE NULL , haff DOUBLE NULL ,hass DOUBLE NULL,tot DOUBLE NULL , mad DOUBLE NULL ,mot DOUBLE NULL,id INT NULL)".format(newname)
                                mycursor.execute("insert into workers values(%s,%s,%s,%s)",(self.idd.get(),self.name.get(),self.ideg.get(),self.phon.get()))
                                mycursor.execute(strr)
                                conn.commit()
                                self.fechcom()
                                conn.close()
                                messagebox.showinfo("صحيـح","تم الاضـافة بشكل صحيــح")
                        except:
                                messagebox.showerror("خطــأ","ادخــال غيــر صحيـــح")
                    else:
                        messagebox.showerror("تصحيح","اذا كنت لا تريد ادخال رقم الهاتـف قم بادخال 0")
                else :
                    messagebox.showwarning("خطأ برمجي", "workers لا يمكن استخدام الاسم  ")
            else :   
                messagebox.showerror("تصحيح","اذا كنت لا تريد ادخال رقم البطاقة قم بادخال 0")
    def fechcom(self):
        conn=mysql.connector.connect(
                host = "localhost",database="nader", 
                username ="root",
                password = "nader01227546543N",)
        mycursor = conn.cursor()
        mycursor.execute("select name from workers")


        self.listee=[]
        rows = mycursor.fetchall()
        for i in range(len(rows)):
            self.listee.append( rows[i][0])
        
        self.comb1['values']=self.listee
        self.comb4['values']=self.listee
        conn.commit()
        conn.close()
    def iadd(self) :
        if self.comb1.get() != "":
            if self.kaa.get()=='0' and self.haff.get()=='0' and self.daa.get()=='0' and self.hass.get()=='0' and self.mad.get()=='0':
                messagebox.showwarning("خطـأ", "لم يتم ادخـال جميع البيانـات")
            else :
                try:
                    conn=mysql.connector.connect(
                    host = "localhost",database="nader", 
                    username ="root",
                    password = "nader01227546543N")

                    newname = ""
                    for i in str(self.comb1.get()):
                        if i == ' ':
                            newname+='_'
                        else:
                            newname+=i

                    strh="select mot from nader.{}".format(newname)
                    rowww= conn.cursor()
                    rowww.execute(strh)
                    row=rowww.fetchall()
                    if len(row) == 0 :
                        help = 0.0
                    else :
                        help =row[len(row)-1][0]
                    self.u = round(round(0.7*float(self.daa.get()),2)+round(0.8*float(self.kaa.get()),2)+float(self.haff.get())+float(-1*float(self.hass.get())) + help,2)
                    # print(self.u)
                    stre='insert into nader.{} values("{}",{},{},{},{},{},{},{},DEFAULT)'.format(newname,str(self.cal.get_date()),round(0.7*float(self.daa.get()),2),round(0.8*float(self.kaa.get()),2),float(self.haff.get()),float(self.hass.get()),float(self.u),float(self.mad.get()),float(float(self.u)-float(self.mad.get())))
                    mycursor = conn.cursor()
                    # print(stre)
                    mycursor.execute(stre)
                    self.modulateId(mycursor)
                    self.medulatetot(mycursor)
                    conn.commit()

                    conn.close()
                    messagebox.showinfo("مقبول","تم الاضـافة بشكل صحيــح")
                    self.fetchdata()
                    self.reset()
                    
                 
                except:
                    messagebox.showerror("خطــأ","ادخــال غيــر صحيـــح")
        else :
            messagebox.showwarning("خطــأ","يرجـي اختيـار السائـق")
    def fetchdata(self,*args) :
        try:
            if str(self.comb1.get())!= "":
                conn=mysql.connector.connect(
                host = "localhost",database="nader", 
                username ="root",
                password = "nader01227546543N")
                self.orders.delete(*self.orders.get_children())
                newname = ""
                for i in str(self.comb1.get()):
                    if i == ' ':
                        newname+='_'
                    else:
                        newname+=i
                self.o = "01"
                self.p=  "01"
                self.yb =str(self.comb3.get())
                self.ya=str( self.comb3.get())
                if self.comb2.get()=="يناير" :
                    self.o = "01"
                    self.p = "02"
                elif self.comb2.get()=="فبراير":
                    self.o = "02"
                    self.p = "03"
                elif self.comb2.get()=="مارس":
                    self.o = "03"
                    self.p = "04"
                elif self.comb2.get()=="ابريل":
                    self.o = "04"
                    self.p = "05"
                elif self.comb2.get()=="مايو":
                    self.o = "05"
                    self.p = "06"
                elif self.comb2.get()=="يونيو":
                    self.o = "06"
                    self.p = "07"
                elif self.comb2.get()=="يوليو":
                    self.o = "07"
                    self.p = "08"
                elif self.comb2.get()=="اغسطس":
                    self.o = "08"
                    self.p = "09"
                elif self.comb2.get()=="سبتمبر":
                    self.o = "09"
                    self.p = "10"
                elif self.comb2.get()=="اكتوبر":
                    self.o = "10"
                    self.p = "11"
                elif self.comb2.get()=="نوفمبر":
                    self.o = "11"
                    self.p = "12"
                elif self.comb2.get()=="ديسمبر":
                    self.o = "12"
                    self.p = "01"
                    self.ya =str( int(self.ya) + 1)
                                
                strh='select * from nader.{} where ta BETWEEN "{}-{}-01" AND "{}-{}-01" order by ta DESC'.format(newname,self.yb,self.o,self.ya,self.p)
                rowww= conn.cursor()
              
                rowww.execute(strh)
                rows=rowww.fetchall()
                if len(rows)!= 0 :
                    self.orders.delete(*self.orders.get_children())
                for i in rows :
                    self.orders.insert("",END,values=i)
                # print(rows)
                conn.commit()
                conn.close()        
            
        except:
            messagebox.showerror("4ekokike")
    def fetchdataaa(self) :
        try:
            if str(self.comb1.get())!= "":
                conn=mysql.connector.connect(
                host = "localhost",database="nader", 
                username ="root",
                password = "nader01227546543N")
                
                
           
                strh='select * from nader.workers where name = "{}"'.format(str(self.comb1.get()))
                rowww= conn.cursor()
                rowww.execute(strh)
                rows=rowww.fetchall()
                if len(rows)!= 0 :
                    self.work.delete(*self.work.get_children())
                for i in rows :
                    self.work.insert("",END,values=i)
                # print(rows)
                conn.commit()
                conn.close()        
            
        except:
            messagebox.showerror("sasa")
    
    def modulateId(self,roe):
        self.rer = 1
        try:
                    # conn=mysql.connector.connect(
                    # host = "localhost",database="nader", 
                    # username ="root",
                    # password = "nader01227546543N")

                    newname = ""
                    for i in str(self.comb1.get()):
                        if i == ' ':
                            newname+='_'
                        else:
                            newname+=i
                    strh="select id , ta from nader.{} order by ta".format(newname)
                
                    roe.execute(strh)
                
                    row=roe.fetchall()
                    for i in row : 
                        st = 'update nader.{} set id = {} where ta = "{}"'.format(newname,self.rer,i[1])
                        roe.execute(st)
                        self.rer+=1
                
                    # self.u = round(round(0.7*float(self.daa.get()),2)+round(0.8*float(self.kaa.get()),2)+float(self.haff.get())+float(-1*float(self.hass.get())) + help,2)
                    # # print(self.u)
                    # stre='insert into nader.{} values("{}",{},{},{},{},{},{},{},DEFAULT)'.format(newname,str(self.cal.get_date()),round(0.7*float(self.daa.get()),2),round(0.8*float(self.kaa.get()),2),float(self.haff.get()),float(self.hass.get()),float(self.u),float(self.mad.get()),float(float(self.u)-float(self.mad.get())))
                    # mycursor = conn.cursor()
                    # # print(stre)
                    # mycursor.execute(stre)
                    # conn.commit()
                   
                    # self.modulateId()
                    # self.reset()
                    # conn.close()
                  
                    # print(r)
                    # messagebox.showinfo("مقبول","تم الاضـافة بشكل صحيــح")
        except:
                    messagebox.showerror("خطــأ","ERROR")
    def medulatetot(self,roe): 
        self.rer = 1
        self.tr = 0 
        try:
                    newname = ""
                    for i in str(self.comb1.get()):
                        if i == ' ':
                            newname+='_'
                        else:
                            newname+=i
                    strh="select id ,daa,kaa,haff,hass from nader.{} order by ta".format(newname)
                
                    roe.execute(strh)
                
                    row=roe.fetchall()
                    for i in row :
                        st = 'update nader.{} set tot = daa + kaa + haff - hass - mad + {}, mot = tot where id = {} ;'.format(newname,self.tr,self.rer)
                        # print(st)
                        roe.execute(st)
                        # print(i[1])
                        self.tr += round(i[1]+i[2]+i[3]-i[4],2)
                        self.rer+=1
                
                    # self.u = round(round(0.7*float(self.daa.get()),2)+round(0.8*float(self.kaa.get()),2)+float(self.haff.get())+float(-1*float(self.hass.get())) + help,2)
                    # # print(self.u)
                    # stre='insert into nader.{} values("{}",{},{},{},{},{},{},{},DEFAULT)'.format(newname,str(self.cal.get_date()),round(0.7*float(self.daa.get()),2),round(0.8*float(self.kaa.get()),2),float(self.haff.get()),float(self.hass.get()),float(self.u),float(self.mad.get()),float(float(self.u)-float(self.mad.get())))
                    # mycursor = conn.cursor()
                    # # print(stre)
                    # mycursor.execute(stre)
                    # conn.commit()
                   
                    # self.modulateId()
                    # self.reset()
                    # conn.close()
           
                    # print(r)
                    # messagebox.showinfo("مقبول","تم الاضـافة بشكل صحيــح")
        except:
                    messagebox.showerror("خطــأ","hee")

    def delete(self):
        try :
                if self.comb1.get() != "" : 
                    if self.key == False  :
                       messagebox.showwarning("خطأ", " اختـار اليوم من الجدول اولا") 
                    else :
                        if self.kaa.get()=='0' and self.haff.get()=='0' and self.daa.get()=='0' and self.hass.get()=='0' and self.mad.get()=='0':
                           messagebox.showwarning("خطـأ", "لم يتم ادخـال جميع البيانـات")
                        else :    
                           if self.comb1.get() != "":

                               newname = ""
                               for i in str(self.comb1.get()):
                                   if i == ' ':
                                       newname+='_'
                                   else:
                                       newname+=i
                               conn=mysql.connector.connect(
                                       host = "localhost",database="nader", 
                                       username ="root",
                                       password = "nader01227546543N")
                               mycursor = conn.cursor()

                               strt='delete from nader.{} where ta = "{}"'.format(newname,str(self.sel.get()))
                               # print(strt)
                               mycursor.execute(strt)
                               srt='select ta from nader.{} where ta = "{}"'.format(str(self.comb1.get()),str(self.sel.get()))   
                               # mycursor.execute(srt)
                               t= self.sel.get()
                               row= mycursor.fetchall()

                               messagebox.showinfo("مقبول","تم الحـذف بشكل صحيـح")
                               self.modulateId(mycursor)
                               self.medulatetot(mycursor)
                               conn.commit()
                               self.orders.delete(*self.orders.get_children())
                               
                               self.fetchdata()
                               self.reset()
                               conn.close()
                else:
                    messagebox.showwarning("خطــأ","يرجـي اختيـار السائـق")
        except:
            messagebox.showerror("ERROR","ERROR")
    def update(self):
            try:
                if self.comb1.get() != "": 
                    if self.key==False :
                       messagebox.showwarning("خطأ", " اختـار اليوم من الجدول اولا") 
                    else :
                        if self.kaa.get()=='0' and self.haff.get()=='0' and self.daa.get()=='0' and self.hass.get()=='0' and self.mad.get()=='0':
                           messagebox.showwarning("خطـأ", "لم يتم ادخـال جميع البيانـات")
                        else :    
                           if self.comb1.get() != "":

                               newname = ""
                               for i in str(self.comb1.get()):
                                   if i == ' ':
                                       newname+='_'
                                   else:
                                       newname+=i
                               conn=mysql.connector.connect(
                                       host = "localhost",database="nader", 
                                       username ="root",
                                       password = "nader01227546543N")
                               mycursor = conn.cursor()

                               strt='update nader.{} set daa = {},kaa={},haff={},hass={} , mad = {} where ta = "{}"'.format(newname,  round(0.7*float(self.daa.get()),2),round(0.8*float(self.kaa.get()),2),round(float(self.haff.get()),2),round(float(self.hass.get()),2),round(float(self.mad.get()),2),str(self.sel.get()))
                               # print(strt)
                               mycursor.execute(strt)
                               srt='select ta from nader.{} where ta = "{}"'.format(str(self.comb1.get()),str(self.sel.get()))   
                               messagebox.showinfo("مقبول","تم التعديل بشكل صحيـح")
                               self.modulateId(mycursor)   
                               self.medulatetot(mycursor)  
                               conn.commit()
                               conn.close()
                               self.fetchdata()
                               self.reset()        
                else:
                    messagebox.showwarning("خطــأ","يرجـي اختيـار السائـق")
            except:
                messagebox.showerror("ERROR","ERROR")
    def getdate(self,*args):
        try:
            if str(self.comb1.get()) != "":
                cursor_row =self.orders.focus()
                content = self.orders.item(cursor_row)
                row= content['values']
                # self.cal.set_date(row[0])
                if len(row) !=0:
                    self.sel.set(row[0])
                    self.daa.set(str(round(1.428571428571429*float(row[1]),2)))
                    self.kaa.set(str(1.25*float(row[2])))
                    self.haff.set(row[3])
                    self.hass.set(row[4])
                    self.mad.set(row[6])
                    self.key=True
        except :
            messagebox.showerror("eree")  
    def updateinfo(self):
        if self.comb1.get() != "": 
            if self.name.get()=='' and self.idd.get()=='' and self.ideg.get()=='' and self.phon.get()=='':
               messagebox.showwarning("خطـأ", "لم يتم ادخـال جميع البيانـات")
            else :    
               if self.comb1.get() != self.name.get() :
                       messagebox.showerror("خطأ","لا يمكـن تعديـل الاســم")
               else :
                    if len(self.ideg.get()) == 14 or self.ideg.get() == "0" :

                                if len(self.phon.get())==11 or len(self.phon.get())==10 or self.phon.get()== "0": 
                                    try:
                                            if self.keyy==False :
                                               messagebox.showwarning("خطأ", " اختـار المعلومات من الجدول اولا") 
                                            else :
                                                            if self.comb1.get() != "":
                                                                conn=mysql.connector.connect(
                                        host = "localhost",database="nader", 
                                        username ="root",
                                        password = "nader01227546543N")
                                                                mycursor = conn.cursor()
                                                                strt='update nader.workers set  id = "{}",ideg= {},phone = {} where name = "{}"'.format(str(self.idd.get()),str(self.ideg.get()),str(self.phon.get()),str(self.comb1.get()))
                                                          
                                                                mycursor.execute(strt)
                                                                # srt='select ta from nader.{} where ta = "{}"'.format(str(self.comb1.get()),str(self.sel.get()))   
                                                                messagebox.showinfo("مقبول","تم التعديل بشكل صحيـح")
                                                                conn.commit()
                                                                conn.close()
                                                                self.fetchdataaa() 
                                    except:
                                        messagebox.showerror("ERROR","ERROR")

                                else:
                                    messagebox.showerror("تصحيح","اذا كنت لا تريد ادخال رقم الهاتـف قم بادخال 0")
                    else :   
                        messagebox.showerror("تصحيح","اذا كنت لا تريد ادخال رقم البطاقة قم بادخال 0")
        else:
            messagebox.showwarning("خطــأ","يرجـي اختيـار السائـق")
    def getdateinfo(self,*args):
        try:
            if str(self.comb1.get()) != "":
                cursor_row =self.work.focus()
                content = self.work.item(cursor_row)
                row= content['values']
                # self.cal.set_date(row[0])
                if len(row) !=0:
                    self.name.set(row[1])
                    self.ideg.set(row[2])
                    self.idd.set(row[0])
                    self.phon.set(row[3])
                    self.keyy=True
                    self.namo.set(row[1])
                    
        except :
            messagebox.showerror("eree")  
    #-------------------------------------------------------
if __name__=="__main__":
    root = Tk()
    obj = Deliver(root)
    root.mainloop()