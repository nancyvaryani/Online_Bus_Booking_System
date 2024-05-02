from tkinter import*
from tkinter.messagebox import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
import sqlite3
mycon=sqlite3.connect("pro_database.db")
mycur=mycon.cursor()
class t:
   def __init__(self ):
                                 bkgref_id=0
                                 name=""
                                 phn=""
                                 gender=""
                                 num_seats=0
                                 aged=0
                                 travel_date=""
                                 bkg_date=""
                                 boarding=""
                                 destin=""
                                 bus_id=0
                                 bus_op=""
                                 bfare=0
   def splash(self):
            def screen2(event):
               root.destroy()
               self.scr2()
            
            

            Label(root,image=bus).grid(row=0,column=1,padx=w//2.5)
            Label(root,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red').grid(row=1,column=1)
            Label(root,text='\n\n').grid(row=2,column=1)
            Label(root,text='Name : Nancy Varyani\n\nErno : 211b405\n\nMobile: 9988776655',fg='blue',font='bold').grid(row=3,column=1)
            Label(root,text='\n\n\n\n').grid(row=4,column=1)
            Label(root,text='Submitted to: Dr Mahesh Kumar',font='Arial 14 bold',bg='light blue',fg='red').grid(row=5,column=1)
            Label(root,text='Project Based Learning',fg='red').grid(row=6,column=1)
            
            root.bind("<KeyPress>",screen2)
            root.mainloop()
   def scr4(self):
      def screen2(event):
               root.destroy()
               self.scr2()
      
      root=Tk()

      h,w=root.winfo_screenheight(),root.winfo_screenwidth()
      root.geometry('%dx%d+0+0'%(w,h))

      fr=Frame(root)

      bus=PhotoImage(file='.\\Bus_for_project.png')
      photo=Label(fr,image=bus)
      heading=Label(fr,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red')
      Label(fr,text='BUS TICKET',font='bold').grid(row=2)
      photo.grid(row=0,padx=w//2.5)
      heading.grid(row=1,padx=w//2.5,pady=h//40)

      fr.grid(row=0,column=1,pady=h//20)
      
      frame=LabelFrame(root)
      Label(frame,text='Passengers : '+self.name,font='bold').grid(row=0,column=0)
      Label(frame,text='Gender :  '+self.gender,font='bold').grid(row=0,column=1)
      Label(frame,text='No of seats :'+str(self.num_seats),font='bold').grid(row=1,column=0)
      Label(frame,text='Phone Number= '+self.phn,font='bold').grid(row=1,column=1)
           
      Label(frame,text='Age : '+ str(self.aged),font='bold').grid(row=2,column=0)
      Label(frame,text='Fare Rs :  '+str(self.bfare ),font='bold').grid(row=2,column=1)
             
      Label(frame,text='Booking Ref : '+str(self.bkgref_id),font='bold').grid(row=3,column=0)
      Label(frame,text='Bus Operator: '+str(self.bus_op),font='bold').grid(row=3,column=1)
              
      Label(frame,text='Travel On : '+self.travel_date,font='bold').grid(row=4,column=0)
      Label(frame,text='Booked On :  '+self.bkg_date,font='bold').grid(row=4,column=1)
      
      Label(frame,text='Boarding Point  : '+self.boarding,font='bold').grid(row=5,column=0)
      Label(frame,text='Destination  : '+self.destin,font='bold').grid(row=6,column=0)
      
      Label(frame,text='Total amount to be paid Rs '+str(self.bfare)+' at the time of boarding of bus ').grid(row=6,column=1)
      frame.grid(row=1,column=1)
      
      root.bind("<KeyPress>",screen2)
      
      root.mainloop()
   def scr5(self):
            def screen2(event):
               root.destroy()
               self.scr2()
      
            root=Tk()
            h,w=root.winfo_screenheight(),root.winfo_screenwidth()
            root.geometry('%dx%d+0+0'%(w,h))

            fr=Frame(root)

            bus=PhotoImage(file='.\\Bus_for_project.png')
            photo=Label(fr,image=bus)
            heading=Label(fr,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red')
            sec_hd=Label(fr,text='Check Your Booking ',font='Arial 14 bold',bg='pale green',fg='dark green')
            sec_hd.grid(row=2,pady=h//40)
            photo.grid(row=0,padx=w//2.5)
            heading.grid(row=1,padx=w//2.5,pady=h//40)

            fr.grid(row=0,column=1,pady=h//40)

            f=Frame(root)

            def cmd():
                  if pnumm.get() =='' :
                     showerror("","Enter a valid number")
                     return
                  elif (pnumm.get() is not None and len(pnumm.get())!=10):
                     showerror("","Ennter a valid mobile number ")
                  else:
                     qry='select bkgid from bkd where pnum=?'
                     mycur.execute(qry,(pnumm.get(),))
                     f=mycur.fetchone()
                  
                     if  f is None or f==():
                        showinfo("No Booking Found","would you like to book a seat now ? ")
                        root.bind("<KeyPress>",screen2)
                     else:
                        bkgin=max(f)
                        print(bkgin)
                        mycur.execute('select *  from bkd where bkgid=?',(bkgin,))
                        tickkk=mycur.fetchone()
                      
                        print(tickkk)
                        mycur.execute('Select name from operator,bus where opid=operid and busid=?',(tickkk[7],))
                        busop=mycur.fetchone()[0]
                        mycur.execute('Select station_name from route where sid=?',(tickkk[8],))
                        src_st=mycur.fetchone()[0]
                        mycur.execute('Select station_name from route where sid=?',(tickkk[9],))
                        dst_st=mycur.fetchone()[0]
                        self.name=tickkk[1]
                        self.gender=tickkk[3]
                        self.num_seats=tickkk[4]
                        self.phn=tickkk[2]
                        self.aged=tickkk[6]
                        self.bfare=tickkk[5]
                        self.bkgref_id=tickkk[0]
                        self.bus_op=busop
                        self.travel_date=tickkk[11]
                        self.bkg_date=tickkk[10]
                        self.boarding=src_st
                        self.destin=dst_st
                        frame=LabelFrame(root)
                        Label(frame,text='Passengers : '+self.name,font='bold').grid(row=0,column=0)
                        Label(frame,text='Gender :  '+self.gender,font='bold').grid(row=0,column=1)
                        Label(frame,text='No of seats :'+str(self.num_seats),font='bold').grid(row=1,column=0)
                        Label(frame,text='Phone Number= '+self.phn,font='bold').grid(row=1,column=1)
                             
                        Label(frame,text='Age : '+ str(self.aged),font='bold').grid(row=2,column=0)
                        Label(frame,text='Fare Rs :  '+str(self.bfare ),font='bold').grid(row=2,column=1)
                               
                        Label(frame,text='Booking Ref : '+str(self.bkgref_id),font='bold').grid(row=3,column=0)
                        Label(frame,text='Bus Operator: '+str(self.bus_op),font='bold').grid(row=3,column=1)
                                
                        Label(frame,text='Travel On : '+self.travel_date,font='bold').grid(row=4,column=0)
                        Label(frame,text='Booked On :  '+self.bkg_date,font='bold').grid(row=4,column=1)
                        
                        Label(frame,text='Boarding Point  : '+self.boarding,font='bold').grid(row=5,column=0)
                        Label(frame,text='Destination  : '+self.destin,font='bold').grid(row=6,column=0)
                        
                        Label(frame,text='Total amount to be paid Rs '+str(self.bfare)+' at the time of boarding of bus ').grid(row=6,column=1)
                        frame.grid(row=2,column=1)
                        root.bind("<KeyPress>",screen2)
                                
            Label(f,text='Enter your mobile number : ',font='Arial 14 bold').grid(row=0,column=0)
            pnumm=Entry(f,width=25)
            pnumm.grid(row=0,column=1)
            Button(f,text='Check Booking',font='Arial 14 bold',command=cmd).grid(row=0,column=2,padx=30)
            f.grid(row=1,column=1)
   def scr7(self):
      def screen6(event):
               root.destroy()
               self.scr6()
      root=Tk()
      h,w=root.winfo_screenheight(),root.winfo_screenwidth()
      root.geometry('%dx%d+0+0'%(w,h))
      bus=PhotoImage(file='.\\Bus_for_project.png')
      fr=Frame(root)
      
      bus=PhotoImage(file='.\\Bus_for_project.png')
      photo=Label(fr,image=bus)
      heading=Label(fr,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red')
      sec_hd=Label(fr,text='Add Bus Operator Details ',font='Arial 14 bold',fg='green')
      sec_hd.grid(row=2,pady=h//40)
      photo.grid(row=0,padx=w//2.5)
      heading.grid(row=1,padx=w//2.5,pady=h//40)

      fr.grid(row=0,column=1,pady=h//40)


      def addcmd():
         if ent1.get()=='' or ent2.get()=='' or ent3.get()=='' or ent4.get()=='' :
                     showerror('',"Add complete details")
         else:
           
                     Label(fr2,text=ent1.get()+'  '+ent2.get()+'  '+ent3.get()+'  '+ent4.get()).grid(row=1,column=3)
                     try:
                           mycur.execute('Insert into operator values(?,?,?,?)',(ent1.get(),ent2.get(),ent3.get(),ent4.get()))
                           mycon.commit()
                           showinfo('',"Details Added\nPress any key to Go Back")
                           root.bind("<KeyPress>",screen6)
                     except Exception:
                           showerror('',"Some issues in entering details \nTry once again")
                    
         root.bind("<KeyPress>",screen6)            


      fr2=Frame(root)
      t=Label(fr2,text='Operator Id ')
      t.grid(row=0,column=0)
      ent1=Entry(fr2)
      ent1.grid(row=0,column=1,padx=20)

      t=Label(fr2,text='Name ')
      t.grid(row=0,column=2)
      ent2=Entry(fr2)
      ent2.grid(row=0,column=3,padx=20)
         
      t=Label(fr2,text='Address ')
      t.grid(row=0,column=4)
      ent3=Entry(fr2)
      ent3.grid(row=0,column=5,padx=20)
         
      t=Label(fr2,text='Email ')
      t.grid(row=0,column=6)
      ent4=Entry(fr2)
      ent4.grid(row=0,column=7,padx=20)

      Button(fr2,text='ADD',bg='pale green',command=addcmd).grid(row=0,column=8,padx=20)   
      

      home=PhotoImage(file='.\\home.png')
      Label(fr2,image=home).grid(row=2,column=6,pady=30)

      fr2.grid(row=1,column=1,pady=h//40)

   def scr9(self):
      def screen6(event):
               root.destroy()
               self.scr6()
      root=Tk()
      h,w=root.winfo_screenheight(),root.winfo_screenwidth()
      root.geometry('%dx%d+0+0'%(w,h))
      fr=Frame(root)
      
      bus=PhotoImage(file='.\\Bus_for_project.png')
      photo=Label(fr,image=bus)
      heading=Label(fr,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red')
      sec_hd=Label(fr,text='Add Bus Route Details ',font='Arial 14 bold',fg='green')
      sec_hd.grid(row=2,pady=h//40)
      photo.grid(row=0,padx=w//2.5)
      heading.grid(row=1,padx=w//2.5,pady=h//40)

      fr.grid(row=0,column=1,pady=h//40)


      def addcmd():
         
         if ent1.get()==''  or ent2.get()=='' or ent3.get()=='':
                     showerror('',"Add complete details")
         else:
                     Label(fr2,text=ent1.get()+'  '+ent2.get()+'  '+ent3.get()).grid(row=1,column=3)
                     showinfo('',"Details Added\nPress any key to Go Back")
                     root.bind("<KeyPress>",screen6)
         
      fr2=Frame(root)
      t=Label(fr2,text='Route Id ')
      t.grid(row=0,column=0)
      ent1=Entry(fr2)
      ent1.grid(row=0,column=1,padx=20)

      t=Label(fr2,text='Station Name')
      t.grid(row=0,column=2)
      ent2=Entry(fr2)
      ent2.grid(row=0,column=3,padx=20)
         
      t=Label(fr2,text='Station Id ')
      t.grid(row=0,column=4)
      ent3=Entry(fr2)
      ent3.grid(row=0,column=5,padx=20)
         

      Button(fr2,text='ADD ROUTE',bg='pale green',command=addcmd).grid(row=0,column=6,padx=20)   
    

      home=PhotoImage(file='.\\home.png')
      Label(fr2,image=home).grid(row=2,column=7,pady=30)

      fr2.grid(row=1,column=1,pady=h//40)


   def scr8(self):
               def screen6(event):
                  root.destroy()
                  self.scr6()
                  
               root=Tk()
               h,w=root.winfo_screenheight(),root.winfo_screenwidth()
               root.geometry('%dx%d+0+0'%(w,h))
               bus=PhotoImage(file='.\\Bus_for_project.png')
                        
               fr=Frame(root)
               bus=PhotoImage(file='.\\Bus_for_project.png')
               photo=Label(fr,image=bus)
               heading=Label(fr,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red')
               sec_hd=Label(fr,text='Add Bus Details ',font='Arial 14 bold',fg='green')
               sec_hd.grid(row=2,pady=h//40)
               photo.grid(row=0,padx=w//2.5)
               heading.grid(row=1,padx=w//2.5,pady=h//40)

               fr.grid(row=0,column=1,pady=h//40)

               fr2=Frame(root)
               t=Label(fr2,text='Bus Id ')
               t.grid(row=0,column=0)
               ent1=Entry(fr2)
               ent1.grid(row=0,column=1,padx=10)

               typ=StringVar();
               typ.set('type')
               typee=['AC 2x2','AC 3x2','Non AC 3x2','Non AC 2x2','AC-Sleeper 2x2','Non AC-Sleeper 2x2']

               gen=OptionMenu(fr2,typ,*(typee)).grid(row=0,column=3,padx=20)
               t=Label(fr2,text='Bus Type ')
               t.grid(row=0,column=2)
                  
               t=Label(fr2,text='Capacity ')
               t.grid(row=0,column=4)
               ent3=Entry(fr2)
               ent3.grid(row=0,column=5,padx=10)
                  
               t=Label(fr2,text='Fare ')
               t.grid(row=0,column=6)
               ent4=Entry(fr2)
               ent4.grid(row=0,column=7,padx=10)

               t=Label(fr2,text='Operator Id ')
               t.grid(row=0,column=8)
               ent6=Entry(fr2)
               ent6.grid(row=0,column=9,padx=10)


               t=Label(fr2,text='Route Id ')
               t.grid(row=0,column=10)
               ent5=Entry(fr2)
               ent5.grid(row=0,column=11,padx=10)

               def add():
                  
                  if ent1.get()=='' or ent3.get()=='' or ent4.get()=='' or ent5.get()=='' or ent6.get()=='':
                     showerror('',"Add complete details")
                  else:
                        try:
                           
                           mycur.execute('Insert into bus values(?,?,?,?,?,?)',(ent1.get(),gen.get(),ent3.get(),ent4.get(),ent6.get(),ent5.get()))
                           mycon.commit()
                           showinfo('',"Details Added\nPress any key to Go Back")
                           root.bind("<KeyPress>",screen6)
                        except Exception:
                           showerror('',"Some issues in entering details \nTry once again")
                        root.bind("<KeyPress>",screen6)
                           
                     
                     
               Button(fr2,text='ADD BUS',bg='pale green',font='Arial 14',command=add).grid(row=2,column=4,padx=10)   
               

               home=PhotoImage(file='.\\home.png')
               Label(fr2,image=home).grid(row=2,column=7,pady=30)

               fr2.grid(row=1,column=1,pady=h//40)
               
   def scr10(self):
      def screen6(event):
                  root.destroy()
                  self.scr6()
      
      root=Tk()
      h,w=root.winfo_screenheight(),root.winfo_screenwidth()
      root.geometry('%dx%d+0+0'%(w,h))

      fr=Frame(root)

      bus=PhotoImage(file='.\\Bus_for_project.png')
      photo=Label(fr,image=bus)
      heading=Label(fr,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red')
      sec_hd=Label(fr,text='Add Bus Running Details ',font='Arial 14 bold',fg='green')
      sec_hd.grid(row=2,pady=h//40)
      photo.grid(row=0,padx=w//2.5)
      heading.grid(row=1,padx=w//2.5,pady=h//40)

      fr.grid(row=0,column=1,pady=h//40)


      def addcmd():
         if ent1.get()==''  or ent2.get()=='' or ent3.get()=='':
                     showerror('',"Add complete details")
         else:
            Label(fr2,text=ent1.get()+'  '+ent2.get()+'  '+ent3.get()).grid(row=1,column=3)
            try:
                           mycur.execute('Insert into route values(?,?,?)',(ent1.get(),ent2.get(),ent3.get()))
                           mycon.commit()
                           showinfo('',"Details Added\nPress any key to Go Back")
                           root.bind("<KeyPress>",screen6)
            except Exception:
                           showerror('',"Some issues in entering details \nTry once again")
            root.bind("<KeyPress>",screen6)
                     
                    
               
      fr2=Frame(root)
      t=Label(fr2,text='Bus Id ')
      t.grid(row=0,column=0)
      ent1=Entry(fr2)
      ent1.grid(row=0,column=1,padx=20)

      t=Label(fr2,text='Running Date')
      t.grid(row=0,column=2)
      ent2=Entry(fr2)
      ent2.grid(row=0,column=3,padx=20)
         
      t=Label(fr2,text='Seat Available ')
      t.grid(row=0,column=4)
      ent3=Entry(fr2)
      ent3.grid(row=0,column=5,padx=20)

      Button(fr2,text='ADD ROUTE',bg='pale green',command=addcmd).grid(row=0,column=6,padx=20)   
     
      

      home=PhotoImage(file='.\\home.png')
      Label(fr2,image=home).grid(row=2,column=7,pady=30)

      fr2.grid(row=1,column=1,pady=h//40)
      
   def scr6(self):
      def screen2(e=1):
               root.destroy()
               self.scr2()
      def screen7(e=1):
         root.destroy()
         self.scr7()
      def screen8(e=1):
         root.destroy()
         self.scr8()
      def screen9(e=1):
         root.destroy()
         self.scr9()
      def screen10(e=1):
         root.destroy()
         self.scr10()
      root=Tk()
     
      
      h,w=root.winfo_screenheight(),root.winfo_screenwidth()
      root.geometry('%dx%d+0+0'%(w,h))
      fr=Frame(root)
      bus=PhotoImage(file='.\\Bus_for_project.png')
      photo=Label(fr,image=bus)
      heading=Label(fr,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red')
      sec_hd=Label(fr,text='Add new details to database ',font='Arial 14 bold',bg='pale green',fg='dark green')
      sec_hd.grid(row=2,pady=h//40)
      photo.grid(row=0,padx=w//2.5)
      heading.grid(row=1,padx=w//2.5,pady=h//40)

      fr.grid(row=0,column=1,pady=h//40)

      nf=Frame(root)
      b1=Button(nf,text='New Operator',bg='pale green',command=screen7)
      b2=Button(nf,text='New Bus',bg='chocolate1',command=screen8)
      b3=Button(nf,text='New Route',bg='SteelBlue2',command=screen9)
      b4=Button(nf,text='New Run',bg='LightPink3',command=screen10)
      b1.grid(row=0,column=0,padx=30)
      b2.grid(row=0,column=1,padx=30)
      b3.grid(row=0,column=2,padx=30)
      b4.grid(row=0,column=3,padx=30)
      nf.grid(row=1,column=1,pady=h//40)
      
   def scr2(self):
      def screen3(e=1):
         root.destroy()
         self.scr3()
      def scr5_chk(e=1):
         root.destroy()
         self.scr5()
      def screen6(e=1):
         root.destroy()
         self.scr6()
         
      root=Tk()
      h,w=root.winfo_screenheight(),root.winfo_screenwidth()
      root.geometry('%dx%d+0+0'%(w,h))


      bus=PhotoImage(file='.\\Bus_for_project.png')
      photo=Label(root,image=bus)
      heading=Label(root,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red')

      photo.grid(row=0,column=0,padx=w//2.5,columnspan=5)

      heading.grid(row=1,column=0,columnspan=5)

      l=Label(root,text='\n'*4)
      l.grid(row=2)

      b1=Button(root,text='Seat Booking',font='bold',bg='pale green',command=screen3)
      b2=Button(root,text='Check Booked Seat',font='bold',bg='lime green',command=scr5_chk)
      b3=Button(root,text='Add Bus Details',font='bold',bg='dark green',command=screen6)

      l=Label(root,text='\n')
      l.grid(row=4)
      l1=Label(root,text='For Admin Only',fg='red')
      b1.grid(row=3,column=0,columnspan=3)

      b2.grid(row=3,column=1,columnspan=3)

      b3.grid(row=3,column=2,columnspan=3)

      l1.grid(row=5,column=2,columnspan=3)

   def scr3(self):
         def screen4(e=1):
            root.destroy()
            self.scr4()
         
         
         root=Tk()
         h,w=root.winfo_screenheight(),root.winfo_screenwidth()
         root.geometry('%dx%d+0+0'%(w,h))

         fr=Frame(root)

         bus=PhotoImage(file='.\\Bus_for_project.png')
         photo=Label(fr,image=bus)
         heading=Label(fr,text='Online Bus Booking System',font='Arial 14 bold',bg='light blue',fg='red')

         photo.grid(row=0,padx=w//2.5)
         heading.grid(row=1,padx=w//2.5)

         sec_hd=Label(fr,text='Enter Journey Details ',font='Arial 14 bold',bg='pale green',fg='dark green')
         sec_hd.grid(row=2,column=0,pady=h//60)

         fr.grid(row=0,column=1)

                   

         def but():
               if date.get() == "" or src.get()=='' or dst.get() =='':
                  showerror(' ',"Enter correct details ")
                  return
               
               else:
                  mycur.execute('select sid from route where station_name =? ',(src.get(),))
                  srt=mycur.fetchone()
                  mycur.execute('select sid from route where station_name =? ',(dst.get(),))
                  ds=mycur.fetchone()
                  
                  if srt==() or ds==():
                     showinfo('',"This station is not available ")
                  elif srt is None or ds is None:
                        showinfo('',"The route is not available")
                  else:
                     src_id=srt[0]
                     dst_id=ds[0]
                     print(src_id,dst_id)
                     bus_on_date='Select bid from runs where rundate = ?'
                     mycur.execute(bus_on_date,(date.get(),))
                     bus_on_date=mycur.fetchall()
                     if bus_on_date==[]:
                        showinfo("-","No bus on this date, Enter another ")
                        print(bus_on_date)
                        
                     else:
                        mycur.execute('select r1.rid from route r1, route r2 where r1.station_name=? and r2.station_name =? and r1.rid =r2.rid',(src.get(),dst.get()))
                        route = mycur.fetchall()
                        if route==[]:
                           showinfo('',"This route is not available \nTry entering another")
                        else:
                           qry='''select busid,routeid, name,type,fare from bus,runs ,operator where rundate =? and busid=bid and operid=opid
                                and routeid in(select r1.rid from route r1, route r2 where r1.station_name=? and r2.station_name =? and r1.rid =r2.rid) ;'''
                           mycur.execute(qry,(date.get(),src.get(),dst.get()))
                           bus_list=mycur.fetchall()
                           
                           

                           
                           Label (fram,text='Select Bus',fg='green').grid(row=5,column=0,padx=50)
                           Label (fram,text='Operator',fg='green').grid(row=5,column=1,padx=50)
                           Label (fram,text='Bus Type',fg='green').grid(row=5,column=2,padx=50)
                           Label (fram,text='Availability',fg='green').grid(row=5,column=3,padx=50)
                           Label (fram,text='Fare',fg='green').grid(row=5,column=4,padx=50)
                           Label(fram,text='\n').grid(row=6)
                           def cmd():
                              selected_bus_id=radio.get()
                              mycur.execute('select busid from bus where routeid=?',(selected_bus_id,))
                              
                              selected_route=mycur.fetchone()[0]
                              newfr=Frame(root)
                              Label(newfr,text='Fill Passenger details to book the bus ticket',font='Arial 14 bold',bg='light blue',fg='red').grid(row=0)
                              newfr.grid(row=6,column=1,padx=70,pady=h//80)
                              t=Label(fr2,text='Name ')
                              t.grid(row=9,column=0)
                              pname=Entry(fr2)
                              pname.grid(row=9,column=1,padx=20)

                              gender=StringVar();
                              gender.set('Male')
                              gen=['Male','Female','Third Gender']
                              Label(fr2,text='Gender').grid(row=9,column=2)
                              gen=OptionMenu(fr2,gender,*(gen)).grid(row=9,column=3,padx=20)

                              t=Label(fr2,text='No. of seats ')
                              t.grid(row=9,column=4)
                              sea=Entry(fr2,width=5)
                              sea.grid(row=9,column=5,padx=20)
                              
                              t=Label(fr2,text='Mobile No ')
                              t.grid(row=9,column=6)
                              mob=Entry(fr2)
                              
                              mob.grid(row=9,column=7,padx=20)
                              
                              t=Label(fr2,text='Age ')
                              t.grid(row=9,column=8)
                              age=Entry(fr2,width=5)
                              
                              age.grid(row=9,column=9,padx=20)

                              def bookseat(busid,fare):
                                    bus_fare=fare*int(sea.get())
                                    qry='select bkgid from bkd'
                                    mycur.execute(qry)
                                    f=mycur.fetchall()
                                    if f==[]:
                                       bkgin=1
                                    else :
                                          bkgin=max(f)[0]+1
                                    print(bkgin)
                                    q2='insert into bkd values (?,?,?,?,?,?,?,?,?,?,?,?);'
                                    dq='select date();'
                                    mycur.execute(dq)
                                    cdate=mycur.fetchone()[0]

                                    val=(bkgin,pname.get(),mob.get(),gender.get(),sea.get(),bus_fare,age.get(),selected_route,src_id,dst_id,cdate,date.get())
                                    print(val)
                                    mycur.execute('Select name from operator,bus where opid=operid and busid=?',(selected_bus_id,))
                                    busop=mycur.fetchone()[0]
                                    self.bkgref_id=bkgin
                                    self.name=pname.get()
                                    self.phn=mob.get()
                                    self.gender=gender.get()
                                    self.num_seats=sea.get()
                                    self.aged=age.get()
                                    self.travel_date=date.get()
                                    self.bkg_date=cdate
                                    self.boarding=src.get()
                                    self.destin=dst.get()
                                    self.bus_id=selected_bus_id
                                    self.bus_op=busop
                                    self.bfare=bus_fare
                                    
                                    mycur.execute(q2,val)
                                    mycon.commit()
                                    print(mycur.fetchall())
                                    
                                    mycur.execute('update runs set seats=seats-? where bid =? and rundate =?',(int(sea.get()),selected_bus_id,date.get()))
                                    mycon.commit()
                                    print("updated *_*")
                                    screen4()
                                    showinfo("","Seat Booked")
                                 
                              def bkbtn():
                                 if pname.get()=='' or gender.get()=='' or sea.get()==0 or mob.get=='' or age.get() ==0:
                                    showerror('incomplete details',"Please fill the full details")
                                 else:
                                       mycur.execute("Select fare from bus where busid=?",(selected_bus_id,))
                                       fare=mycur.fetchone()[0]
                                       mycur.execute('select seats from runs where bid=?',(selected_bus_id,))
                                       avail_seats=mycur.fetchone()[0]
                                       if int(sea.get())>avail_seats:
                                             showerror('Bus full',"Seats not available at this route")
                                       else:
                                          if int (age.get())>120:
                                             showinfo("","Enter a valid age of passenger")
                                          else:
                                             if mob.get !="" and len(mob.get())!=10:
                                              showerror('Incorrect details',"Enter a valid mobilr number")
                                             else:
                                                ch=askyesno("Fare Confirm" ,"Total amount to be paid Rs "+str(fare*int(sea.get())))
                                                if ch:
                                                   bookseat(selected_bus_id,fare)
                                                   
                                       
                              Button(fr2,text='Book Seat',bg='pale green',command=bkbtn).grid(row=9,column=10,padx=20)
                           v=IntVar()
                           radio=IntVar()
                           for i in range(0,len(bus_list)):
                              bus_id=bus_list[i][0]
                              mycur.execute('select seats from runs where bid=?',(bus_id,))
                              avail_seats=mycur.fetchone()[0]
                              
                              
                              Radiobutton(fram,text='Bus '+str(bus_id),bg='light blue',variable=v,value=bus_id,indicator=0).grid(row=7+i,column=0)
                              Label (fram,text=bus_list[i][2],fg='blue').grid(row=7+i,column=1)
                              Label (fram,text=bus_list[i][3],fg='blue').grid(row=7+i,column=2)
                              Label (fram,text=avail_seats,fg='blue').grid(row=7+i,column=3)
                              Label (fram,text=bus_list[i][4],fg='blue').grid(row=7+i,column=4)
                              
                              Radiobutton(fram,text='Proceed to Book',bg='pale green',variable=radio,value=bus_id,command=cmd,indicator=0).grid(row=7+i,column=5,padx=70)
                              Label(fram,text='\n').grid(row=8+i)
                          
                           
         fra=Frame(root)

         t=Label(fra,text='To  ')
         t.grid(row=4,column=0)

         src=Entry(fra)
         src.grid(row=4,column=1)

         t=Label(fra,text='  From  ')
         t.grid(row=4,column=2)

         dst=Entry(fra)
         dst.grid(row=4,column=3)

         t=Label(fra,text='  Journey Date  ')
         t.grid(row=4,column=4)

         date=Entry(fra)
         date.grid(row=4,column=5)

            
         but=Button(fra,text='Show Bus',bg='medium sea green',command=but)
         but.grid(row=4,column=6,padx=20)


         home=PhotoImage(file='.\\home.png')
         Label(fra,image=home).grid(row=4,column=7)

         fra.grid(row=4,column=1,pady=h//40)
         fram=Frame(root)
         fram.grid(row=5,column=1)
         fr2=Frame(root)
         fr2.grid(row=7,column=1,pady=h//50)

t1=t()
t1.splash()

