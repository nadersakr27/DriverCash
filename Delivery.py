#Libraries
## for tkinter window 
from tkinter import*
from tkinter import ttk
import tkinter  as tk 
from tkcalendar import DateEntry
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import filedialog
import os
## to creat pdf as a list of tasks
from fpdf import FPDF 
## to add images
from PIL import ImageTk , Image
# to calculate our day and datetime data type
import datetime as dt
# to connect with database  
import mysql.connector

# fun to resize image
# def Resize_Image(image, maxsize):
#     r1 = image.size[0]/maxsize[0] # width ratio
#     r2 = image.size[1]/maxsize[1] # height ratio
#     ratio = max(r1, r2)
#     newsize = (int(image.size[0]/ratio), int(image.size[1]/ratio))
#     image = image.resize(newsize, Image.ANTIALIAS)
#     return image
#list of monthes
monthes=["يناير","فبراير","مارس","ابريل","مايو","يونيو","يوليو","اغسطس","سبتمبر","اكتوبر","نوفمبر","ديسمبر"]
# list of years 
years= [2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040]
# our main class 
class Deliver:

    def __init__(self,root) :
        # to edit root window     
        self.root = root 
        self.root.title("Deliver system")
        self.root.geometry("1550x800+0+0")
         # declaring string variable 
        self.x = dt.datetime.now()
        self.tt=StringVar()
        self.daa=StringVar()
        self.kaa=StringVar()
        self.namm=StringVar()
        self.dayy=StringVar()
        self.mon=StringVar()
        self.year=StringVar()
        self.store=StringVar()
        self.haff=StringVar()
        self.hass=StringVar()
        self.id=StringVar()
        self.date=StringVar()
        self.trr=StringVar()
        self.mad=StringVar()
        self.name=StringVar()
        self.sel=StringVar()
        self.today=StringVar()
        self.idd=StringVar()
        self.ideg= StringVar()
        self.addre=StringVar()
        self.phon=StringVar()
        self.namo = StringVar()
        self.key = False
        self.keyy= False
        #-------------------------------------------
        # to rest all variable to its default values
        self.reset()
        #--------------------------------------------
        #the whole name of the market
        MarketName= Label(self.root,text="علــــي الســـريـــع",bd=2,bg="teal",fg="white",relief=RIDGE,pady=5,padx=4,font=("times new roman",32,""))
        MarketName.pack(side=TOP,fill=X,ipady=14)
        # padding to position of all widgits
        x = 0
        y = 15
        # select worker from a workercombo
        SelectworkerFrame= Frame(self.root,relief=RIDGE,bg="white")
        SelectworkerFrame.place(x=1290,y=115,height=100,width=220,)
        labelOfDelectworker=Label(SelectworkerFrame,text="اختـــار السائـق",fg='white',bg="teal",font=("arial",14,"bold"))
        labelOfDelectworker.pack(side=TOP,fill=X,ipady=14)
        self.workercombo=ttk.Combobox(SelectworkerFrame,width=30,font=("arial",14,""),state="readonly",justify="center")
        self.workercombo.pack(side=TOP,fill=X,ipady=14)
        # select month fram
        monthSelectionFram= Frame(self.root,relief=RIDGE,bg="white")
        monthSelectionFram.place(x=1045,y=115,height=100,width=220,)
        monthSelectionLabel=Label(monthSelectionFram,text= "اختــار الشهــر",fg='white',bg="teal",font=("arial",14,"bold"))
        monthSelectionLabel.pack(side=TOP,fill=X,ipady=14)
        self.monthSelectioncombo=ttk.Combobox(monthSelectionFram,width=30,font=("arial",14,""),state="readonly",justify="center")
        self.monthSelectioncombo.pack(side=TOP,fill=X,ipady=14)
        self.monthSelectioncombo['values']=monthes
        # select year fram
        selectYearFram= Frame(self.root,relief=RIDGE,bg="white")
        selectYearFram.place(x=800,y=115,height=100,width=220,)
        selectYearLabel=Label(selectYearFram,text="اختــار السنـة",fg='white',bg="teal",font=("arial",14,"bold"))
        selectYearLabel.pack(side=TOP,fill=X,ipady=14)
        self.selectYearcombo=ttk.Combobox(selectYearFram,width=30,font=("arial",14,""),state="readonly",justify="center")
        self.selectYearcombo.pack(side=TOP,fill=X,ipady=14)
        self.selectYearcombo['values']=years   
        


        # adding editing and deleting order fram table of worker
        addingorderFram= Frame(self.root,relief=RIDGE,bg="white")
        addingorderFram.place(x=800,y=240,height=260+y,width=710,)
       
        addingorderlabel=Label(addingorderFram,text="قائمة التوصيلات",fg="white",bg="darkgreen",font=("times new roman",14,"bold"))
        addingorderlabel.pack(side=TOP,fill=X,ipady=14)
        addinglabel1=Label(addingorderFram,text="قيمة الداخلــــي بالجنية",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        addinglabel1.place(x=535+x,y=60+y) 
        addingentry1=Entry(addingorderFram,textvariable=self.daa,font=("arial",14,""),relief=RIDGE,borderwidth=2,width=12)
        addingentry1.place(x=360+x,y=60+y) 
        addinglabel2=Label(addingorderFram,text="قيمة الخارجـــي بالجنية",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        addinglabel2.place(x=535+x,y=105+y) 
        addingentry2=Entry(addingorderFram,textvariable=self.kaa,font=("arial",14,""),relief=RIDGE,borderwidth=2,width=12)
        addingentry2.place(x=360+x,y=105+y)
        addinglabel3=Label(addingorderFram,text="قيمة الحـــافــز بالجنية",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        addinglabel3.place(x=190+x,y=60+y) 
        addingentry3=Entry(addingorderFram,font=("arial",14,""),textvariable=self.haff,relief=RIDGE,borderwidth=2,width=12)
        addingentry3.place(x=14+x,y=60+y) 
        addinglabel4=Label(addingorderFram,text="قيمة الخــصــم بالجنية",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        addinglabel4.place(x=190+x,y=105+y) 
        addingentry4=Entry(addingorderFram,textvariable=self.hass,font=("arial",14,""),relief=RIDGE,borderwidth=2,width=12)
        addingentry4.place(x=14+x,y=105+y)
        lab9=Label(addingorderFram,text="المدفوع اليوم",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab9.place(x=215+x,y=155+y) 
        entr41=Entry(addingorderFram,textvariable=self.mad,font=("arial",14,""),relief=RIDGE,borderwidth=2,width=12)
        entr41.place(x=14+x,y=155+y)
        
        lab10=Label(addingorderFram,text="التـاريـخ",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab10.place(x=570+x,y=155+y) 
        #datetime---------------------------------------------
        # set todaytime
        self.noww=dt.datetime.now()
        #-----------------------------------------------------
        # dataentry for day which we add task in
        self.cal=DateEntry(addingorderFram, date_pattern='dd/mm/yy',textvariable=self.sel,year =int(self.noww.strftime("%y")), month = int(self.noww.strftime("%m")),day = int(self.noww.strftime("%d")))
        self.cal.place(x=360+x,y=155+y)             
        # adding buttones
        buttadd7=Button(addingorderFram,text="اضــافــة",font=("arial",14,"bold"),fg="white",width=20,bg="darkgreen",command=self.iadd)
        buttadd7.place(x=350,y=220)
        buttadd6=Button(addingorderFram,text="تعديــل",font=("arial",14,"bold"),fg="white",width=10,bg="darkblue",command=self.update)
        buttadd6.place(x=150,y=220) 
        buttadd5=Button(addingorderFram,text="حـذف",font=("arial",14,"bold"),fg="white",width=10,bg="darkred",command=self.delete)
        buttadd5.place(x=10,y=220) 
        # trace if user change day in dataentry 
        # self.sel.trace("w",self.reset)
#         
# 
# 
# 
# 
# 
# 
# 
# 
        # enter a data of worker
        addingworkerFram= Frame(self.root,relief=RIDGE,bg="white")
        addingworkerFram.place(x=800,y=540,height=230,width=710,)

        lab11=Label(addingworkerFram,text="اضــافة سائــق",fg="white",bg="darkgreen",font=("times new roman",14,"bold"))
        lab11.pack(side=TOP,fill=X,ipady=14)
        lab12=Label(addingworkerFram,text="الاســم",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab12.place(x=550,y=60+y) 
        entr11=Entry(addingworkerFram,textvariable=self.name,font=("arial",14,""),relief=RIDGE,borderwidth=2,width=12)
        entr11.place(x=360,y=60+y) 
        lab13=Label(addingworkerFram,text="رقم الهـــاتف",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab13.place(x=550,y=105+y) 
        entr12=Entry(addingworkerFram,textvariable=self.phon,font=("arial",14,""),relief=RIDGE,borderwidth=2,width=12)
        entr12.place(x=360,y=105+y)
        lab14=Label(addingworkerFram,text="رقم البطاقــة",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab14.place(x=190,y=60+y) 
        entr13=Entry(addingworkerFram,font=("arial",14,""),textvariable=self.ideg,relief=RIDGE,borderwidth=2,width=12)
        entr13.place(x=14,y=60+y) 
        lab15=Label(addingworkerFram,text="لوحة المركبة",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab15.place(x=190,y=105+y) 
        entr14=Entry(addingworkerFram,textvariable=self.idd,font=("arial",14,""),relief=RIDGE,borderwidth=2,width=12)
        entr14.place(x=14,y=105+y)
        buttadd2=Button(addingworkerFram,text="اضــافــة",font=("arial",14,"bold"),fg="white",width=20,bg="darkgreen",command=self.iaddinfo)
        buttadd2.place(x=350,y=160+y)
        buttadd3=Button(addingworkerFram,text="تعديــل",font=("arial",14,"bold"),fg="white",width=10,bg="darkblue",command=self.updateinfo)
        buttadd3.place(x=100,y=160+y)
# 





# 
# display data in orders table in database where name is in selectworkercombbox
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
        # trace when user click on row in tabel
        self.orders.bind("<ButtonRelease-1>",self.getdate)

        # close change values in combobox with mouse wheel
        self.workercombo.unbind_class("TCombobox", "<MouseWheel>")
        # trace when user change the value in worker combobox
        self.workercombo.bind("<<ComboboxSelected>>",self.ref)
        # trace when user change the value in monthes combobox
        self.monthSelectioncombo.bind("<<ComboboxSelected>>",self.fetchdata)
        # trace when user change the value in years combobox
        self.selectYearcombo.bind("<<ComboboxSelected>>",self.fetchdata)
      
      



        #  display the data of worker in database  ----------------------------------------------------------
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
        self.selectYearcombo.set(int(self.noww.strftime("%Y")))
        self.monthSelectioncombo.set(monthes[int(self.noww.strftime("%m"))-1])
        
    # to make a list of orders in month which user select ----------------------------------------------------------
        
        dataframeleft3= Frame(self.root,relief=RIDGE,bg="white")
        dataframeleft3.place(x=25,y=540,height=230,width=750,)
        lab11=Label(dataframeleft3,text="استخراج فـاتورة شهرية",fg="white",bg="darkgreen",font=("times new roman",14,"bold"))
        lab11.pack(side=TOP,fill=X,ipady=14)
        # choise the worker
        lab12=Label(dataframeleft3,text="اختار السائـق",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab12.place(x=550,y=60+y) 
        self.comb4=ttk.Combobox(dataframeleft3,width=12,font=("arial",14,""),state="readonly",justify="center")
        self.comb4.place(x=360,y=60+y)
        # label of month
        lab14=Label(dataframeleft3,text="الشـهر",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab14.place(x=260,y=60+y)
        # to select month
        self.comb5=ttk.Combobox(dataframeleft3,width=12,font=("arial",14,""),state="readonly",justify="center")
        self.comb5.set("")
        self.comb5.place(x=90,y=60+y)
        self.comb5['values']=monthes
        self.comb5.set(monthes[int(self.noww.strftime("%m"))-1])
        # choice your path in device
        buttadd4=Button(dataframeleft3,text="اختار مكان التخزيـن",font=("arial",14,"bold"),fg="white",width=10,bg="darkblue",command=self.openpath)
        buttadd4.place(x=100,y=160+y)
        # display the path
        lab17=Label(dataframeleft3,text="مكان التخزين",bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab17.place(x=550,y=105+y) 
        lab18=Label(dataframeleft3,textvariable=self.store,bg='white',fg="black",font=("arial",14,""),justify=RIGHT)
        lab18.place(x=90,y=105+y) 
        # to save the list as a pdf
        buttadd2=Button(dataframeleft3,text="حفــظ الفـاتــورة",font=("arial",14,"bold"),fg="white",width=20,bg="darkgreen")
        buttadd2.place(x=350,y=160+y)





        # fetch all workers in database in workerscombobox when user come into program
        self.fechcom()

    #--------------------------------------------
    # create table workers (id varchar(255) not null,name varchar(255) unique null,ideg BigINT NULL, phone varchar(11));
    #--------------------------------------------
    def openpath(self):
        filename = filedialog.askdirectory(initialdir=os.getcwdb(),title='اختــار مكان تخزين الفاتورة')
        self.store.set(str(filename))
    def ref(self,arg):
        self.orders.delete(*self.orders.get_children())
        self.fetchdata()
        self.fetchdataaa()
        self.rr=self.workercombo.get()
        self.namm.set(self.rr)
    def reset(self,*args):
        self.mad.set(0)
        self.daa.set(0)
        self.kaa.set(0)
        self.hass.set(0)
        self.haff.set(0)
        self.sel.set(self.tt.get())
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
                                strr ="create table nader.{} (ta DATE UNIQUE NULL ,daa DOUBLE NULL,kaa DOUBLE NULL , haff DOUBLE NULL ,hass DOUBLE NULL,tot DOUBLE NULL , mad DOUBLE NULL ,mot DOUBLE NULL,id INT NULL)".format(self.name.get().strip())
                                ext2=f'insert into workers values("{self.idd.get()}","{self.name.get()}",{self.ideg.get()},{self.phon.get()})'
                                mycursor.execute(ext2)
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
        
        self.workercombo['values']=self.listee
        self.comb4['values']=self.listee
        conn.commit()
        conn.close()
    def iadd(self) :
        if self.workercombo.get() != "":
            if self.kaa.get()=='0' and self.haff.get()=='0' and self.daa.get()=='0' and self.hass.get()=='0' and self.mad.get()=='0':
                messagebox.showwarning("خطـأ", "لم يتم ادخـال جميع البيانـات")
            else :
                try:
                    conn=mysql.connector.connect(
                    host = "localhost",database="nader", 
                    username ="root",
                    password = "nader01227546543N")
                    strh="select mot from nader.{}".format(self.workercombo.get().strip())
                    rowww= conn.cursor()
                    rowww.execute(strh)
                    row=rowww.fetchall()
                    if len(row) == 0 :
                        help = 0.0
                    else :
                        help =row[len(row)-1][0]
                    self.u = round(round(0.7*float(self.daa.get()),2)+round(0.8*float(self.kaa.get()),2)+float(self.haff.get())+float(-1*float(self.hass.get())) + help,2)
           
                    stre='insert into nader.{} values("{}",{},{},{},{},{},{},{},DEFAULT)'.format(self.workercombo.get().strip(),str(self.cal.get_date()),round(0.7*float(self.daa.get()),2),round(0.8*float(self.kaa.get()),2),float(self.haff.get()),float(self.hass.get()),float(self.u),float(self.mad.get()),float(float(self.u)-float(self.mad.get())))
                    mycursor = conn.cursor()
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
            if str(self.workercombo.get())!= "":
                conn=mysql.connector.connect(
                host = "localhost",database="nader", 
                username ="root",
                password = "nader01227546543N")
                self.orders.delete(*self.orders.get_children())
                self.o = "01"
                self.p=  "01"
                self.yb =str(self.selectYearcombo.get())
                self.ya=str( self.selectYearcombo.get())
                if self.monthSelectioncombo.get()=="يناير" :
                    self.o = "01"
                    self.p = "02"
                elif self.monthSelectioncombo.get()=="فبراير":
                    self.o = "02"
                    self.p = "03"
                elif self.monthSelectioncombo.get()=="مارس":
                    self.o = "03"
                    self.p = "04"
                elif self.monthSelectioncombo.get()=="ابريل":
                    self.o = "04"
                    self.p = "05"
                elif self.monthSelectioncombo.get()=="مايو":
                    self.o = "05"
                    self.p = "06"
                elif self.monthSelectioncombo.get()=="يونيو":
                    self.o = "06"
                    self.p = "07"
                elif self.monthSelectioncombo.get()=="يوليو":
                    self.o = "07"
                    self.p = "08"
                elif self.monthSelectioncombo.get()=="اغسطس":
                    self.o = "08"
                    self.p = "09"
                elif self.monthSelectioncombo.get()=="سبتمبر":
                    self.o = "09"
                    self.p = "10"
                elif self.monthSelectioncombo.get()=="اكتوبر":
                    self.o = "10"
                    self.p = "11"
                elif self.monthSelectioncombo.get()=="نوفمبر":
                    self.o = "11"
                    self.p = "12"
                elif self.monthSelectioncombo.get()=="ديسمبر":
                    self.o = "12"
                    self.p = "01"
                    self.ya =str( int(self.ya) + 1)
                                
                strh='select * from nader.{} where ta BETWEEN "{}-{}-01" AND "{}-{}-01" order by ta DESC'.format(self.workercombo.get().strip(),self.yb,self.o,self.ya,self.p)
                rowww= conn.cursor()
                rowww.execute(strh)
                rows=rowww.fetchall()
                if len(rows)!= 0 :
                    self.orders.delete(*self.orders.get_children())
                for i in rows :
                    self.orders.insert("",END,values=i)             
                conn.commit()
                conn.close()        
        except:
            messagebox.showerror("4ekokike")
    def fetchdataaa(self) :
        try:
            if str(self.workercombo.get())!= "":
                conn=mysql.connector.connect(
                host = "localhost",database="nader", 
                username ="root",
                password = "nader01227546543N")
                
                
           
                strh='select * from nader.workers where name = "{}"'.format(str(self.workercombo.get()))
                rowww= conn.cursor()
                rowww.execute(strh)
                rows=rowww.fetchall()
                if len(rows)!= 0 :
                    self.work.delete(*self.work.get_children())
                for i in rows :
                    self.work.insert("",END,values=i)
               
                conn.commit()
                conn.close()        
            
        except:
            messagebox.showerror("sasa")
    def modulateId(self,roe):
        self.rer = 1
        try:
                    strh="select id , ta from nader.{} order by ta".format(self.workercombo.get().strip())
                
                    roe.execute(strh)
                
                    row=roe.fetchall()
                    for i in row : 
                        st = 'update nader.{} set id = {} where ta = "{}"'.format(self.workercombo.get().strip(),self.rer,i[1])
                        roe.execute(st)
                        self.rer+=1
        except:
                    messagebox.showerror("خطــأ","ERROR")
    def medulatetot(self,roe): 
        self.rer = 1
        self.tr = 0 
        try:
                    strh="select id ,daa,kaa,haff,hass from nader.{} order by ta".format(self.workercombo.get().strip())
                
                    roe.execute(strh)
                
                    row=roe.fetchall()
                    for i in row :
                        st = 'update nader.{} set tot = daa + kaa + haff - hass - mad + {}, mot = tot where id = {} ;'.format(self.workercombo.get().strip(),self.tr,self.rer)
                    
                        roe.execute(st)
                  
                        self.tr += round(i[1]+i[2]+i[3]-i[4],2)
                        self.rer+=1
        except:
                    messagebox.showerror("خطــأ","hee")
    def delete(self):
        try :
                if self.workercombo.get() != "" : 
                    if self.key == False  :
                       messagebox.showwarning("خطأ", " اختـار اليوم من الجدول اولا") 
                    else :
                        if self.kaa.get()=='0' and self.haff.get()=='0' and self.daa.get()=='0' and self.hass.get()=='0' and self.mad.get()=='0':
                           messagebox.showwarning("خطـأ", "لم يتم ادخـال جميع البيانـات")
                        else :    
                           if self.workercombo.get() != "":
                               conn=mysql.connector.connect(
                                       host = "localhost",database="nader", 
                                       username ="root",
                                       password = "nader01227546543N")
                               mycursor = conn.cursor()

                               strt='delete from nader.{} where ta = "{}"'.format(self.workercombo.get().strip(),str(self.sel.get()))
                        
                               mycursor.execute(strt)
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
                if self.workercombo.get() != "": 
                    if self.key==False :
                       messagebox.showwarning("خطأ", " اختـار اليوم من الجدول اولا") 
                    else :
                        if self.kaa.get()=='0' and self.haff.get()=='0' and self.daa.get()=='0' and self.hass.get()=='0' and self.mad.get()=='0':
                           messagebox.showwarning("خطـأ", "لم يتم ادخـال جميع البيانـات")
                        else :    
                           if self.workercombo.get() != "":
                               conn=mysql.connector.connect(
                                       host = "localhost",database="nader", 
                                       username ="root",
                                       password = "nader01227546543N")
                               mycursor = conn.cursor()

                               strt='update nader.{} set daa = {},kaa={},haff={},hass={} , mad = {} where ta = "{}"'.format(self.workercombo.get().strip(),  round(0.7*float(self.daa.get()),2),round(0.8*float(self.kaa.get()),2),round(float(self.haff.get()),2),round(float(self.hass.get()),2),round(float(self.mad.get()),2),str(self.sel.get()))
                              
                               mycursor.execute(strt)
                               srt='select ta from nader.{} where ta = "{}"'.format(str(self.workercombo.get()),str(self.sel.get()))   
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
            if str(self.workercombo.get()) != "":
                cursor_row =self.orders.focus()
                content = self.orders.item(cursor_row)
                row= content['values']
                if len(row) !=0:
                    if self.key == False:
                        self.tt.set(self.sel.get())
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
        if self.workercombo.get() != "": 
            if self.name.get()=='' and self.idd.get()=='' and self.ideg.get()=='' and self.phon.get()=='':
               messagebox.showwarning("خطـأ", "لم يتم ادخـال جميع البيانـات")
            else :    
               if self.workercombo.get() != self.name.get() :
                       messagebox.showerror("خطأ","لا يمكـن تعديـل الاســم")
               else :
                    if len(self.ideg.get()) == 14 or self.ideg.get() == "0" :

                                if len(self.phon.get())==11 or len(self.phon.get())==10 or self.phon.get()== "0": 
                                    try:
                                            if self.keyy==False :
                                               messagebox.showwarning("خطأ", " اختـار المعلومات من الجدول اولا") 
                                            else :
                                                            if self.workercombo.get() != "":
                                                                conn=mysql.connector.connect(
                                        host = "localhost",database="nader", 
                                        username ="root",
                                        password = "nader01227546543N")
                                                                mycursor = conn.cursor()
                                                                strt='update nader.workers set  id = "{}",ideg= {},phone = {} where name = "{}"'.format(str(self.idd.get()),str(self.ideg.get()),str(self.phon.get()),str(self.workercombo.get()))
                                                          
                                                                mycursor.execute(strt)
                                                                # srt='select ta from nader.{} where ta = "{}"'.format(str(self.workercombo.get()),str(self.sel.get()))   
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
            if str(self.workercombo.get()) != "":
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