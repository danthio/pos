import tkinter as tk
import math
from tkinter import filedialog
from PIL import Image,ImageTk,ImageEnhance
import sqlite3 as db

import os
import time

from tkinter import ttk

import datetime


profileid=0

showp=()
dshowp=()
pst=0




"""
dbuser=db.connect('data/users.db')
cur=dbuser.cursor()
cur.execute("UPDATE user SET admin='"+str(1)+"' WHERE user_id="+str(1)+" ")

dbuser.commit()



dbuser=db.connect('data/users.db')
cur=dbuser.cursor()


cur.execute("SELECT * FROM user")
rows=cur.fetchall()


for row in rows:
	print(row)"""

start_time=()
inve=0


def login(e):

	global intro,un,pw,lvar,state,dvar,dvar2,dashb_state,main2
	global cal_year,cal_month,cal_day,daten,profileid,admin_st1,admin_st2_1,admin_st2_2,myp,mypv,myp3
	global start_time,inve,pst,sss
	global fff,vbar1,cart8,cart_array

	x_,y_=(wd/2)-350/2,(ht-200)/2

	if x_+150+168-10+10-5<=e.x<=x_+150+168-10+10-5+29:
		if y_+30-2+50<=e.y<=y_+30-2+50+29:
			

			if pst==0:
				pst=1
			elif pst==1:
				pst=0

			show()

	

	if x_+85<=e.x<=x_+265:
		if y_+150<=e.y<=y_+180:




			dbuser=db.connect('data/users.db')
			cur=dbuser.cursor()

			cur.execute("SELECT * FROM user")
			rows=cur.fetchall()

			for row in rows:

				uname=row[1]
				passw=row[5]

				lcon=0



				if un.get()==uname and pw.get()==passw:
					pst=0
					cart_array=[]
					cart__()


					lcon=1

					myp=[]

					for i in row:
						myp.append(i)
					profileid=row[0]
					admin_st1=row[-1]
					admin_st2_1=row[-1]

					myp3=[row[1],row[2],row[3],row[-2]]

					un.place_forget()
					pw.place_forget()

					un.delete(0,tk.END)
					pw.delete(0,tk.END)

					intro.place_forget()

					state="sell_items"

					dashb_state="sell_items"

					main2["scrollregion"]=(0,0,wd,ht-50)

					dvar=2
					dvar2=1
					dx=0

					draw_dashb()

					draw_main1()

					vbar1.pack_forget()
					main2.pack_forget()
					fff.pack_forget()
					main2.pack(side=tk.LEFT)

					vbar1.pack(side=tk.LEFT,fill=tk.Y)
					fff.pack(side=tk.LEFT)

					now=datetime.datetime.now()
					yy=now.year
					mm=now.month
					dd=now.day
					daten=str(dd)+"-"+str(mm)+"-"+str(yy)

					cal_year=int(yy)
					cal_month=int(mm)
					cal_day=int(dd)

					draw_cal()

					draw_sellitems()
					

					lvar=1
				if lcon==0:
					inve=1
					start_time=time.time()


inv1,inv2,inv3,inv4,inv_=(),(),(),(),0
def invalide():

	global start_time,inve,inv1,inv2,inv3,inv4,intro,wd,inv_,un,pw,pst


	if inve==1:


		x_,y_=(wd/2)-350/2,(ht-200)/2

		if inv_==0:

			un.delete(0,tk.END)
			pw.delete(0,tk.END)

			un.focus_set()
			pst=0
			show()

			inv1=intro.create_rectangle(x_+(350/2)-70,y_+230-30+10, x_+(350/2)+70,y_+230-30+10+30,fill="#fa677f",outline="#fa677f")
			inv2=intro.create_oval(x_+(350/2)-70-15,y_+230-30+10, x_+(350/2)-70+15,y_+230-30+10+30,fill="#fa677f",outline="#fa677f")
			inv3=intro.create_oval(x_+(350/2)+70-15,y_+230-30+10, x_+(350/2)+70+15,y_+230-30+10+30,fill="#fa677f",outline="#fa677f")
			inv4=intro.create_text(x_+(350/2),y_+230-30+10+15,text="Invalid Entry",fill="#000000",font=("FreeMono",13),
				anchor="c")
			inv_=1


		if time.time()>start_time+2:
			intro.delete(inv1)
			intro.delete(inv2)
			intro.delete(inv3)
			intro.delete(inv4)

			inve=0

			inv_=0



	root.after(1,invalide)












root=tk.Tk()

wd=root.winfo_screenwidth()-15
ht=root.winfo_screenheight()-75


root.resizable(0,0)
root.title("HPOS")
root.geometry(str(wd)+"x"+str(ht)+"+0+0")
#root.wm_attributes("-topmost",1)


########################

def main1_commands(e):
	global dvar,dvar2,dashb_state,main2,as_im,as_image,ax,ay,intro,lvar,si_con,ms_con
	global si_quantity,psoldat,si_desc,as_n,as_bp,as_sp,as_q,as_de,rr_,searche,cart,cal_con,wd,cartframe,cart_array
	global ascon2,as_image,ascon,uns,ems,cons,pss,userframe,barc,pst

			

	if wd-20-25<=e.x<=wd-20:
		if 10<=e.y<=35:



			ascon2=0
			as_image=""
			ascon=0
			dvar=0
			dvar2=1

			barc=[]



			uns,ems,cons,pss

			uns.place_forget()
			ems.place_forget()
			cons.place_forget()
			pss.place_forget()

			userframe.place_forget()


			cartframe.place_forget()
			cart_array=[]

			si_quantity.place_forget()
			psoldat.place_forget()
			si_desc.place_forget()
			cart.place_forget()
			cart_array=[]

			as_n.place_forget()
			as_bp.place_forget()
			as_sp.place_forget()
			as_q.place_forget()
			as_de.place_forget()

			rr_.place_forget()

			searche.place_forget()

			searche.delete(0,tk.END)


			x_,y_=(wd/2)-350/2,(ht-200)/2
			lvar=0
			searche.place_forget()
			intro.place(in_=root,x=0,y=0)
			un.place(in_=root,x=x_+150-10,y=y_+30)
			pw.place(in_=root,x=x_+150-10,y=y_+30+50)
			pst=0
			show()

			cal.place_forget()


			ms_con=0
			si_con=0

			un.focus_set()

	if dashb_state=="reports":




		x_=90+(wd-90-1020)/2


		if x_<=e.x<=x_+30:
			if 10<=e.y<=40:

				if cal_con==0:
					cal.place(in_=root,x=x_+40,y=40)
					cal_con=1

				elif cal_con==1:

					cal.place_forget()
					cal_con=0

def _on_mousewheel(e):
	global main2,dashb_state,si_con,ms_con,yvar,ht,cartc,yvar2,yvar2,cartc,userc,yvar3,ycart,cart8,mot

	if dashb_state=="sell_items" and si_con==0 and yvar>ht-50 and mot==1:
		main2.yview_scroll(int(-1*(e.delta/120)), "units")



	if dashb_state=="stock" and ms_con==0 and yvar>ht-50:
		main2.yview_scroll(int(-1*(e.delta/120)), "units")


	if dashb_state=="reports" and yvar>ht-50:
		main2.yview_scroll(int(-1*(e.delta/120)), "units")

	if dashb_state=="profiles" and yvar3>368:
		userc.yview_scroll(int(-1*(e.delta/120)), "units")


	if dashb_state=="sell_items" and si_con==0 and ycart>ht-50-30-130 and mot==2 :
		cart8.yview_scroll(int(-1*(e.delta/120)), "units")

		cart_border(0)



def main2_commands(e):
	global file_path,as_image,main2,as_im,ascon,ax,ay,ascon2,sellarray, si_con,seli, msarray,ms_con
	global as_n,as_bp,as_sp,as_q,as_de,msimage,msi,msf,mscon,mscon2,vbar1,cal_con,cal,cart_array,cv,dashb
	global cartframe,ht,wd
	global prof_st,admin_st1,admin_st2_1,admin_st2_2,prof0,prof1,profileid,myp2,myp3,mypv,myp,prof2
	global userframe,userc,barc,bc,pst,sss2,showp,dshowp,pss,cons,ems,uns,fff

	global cart5,cart8,cart7,cartq,cart3,cvbar




	if dashb_state=="profiles":

		x_,y_=90+(wd-800-90)/2,((ht-50)-500)/2

		
		if x_+417<=e.x<=x_+417+29:
			if y_+293<=e.y<=y_+293+29:

				if prof_st==0:
					myp3=[uns.get(),ems.get(),cons.get(),pss.get()]
				elif prof_st==1:
					myp2=[uns.get(),ems.get(),cons.get(),pss.get()]


				main2.delete(sss2)


				if pst==0:
					pst=1
				elif pst==1:
					pst=0

				av=60

				if pst==0:
					showp=ImageTk.PhotoImage(file="data/show.png")

					sss2=main2.create_image(x_+171+164+4+55-40+53+10,y_+100-10-4+av*3+10-20+37,image=showp,anchor="nw")
					pss["show"]="*"
				elif pst==1:
					dshowp=ImageTk.PhotoImage(file="data/dshow.png")

					sss2=main2.create_image(x_+171+164+4+55-40+53+10,y_+100-10-4+av*3+10-20+37,image=dshowp,anchor="nw")
					pss["show"]=""





				return

		if x_+20<=e.x<=x_+20+140:
			if y_+20<=e.y<=y_+45:
				prof_st=0
				prof2=0
				pst=0


				dbuser=db.connect('data/users.db')
				cur=dbuser.cursor()

				cur.execute("SELECT * FROM user WHERE user_id="+str(myp[0])+" ")
				rows=cur.fetchall()


				for row in rows:

					myp3=[row[1],row[2],row[3],row[-2]]

				admin_st2_1=myp[-1]
				draw_profiles()

				userframe.place_forget()


				return

		if x_+20+140+2<=e.x<=x_+20+140+140+2:
			if y_+20<=e.y<=y_+45:
				pst=0

				userframe.place_forget()

				prof1=""
				prof_st=1
				admin_st2_2=0
				draw_profiles()

				myp2=[]

				return

		if x_+20+140+2+2+140<=e.x<=x_+20+140+140+2+140+2:
			if y_+20<=e.y<=y_+45:

				prof_st=2
				userc["scrollregion"]=(0,0,620+60,368)
				draw_profiles()

				return




		if x_+590-50+55<=e.x<=x_+677-50+55:
			if y_+110+20+37-4<=e.y<=y_+130+20+37-4:
				#add image

				if prof_st==1:
					if myp[-1]==0:
						return

				msf2=filedialog.askopenfilename()

				e=msf2.split(".")[-1]

				if not e=="jpg":
					im = Image.open(msf2)

					# converting to jpg
					im = im.convert("RGB")	
					im.save("data/settv.jpg")	
					msf2="data/settv.jpg"



				im=Image.open(msf2)

				x,y=im.size

				if x>y:
					xv=int((x-y)/2)

					im=im.crop((xv,0,x-xv,y))
				if y>x:
					yv=int((y-x)/2)

					im=im.crop((0,yv,x,y-yv))

				im=im.resize((120,120))

				im.save("data/setti.jpg")

				if prof_st==0:
					myp3=[uns.get(),ems.get(),cons.get(),pss.get()]

					prof0=ImageTk.PhotoImage(file="data/setti.jpg")
					prof2=1




				if prof_st==1:
					myp2=[uns.get(),ems.get(),cons.get(),pss.get()]

					prof1=ImageTk.PhotoImage(file="data/setti.jpg")
				

				draw_profiles()

				return

		if x_+310<=e.x<=x_+490:
			if y_+440<=e.y<=y_+470:
				#save

				conp=0
				if prof_st==1:
					if myp[-1]==0:
						return

				name=uns.get()
				email=ems.get()
				contact=cons.get()
				pw=pss.get()

				if name=="" or email=="" or contact=="" or pw=="":
					message(main2,90+(wd-800-90)/2+400,(ht-50)/2+250+20,0,"Fill all details!")
					return


				dbuser=db.connect('data/users.db')
				cur=dbuser.cursor()



				if prof_st==1:
					cur.execute("SELECT MAX(user_id) FROM user")
					rows=cur.fetchall()

					v=0
					for row in rows:
						v=row[0]
					if v==None:
						v=1
					else:
						v+=1


					if prof1=="":
						pic=0


					else:
						pic=1

						im=Image.open("data/setti.jpg")
						im.save("Images/pp_"+str(v)+"l.jpg")

						im=im.resize((40,40))
						im.save("Images/pp_"+str(v)+"s.jpg")




					cur.execute("INSERT INTO 	user VALUES("+str(v)+",'"+name+"','"+str(email)+"','"+str(contact)+"',"+str(pic)+",'"+str(pw)+"',"+str(admin_st2_2)+")")

					dbuser.commit()

					prof1=""
					myp2=[]

					conp=1
					
				elif prof_st==0:
					pic=myp[-3]

					if prof0=="":
						if prof2==1:
							pic=0
							if myp[4]==1:

								f="Images"
								dir_=os.listdir(f)




								for a in dir_:
									if a=="pp_"+str(myp[0])+"l.jpg":
										os.remove("Images/"+"pp_"+str(myp[0])+"l.jpg")				

									if a=="pp_"+str(myp[0])+"s.jpg":
										os.remove("Images/"+"pp_"+str(myp[0])+"s.jpg")
							myp[4]=0



					else:
						pic=1
						




						if myp[4]==1:

							f="Images"
							dir_=os.listdir(f)




							for a in dir_:
								if a=="pp_"+str(myp[0])+"l.jpg":
									os.remove("Images/"+"pp_"+str(myp[0])+"l.jpg")				

								if a=="pp_"+str(myp[0])+"s.jpg":
									os.remove("Images/"+"pp_"+str(myp[0])+"s.jpg")

						im=Image.open("data/setti.jpg")
						im.save("Images/pp_"+str(myp[0])+"l.jpg")

						im=im.resize((40,40))
						im.save("Images/pp_"+str(myp[0])+"s.jpg")
						
						myp[4]=1



					cur.execute("UPDATE user SET name='"+str(name)+"' WHERE user_id="+str(profileid)+" ")
					cur.execute("UPDATE user SET email='"+str(email)+"' WHERE user_id="+str(profileid)+"  ")
					cur.execute("UPDATE user SET contact='"+str(contact)+"' WHERE user_id="+str(profileid)+" ")
					cur.execute("UPDATE user SET pic="+str(pic)+" WHERE user_id="+str(profileid)+" ")
					cur.execute("UPDATE user SET password='"+str(pw)+"' WHERE user_id="+str(profileid)+" ")	
					cur.execute("UPDATE user SET admin='"+str(admin_st2_1)+"' WHERE user_id="+str(profileid)+" ")	

					dbuser.commit()
					prof2=0
					prof0=""

					cur.execute("SELECT * FROM user WHERE user_id="+str(myp[0])+" ")
					rows=cur.fetchall()

					myp=[]

					for row in rows:
						for i in row:
							myp.append(i)

						myp3=[row[1],row[2],row[3],row[-2]]

					draw_main1()

					conp=1

				draw_profiles()
				draw_dashb()

				message(main2,90+(wd-800-90)/2+400,(ht-50)/2+250+20,1,"User details saved!")

				return

		if x_+140+55-40<=e.x<=x_+190+55-40:
			if y_+387.5-30-20+37<=e.y<=y_+412.5-30-20+37:
				#admin
				if prof_st==1:
					if myp[-1]==0:
						return


				if admin_st1==1:

					if prof_st==0:
						myp3=[uns.get(),ems.get(),cons.get(),pss.get()]
						if admin_st2_1==0:
							admin_st2_1=1
						elif admin_st2_1==1:
							admin_st2_1=0
					if prof_st==1:

						myp2=[uns.get(),ems.get(),cons.get(),pss.get()]
						if admin_st2_2==0:
							admin_st2_2=1
						elif admin_st2_2==1:
							admin_st2_2=0

					draw_profiles()
					return



		cx,cy=x_+582.5-50+55,y_+162.5+20+37-4

		r=math.sqrt((e.x-cx)**2 + (e.y-cy)**2)

		if r<=12.5:

			if prof_st==1:
				if myp[-1]==0:
					return

			if prof_st==0:
				myp3=[uns.get(),ems.get(),cons.get(),pss.get()]
				prof0=""
				prof2=1
			if prof_st==1:
				myp2=[uns.get(),ems.get(),cons.get(),pss.get()]
				prof1=""		
			draw_profiles()
			
			return



	elif dashb_state=="stock":

		if myp[-1]==0:
			return

		y=main2.canvasy(e.y)
		yy=main2.canvasy(0)

		for v in msarray:

			if v[1]<=e.x<=v[3]:
				if v[2]<=y<=v[4]:
					

					if ms_con==0:
						ms_con=1
						seli=v[0]
						draw_stock()
						return



		x1,y1=90+(wd-90-800)/2,((ht-50)-500)/2+main2.canvasy(0)

		if x1+260<=e.x<=x1+340:
			if y1+390<=y<=y1+420:
				barc=[]
				main2.delete(bc)
				bc=main2.create_text(x1+30+60+10+30-20,y1+20+400-15,text=str(len(barc)), fill="#000000",font=("FreeMono",13),anchor="w")

				return

		cx,cy=x1+785-5+40,y1+15-2.5

		r=math.sqrt((e.x-cx)**2 + (y-cy)**2)

		if r<=12.5:
			ms_con=0
			draw_stock()
			vbar1.pack_forget()
			main2.pack_forget()

			vbar1.pack(side=tk.RIGHT,fill=tk.Y)
			main2.pack(side=tk.LEFT)
			as_n.place_forget()
			as_bp.place_forget()
			as_sp.place_forget()
			as_de.place_forget()
			as_q.place_forget()

			msimage=""

			return

		if x1+135<=e.x<=x1+265:
			if y1+460<=y<=y1+490:

				#as_n,as_bp,as_sp,as_q,as_de


				n=as_n.get()
				bp=as_bp.get()
				sp=as_sp.get()
				q=as_q.get()
				de=as_de.get(0.0,tk.END)


				de=de.split("\n")[0]

				dbstock=db.connect('data/stock.db')
				cur=dbstock.cursor()

				cur.execute("UPDATE items SET name='"+str(n)+"' WHERE items_id="+str(seli)+" ")
				cur.execute("UPDATE items SET bp="+str(bp)+" WHERE items_id="+str(seli)+"  ")
				cur.execute("UPDATE items SET sp="+str(sp)+" WHERE items_id="+str(seli)+" ")
				cur.execute("UPDATE items SET quantity="+str(q)+" WHERE items_id="+str(seli)+" ")
				cur.execute("UPDATE items SET description='"+str(de)+"' WHERE items_id="+str(seli)+" ")	

				dbstock.commit()			




				dbstock=db.connect('data/stock.db')
				cur=dbstock.cursor()

				cur.execute("SELECT * FROM items WHERE items_id="+str(seli)+"")

				rows=cur.fetchall()	

				for row in rows:
					pic=row[6]

				if pic==1 and msimage=="":

					f="Images"
					dir_=os.listdir(f)




					for a in dir_:
						if a.split(".")[0]==str(seli):
							ext=a.split(".")[-1]


							if os.path.isfile("Images/"+a):
								os.remove("Images/"+a)

							ff="Images/"+str(seli)+"_s."+ext
							if os.path.isfile(ff):
								os.remove(ff)    							



					cur.execute("UPDATE items SET picture=0 WHERE items_id="+str(seli)+" ")
					dbstock.commit()

				elif pic==1:
					if not msimage=="":
						if mscon2==1:




							f="Images"
							dir_=os.listdir(f)





							for a in dir_:
								if a.split(".")[0]==str(seli):
									ext=a.split(".")[-1]


									if os.path.isfile("Images/"+a):
										os.remove("Images/"+a)

									ff="Images/"+str(seli)+"_s."+ext
									if os.path.isfile(ff):
										os.remove(ff)    							


							im=Image.open(msf)
							im.save("Images/"+str(seli)+"."+msf.split(".")[1])


							x,y=im.size





							if (x/y)>(150/100):
								bx=x-(x*((150/100)/(x/y) ) )
								im=im.crop((bx,0,x-bx,y))
								im=im.resize((150,100))
								im.save("Images/"+str(seli)+"_s."+msf.split(".")[1])
								

							elif (x/y)<(150/100):
								by=(y-(y*((x/y)/(150/100))  ))/2

								im=im.crop((0,by,x,y-by))
								im=im.resize((150,100))
								im.save("Images/"+str(seli)+"_s."+msf.split(".")[1])
								
							elif (x/y)==(1.5):
								im=im.resize((150,100))
								im.save("Images/"+str(seli)+"_s."+msf.split(".")[1])
								


				elif pic==0:
					if not msimage=="":
						dbstock=db.connect('data/stock.db')
						cur=dbstock.cursor()

						cur.execute("UPDATE items SET picture=1 WHERE items_id="+str(seli)+" ")
						dbstock.commit()	


						im=Image.open(msf)
						im.save("Images/"+str(seli)+"."+msf.split(".")[1])


						x,y=im.size






						if (x/y)>(150/100):
							bx=x-(x*((150/100)/(x/y) ) )
							im=im.crop((bx,0,x-bx,y))
							im=im.resize((150,100))
							im.save("Images/"+str(seli)+"_s."+msf.split(".")[1])
							

						elif (x/y)<(150/100):
							by=(y-(y*((x/y)/(150/100))  ))/2

							im=im.crop((0,by,x,y-by))
							im=im.resize((150,100))
							im.save("Images/"+str(seli)+"_s."+msf.split(".")[1])
							
						elif (x/y)==(1.5):
							im=im.resize((150,100))
							im.save("Images/"+str(seli)+"_s."+msf.split(".")[1])
							




				vbar1.pack_forget()
				main2.pack_forget()

				vbar1.pack(side=tk.RIGHT,fill=tk.Y)
				main2.pack(side=tk.LEFT)

				ms_con=0



				as_n.delete(0,tk.END)
				as_bp.delete(0,tk.END)
				as_sp.delete(0,tk.END)
				as_q.delete(0,tk.END)
				as_de.delete(0.0,tk.END)

				as_n.place_forget()
				as_bp.place_forget()
				as_sp.place_forget()
				as_q.place_forget()
				as_de.place_forget()

				draw_stock()
				main2.focus_set()

				mscon2=0

				msf=""
				msimage=""

				message(main2,90+(wd-800-90)/2+400,main2.canvasy((ht-50)/2+250+20),1,"Details saved!")
				return



		if x1+535<=e.x<=x1+665:
			if y1+460<=y<=y1+490:





				dbstock=db.connect('data/stock.db')
				cur=dbstock.cursor()

				cur.execute("SELECT * FROM items WHERE items_id="+str(seli)+"")

				rows=cur.fetchall()	

				for row in rows:
					pic=row[6]



				if pic==1:

					f="Images"
					dir_=os.listdir(f)


					for a in dir_:
						if a.split(".")[0]==str(seli):
							ext=a.split(".")[-1]


							if os.path.isfile("Images/"+a):
								os.remove("Images/"+a)

							ff="Images/"+str(seli)+"_s."+ext
							if os.path.isfile(ff):
								os.remove(ff)    							
 

				cur.execute("DELETE FROM items WHERE items_id="+str(seli)+"")
				dbstock.commit()

				ms_con=0

				vbar1.pack_forget()
				main2.pack_forget()

				vbar1.pack(side=tk.RIGHT,fill=tk.Y)
				main2.pack(side=tk.LEFT)
				as_n.delete(0,tk.END)
				as_bp.delete(0,tk.END)
				as_sp.delete(0,tk.END)
				as_q.delete(0,tk.END)
				as_de.delete(0.0,tk.END)

				as_n.place_forget()
				as_bp.place_forget()
				as_sp.place_forget()
				as_q.place_forget()
				as_de.place_forget()

				draw_stock()
				main2.focus_set()

				mscon2=0

				msf=""
				msimage=""

				message(main2,90+(wd-800-90)/2+400,main2.canvasy((ht-50)/2+250+20),1,"Item removed!")
				return

		cx,cy=x1+580,y1+220+10

		r=math.sqrt((e.x-cx)**2 + (y-cy)**2)


		if r<=40 and msimage=="":
			msf=filedialog.askopenfilename()

			e=msf.split(".")[-1]

			if not e=="jpg":
				im = Image.open(msf)

				# converting to jpg
				im = im.convert("RGB")	
				im.save("data/iv.jpg")	
				msf="data/iv.jpg"



			im=Image.open(msf)
			mscon2=1
			mscon=1

			ext=msf.split(".")[-1]

			w,h=im.size

			if (w/h)>1:

				bx=400
				by=int(bx*h/w)

				im=im.resize((bx,by))
			elif (w/h)<1:
				by=400
				bx=int(by*w/h)
				im=im.resize((bx,by))

			elif (w/h)==1:
				bx=400
				by=400
				im=im.resize((bx,by))

			ax=(400-bx)/2
			ay=(400-by)/2

			im.save("data/msi."+ext)

			msimage=ImageTk.PhotoImage(file="data/msi."+ext)

			msi=main2.create_image(x1+400-20+ax,y1+20+ay,image=msimage,anchor="nw")

			cx,cy=x1+400-20-1+10,y1+20-1+10
			ar=[x1+400-20-1,y1+20-1]
			a_=180
			for a in range(90):
				x=10*math.sin(math.radians(a_))+cx
				y=10*math.cos(math.radians(a_))+cy
				ar.append(x)
				ar.append(y)

				a_+=1
			ar.append(x1+400-20-1)
			ar.append(y1+20-1)

			main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")


			cx,cy=x1+400-20-1+10,y1+20+400-10
			ar=[x1+400-20-1,y1+20+400]
			a_=270
			for a in range(90):
				x=10*math.sin(math.radians(a_))+cx
				y=10*math.cos(math.radians(a_))+cy
				ar.append(x)
				ar.append(y)

				a_+=1
			ar.append(x1+400-20-1)
			ar.append(y1+20+400)

			main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")


			cx,cy=x1+400+400-20-10,y1+20+400-10
			ar=[x1+400+400-20,y1+20+400]
			a_=0
			for a in range(90):
				x=10*math.sin(math.radians(a_))+cx
				y=10*math.cos(math.radians(a_))+cy
				ar.append(x)
				ar.append(y)

				a_+=1
			ar.append(x1+400+400-20)
			ar.append(y1+20+400)

			main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")


			cx,cy=x1+400+400-20-10,y1+20-1+10
			ar=[x1+400+400-20,y1+20-1]
			a_=90
			for a in range(90):
				x=10*math.sin(math.radians(a_))+cx
				y=10*math.cos(math.radians(a_))+cy
				ar.append(x)
				ar.append(y)

				a_+=1
			ar.append(x1+400+400-20)
			ar.append(y1+20-1)

			main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")
			#x1+400-20-1,y1+20-1, x1+400+400-20,y1+20+400

			main2.create_arc(x1+400-20-1,y1+20-1, x1+400-20-1+20,y1+20-1+20,style="arc",start=90,extent=90,outline="#777777")
			main2.create_arc(x1+400+400-20,y1+20-1, x1+400+400-20-20,y1+20-1+20,style="arc",start=0,extent=90,outline="#777777")
			main2.create_arc(x1+400+400-20,y1+20+400-20, x1+400+400-20-20,y1+20+400,style="arc",start=270,extent=90,outline="#777777")	
			main2.create_arc(x1+400-20-1,y1+20+400-20, x1+400-20-1+20,y1+20+400,style="arc",start=180,extent=90,outline="#777777")	


			main2.create_line(x1+400-20-1+10,y1+20-1,  x1+400+400-20-10,y1+20-1,fill="#777777" )
			main2.create_line(x1+400-20-1+10-1,y1+20+400,  x1+400+400-20-10,y1+20+400,fill="#777777" )
			main2.create_line(x1+400-20-1,y1+20-1+10-1, x1+400-20-1,y1+20+400-10,fill="#777777" )
			main2.create_line(x1+400+400-20,y1+20-1+10, x1+400+400-20,y1+20+400-10,fill="#777777" )


			return
		cx,cy=x1+755+12.5,y1+422.5+12.5

		r=math.sqrt((e.x-cx)**2 + (y-cy)**2)

		if r<=12.5:
			if not msimage=="":

				main2.delete(msi)
				msimage=""
				mscon=0
				mscon2=0
				msf=""

				return
			

	elif dashb_state=="sell_items":
		y=main2.canvasy(e.y)
		yy=main2.canvasy(0)





		x1,y1=90+(wd-800-90-300)/2,((ht-50)-500)/2+yy



		for v in sellarray:

			if v[1]<=e.x<=v[3]:
				if v[2]<=y<=v[4]:
					

					if si_con==0:
						si_con=1
						seli=v[0]

						cart_border(1)
						create_rectangle(cart5,0,0,5,ht-50-30-130, fill='#000000', alpha=.5)
						create_rectangle(cart8,0,int(cart8.canvasy(0)),290,int(cart8.canvasy(ht-50-30-130+5)), fill='#000000', alpha=.5)
						create_rectangle(cart7,0,0,5,ht-50-30-130, fill='#000000', alpha=.5)
						create_rectangle(cartq,0,0,300,30, fill='#000000', alpha=.5)
						create_rectangle(cart3,0,0,300,125, fill='#000000', alpha=.5)


						draw_sellitems()




						





						cart5.pack_forget()
						cart6.pack_forget()
						cart8.pack_forget()
						cvbar.pack_forget()
						cart7.pack_forget()

						cart8["width"]=290




						cart5.pack(side=tk.LEFT)
						cart8.pack(side=tk.LEFT)
						cart6.pack(side=tk.LEFT)
						cart7.pack(side=tk.LEFT)

						



						

						return
						

		cx,cy=x1+785-5+40,y1+15-2.5

		r=math.sqrt((e.x-cx)**2 + (y-cy)**2)

		if r<=12.5:
			si_con=0

			vbar1.pack_forget()
			main2.pack_forget()
			fff.pack_forget()

			main2.pack(side=tk.LEFT)
			vbar1.pack(side=tk.LEFT,fill=tk.Y)
			fff.pack(side=tk.LEFT)

			draw_sellitems()

			re_cart()
			return

		if x1+555<=e.x<=x1+745:
			if y1+420+30<=y<=y1+450+30:
				#add to cart


				ps=psoldat.get()
				quantity=si_quantity.get()


				try:
					ps=int(ps)
					quantity=int(quantity)
				except:
					return

				cart_array.append([seli,int(ps),int(quantity)])

				dashb.delete(cv)
				yy=ht-140-40-20
				cv=dashb.create_text(100+15-10,yy+33.5,text=str(len(cart_array)),fill="#32fca7",font=("FreeMono",13),anchor="w")

				cart__()

				si_con=0

				psoldat.delete(0,tk.END)
				si_quantity.delete(0,tk.END)

				psoldat.place_forget()
				si_quantity.place_forget()


				vbar1.pack_forget()
				main2.pack_forget()
				fff.pack_forget()

				main2.pack(side=tk.LEFT)
				vbar1.pack(side=tk.LEFT,fill=tk.Y)
				fff.pack(side=tk.LEFT)
				

				draw_sellitems()

				re_cart()

				return






	elif dashb_state=="add_stock":

		if myp[-1]==0:
			return

		x_,y_=90+(wd-90-800)/2,((ht-50)-500)/2

		cx,cy=x_+580,y_+220

		r=math.sqrt((e.x-cx)**2 + (main2.canvasy(e.y)-cy)**2)


		if r<=40 and ascon==0:
			file_path=filedialog.askopenfilename()


			e=file_path.split(".")[-1]

			if not e=="jpg":
				im = Image.open(file_path)

				# converting to jpg
				im = im.convert("RGB")	
				im.save("data/iv.jpg")	
				file_path="data/iv.jpg"
			try:
				im=Image.open(file_path)

				x,y=im.size

				if x>y:
					bx=400
					by=int(y*(400/x))

					im2=im.resize((bx,by))
					im2.save("data/mod."+file_path.split(".")[1])
					ax,ay=0,(400-by)/2
				elif y>x:
					bx=int(x*(400/y))
					by=400

					im2=im.resize((bx,by))
					im2.save("data/mod."+file_path.split(".")[1])
					ax,ay=(400-bx)/2,0

				elif x==y:
					bx,by=400,400
					ax,ay=0,0

					im2=im.resize((bx,by))
					im2.save("data/mod."+file_path.split(".")[1])


				as_image=ImageTk.PhotoImage(file="data/mod."+file_path.split(".")[1])

				
				as_im=main2.create_image(x_+400-20+ax,y_+20+ay,image=as_image,anchor="nw")

				ascon=1
			except:
				file_path=""

			draw_addstock()

			return

		cx,cy=x_+765+5,y_+435

		r=math.sqrt((e.x-cx)**2 + (e.y-cy)**2)

		if r<=12.5:
			as_image=""
			file_path=""
			ascon=0

			main2.delete(as_im)
			return


		if x_+325<=e.x<=x_+475:
			if y_+460<=e.y<=y_+490:

				try:



					name=as_n.get()
					bp=as_bp.get()
					sp=as_sp.get()
					q=as_q.get()
					de=as_de.get(0.0, tk.END)


					de=de.split("\n")[0]

					if name=="" or bp=="" or sp=="" or q=="":
						draw_addstock()

						message(main2,90+(wd-800-90)/2+400,(ht-50)/2+250+30,0,"Fill all details!")

						return

					


					dbstock=db.connect('data/stock.db')
					cur=dbstock.cursor()

					data=cur.execute("SELECT * FROM items")

					con=0
					for i in data:
						con=1

					if con==0:
						var=1
					else:
						data=cur.execute("SELECT MAX(items_id) FROM items")
						for b in data:
							var=int(b[0])+1

					pic=0
					if not as_image=="":
						im=Image.open(file_path)
						im.save("Images/"+str(var)+"."+file_path.split(".")[1])


						pic=1

						x,y=im.size



		


						if (x/y)>(150/100):
							bx=x-(x*((150/100)/(x/y) ) )
							im=im.crop((bx,0,x-bx,y))
							im=im.resize((150,100))
							im.save("Images/"+str(var)+"_s."+file_path.split(".")[1])
							

						elif (x/y)<(150/100):
							by=(y-(y*((x/y)/(150/100))  ))/2

							im=im.crop((0,by,x,y-by))
							im=im.resize((150,100))
							im.save("Images/"+str(var)+"_s."+file_path.split(".")[1])
							
						elif (x/y)==(150/100):
							im=im.resize((150,100))
							im.save("Images/"+str(var)+"_s."+file_path.split(".")[1])
							




					stock_addstock(var,name,bp,sp,q,de,str(pic))

					as_n.delete(0,tk.END)
					as_bp.delete(0,tk.END)
					as_sp.delete(0,tk.END)
					as_q.delete(0,tk.END)
					as_de.delete(0.0,tk.END)





					main2.focus_set()

					ascon2=0
					ascon=0
					as_image=""
					draw_addstock()

					message(main2,90+(wd-800-90)/2+400,(ht-50)/2+250+30,1,"Item added to stock!")


				except:
					message(main2,90+(wd-800-90)/2+400,(ht-50)/2+250+30,0,"Enter correct details!")

				return

				
def stock_addstock(id_,name,bp,sp,quantity,desc,pic):


	dbstock=db.connect('data/stock.db')
	cur=dbstock.cursor()


	cur.execute("INSERT INTO 	items VALUES("+str(id_)+",'"+name+"',"+str(bp)+","+str(sp)+","+str(quantity)+",'"+desc+"',"+pic+")")

	dbstock.commit()
def sales_(id_,name,sp,ps,quantity,date_,total,profit):


	dbs=db.connect('data/sales.db')
	cur=dbs.cursor()


	cur.execute("INSERT INTO sales_ VALUES("+str(id_)+",'"+str(name)+"',"+str(sp)+","+str(ps)+","+str(quantity)+",'"+str(date_)+"',"+str(total)+", "+str(profit)+" )")

	dbs.commit()





mot=0

def main2_mot(e):
	global mot
	mot=1
def cart8_mot(e):
	global mot
	mot=2




file_path=""
as_image=""
as_im=()
ax,ay=0,0
frame=tk.Frame(width=wd,height=ht,bg="#ffffff")
frame.pack()



main1=tk.Canvas(frame,width=wd,height=50,relief="flat",highlightthickness=0,border=0,bg="#222222")
main1.bind("<Button-1>",main1_commands)
main1.pack(side=tk.TOP)

main1.create_line( 13,8, 21,16, 13,24,fill="#000000",width=2)



style=ttk.Style()
style.element_create("My.Vertical.TScrollbar.trough", "from", "clam")
style.element_create("My.Vertical.TScrollbar.thumb", "from", "clam")
style.element_create("My.Vertical.TScrollbar.grip", "from", "clam")

style.layout("My.Vertical.TScrollbar",
   [('My.Vertical.TScrollbar.trough',
     {'children': [('My.Vertical.TScrollbar.thumb',
                    {'unit': '1',
                     'children':
                        [('My.Vertical.TScrollbar.grip', {'sticky': ''})],
                     'sticky': 'nswe'})
                  ],
      'sticky': 'ns'})])


style.configure("My.Vertical.TScrollbar", gripcount=0, background="#666666",
                troughcolor='#ffffff', borderwidth=0, bordercolor='#ffffff',
                lightcolor='#ffffff',relief="flat", darkcolor='#ffffff',
                arrowsize=7)

fmain2=tk.Frame(frame,width=wd,height=ht-50,bg="#ffffff")
fmain2.pack(side=tk.TOP)

main2=tk.Canvas(fmain2,width=wd-300-7,height=ht-50,bg="#ffffff",relief="flat",highlightthickness=0,border=0,
	scrollregion=(0,0,wd-300-10,ht-50))
main2.bind("<Button-1>",main2_commands)
main2.bind_all("<MouseWheel>",_on_mousewheel)
main2.bind("<Motion>",main2_mot)


fff=tk.Frame(fmain2,width=300,height=ht-50,bg="#ffffff")

cbb=()




def cart_border(v):

	pass



def re_cart():

	global cart2,cart5,cart6,cart8,cart7,cartq,cart3,cvbar

	

	cart5.delete("all")
	cart8.delete("all")
	cart7.delete("all")
	cartq.delete("all")
	cart3.delete("all")

	cart5.create_line(0,0,0,ht-50-30-130,fill="#999999")
	cartq.create_line(0,0,0,30,fill="#999999")
	cart3.create_line(0,0,0,125,fill="#999999")

	cart8["width"]=290-7

	cart_border(0)


	cart5.pack_forget()
	cart6.pack_forget()
	cart8.pack_forget()
	cvbar.pack_forget()
	cart7.pack_forget()

	cart5.pack(side=tk.LEFT)
	cart6.pack(side=tk.LEFT)
	cart8.pack(side=tk.LEFT)
	cvbar.pack(side=tk.LEFT,fill=tk.Y)
	cart7.pack(side=tk.LEFT)


	cart8.pack(side=tk.LEFT)
	cvbar.pack(side=tk.LEFT,fill=tk.Y)



	cart3.create_text(10,30-10,text="Total",font=("FreeMono",13),anchor="w",fill="#ffffff")
	cart3.create_text(10,60-5,text="Discount",font=("FreeMono",13),anchor="w",fill="#ffffff")


	cart3.create_oval(10,125-10-30, 10+10,125-10-30+10,fill="#ffffff",outline="#ffffff")
	cart3.create_oval(10,125-10-10, 10+10,125-10,fill="#ffffff",outline="#ffffff")
	cart3.create_oval(10+135-10,125-10-30, 10+135,125-10-30+10,fill="#ffffff",outline="#ffffff")
	cart3.create_oval(10+135-10,125-10-10, 10+135,125-10,fill="#ffffff",outline="#ffffff")

	cart3.create_polygon(10+5,125-10-30, 10+135-5,125-10-30, 10+135,125-10-30+5,
		10+135,125-10-5, 10+135-5,125-10, 10+5,125-10, 10,125-10-5, 10,125-10-30+5,fill="#ffffff",outline="#ffffff")



	cart3.create_text(10+135/2,125-10-15,text="Clear",fill="#000000",font=("FreeMono",13))


	cart3.create_oval(10+135+10,125-10-30, 10+10+135+10,125-10-30+10,fill="#ffffff",outline="#ffffff")
	cart3.create_oval(10+135+10,125-10-10, 10+10+135+10,125-10,fill="#ffffff",outline="#ffffff")
	cart3.create_oval(10+135+10+135-10,125-10-30, 10+135+135+10,125-10-30+10,fill="#ffffff",outline="#ffffff")
	cart3.create_oval(10+135+10+135-10,125-10-10, 10+135+135+10,125-10,fill="#ffffff",outline="#ffffff")

	cart3.create_polygon(10+5+135+10,125-10-30, 10+135-5+135+10,125-10-30, 10+135+135+10,125-10-30+5,
		10+135+135+10,125-10-5, 10+135-5+135+10,125-10, 10+5+135+10,125-10, 10+135+10,125-10-5, 10+135+10,125-10-30+5,fill="#ffffff",outline="#ffffff")

	cart3.create_text(10+135+10+135/2,125-10-15,text="Sell",fill="#000000",font=("FreeMono",13))



	cart__()









cart2=tk.Frame(fff,width=300,height=ht-50-30-130+5,bg="#222222")
cart2.pack(side=tk.TOP)





cart5=tk.Canvas(cart2,width=5,height=ht-50-30-130+5,bg="#222222",relief="flat",highlightthickness=0,border=0)

cart5.pack(side=tk.LEFT)


cart6=tk.Frame(cart2,width=290,height=ht-50-30-130+5,bg="#222222")
cart6.pack(side=tk.LEFT)


cart_arr_=[]
qu2=()
def cart__():
	global cart_array,cart8,ycart,c1,cart3,ct,cd,qu2,cart_arr_,cartq

	cart8.delete("all")
	cart_arr_=[]


	y=0

	db_stock=db.connect("data/stock.db")

	cur=dbstock.cursor()

	tt=0
	dd=0

	qu2=ImageTk.PhotoImage(file="data/removeb.png")




	for n in range( len(cart_array)):
		i=cart_array[n]

		rows=cur.execute("SELECT * FROM items WHERE items_id="+str(i[0]))

		for row in rows:
			name=row[1]

			sp=row[3]

		tt+=i[1]*i[2]

		dd+=(sp-i[1])*i[2]

		cart8.create_image(290-7-10-20,y+5,image=qu2	,anchor="nw")

		cart_arr_.append([n,290-7-10-20+10,y+5+10])

		cart8.create_text(10,y+20,text=str(name),anchor="w",font=("FreeMono",13),fill="#000000")

		if int(i[2])==1:
			units="unit"
		elif int(i[2])!=1:
			units="units"

		cart8.create_text(10,y+50,text=str(i[2])+" "+units,anchor="w",font=("FreeMono",13),fill="#000000")

		cart8.create_text(290-7-10,y+50,text=add_comma( str(i[1]*i[2]))+" Ksh",anchor="e",font=("FreeMono",13),fill="#000000")



		cart8.create_line(0,y+70,290-7,y+70,fill="#999999")

		y+=70



	cart_border(0)
	cartq.delete(c1)
	c1=cartq.create_text(10,15,text=str(len(cart_array))+" item(s)",fill="cyan",font=("FreeMono",13),anchor="w")

	cart8["scrollregion"]=(0,0,290-7,y+50)

	ycart=y+50

	cart3.delete(ct)
	cart3.delete(cd)

	ct=cart3.create_text(300-10,30-10,text=str(tt)+" Ksh",font=("FreeMono",13),anchor="e",fill="#ffffff")

	cd=cart3.create_text(300-10,60-5,text=str(dd)+" Ksh",font=("FreeMono",13),anchor="e",fill="#ffffff")










def cart8_comm(e):
	global cart_array,cart_arr_,cart8


	for i in cart_arr_:

		cx=i[1]
		cy=i[2]

		r=math.sqrt((cx-cart8.canvasx(e.x))**2+(cy-cart8.canvasy(e.y))**2)

		if r<=10:

			cart_array.pop(i[0])
			cart__()
			draw_sellitems()

			cart_border(0)



cart8=tk.Canvas(cart6,width=290-7,height=ht-50-30-130+5,bg="#ffffff",relief="flat",highlightthickness=0,border=0)
cart8.pack(side=tk.LEFT)

cart8.bind("<Button-1>",cart8_comm)
cart8.bind_all("<MouseWheel>",_on_mousewheel)
cart8.bind("<Motion>",cart8_mot)


ycart=0
cart8["scrollregion"]=(0,0,290-7,ht-50-30-130)

cvbar=ttk.Scrollbar(cart6,orient=tk.VERTICAL,style="My.Vertical.TScrollbar")

cvbar.config(command=cart8.yview)

cart8.config(yscrollcommand=cvbar.set)
cvbar.pack(side=tk.LEFT,fill=tk.Y)




cart7=tk.Canvas(cart2,width=5,height=ht-50-30-130,bg="#222222",relief="flat",highlightthickness=0,border=0)
cart7.pack(side=tk.LEFT)


def cart3_comm(e):

	global cart_array,cart8,si_con


	if si_con==0:

		if 10<=e.x<=10+135:
			if 125-10-30<=e.y<=125-10:
				cart_array=[]

				cart8["scrollregion"]=(0,0,0,0)
				cart__()
				draw_sellitems()

		if 10+135+10<=e.x<=10+135+135+10:
			if 125-10-30<=e.y<=125-10:



				#sell items




				for va in cart_array:


					dbsales=db.connect("data/sales.db")
					cur1=dbsales.cursor()

					dbstock=db.connect("data/stock.db")
					cur2=dbstock.cursor()

					ps=va[1]
					quantity=va[2]



					cur1.execute("SELECT MAX(sales_id) FROM sales_")
					rows=cur1.fetchall()

					v=0

					for row in rows:
						v=row[0]


					if v==None:
						v=1
					else:
						v+=1





					cur2.execute("SELECT * FROM items WHERE items_id="+str(va[0])+"")
					rows=cur2.fetchall()

					for row in rows:
						name=row[1]
						sp=row[3]
						bp=row[2]

						q=row[4]


					

					date_=datetime.datetime.now()

					total=ps*quantity

					profit=total-(int(bp)*quantity)




					sales_(v,name,sp,ps,quantity,date_,total,profit)



					cur2.execute("UPDATE items SET quantity="+str(q-quantity)+" WHERE items_id="+str(va[0])+" ")

					dbstock.commit()

				cart_array=[]
				cart8["scrollregion"]=(0,0,0,0)
				cart__()
				draw_sellitems()

				message(main2,90+(wd-300)/2,main2.canvasy((ht-50)/2+250+20),1,"Purchase successful!")


cartq=tk.Canvas(fff,width=300,height=30,bg="#222222",relief="flat",highlightthickness=0,border=0)
cartq.pack(side=tk.TOP)


c1=cartq.create_text(10,15,text="0 item(s)",fill="cyan",font=("FreeMono",13),anchor="w")

cart3=tk.Canvas(fff,width=300,height=125,bg="#222222",relief="flat",highlightthickness=0,border=0)
cart3.pack(side=tk.TOP)

cart3.bind("<Button-1>",cart3_comm)
cart3.create_text(10,30-10,text="Total",font=("FreeMono",13),anchor="w",fill="#ffffff")
cart3.create_text(10,60-5,text="Discount",font=("FreeMono",13),anchor="w",fill="#ffffff")


ct=cart3.create_text(300-10,30-5,text="0 Ksh",font=("FreeMono",13),anchor="e",fill="#ffffff")

cd=cart3.create_text(300-10,60-5,text="0 Ksh",font=("FreeMono",13),anchor="e",fill="#ffffff")


cart3.create_oval(10,125-10-30, 10+10,125-10-30+10,fill="#ffffff",outline="#ffffff")
cart3.create_oval(10,125-10-10, 10+10,125-10,fill="#ffffff",outline="#ffffff")
cart3.create_oval(10+135-10,125-10-30, 10+135,125-10-30+10,fill="#ffffff",outline="#ffffff")
cart3.create_oval(10+135-10,125-10-10, 10+135,125-10,fill="#ffffff",outline="#ffffff")

cart3.create_polygon(10+5,125-10-30, 10+135-5,125-10-30, 10+135,125-10-30+5,
	10+135,125-10-5, 10+135-5,125-10, 10+5,125-10, 10,125-10-5, 10,125-10-30+5,fill="#ffffff",outline="#ffffff")


cart3.create_text(10+135/2,125-10-15,text="Clear",fill="#000000",font=("FreeMono",13))


cart3.create_oval(10+135+10,125-10-30, 10+10+135+10,125-10-30+10,fill="#ffffff",outline="#ffffff")
cart3.create_oval(10+135+10,125-10-10, 10+10+135+10,125-10,fill="#ffffff",outline="#ffffff")
cart3.create_oval(10+135+10+135-10,125-10-30, 10+135+135+10,125-10-30+10,fill="#ffffff",outline="#ffffff")
cart3.create_oval(10+135+10+135-10,125-10-10, 10+135+135+10,125-10,fill="#ffffff",outline="#ffffff")

cart3.create_polygon(10+5+135+10,125-10-30, 10+135-5+135+10,125-10-30, 10+135+135+10,125-10-30+5,
	10+135+135+10,125-10-5, 10+135-5+135+10,125-10, 10+5+135+10,125-10, 10+135+10,125-10-5, 10+135+10,125-10-30+5,fill="#ffffff",outline="#ffffff")

cart3.create_text(10+135+10+135/2,125-10-15,text="Sell",fill="#000000",font=("FreeMono",13))

vbar1=ttk.Scrollbar(fmain2,orient=tk.VERTICAL,style="My.Vertical.TScrollbar")
#vbar1.pack(side=tk.RIGHT,fill=tk.Y)
vbar1.config(command=main2.yview)

main2.config(yscrollcommand=vbar1.set)

main2.pack(side=tk.LEFT)

vbar1.pack(side=tk.LEFT,fill=tk.Y)
fff.pack(side=tk.LEFT)


###################

def dashb_commands(e):

	global dvar,dashb,dashb_state,dvar2,as_im,as_image,ax,ay,si_con,ms_con,cal,cal_con
	global as_n,as_bp,as_sp,as_q,as_de,ht,wd,main2,si_quantity,psoldat,si_desc,searche,vbar1,cart
	global cart_array,cartframe,uns,ems,cons,pss,photo1,photo2,admin_st1
	global admin_st2,admin_st2_1,admin_st2_2,prof_st,prof0,prof1,prof2,myp,myp2,myp3,mypv
	global ascon2,ascon,daten,cal_day,cal_month,cal_year,userframe,pst
	global fff
			




	if 0<e.y<=100:
		dashb_state="sell_items"
		draw_dashb()
		re_cart()


		main2["scrollregion"]=(0,0,wd-90-300-10,ht-50)

		userframe.place_forget()
		cartframe.place_forget()

		cal.place_forget()
		cal_con=0

		si_con=0

		vbar1.pack_forget()
		main2.pack_forget()
		fff.pack_forget()

		main2["width"]=wd-300-10


		main2.pack(side=tk.LEFT)

		vbar1.pack(side=tk.LEFT,fill=tk.Y)
		fff.pack(side=tk.LEFT)
		

		uns.place_forget()
		ems.place_forget()
		cons.place_forget()
		pss.place_forget()


		cart.place_forget()
		as_n.place_forget()
		as_bp.place_forget()
		as_sp.place_forget()
		as_q.place_forget()
		as_de.place_forget()

		rr_.place_forget()

		searche.place_forget()

		searche.delete(0,tk.END)


		draw_sellitems()
	elif 300<e.y<=400:

		dashb_state="add_stock"
		main2["scrollregion"]=(0,0,wd,ht-50)

		main2["width"]=wd

		fff.pack_forget()



		as_n.delete(0,tk.END)
		as_bp.delete(0,tk.END)
		as_sp.delete(0,tk.END)
		as_q.delete(0,tk.END)
		as_de.delete(0.0,tk.END)


		ascon2=0
		ascon=0
		as_image=""
		userframe.place_forget()

		draw_dashb()
		draw_addstock()
		searche.delete(0,tk.END)
		cart.place_forget()
		cartframe.place_forget()
		cal.place_forget()
		cal_con=0
		rr_.place_forget()

		uns.place_forget()
		ems.place_forget()
		cons.place_forget()
		pss.place_forget()


		vbar1.pack_forget()

		si_quantity.place_forget()
		psoldat.place_forget()
		si_desc.place_forget()

		searche.place_forget()

	elif 200<e.y<=300:
		dashb_state="stock"

		main2["width"]=wd-10


		fff.pack_forget()
		ms_con=0
		draw_dashb()
		main2["scrollregion"]=(0,0,wd,ht-50)
		searche.delete(0,tk.END)
		cartframe.place_forget()
		cart.place_forget()
		cal.place_forget()
		cal_con=0
		vbar1.pack_forget()
		main2.pack_forget()

		userframe.place_forget()
		vbar1.pack(side=tk.RIGHT,fill=tk.Y)
		main2.pack(side=tk.LEFT)

		uns.place_forget()
		ems.place_forget()
		cons.place_forget()
		pss.place_forget()


		as_n.place_forget()
		as_bp.place_forget()
		as_sp.place_forget()
		as_q.place_forget()
		as_de.place_forget()
		si_quantity.place_forget()
		psoldat.place_forget()
		si_desc.place_forget()
		searche.place_forget()
		rr_.place_forget()
		draw_stock()
	elif 100<e.y<=200:

		main2["width"]=wd-10

		fff.pack_forget()
		dashb_state="reports"
		vbar1.pack_forget()
		main2.pack_forget()
		cart.place_forget()
		cal.place_forget()
		cal_con=0
		cartframe.place_forget()
		vbar1.pack(side=tk.RIGHT,fill=tk.Y)
		main2.pack(side=tk.LEFT)

		userframe.place_forget()

		now=datetime.datetime.now()
		yy=now.year
		mm=now.month
		dd=now.day
		daten=str(dd)+"-"+str(mm)+"-"+str(yy)

		cal_day,cal_month,cal_year=int(dd),int(mm),int(yy)

		draw_cal()



		draw_dashb()
		main2["scrollregion"]=(0,0,wd,ht-50)

		uns.place_forget()
		ems.place_forget()
		cons.place_forget()
		pss.place_forget()


		searche.delete(0,tk.END)
		as_n.place_forget()
		as_bp.place_forget()
		as_sp.place_forget()
		as_q.place_forget()
		as_de.place_forget()

		searche.place_forget()
		si_quantity.place_forget()
		psoldat.place_forget()
		si_desc.place_forget()

		draw_reports()


	elif 400<e.y<=500:

		main2["width"]=wd
		pst=0
		fff.pack_forget()
		dashb_state="profiles"
		vbar1.pack_forget()
		main2.pack_forget()
		cart.place_forget()
		cal.place_forget()
		cal_con=0
		cartframe.place_forget()
		rr_.place_forget()

		userframe.place_forget()

		#vbar1.pack(side=tk.RIGHT,fill=tk.Y)
		main2.pack(side=tk.LEFT)

		draw_dashb()
		main2["scrollregion"]=(0,0,wd,ht-50)

		searche.delete(0,tk.END)
		as_n.place_forget()
		as_bp.place_forget()
		as_sp.place_forget()
		as_q.place_forget()
		as_de.place_forget()

		searche.place_forget()
		si_quantity.place_forget()
		psoldat.place_forget()
		si_desc.place_forget()


		photo1=()
		photo2=()


		admin_st2=0

		admin_st2_2=0
		prof_st=0
		prof0=""
		prof1=""
		prof2=0


		myp2=[]

		mypv=0
		userc["scrollregion"]=(0,0,620+60,368)

		dbuser=db.connect('data/users.db')
		cur=dbuser.cursor()

		cur.execute("SELECT * FROM user WHERE user_id="+str(profileid))
		rows=cur.fetchall()

		for row in rows:

	
			myp=[]

			for i in row:
				myp.append(i)

			admin_st1=row[-1]
			admin_st2_1=row[-1]

			myp3=[row[1],row[2],row[3],row[-2]]


		draw_profiles()


	if dashb_state=="sell_items":

		yy=ht-140-40-20

		if 23<=e.x<=250-23:
			if yy+60<=e.y<=yy+90:

				si_con=0

				cart_array=[]
				draw_dashb()
				draw_sellitems()
				cartframe.place_forget()


		if 23<=e.x<=250-23:
			if yy+100<=e.y<=yy+130:

				if len(cart_array)>0:
					si_con=2
					draw_sellitems()

pp=()
sell_items_icon1=()
sell_items_icon2=()




newstock_icon1=()
newstock_icon2=()

manage_stock_icon1=()
manage_stock_icon2=()


reports_icon1=()
reports_icon2=()

profiles_icon1=()
profiles_icon2=()
def draw_dashb():
	global dashb,dashb_state
	global diw,carti,cv
	global cart_array
	global pp,myp
	global sell_items_icon1,sell_items_icon2,newstock_icon1,newstock_icon2,manage_stock_icon1,manage_stock_icon2,reports_icon1,reports_icon2,profiles_icon1,profiles_icon2



	dashb.delete("all")

	dashb.create_line(89,0,89,ht-50,fill="#999999")




	sell_items_icon1=ImageTk.PhotoImage(file="icons/cart.png")
	sell_items_icon2=ImageTk.PhotoImage(file="icons/cartr.png")


	reports_icon1=ImageTk.PhotoImage(file="icons/report.png")
	reports_icon2=ImageTk.PhotoImage(file="icons/reportr.png")


	manage_stock_icon1=ImageTk.PhotoImage(file="icons/manage.png")
	manage_stock_icon2=ImageTk.PhotoImage(file="icons/manager.png")

	newstock_icon1=ImageTk.PhotoImage(file="icons/add.png")
	newstock_icon2=ImageTk.PhotoImage(file="icons/addr.png")





	profiles_icon1=ImageTk.PhotoImage(file="icons/profile.png")
	profiles_icon2=ImageTk.PhotoImage(file="icons/profiler.png")

	if dashb_state=="sell_items":
		v1,v2,v3,v4,v5=1,0,0,0,0


	elif dashb_state=="reports":
		v1,v2,v3,v4,v5=0,1,0,0,0
	elif dashb_state=="stock":
		v1,v2,v3,v4,v5=0,0,1,0,0
	elif dashb_state=="add_stock":
		v1,v2,v3,v4,v5=0,0,0,1,0
	elif dashb_state=="profiles":
		v1,v2,v3,v4,v5=0,0,0,0,1		


	if v1==0:

		dashb.create_image(20,20,image=sell_items_icon1,anchor="nw")
		dashb.create_text(45,85,text="Sell Items",fill="#000000",font=("FreeMono",13))
	else:

		dashb.create_image(20,20,image=sell_items_icon2,anchor="nw")
		dashb.create_text(45,85,text="Sell Items",fill="#E3355C",font=("FreeMono",13))



	if v2==0:

		dashb.create_image(20,20+100,image=reports_icon1,anchor="nw")
		dashb.create_text(45,85+100,text="Reports",fill="#000000",font=("FreeMono",13))
	else:

		dashb.create_image(20,20+100,image=reports_icon2,anchor="nw")
		dashb.create_text(45,85+100,text="Reports",fill="#E3355C",font=("FreeMono",13))






	if v3==0:

		dashb.create_image(20,20+100*2,image=manage_stock_icon1,anchor="nw")
		dashb.create_text(45,85+100*2,text="Manage \n  Items",fill="#000000",font=("FreeMono",13))
	else:

		dashb.create_image(20,20+100*2,image=manage_stock_icon2,anchor="nw")
		dashb.create_text(45,85+100*2,text="Manage \n  Items",fill="#E3355C",font=("FreeMono",13))


	if v4==0:

		dashb.create_image(20,20+100*3,image=newstock_icon1,anchor="nw")
		dashb.create_text(45,85+100*3,text="New item",fill="#000000",font=("FreeMono",13))
	else:

		dashb.create_image(20,20+100*3,image=newstock_icon2,anchor="nw")
		dashb.create_text(45,85+100*3,text="New item",fill="#E3355C",font=("FreeMono",13))



	if v5==0:

		dashb.create_image(20,20+100*4,image=profiles_icon1,anchor="nw")
		dashb.create_text(45,85+100*4,text="Profiles",fill="#000000",font=("FreeMono",13))
	else:

		dashb.create_image(20,20+100*4,image=profiles_icon2,anchor="nw")
		dashb.create_text(45,85+100*4,text="Profiles",fill="#E3355C",font=("FreeMono",13))




cv=()
dvar=0
dvar2=1
dx=0
dashb_state="sell_items"
#6e0a1e
dashb=tk.Canvas(relief="flat",width=90,height=ht-50,bg="#ffffff",highlightthickness=0,border=0)
dashb.bind("<Button-1>",dashb_commands)
dashb.place(in_=root,x=0,y=50)





def show():
	global intro,pst,sss,pw,showp,dshowp

	intro.delete(sss)
	x_,y_=(wd/2)-350/2,(ht-200)/2


	if pst==0:
		showp=ImageTk.PhotoImage(file="data/show.png")

		sss=intro.create_image(x_+150+168-10+10-5,y_+30-2+50,image=showp,anchor="nw")
		pw["show"]="*"
	elif pst==1:
		dshowp=ImageTk.PhotoImage(file="data/dshow.png")

		sss=intro.create_image(x_+150+168-10+10-5,y_+30-2+50,image=dshowp,anchor="nw")
		pw["show"]=""




################

sss=()
intro=tk.Canvas(width=wd,height=ht,bg="#222222",highlightthickness=0,border=0,relief="flat")
intro.bind("<Button-1>",login)
intro.place(in_=root,x=0,y=0)



x_,y_=(wd/2)-350/2,(ht-200)/2
#87.5 262.5
#150 175


intro.create_polygon(x_+10,y_, x_+350-10,y_, x_+350,y_+10, x_+350,y_+220-30, x_+340,y_+230-30, x_+10,y_+230-30,
	x_,y_+220-30, x_,y_+10,fill="#ffffff",outline="#ffffff")


intro.create_oval(x_,y_,x_+20,y_+20,fill="#ffffff",outline="#ffffff")
intro.create_oval(x_,y_+230-20-30,x_+20,y_+230-30,fill="#ffffff",outline="#ffffff")
intro.create_oval(x_+350-20,y_+230-20-30,x_+350,y_+230-30,fill="#ffffff",outline="#ffffff")
intro.create_oval(x_+350-20,y_,x_+350,y_+20,fill="#ffffff",outline="#ffffff")
"""
intro.create_arc(x_,y_,x_+20,y_+20,style="arc",start=90,extent=90,outline="#000000")
intro.create_arc(x_,y_+230-20,x_+20,y_+230,style="arc",start=180,extent=90,outline="#000000")
intro.create_arc(x_+350-20,y_+230-20,x_+350,y_+230,style="arc",start=270,extent=90,outline="#000000")
intro.create_arc(x_+350-20,y_,x_+350,y_+20,style="arc",start=0,extent=90,outline="#000000")

intro.create_line(x_+10,y_, x_+340,y_, fill="#000000")
intro.create_line(x_+10-1,y_+230, x_+340,y_+230, fill="#000000")

intro.create_line(x_,y_+10-1,x_,y_+220, fill="#000000")
intro.create_line(x_+350,y_+10,x_+350,y_+220, fill="#000000")"""

def eun(e):
	global pw

	pw.focus_set()


intro.create_text(x_+30+10-10,y_+40, anchor="w",text="User name",fill="#000000",font=("FreeMono","13"))
intro.create_text(x_+30+10-10,y_+40+50, anchor="w",text="Password",fill="#000000",font=("FreeMono","13"))




intro.create_arc(x_+150-2-10,y_+30-2, x_+150-2+10-10,y_+30-2+10,style="arc",start=90,extent=90,outline="#000000")
intro.create_arc(x_+150-2-10,y_+30+20+5-10, x_+150-2+10-10,y_+30+20+5,style="arc",start=180,extent=90,outline="#000000")
intro.create_arc(x_+150+168-10-10,y_+30-2, x_+150+168-10,y_+30-2+10,style="arc",start=0,extent=90,outline="#000000")
intro.create_arc(x_+150+168-10-10,y_+30+20+5-10, x_+150+168-10,y_+30+20+5,style="arc",start=270,extent=90,outline="#000000")

intro.create_line(x_+150-2-10,y_+30-2+5, x_+150-2-10,y_+30+20+5-5,fill="#000000")
intro.create_line(x_+150+168-10,y_+30-2+5, x_+150+168-10,y_+30+20+5-5,fill="#000000")

intro.create_line(x_+150-2+5-10,y_+30-2, x_+150+168-5+1-10,y_+30-2,fill="#000000")
intro.create_line(x_+150-2+5-10,y_+30+20+5, x_+150+168-5-10,y_+30+20+5,fill="#000000")


intro.create_arc(x_+150-2-10,y_+30-2+50, x_+150-2+10-10,y_+30-2+10+50,style="arc",start=90,extent=90,outline="#000000")
intro.create_arc(x_+150-2-10,y_+30+20+5-10+50, x_+150-2+10-10,y_+30+20+5+50,style="arc",start=180,extent=90,outline="#000000")
intro.create_arc(x_+150+168-10-10,y_+30-2+50, x_+150+168-10,y_+30-2+10+50,style="arc",start=0,extent=90,outline="#000000")
intro.create_arc(x_+150+168-10-10,y_+30+20+5-10+50, x_+150+168-10,y_+30+20+5+50,style="arc",start=270,extent=90,outline="#000000")

intro.create_line(x_+150-2-10,y_+30-2+5+50, x_+150-2-10,y_+30+20+5-5+50,fill="#000000")
intro.create_line(x_+150+168-10,y_+30-2+5+50, x_+150+168-10,y_+30+20+5-5+50,fill="#000000")

intro.create_line(x_+150-2+5-10,y_+30-2+50, x_+150+168-5+1-10,y_+30-2+50,fill="#000000")
intro.create_line(x_+150-2+5-10,y_+30+20+5+50, x_+150+168-5-10,y_+30+20+5+50,fill="#000000")


un=tk.Entry(width=18,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,font=("FreeMono","13"))
un.place(in_=root,x=x_+151-10,y=y_+31)
un.bind("<Return>",eun)

pw=tk.Entry(width=18,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,font=("FreeMono","13"),show="*")
pw.place(in_=root,x=x_+151-10,y=y_+31+50)

show()



intro.create_arc(x_+100-(30/2), y_+130+20+30-30, x_+100+(30/2), y_+130+20+30-30+30,style="arc",start=90
	,extent=180,outline="#000000")
intro.create_arc(x_+250-(30/2), y_+130+20+30-30, x_+250+(30/2), y_+130+20+30-30+30,style="arc",start=270
	,extent=180,outline="#000000")

intro.create_line(x_+100,y_+130+20+30-30, x_+250,y_+130+20+30-30,fill="#000000")
intro.create_line(x_+100-1,y_+130+20+30-30+30, x_+250,y_+130+20+30-30+30,fill="#000000")


#intro.create_rectangle(x_+100,y_+130+20+30-30, x_+250,y_+130+20+30-30+30, fill="#222222",outline="#222222")
#intro.create_oval(x_+100-(30/2), y_+130+20+30-30, x_+100+(30/2), y_+130+20+30-30+30,fill="#222222",outline="#222222")

#intro.create_oval(x_+250-(30/2), y_+130+20+30-30, x_+250+(30/2), y_+130+20+30-30+30,fill="#222222",outline="#222222")

intro.create_text(x_+350/2,y_+130+20+30-30+15,text="Login",font=("FreeMono","13"),fill="#000000")

# sell items


se=()

images = []  # to hold the newly created image

def create_rectangle(can,x1, y1, x2, y2, **kwargs):
	global images
	if 'alpha' in kwargs:
		alpha = int(kwargs.pop('alpha') * 255)
		fill = kwargs.pop('fill')
		fill = root.winfo_rgb(fill) + (alpha,)
		image = Image.new('RGBA', (x2-x1, y2-y1), fill)
		images.append(ImageTk.PhotoImage(image))
		can.create_image(x1, y1, image=images[-1], anchor='nw')
	#main2.create_rectangle(x1, y1, x2, y2, **kwargs)
	#print("drawn")

def draw_sellitems():
	global main1,main2,dvar2,wd, si_con,sellarray,seli,si_quantity,psoldat,total, pos,si_desc,yvar
	global searche,svar,vbar1,cart,cart_array,carti,diw2,dib,logw,logb,se
	global cartframe,cartc,cartc_array,yvar2,rem,qq,cl,xvarray
	
	main2.delete("all")


	main2["width"]=wd-300-7


	#cart.delete("all")


	x_=90+(wd-90-300)/2


	col="#f3f3f3"
	col2="#000000"
	col3="#f3f3f3"
	col4="#f3f3f3"

	if si_con==0:
		v1=0
	if si_con==1 or si_con==2:
		v1=1
	pic_="s"



	rem=ImageTk.PhotoImage(file="data/remove.png")


	

	draw_main1()





	searche.focus_set()


	



	main1.create_oval(x_-150-15,10, x_-150+15,40,fill="#ffffff",outline="#ffffff")
	main1.create_oval(x_+150-15,10, x_+150+15,40,fill="#ffffff",outline="#ffffff")

	main1.create_rectangle(x_-150,10, x_+150,40,fill="#ffffff",outline="#ffffff")





	se=ImageTk.PhotoImage(file="data/search.png")
	qq=ImageTk.PhotoImage(file="data/quitb.png")
	cl=ImageTk.PhotoImage(file="data/checklist.png")

	main1.create_image(x_+150+50-30,15,image=se,anchor="nw")










	searche.place(in_=root,x=x_-148,y=14)

	si_quantity.place_forget()
	psoldat.place_forget()
	si_desc.place_forget()

	psoldat.delete(0,tk.END)
	si_quantity.delete(0,tk.END)

	sellarray=[]


	main2["bg"]=col
	n=0

	dbstock=db.connect('data/stock.db')
	cur=dbstock.cursor()

	cur.execute("SELECT * FROM items ORDER BY name ASC")

	rows=cur.fetchall()


	_items=[]
	for row in rows:

		con=0

		ss=searche.get().lower().split(" ")

		for s in ss:
			if not s==" ":
				if s=="":

					if len(ss)==1:
						if ss[0]==s:
							if not con==1:
								if not row[1].lower().find(s)==-1:
									con=1
									n+=1

									_items.append(row)
				else:
					if not con==1:
						if not row[1].lower().find(s)==-1:
							con=1
							n+=1

							_items.append(row)


		if con==0:
			for s in ss:
				if not s==" ":
					if s=="":
						if len(ss)==1:
							if ss[0]==s:

								if not con==2:

									if not row[-2].lower().find(s)==-1:
										con=2
										
										n+=1

										_items.append(row)

					else:			
						if not con==2:

							if not row[-2].lower().find(s)==-1:
								con=2
								
								n+=1

								_items.append(row)


	def getsiz():
		global wd
		n=1

		while 1:
			xx_=(wd-90-300-(154*n)-20)/(n+1)


			if xx_<20:
				return [n-1,(wd-90-300-(154*(n-1))-20)/(n)]

			n+=1



	xx=90+10

	e,bx=getsiz()


		
		
	

	b=int(n/e)
	c=n%e

	if c>0:
		b+=1

	count=0

	nn=0
	y=10

	con=0
	for a in range(b):
		x=xx

		for s in range(e):

			

			conn=0
			


			if main2.canvasy(0)<=y<=main2.canvasy(ht-50):
				conn=1


			if  main2.canvasy(0)<=y+300<=main2.canvasy(ht-50):
				conn=1

			if conn==1:

				sellarray.append([_items[count][0], x+bx,y,x+bx+154,y+195])

				main2.create_rectangle(x+bx,y, x+bx+154-1,y+195,fill="#ffffff",outline="#cccccc")



				if _items[count][6]==1:

					



					f="Images"
					dir_=os.listdir(f)


					for a in dir_:


						try:
							if int(a.split(".")[0])==_items[count][0]:
								ext=a.split(".")[-1]

								xvarray[nn]=ImageTk.PhotoImage(file="Images/"+str(_items[count][0])+"_"+pic_+"."+ext)

								main2.create_image(x+bx+2,y+2,anchor="nw",image=xvarray[nn])

								nn+=1


						except:
							pass


				coll=col4
				w=1

				for c in cart_array:


					if int(_items[count][0])==int(c[0]):

						if si_con==0:

							coll="#fa677f"
							#w=2

							


							main2.create_oval(x+bx+154-15-5-2.5,y+5+2.5, x+bx+154-5-2.5,y+5+2.5+15,fill="#ffffff",
								outline="#ffffff")

							main2.create_image(x+bx+154-5-20,y+5,image=cl,anchor="nw")
							
							#coll="#000000"
							




						


				
				name=_items[count][1]
				price=_items[count][3]
				items_=_items[count][4]
				desc=_items[count][-2]

				if len(desc)==0:
					desc="No Description"

				main2.create_text(x+bx+10,y+100+20,anchor="w",text=str(name).lower()[:32],font=("FreeMono","13"),fill=col2)
				main2.create_text(x+bx+10,y+100+20+30,anchor="w",text=add_comma(str(price)[:32])+" Ksh",font=("FreeMono","13"),fill=col2)
				main2.create_text(x+bx+10,y+100+20+60,anchor="w",text=add_comma(str(items_)[:32])+" items",font=("FreeMono","13"),fill="#777777")
				

			x+=154+bx
			count+=1

			if count==n:
				con=1
				break
		y+=195+30
		if con==1:
			break


	yvar=y
	main2["scrollregion"]=(0,0,wd,yvar+50)



	if v1==1:
		searche.place_forget()

		create_rectangle(main2,0, int(main2.canvasy(0)), wd, int(main2.canvasy(0)+ht-50), fill='#000000', alpha=.5)

		#create_rectangle(main1,0, 0, wd, 50, fill='#000000', alpha=.8)

		#main1.create_image(wd-20-25,10,image=logw,anchor="nw")


	if si_con==1:

		vbar1.pack_forget()

		main2["width"]=wd-300

		searche.place_forget()
		yy=main2.canvasy(0)

		x1,y1=90+(wd-800-90-300)/2,((ht-50)-500)/2+yy




		dbstock=db.connect('data/stock.db')
		cur=dbstock.cursor()



		cur.execute("SELECT * FROM items WHERE items_id="+str(seli)+"")

		rows=cur.fetchall()

		for row in rows:
			id_=str(row[0])
			name2=str(row[1])
			price=str(row[3])
			quant=str(row[4])
			desc=str(row[5])
			pic=row[6]




		main2.create_oval(x1,y1,x1+20,y1+20,fill="#ffffff",outline="#ffffff")
		main2.create_oval(x1,y1+480,x1+20,y1+500,fill="#ffffff",outline="#ffffff")

		main2.create_oval(x1+780,y1,x1+800,y1+20,fill="#ffffff",outline="#ffffff")
		main2.create_oval(x1+780,y1+480,x1+800,y1+500,fill="#ffffff",outline="#ffffff")

		main2.create_polygon(x1+10,y1, x1+790,y1, x1+800,y1+10, x1+800,y1+490,
			x1+790,y1+500, x1+10,y1+500,x1,y1+490, x1,y1+10,fill="#ffffff",outline="#ffffff")


		main2.create_image(x1+785-5-15+40+2.5,y1,image=qq,anchor="nw")

		main2.create_line(x1+500,y1+20,x1+500,y1+480,fill="#f3f3f3",width=1)

		main2.create_text(x1+250,y1+20,text=name2.upper()[:36],fill="#000000",font=("FreeMono",15,))

		main2.create_text(x1+500+20,y1+70, fill="#000000",font=("FreeMono",13),text="Price",anchor="w")
		main2.create_text(x1+500+20+90,y1+70, fill="#000000",font=("FreeMono",13),text=add_comma(price),anchor="w")
		main2.create_text(x1+500+20,y1+70+40, fill="#000000",font=("FreeMono",13),text="Items left"
			,anchor="w")

		main2.create_text(x1+500+20+90,y1+70+40, fill="#000000",font=("FreeMono",13),text=add_comma(quant),anchor="w")

		main2.create_line(x1+500+30,y1+140, x1+800-30,y1+140,fill="#f3f3f3" )

		main2.create_text(x1+500+20,y1+170,fill="#000000",text="Sold at",font=("FreeMono",13),anchor="w")
		main2.create_text(x1+500+20,y1+170+40,fill="#000000",text="Quantity",font=("FreeMono",13),anchor="w")


		main2.create_arc(x1+500+120-2,y1+170-10-2, x1+500+120-2+10,y1+170-10-2+10,style="arc",start=90,extent=90,outline="#000000")
		main2.create_arc(x1+500+120-2,y1+170-10+100-50-20-5-10, x1+500+120-2+10,y1+170-10+100-50-20-5,style="arc",start=180,extent=90,outline="#000000")

		main2.create_arc(x1+500+120+200-90+3-10,y1+170-10-2, x1+500+120+200-90+3,y1+170-10-2+10,style="arc",start=0,extent=90,outline="#000000")
		main2.create_arc(x1+500+120+200-90+3-10,y1+170-10+100-50-20-5-10, x1+500+120+200-90+3,y1+170-10+100-50-20-5,style="arc",start=270,extent=90,outline="#000000")

		main2.create_line(x1+500+120-2+5,y1+170-10-2, x1+500+120+200-90+3-5+1,y1+170-10-2,fill="#000000")
		main2.create_line(x1+500+120-2+5,y1+170-10+100-50-20-5, x1+500+120+200-90+3-5,y1+170-10+100-50-20-5,fill="#000000")

		main2.create_line(x1+500+120-2,y1+170-10-2+5, x1+500+120-2,y1+170-10+100-50-20-5-5,fill="#000000")
		main2.create_line(x1+500+120+200-90+3,y1+170-10-2+5, x1+500+120+200-90+3,y1+170-10+100-50-20-5-5,fill="#000000")






		main2.create_arc(x1+500+120-2,y1+170-10-2+40, x1+500+120-2+10,y1+170-10-2+10+40,style="arc",start=90,extent=90,outline="#000000")
		main2.create_arc(x1+500+120-2,y1+170-10+100-50-20-5-10+40, x1+500+120-2+10,y1+170-10+100-50-20-5+40,style="arc",start=180,extent=90,outline="#000000")

		main2.create_arc(x1+500+120+200-90+3-10,y1+170-10-2+40, x1+500+120+200-90+3,y1+170-10-2+10+40,style="arc",start=0,extent=90,outline="#000000")
		main2.create_arc(x1+500+120+200-90+3-10,y1+170-10+100-50-20-5-10+40, x1+500+120+200-90+3,y1+170-10+100-50-20-5+40,style="arc",start=270,extent=90,outline="#000000")

		main2.create_line(x1+500+120-2+5,y1+170-10-2+40, x1+500+120+200-90+3-5+1,y1+170-10-2+40,fill="#000000")
		main2.create_line(x1+500+120-2+5,y1+170-10+100-50-20-5+40, x1+500+120+200-90+3-5,y1+170-10+100-50-20-5+40,fill="#000000")

		main2.create_line(x1+500+120-2,y1+170-10-2+5+40, x1+500+120-2,y1+170-10+100-50-20-5-5+40,fill="#000000")
		main2.create_line(x1+500+120+200-90+3,y1+170-10-2+5+40, x1+500+120+200-90+3,y1+170-10+100-50-20-5-5+40,fill="#000000")





		psoldat.delete(0,tk.END)
		si_quantity.delete(0,tk.END)

		psoldat.insert(0,price)
		si_quantity.insert(0,str(1))


		psoldat.focus_set()


		psoldat.place(in_=root,x=x1+500+120+1+5-3,y=((ht-50)-500)/2+189.5+21+1)
		si_quantity.place(in_=root,x=x1+500+120+5-3,y=((ht-50)-500)/2+189.5+21+40+1)

		si_desc.place(in_=root,x=x1+55+40+5-7,y=((ht-50)-500)/2+469.5)

		
		si_desc["fg"]="#000000"
		if len(desc)>35:



			si_desc["text"]=desc[:35]+"..."


		else:
			si_desc["text"]=desc





		pos=[x1,y1]

		#main2.create_rectangle(x1+500+20,y1+500-50-80,x1+500+300-20,y1+500-50-70+20,fill="#ffffff",outline="#000000",width=2)


		main2.create_text(x1+500+20,y1+500-50-70+5+30,text="Total",fill="red",font=
			("FreeMono",13),anchor="w")

		total=main2.create_text(x1+500+300-20,y1+500-50-70+5+30,text="0",fill="#000000",font=
			("FreeMono",13),anchor="e")




		#main2.create_rectangle(x1+500+40+30,y1+500-50-30+30, x1+800-40-30,y1+500-50+30,fill="cyan",outline="cyan")
		#main2.create_oval(x1+500+40+30-15,y1+500-50-30+30, x1+500+40+30+15,y1+500-50+30,fill="cyan",outline="cyan")
		#main2.create_oval(x1+800-40-30-15,y1+500-50-30+30, x1+800-40-30+15,y1+500-50+30,fill="cyan",outline="cyan" )


		main2.create_arc(x1+500+40+30-15,y1+500-50-30+30, x1+500+40+30+15,y1+500-50+30,
			style="arc",outline="#000000",start=90,extent=180)
		main2.create_arc(x1+800-40-30-15,y1+500-50-30+30, x1+800-40-30+15,y1+500-50+30,
			style="arc",outline="#000000",start=270,extent=180)
		main2.create_line(x1+500+40+30,y1+500-50-30+30, x1+800-40-30,y1+500-50-30+30,fill="#000000")
		main2.create_line(x1+500+40+30-1,y1+500-50+30, x1+800-40-30,y1+500-50+30,fill="#000000")


		main2.create_text(x1+500+150,y1+500-50-15+30,fill="#000000",text="Add to cart",font=("FreeMono",13))



		if pic==1:

			f="Images"
			dir_=os.listdir(f)

			for a in dir_:
				if a.split(".")[0]==str(id_):
					ext=a.split(".")[-1]

			im=Image.open("images/"+str(id_)+"."+ext)
			x,y=im.size

			if (x/y)>(400/300):

				bx=400
				by=int(y*(400/x))

				ax=50
				ay=100

				ay+=(300-by)/2

			elif (x/y)<(400/300):
				by=300
				bx=int(x*300/y)
				ay=100
				ax=50

				ax+=(400-bx)/2
			elif (x/y)==(400/300):
				bx=400
				by=300
				ax=50
				ay=100

			im=im.resize((bx,by))

			im.save("data/m."+ext)
			global se_image
			
			se_image=ImageTk.PhotoImage(file="data/m."+ext)

			main2.create_image(x1+ax,y1+ay,image=se_image,anchor="nw")


def gentotal():
	global main2,total,si_con,dashb_state,pos,psoldat,si_quantity,total_

	if si_con==1 and dashb_state=="sell_items":

		try:

			v1=int(psoldat.get())
			v2=int(si_quantity.get())

			total_=v1*v2
			main2.delete(total)


			x,y=pos[0],pos[1]
			total=main2.create_text(x+500+300-30,y+500-50-70+5+30,text=add_comma(str(total_)),fill="#000000",font=
			("FreeMono",13),anchor="e")
		except:
			x,y=pos[0],pos[1]
			main2.delete(total)
			total=main2.create_text(x+500+300-30,y+500-50-70+5+30,text="0",fill="#000000",font=
			("FreeMono",13),anchor="e")

	root.after(1,gentotal)
		
		



si_con=0
sellarray=[]
seli=0

se_image=""
total=()
total_=0
pos=[]

def psoldate(e):
	global si_quantity

	si_quantity.focus_set()



psoldat=tk.Entry(width=12,bg="#ffffff",relief="flat", highlightthickness=0,border=0,font=
	("FreeMono",13),fg="#000000")
psoldat.bind("<Return>",psoldate)


si_quantity=tk.Entry(width=12,bg="#ffffff",relief="flat", highlightthickness=0,border=0,font=
	("FreeMono",13),fg="#000000")

si_desc=tk.Label(width=35,height=3,bg="#ffffff",relief="flat", highlightthickness=0,border=0,font=
	("FreeMono",13),justify="center",fg="#000000")
# Add stock

def draw_addstock():
	global main1,main2,as_n,as_bp,as_sp,as_q,as_de,dvar2,ascon2,as_im
	global wd,ht,si_quantity,psoldat,ms_con,diw2,logw,qu,bc,myp,info,barc



	as_n.focus_set()

	main2.delete("all")


	

	main2["bg"]="#f3f3f3"

	main2["width"]=wd

	draw_main1()


	x_,y_=90+(wd-90-800)/2,((ht-50)-500)/2


	if myp[-1]==0:

		main1["bg"]="#222222"

		x_,y_=90+(wd-90-800)/2,(ht)/2-50

		info=ImageTk.PhotoImage(file="data/info.png")

		main2.create_image(x_+200+30-10,y_-50,image=info,anchor="nw")

		main2.create_text(x_+200+100+30+30-10,y_,text="Login as Administrator",font=("FreeMono",15),anchor="w",fill="#111111")
		return

	main2["bg"]="#222222"



	main2.create_oval(x_,y_, x_+20,y_+20,outline="#ffffff",fill="#ffffff")
	main2.create_oval(x_-20+800,y_, x_+800,y_+20,outline="#ffffff",fill="#ffffff")
	main2.create_oval(x_,y_+500-20, x_+20,y_+500,outline="#ffffff",fill="#ffffff")
	main2.create_oval(x_-20+800,y_+500-20, x_+800,y_+500,outline="#ffffff",fill="#ffffff")

	main2.create_polygon(x_+10,y_,x_+790,y_, x_+800,y_+10,x_+800,y_+490, x_+790,y_+500,
		x_+10,y_+500, x_,y_+490,x_,y_+10,fill="#ffffff",outline="#ffffff")


	yy=50
	main2.create_text(x_+30,y_+40,text="Name",font=("FreeMono",13),fill="#000000",anchor="w")
	main2.create_text(x_+30,y_+40+yy+10,text="Buying Price",font=("FreeMono",13),fill="#000000",anchor="w")
	main2.create_text(x_+30,y_+40+yy*2+20,text="Selling Price",font=("FreeMono",13),fill="#000000",anchor="w")	
	main2.create_text(x_+30,y_+40+yy*3+30,text="Quantity",font=("FreeMono",13),fill="#000000",anchor="w")


	main2.create_arc(x_+170-2,40+yy+50-13-yy-2-yy+y_, x_+170-2+10,40+yy+50-13-yy-2-yy+y_+10,
		style="arc",start=90,extent=90,outline="#777777")
	main2.create_arc(x_+170-2,40+yy+50-13-yy+28-yy-3+y_-10, x_+170-2+10,40+yy+50-13-yy+28-yy-3+y_,
		style="arc",start=180,extent=90,outline="#777777")
	main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy-2-yy+y_, x_+170+170-2,40+yy+50-13-yy-2-yy+y_+10,
		style="arc",start=0,extent=90,outline="#777777")
	main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy+28-yy-3+y_-10, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_,
		style="arc",start=270,extent=90,outline="#777777")
	main2.create_line(x_+170-2+5,40+yy+50-13-yy-2-yy+y_, x_+170+170-2-5+1,40+yy+50-13-yy-2-yy+y_,fill="#777777")
	main2.create_line(x_+170-2+5,40+yy+50-13-yy+28-yy-3+y_, x_+170+170-2-5,40+yy+50-13-yy+28-yy-3+y_,fill="#777777")
	main2.create_line(x_+170-2,40+yy+50-13-yy-2-yy+y_+5, x_+170-2,40+yy+50-13-yy+28-yy-3+y_-5,fill="#777777")
	main2.create_line(x_+170+170-2,40+yy+50-13-yy-2-yy+y_+5, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_-5,fill="#777777")


	main2.create_arc(x_+170-2,40+yy+50-13-yy-2-yy+y_+50+10, x_+170-2+10,40+yy+50-13-yy-2-yy+y_+10+50+10,
		style="arc",start=90,extent=90,outline="#777777")
	main2.create_arc(x_+170-2,40+yy+50-13-yy+28-yy-3+y_-10+50+10, x_+170-2+10,40+yy+50-13-yy+28-yy-3+y_+50+10,
		style="arc",start=180,extent=90,outline="#777777")
	main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy-2-yy+y_+50+10, x_+170+170-2,40+yy+50-13-yy-2-yy+y_+10+50+10,
		style="arc",start=0,extent=90,outline="#777777")
	main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy+28-yy-3+y_-10+50+10, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_+50+10,
		style="arc",start=270,extent=90,outline="#777777")
	main2.create_line(x_+170-2+5,40+yy+50-13-yy-2-yy+y_+50+10, x_+170+170-2-5+1,40+yy+50-13-yy-2-yy+y_+50+10,fill="#777777")
	main2.create_line(x_+170-2+5,40+yy+50-13-yy+28-yy-3+y_+50+10, x_+170+170-2-5,40+yy+50-13-yy+28-yy-3+y_+50+10,fill="#777777")
	main2.create_line(x_+170-2,40+yy+50-13-yy-2-yy+y_+5+50+10, x_+170-2,40+yy+50-13-yy+28-yy-3+y_-5+50+10,fill="#777777")
	main2.create_line(x_+170+170-2,40+yy+50-13-yy-2-yy+y_+5+50+10, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_-5+50+10,fill="#777777")





	main2.create_arc(x_+170-2,40+yy+50-13-yy-2-yy+y_+100+20, x_+170-2+10,40+yy+50-13-yy-2-yy+y_+10+100+20,
		style="arc",start=90,extent=90,outline="#777777")
	main2.create_arc(x_+170-2,40+yy+50-13-yy+28-yy-3+y_-10+100+20, x_+170-2+10,40+yy+50-13-yy+28-yy-3+y_+100+20,
		style="arc",start=180,extent=90,outline="#777777")
	main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy-2-yy+y_+100+20, x_+170+170-2,40+yy+50-13-yy-2-yy+y_+10+100+20,
		style="arc",start=0,extent=90,outline="#777777")
	main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy+28-yy-3+y_-10+100+20, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_+100+20,
		style="arc",start=270,extent=90,outline="#777777")
	main2.create_line(x_+170-2+5,40+yy+50-13-yy-2-yy+y_+100+20, x_+170+170-2-5+1,40+yy+50-13-yy-2-yy+y_+100+20,fill="#777777")
	main2.create_line(x_+170-2+5,40+yy+50-13-yy+28-yy-3+y_+100+20, x_+170+170-2-5,40+yy+50-13-yy+28-yy-3+y_+100+20,fill="#777777")
	main2.create_line(x_+170-2,40+yy+50-13-yy-2-yy+y_+5+100+20, x_+170-2,40+yy+50-13-yy+28-yy-3+y_-5+100+20,fill="#777777")
	main2.create_line(x_+170+170-2,40+yy+50-13-yy-2-yy+y_+5+100+20, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_-5+100+20,fill="#777777")





	main2.create_arc(x_+170-2,40+yy+50-13-yy-2-yy+y_+150+30, x_+170-2+10,40+yy+50-13-yy-2-yy+y_+10+150+30,
		style="arc",start=90,extent=90,outline="#777777")
	main2.create_arc(x_+170-2,40+yy+50-13-yy+28-yy-3+y_-10+150+30, x_+170-2+10,40+yy+50-13-yy+28-yy-3+y_+150+30,
		style="arc",start=180,extent=90,outline="#777777")
	main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy-2-yy+y_+150+30, x_+170+170-2,40+yy+50-13-yy-2-yy+y_+10+150+30,
		style="arc",start=0,extent=90,outline="#777777")
	main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy+28-yy-3+y_-10+150+30, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_+150+30,
		style="arc",start=270,extent=90,outline="#777777")
	main2.create_line(x_+170-2+5,40+yy+50-13-yy-2-yy+y_+150+30, x_+170+170-2-5+1,40+yy+50-13-yy-2-yy+y_+150+30,fill="#777777")
	main2.create_line(x_+170-2+5,40+yy+50-13-yy+28-yy-3+y_+150+30, x_+170+170-2-5,40+yy+50-13-yy+28-yy-3+y_+150+30,fill="#777777")
	main2.create_line(x_+170-2,40+yy+50-13-yy-2-yy+y_+5+150+30, x_+170-2,40+yy+50-13-yy+28-yy-3+y_-5+150+30,fill="#777777")
	main2.create_line(x_+170+170-2,40+yy+50-13-yy-2-yy+y_+5+150+30, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_-5+150+30,fill="#777777")


	as_n.place(in_=root,x=x_+171,y=40+yy+50-13-yy+y_+1)
	as_bp.place(in_=root,x=x_+171,y=40+yy+50-13+y_+1+10)
	as_sp.place(in_=root,x=x_+171,y=40+yy+50-13+yy+y_+1+20)
	as_q.place(in_=root,x=x_+171,y=40+yy+50-13+yy+yy+y_+1+30)



	#main2.create_rectangle(x_+30,y_+300, x_+30+320,y_+300+100,fill="red")

	main2.create_text(x_+50+5,y_+300+25+2-70+66,text="Description",anchor="sw",font=("FreeMono",13),fill="#000000")


	main2.create_arc(x_+30,y_+300-5+25-70+66, x_+30+10,y_+300-5+25+10-70+66,style="arc",start=90,extent=90,outline="#777777")
	main2.create_arc(x_+30, y_+300+95+25-10-70+5+66, x_+30+10, y_+300+95+25-70+5+66,style="arc",start=180,extent=90,outline="#777777")
	main2.create_arc(x_+300+40-10, y_+300+95+25-10-70+5+66, x_+300+40, y_+300+95+25-70+5+66,style="arc",start=270,extent=90,outline="#777777")
	main2.create_arc(x_+300+40-10, y_+300-5+25-70+66, x_+300+40, y_+300-5+25+10-70+66,style="arc",start=0,extent=90,outline="#777777")

	main2.create_line(x_+30+20,y_+300-5+25-70+66, x_+30+5,y_+300-5+25-70+66,fill="#777777")
	main2.create_line(x_+30,y_+300-5+25+5-70+66, x_+30, y_+300+95+25-5-70+5+66,fill="#777777")
	main2.create_line(x_+30+5, y_+300+95+25-70+5+66, x_+300+40-5, y_+300+95+25-70+5+66,fill="#777777")
	main2.create_line(x_+300+40, y_+300+95+25-5-70+5+66,x_+300+40, y_+300-5+25+4-70+66,fill="#777777")
	main2.create_line(x_+300+40-5, y_+300-5+25-70+66 ,x_+300+40-190+5-15, y_+300-5+25-70+66,fill="#777777")


	as_de.place(in_=root,x=x_+30+5,y=y_+300+50+25-70+66)

	#main2.create_rectangle(x_+400-20-1,y_+20-1, x_+400+400-20,y_+20+400,fill="#ffffff",outline="#333333")



	main2.create_text(x_-20+400+200,y_+100+20,text="Add Image",fill="#777777", font=("FreeMono",30))

	main2.create_oval(x_-20+400+200-40,y_+20+200-40, x_-20+400+200+40,y_+20+200+40, fill="#ffffff", outline="#777777",width=1 )

	main2.create_line(x_-20+400+200,y_+20+200-20, x_-20+400+200,y_+20+200+20,fill="#777777",width=1 )
	main2.create_line(x_-20+400-20+200,y_+20+200, x_-20+400+200+20,y_+20+200,fill="#777777",width=1 )

	qu=ImageTk.PhotoImage(file="data/quitb.png")


	main2.create_image(x_+400+400-20-15+5-12.5,y_+20+400+15-12.5,image=qu,anchor="nw")

	#main2.create_line(x_+400+400-20-15-5+5,y_+20+400+15-5, x_+400+400-20-15+5+5,y_+20+400+15+5,fill="red",width=2)
	#main2.create_line(x_+400+400-20-15-5+5,y_+20+400+15+5, x_+400+400-20-15+5+5,y_+20+400+15-5,fill="#000000",width=2)

	if ascon2==1:
		main2.create_text(x_+400, y_+500-60,text="Fill all fields.",fill="red",font=("FreeMono",13))


	if not as_image=="":
		as_im=main2.create_image(x_+400-20+ax,y_+20+ay,image=as_image,anchor="nw")


	cx,cy=x_+400-20-1+10,y_+20-1+10
	ar=[x_+400-20-1,y_+20-1]
	a_=180
	for a in range(90):
		x=10*math.sin(math.radians(a_))+cx
		y=10*math.cos(math.radians(a_))+cy
		ar.append(x)
		ar.append(y)

		a_+=1
	ar.append(x_+400-20-1)
	ar.append(y_+20-1)

	main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")


	cx,cy=x_+400-20-1+10,y_+20+400-10
	ar=[x_+400-20-1,y_+20+400]
	a_=270
	for a in range(90):
		x=10*math.sin(math.radians(a_))+cx
		y=10*math.cos(math.radians(a_))+cy
		ar.append(x)
		ar.append(y)

		a_+=1
	ar.append(x_+400-20-1)
	ar.append(y_+20+400)

	main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")


	cx,cy=x_+400+400-20-10,y_+20+400-10
	ar=[x_+400+400-20,y_+20+400]
	a_=0
	for a in range(90):
		x=10*math.sin(math.radians(a_))+cx
		y=10*math.cos(math.radians(a_))+cy
		ar.append(x)
		ar.append(y)

		a_+=1
	ar.append(x_+400+400-20)
	ar.append(y_+20+400)

	main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")


	cx,cy=x_+400+400-20-10,y_+20-1+10
	ar=[x_+400+400-20,y_+20-1]
	a_=90
	for a in range(90):
		x=10*math.sin(math.radians(a_))+cx
		y=10*math.cos(math.radians(a_))+cy
		ar.append(x)
		ar.append(y)

		a_+=1
	ar.append(x_+400+400-20)
	ar.append(y_+20-1)

	main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")
	#x_+400-20-1,y_+20-1, x_+400+400-20,y_+20+400

	main2.create_arc(x_+400-20-1,y_+20-1, x_+400-20-1+20,y_+20-1+20,style="arc",start=90,extent=90,outline="#777777")
	main2.create_arc(x_+400+400-20,y_+20-1, x_+400+400-20-20,y_+20-1+20,style="arc",start=0,extent=90,outline="#777777")
	main2.create_arc(x_+400+400-20,y_+20+400-20, x_+400+400-20-20,y_+20+400,style="arc",start=270,extent=90,outline="#777777")	
	main2.create_arc(x_+400-20-1,y_+20+400-20, x_+400-20-1+20,y_+20+400,style="arc",start=180,extent=90,outline="#777777")	


	main2.create_line(x_+400-20-1+10,y_+20-1,  x_+400+400-20-10,y_+20-1,fill="#777777" )
	main2.create_line(x_+400-20-1+10-1,y_+20+400,  x_+400+400-20-10,y_+20+400,fill="#777777" )
	main2.create_line(x_+400-20-1,y_+20-1+10-1, x_+400-20-1,y_+20+400-10,fill="#777777" )
	main2.create_line(x_+400+400-20,y_+20-1+10, x_+400+400-20,y_+20+400-10,fill="#777777" )


	#main2.create_rectangle(x_+400-60, y_+500-60+20, x_+400+60,y_+500-30+20,fill="cyan",outline="cyan")
	#main2.create_oval(x_+400-60-15, y_+500-60+20, x_+400-60+15, y_+500-60+20+30,fill="cyan",outline="cyan")
	#main2.create_oval(x_+400+60-15,y_+500-60+20, x_+400+60+15,y_+500-60+20+30,fill="cyan",outline="cyan")

	main2.create_arc(x_+400-60-15, y_+500-60+20, x_+400-60+15, y_+500-60+20+30,style="arc",
		start=90,extent=180,outline="#000000")
	main2.create_arc(x_+400+60-15,y_+500-60+20, x_+400+60+15,y_+500-60+20+30,style="arc",
		start=270,extent=180,outline="#000000")
	main2.create_line(x_+400-60, y_+500-60+20, x_+400+60, y_+500-60+20,fill="#000000")
	main2.create_line(x_+400-60-1, y_+500-30+20, x_+400+60, y_+500-30+20,fill="#000000")


	#main2.create_line(x_+30,y_+20+400, x_+30,y_+20+400-50,fill="red")

	#bc=ImageTk.PhotoImage(file="data/barcode.jpg")


	main2.create_text(x_+400,y_+500-30+20-15,text="Add Stock", fill="#000000",font=("FreeMono",13))




def asne(e):
	global as_bp

	as_bp.focus_set()

def asbpe(e):
	global as_sp

	as_sp.focus_set()

def asspe(e):
	global as_q

	as_q.focus_set()

def asqe(e):
	global as_de

	as_de.focus_set()

ascon=0
ascon2=0
as_n=tk.Entry(bg="#ffffff",width=18,font=("FreeMono",13),relief="flat",highlightthickness=0,border=0)
as_n.bind("<Return>",asne)
as_bp=tk.Entry(bg="#ffffff",width=18,font=("FreeMono",13),relief="flat",highlightthickness=0,border=0)
as_bp.bind("<Return>",asbpe)
as_sp=tk.Entry(bg="#ffffff",width=18,font=("FreeMono",13),relief="flat",highlightthickness=0,border=0)
as_sp.bind("<Return>",asspe)
as_q=tk.Entry(bg="#ffffff",width=18,font=("FreeMono",13),relief="flat",highlightthickness=0,border=0)
as_q.bind("<Return>",asqe)
as_de=tk.Text(bg="#ffffff",width=33,height=5,font=("FreeMono",13),relief="flat",highlightthickness=0,border=0)

# stock

def draw_stock():
	global main1,main2,dvar2,wd, si_con,msarray,ms_con,seli,wd,ht
	global as_n,as_bp,as_sp,as_q,as_de,msimage,msi,yvar,vbar1,svar,searche,diw2,dib,logw,logb,se,qq,qu,bc,myp,info,xvarray
	
	main2.delete("all")

	



	if myp[-1]==0:
		x_,y_=90+(wd-90-800)/2,(ht)/2-50

		main2["width"]=wd



		main1["bg"]="#222222"
		main2["bg"]="#f3f3f3"


		logw=ImageTk.PhotoImage(file="data/logoutw.png")

		main1.create_image(wd-20-25,10,image=logw,anchor="nw")

		vbar1.pack_forget()
		searche.place_forget()

		info=ImageTk.PhotoImage(file="data/info.png")

		main2.create_image(x_+200+30-10,y_-50,image=info,anchor="nw")

		main2.create_text(x_+200+100+30+30-10,y_,text="Login as Administrator",font=("FreeMono",15),anchor="w",fill="#111111")
		return


	col="#f3f3f3"
	col2="#000000"
	col4="#f3f3f3"




	if ms_con==0:
		v1=0
	elif ms_con==1:

		v1=1

	pic_="s"

	as_n.delete(0,tk.END)
	as_bp.delete(0,tk.END)
	as_sp.delete(0,tk.END)
	as_q.delete(0,tk.END)
	as_de.delete(0.0,tk.END)


	draw_main1()


	x_=wd/2

	searche.focus_set()

	main1.create_oval(x_-150-15,10, x_-150+15,40,fill="#ffffff",outline="#ffffff")
	main1.create_oval(x_+150-15,10, x_+150+15,40,fill="#ffffff",outline="#ffffff")

	main1.create_rectangle(x_-150,10, x_+150,40,fill="#ffffff",outline="#ffffff")
		




	se=ImageTk.PhotoImage(file="data/search.png")
	qq=ImageTk.PhotoImage(file="data/quitb.png")
	main1.create_image(x_+150+50-30,15,image=se,anchor="nw")


	





	searche.place(in_=root,x=x_-148,y=14)


	msarray=[]


	main2["bg"]=col
	n=0

	dbstock=db.connect('data/stock.db')
	cur=dbstock.cursor()

	cur.execute("SELECT * FROM items ORDER BY name ASC")

	rows=cur.fetchall()


	_items=[]
	for row in rows:

		con=0

		ss=searche.get().lower().split(" ")

		for s in ss:
			if not s==" ":
				if s=="":

					if len(ss)==1:
						if ss[0]==s:
							if not con==1:
								if not row[1].lower().find(s)==-1:
									con=1
									n+=1

									_items.append(row)
				else:
					if not con==1:
						if not row[1].lower().find(s)==-1:
							con=1
							n+=1

							_items.append(row)


		if con==0:
			for s in ss:
				if not s==" ":
					if s=="":
						if len(ss)==1:
							if ss[0]==s:

								if not con==2:

									if not row[-2].lower().find(s)==-1:
										con=2
										
										n+=1

										_items.append(row)

					else:			
						if not con==2:

							if not row[-2].lower().find(s)==-1:
								con=2
								
								n+=1

								_items.append(row)	
	def getsiz():
		global wd
		n=1

		while 1:
			xx_=(wd-90-(154*n)-20)/(n+1)


			if xx_<20:
				return [n-1,(wd-90-(154*(n-1))-20)/(n)]

			n+=1



	xx=90+10

	e,bx=getsiz()
	

	b=int(n/e)
	c=n%e

	if c>0:
		b+=1

	count=0

	
	y=30

	con=0

	nn=0
	for a in range(b):
		x=xx

		for s in range(e):

			


			conn=0
			


			if main2.canvasy(0)<=y<=main2.canvasy(ht-50):
				conn=1

			if  main2.canvasy(0)<=y+300<=main2.canvasy(ht-50):
				conn=1

			if conn==1:

				msarray.append([_items[count][0], x+bx,y,x+bx+154,y+195])


				main2.create_rectangle(x+bx,y,x+bx+154,y+195,fill="#ffffff",outline="#cccccc")

				if _items[count][6]==1:

					



					f="Images"
					dir_=os.listdir(f)


					for a in dir_:


						try:
							if int(a.split(".")[0])==_items[count][0]:
								ext=a.split(".")[-1]

								xvarray[nn]=ImageTk.PhotoImage(file="Images/"+str(_items[count][0])+"_"+pic_+"."+ext)

								main2.create_image(x+bx+2,y+2,anchor="nw",image=xvarray[nn])

								nn+=1


						except:
							pass


		



						


				
				name=_items[count][1]
				price=_items[count][3]
				items_=_items[count][4]
				desc=_items[count][-2]

				if len(desc)==0:
					desc="No Description"

				main2.create_text(x+bx+10,y+100+20,anchor="w",text=str(name).lower()[:32],font=("FreeMono","13"),fill=col2)
				main2.create_text(x+bx+10,y+100+20+30,anchor="w",text=add_comma(str(price)[:32])+" Ksh",font=("FreeMono","13"),fill=col2)
				main2.create_text(x+bx+10,y+100+20+60,anchor="w",text=add_comma(str(items_)[:32])+" items",font=("FreeMono","13"),fill="#777777")



			x+=154+bx
			count+=1

			if count==n:
				con=1
				break
		y+=195+30
		if con==1:
			break





	yvar=y
	main2["scrollregion"]=(0,0,wd,y)
	if v1==1:
		searche.place_forget()

		create_rectangle(main2,0, int(main2.canvasy(0)), wd, int(main2.canvasy(0)+ht-50), fill='#000000', alpha=.5)

		main1.create_image(wd-20-25,10,image=logw,anchor="nw")







	x_,y_=90+(wd-90-800)/2,((ht-50)-500)/2+main2.canvasy(0)







	if ms_con==1:
		as_n.focus_set()

		main2.create_oval(x_,y_,x_+20,y_+20,fill="#ffffff",outline="#ffffff")
		main2.create_oval(x_,y_+480,x_+20,y_+500,fill="#ffffff",outline="#ffffff")

		main2.create_oval(x_+780,y_,x_+800,y_+20,fill="#ffffff",outline="#ffffff")
		main2.create_oval(x_+780,y_+480,x_+800,y_+500,fill="#ffffff",outline="#ffffff")

		main2.create_polygon(x_+10,y_, x_+790,y_, x_+800,y_+10, x_+800,y_+490,
			x_+790,y_+500, x_+10,y_+500,x_,y_+490, x_,y_+10,fill="#ffffff",outline="#ffffff")


		main2.create_image(x_+785-5-15+40+2.5,y_,image=qq,anchor="nw")

		vbar1.pack_forget()
		searche.place_forget()


		dbstock=db.connect('data/stock.db')
		cur=dbstock.cursor()



		cur.execute("SELECT * FROM items WHERE items_id="+str(seli)+"")

		rows=cur.fetchall()

		p=""
		for row in rows:
			name_=str(row[1])
			bp=str(row[2])
			sp=str(row[3])
			q=str(row[4])
			de=str(row[5])

			p=row[6]

			as_n.insert(0,name_)
			as_bp.insert(0,bp)
			as_sp.insert(0,sp)
			as_q.insert(0,q)
			as_de.insert("1.0",de)






		yy=50



		main2.create_arc(x_+170-2,40+yy+50-13-yy-2-yy+y_, x_+170-2+10,40+yy+50-13-yy-2-yy+y_+10,
			style="arc",start=90,extent=90,outline="#777777")
		main2.create_arc(x_+170-2,40+yy+50-13-yy+28-yy-3+y_-10, x_+170-2+10,40+yy+50-13-yy+28-yy-3+y_,
			style="arc",start=180,extent=90,outline="#777777")
		main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy-2-yy+y_, x_+170+170-2,40+yy+50-13-yy-2-yy+y_+10,
			style="arc",start=0,extent=90,outline="#777777")
		main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy+28-yy-3+y_-10, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_,
			style="arc",start=270,extent=90,outline="#777777")
		main2.create_line(x_+170-2+5,40+yy+50-13-yy-2-yy+y_, x_+170+170-2-5+1,40+yy+50-13-yy-2-yy+y_,fill="#777777")
		main2.create_line(x_+170-2+5,40+yy+50-13-yy+28-yy-3+y_, x_+170+170-2-5,40+yy+50-13-yy+28-yy-3+y_,fill="#777777")
		main2.create_line(x_+170-2,40+yy+50-13-yy-2-yy+y_+5, x_+170-2,40+yy+50-13-yy+28-yy-3+y_-5,fill="#777777")
		main2.create_line(x_+170+170-2,40+yy+50-13-yy-2-yy+y_+5, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_-5,fill="#777777")


		main2.create_arc(x_+170-2,40+yy+50-13-yy-2-yy+y_+50+10, x_+170-2+10,40+yy+50-13-yy-2-yy+y_+10+50+10,
			style="arc",start=90,extent=90,outline="#777777")
		main2.create_arc(x_+170-2,40+yy+50-13-yy+28-yy-3+y_-10+50+10, x_+170-2+10,40+yy+50-13-yy+28-yy-3+y_+50+10,
			style="arc",start=180,extent=90,outline="#777777")
		main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy-2-yy+y_+50+10, x_+170+170-2,40+yy+50-13-yy-2-yy+y_+10+50+10,
			style="arc",start=0,extent=90,outline="#777777")
		main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy+28-yy-3+y_-10+50+10, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_+50+10,
			style="arc",start=270,extent=90,outline="#777777")
		main2.create_line(x_+170-2+5,40+yy+50-13-yy-2-yy+y_+50+10, x_+170+170-2-5+1,40+yy+50-13-yy-2-yy+y_+50+10,fill="#777777")
		main2.create_line(x_+170-2+5,40+yy+50-13-yy+28-yy-3+y_+50+10, x_+170+170-2-5,40+yy+50-13-yy+28-yy-3+y_+50+10,fill="#777777")
		main2.create_line(x_+170-2,40+yy+50-13-yy-2-yy+y_+5+50+10, x_+170-2,40+yy+50-13-yy+28-yy-3+y_-5+50+10,fill="#777777")
		main2.create_line(x_+170+170-2,40+yy+50-13-yy-2-yy+y_+5+50+10, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_-5+50+10,fill="#777777")





		main2.create_arc(x_+170-2,40+yy+50-13-yy-2-yy+y_+100+20, x_+170-2+10,40+yy+50-13-yy-2-yy+y_+10+100+20,
			style="arc",start=90,extent=90,outline="#777777")
		main2.create_arc(x_+170-2,40+yy+50-13-yy+28-yy-3+y_-10+100+20, x_+170-2+10,40+yy+50-13-yy+28-yy-3+y_+100+20,
			style="arc",start=180,extent=90,outline="#777777")
		main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy-2-yy+y_+100+20, x_+170+170-2,40+yy+50-13-yy-2-yy+y_+10+100+20,
			style="arc",start=0,extent=90,outline="#777777")
		main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy+28-yy-3+y_-10+100+20, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_+100+20,
			style="arc",start=270,extent=90,outline="#777777")
		main2.create_line(x_+170-2+5,40+yy+50-13-yy-2-yy+y_+100+20, x_+170+170-2-5+1,40+yy+50-13-yy-2-yy+y_+100+20,fill="#777777")
		main2.create_line(x_+170-2+5,40+yy+50-13-yy+28-yy-3+y_+100+20, x_+170+170-2-5,40+yy+50-13-yy+28-yy-3+y_+100+20,fill="#777777")
		main2.create_line(x_+170-2,40+yy+50-13-yy-2-yy+y_+5+100+20, x_+170-2,40+yy+50-13-yy+28-yy-3+y_-5+100+20,fill="#777777")
		main2.create_line(x_+170+170-2,40+yy+50-13-yy-2-yy+y_+5+100+20, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_-5+100+20,fill="#777777")


		main2.create_arc(x_+170-2,40+yy+50-13-yy-2-yy+y_+150+30, x_+170-2+10,40+yy+50-13-yy-2-yy+y_+10+150+30,
			style="arc",start=90,extent=90,outline="#777777")
		main2.create_arc(x_+170-2,40+yy+50-13-yy+28-yy-3+y_-10+150+30, x_+170-2+10,40+yy+50-13-yy+28-yy-3+y_+150+30,
			style="arc",start=180,extent=90,outline="#777777")
		main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy-2-yy+y_+150+30, x_+170+170-2,40+yy+50-13-yy-2-yy+y_+10+150+30,
			style="arc",start=0,extent=90,outline="#777777")
		main2.create_arc(x_+170+170-2-10,40+yy+50-13-yy+28-yy-3+y_-10+150+30, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_+150+30,
			style="arc",start=270,extent=90,outline="#777777")
		main2.create_line(x_+170-2+5,40+yy+50-13-yy-2-yy+y_+150+30, x_+170+170-2-5+1,40+yy+50-13-yy-2-yy+y_+150+30,fill="#777777")
		main2.create_line(x_+170-2+5,40+yy+50-13-yy+28-yy-3+y_+150+30, x_+170+170-2-5,40+yy+50-13-yy+28-yy-3+y_+150+30,fill="#777777")
		main2.create_line(x_+170-2,40+yy+50-13-yy-2-yy+y_+5+150+30, x_+170-2,40+yy+50-13-yy+28-yy-3+y_-5+150+30,fill="#777777")
		main2.create_line(x_+170+170-2,40+yy+50-13-yy-2-yy+y_+5+150+30, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_-5+150+30,fill="#777777")




		main2.create_text(x_+30,y_+40,text="Name",font=("FreeMono",13),fill="#000000",anchor="w")
		main2.create_text(x_+30,y_+40+yy+10,text="Buying Price",font=("FreeMono",13),fill="#000000",anchor="w")
		main2.create_text(x_+30,y_+40+yy*2+20,text="Selling Price",font=("FreeMono",13),fill="#000000",anchor="w")	
		main2.create_text(x_+30,y_+40+yy*3+30,text="Quantity",font=("FreeMono",13),fill="#000000",anchor="w")


		as_n.place(in_=root,x=x_+171+5,y=1+40+yy+50-13-yy+y_-main2.canvasy(0))
		as_bp.place(in_=root,x=x_+171+5,y=1+40+yy+50-13+y_-main2.canvasy(0)+10)
		as_sp.place(in_=root,x=x_+171+5,y=1+40+yy+50-13+yy+y_-main2.canvasy(0)+20)
		as_q.place(in_=root,x=x_+171+5,y=1+40+yy+50-13+yy+yy+y_-main2.canvasy(0)+30)


		main2.create_text(x_+50+5,y_+300+25+2-70+66,text="Description",anchor="sw",font=("FreeMono",13),fill="#000000")
	



		main2.create_arc(x_+30,y_+300-5+25-70+66, x_+30+10,y_+300-5+25+10-70+66,style="arc",start=90,extent=90,outline="#777777")
		main2.create_arc(x_+30, y_+300+95+25-10-70+5+66, x_+30+10, y_+300+95+25-70+5+66,style="arc",start=180,extent=90,outline="#777777")
		main2.create_arc(x_+300+40-10, y_+300+95+25-10-70+5+66, x_+300+40, y_+300+95+25-70+5+66,style="arc",start=270,extent=90,outline="#777777")
		main2.create_arc(x_+300+40-10, y_+300-5+25-70+66, x_+300+40, y_+300-5+25+10-70+66,style="arc",start=0,extent=90,outline="#777777")

		main2.create_line(x_+30+10+10,y_+300-5+25-70+66, x_+30+5,y_+300-5+25-70+66,fill="#777777")
		main2.create_line(x_+30,y_+300-5+25+5-70+66, x_+30, y_+300+95+25-5-70+5+66,fill="#777777")
		main2.create_line(x_+30+5, y_+300+95+25-70+5+66, x_+300+40-5, y_+300+95+25-70+5+66,fill="#777777")
		main2.create_line(x_+300+40, y_+300+95+25-5-70+5+66,x_+300+40, y_+300-5+25+4-70+66,fill="#777777")
		main2.create_line(x_+300+40-5, y_+300-5+25-70+66,x_+300+40-190+5-15, y_+300-5+25-70+66,fill="#777777")




		as_de["fg"]="#000000"


		as_de.place(in_=root,x=x_+30+5+5,y=y_+300+50+25-main2.canvasy(0)-70+66)

		#main2.create_rectangle(x_+400-20-1,y_+20+10-1, x_+400+400-20,y_+20+400+10,fill="#ffffff",outline="#333333")

		main2.create_text(x_-20+400+200,y_+100+20,text="Add Image",fill="#777777", font=("FreeMono",30))
		main2.create_oval(x_-20+400+200-40,y_+20+200-40, x_-20+400+200+40,y_+20+200+40, fill="#ffffff", outline="#777777",width=1 )

		main2.create_line(x_-20+400+200,y_+20+200-20, x_-20+400+200,y_+20+200+20,fill="#777777",width=1 )
		main2.create_line(x_-20+400-20+200,y_+20+200, x_-20+400+200+20,y_+20+200,fill="#777777",width=1 )

		qu=ImageTk.PhotoImage(file="data/quitb.png")


		main2.create_image(x_+400+400-20-25,y_+20+400+15-12.5,image=qu,anchor="nw")	

		a=200



		#main2.create_rectangle(x_+400-50-a,y_+500-50+10,x_+400+50-a,y_+500-20+10,fill="cyan",outline="cyan")
		#main2.create_oval(x_+400-50-15-a,y_+500-50+10, x_+400-50+15-a,y_+500-20+10,fill="cyan",outline="cyan")
		#main2.create_oval(x_+400+50-15-a,y_+500-50+10, x_+400+50+15-a,y_+500-20+10,fill="cyan",outline="cyan")
		main2.create_arc(x_+400-50-15-a,y_+500-50+10, x_+400-50+15-a,y_+500-20+10,style="arc",start=90,extent=180,
			outline="#000000")
		main2.create_arc(x_+400+50-15-a,y_+500-50+10, x_+400+50+15-a,y_+500-20+10,style="arc",start=270,extent=180,
			outline="#000000")
		main2.create_line(x_+400-50-15-a+15,y_+500-50+10, x_+400+50+15-a-15,y_+500-50+10,fill="#000000")
		main2.create_line(x_+400-50-15-a+15-1,y_+500-20+10, x_+400+50+15-a-15,y_+500-20+10,fill="#000000")



		main2.create_text(x_+400-a,y_+500-20-15+10,fill="#000000",text="Save",font=("FreeMono",13))

		#print(400-50-15-a,400+50+15-a)





		#main2.create_rectangle(x_+400-50+a,y_+500-50+10,x_+400+50+a,y_+500-20+10,fill="cyan",outline="cyan")
		#main2.create_oval(x_+400-50-15+a,y_+500-50+10, x_+400-50+15+a,y_+500-20+10,fill="cyan",outline="cyan")
		#main2.create_oval(x_+400+50-15+a,y_+500-50+10, x_+400+50+15+a,y_+500-20+10,fill="cyan",outline="cyan")

		main2.create_arc(x_+400-50-15+a,y_+500-50+10, x_+400-50+15+a,y_+500-20+10,style="arc",start=90,extent=180,
			outline="#000000")
		main2.create_arc(x_+400+50-15+a,y_+500-50+10, x_+400+50+15+a,y_+500-20+10,style="arc",start=270,extent=180,
			outline="#000000")
		main2.create_line(x_+400-50+a,y_+500-50+10, x_+400+50+a,y_+500-50+10,fill="#000000")
		main2.create_line(x_+400-50+a-1,y_+500-20+10, x_+400+50+a,y_+500-20+10,fill="#000000")




		main2.create_text(x_+400+a,y_+500-20-15+10,fill="#000000",text="Delete",font=("FreeMono",13))

		#print(400-50-15+a,400+50+15+a)


		if p==1:
			f="Images"
			dir_=os.listdir(f)


			for a in dir_:
				if a.split(".")[0]==str(seli):
					ext=a.split(".")[1]


					im=Image.open("Images/"+a)

					w,h=im.size

					if (w/h)>1:

						bx=400
						by=int(bx*h/w)

						im=im.resize((bx,by))
					elif (w/h)<1:
						by=400
						bx=int(by*w/h)
						im=im.resize((bx,by))

					elif (w/h)==1:
						bx=400
						by=400
						im=im.resize((bx,by))

					ax=(400-bx)/2
					ay=(400-by)/2

					im.save("data/msi."+ext)

					msimage=ImageTk.PhotoImage(file="data/msi."+ext)

					msi=main2.create_image(x_+400-20+ax,y_+20+ay,image=msimage,anchor="nw")



		cx,cy=x_+400-20-1+10,y_+20-1+10
		ar=[x_+400-20-1,y_+20-1]
		a_=180
		for a in range(90):
			x=10*math.sin(math.radians(a_))+cx
			y=10*math.cos(math.radians(a_))+cy
			ar.append(x)
			ar.append(y)

			a_+=1
		ar.append(x_+400-20-1)
		ar.append(y_+20-1)

		main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")


		cx,cy=x_+400-20-1+10,y_+20+400-10
		ar=[x_+400-20-1,y_+20+400]
		a_=270
		for a in range(90):
			x=10*math.sin(math.radians(a_))+cx
			y=10*math.cos(math.radians(a_))+cy
			ar.append(x)
			ar.append(y)

			a_+=1
		ar.append(x_+400-20-1)
		ar.append(y_+20+400)

		main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")


		cx,cy=x_+400+400-20-10,y_+20+400-10
		ar=[x_+400+400-20,y_+20+400]
		a_=0
		for a in range(90):
			x=10*math.sin(math.radians(a_))+cx
			y=10*math.cos(math.radians(a_))+cy
			ar.append(x)
			ar.append(y)

			a_+=1
		ar.append(x_+400+400-20)
		ar.append(y_+20+400)

		main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")


		cx,cy=x_+400+400-20-10,y_+20-1+10
		ar=[x_+400+400-20,y_+20-1]
		a_=90
		for a in range(90):
			x=10*math.sin(math.radians(a_))+cx
			y=10*math.cos(math.radians(a_))+cy
			ar.append(x)
			ar.append(y)

			a_+=1
		ar.append(x_+400+400-20)
		ar.append(y_+20-1)

		main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")
		#x_+400-20-1,y_+20-1, x_+400+400-20,y_+20+400

		main2.create_arc(x_+400-20-1,y_+20-1, x_+400-20-1+20,y_+20-1+20,style="arc",start=90,extent=90,outline="#777777")
		main2.create_arc(x_+400+400-20,y_+20-1, x_+400+400-20-20,y_+20-1+20,style="arc",start=0,extent=90,outline="#777777")
		main2.create_arc(x_+400+400-20,y_+20+400-20, x_+400+400-20-20,y_+20+400,style="arc",start=270,extent=90,outline="#777777")	
		main2.create_arc(x_+400-20-1,y_+20+400-20, x_+400-20-1+20,y_+20+400,style="arc",start=180,extent=90,outline="#777777")	


		main2.create_line(x_+400-20-1+10,y_+20-1,  x_+400+400-20-10,y_+20-1,fill="#777777" )
		main2.create_line(x_+400-20-1+10-1,y_+20+400,  x_+400+400-20-10,y_+20+400,fill="#777777" )
		main2.create_line(x_+400-20-1,y_+20-1+10-1, x_+400-20-1,y_+20+400-10,fill="#777777" )
		main2.create_line(x_+400+400-20,y_+20-1+10, x_+400+400-20,y_+20+400-10,fill="#777777" )


		#bc=ImageTk.PhotoImage(file="data/barcode.jpg")

# reports




msimage=""

msf=""
mscon=0
mscon2=0

msicon=0
ms_con=0
msarray=[]

# reports
def draw_reports():
	global main1,main2,rr_,dvar2,yvar,svar,dashb_state,daten,date__,cali,dib,logw,se,vbar1


	main2.delete("all")
	draw_main1()
	

	main2["bg"]="#ffffff"



	vbar1.pack_forget()
	main2.pack_forget()
	vbar1.pack(side=tk.RIGHT,fill=tk.Y)
	main2.pack(side=tk.LEFT)


	tot1=0

	tot2=0


	x_=90+(wd-90)/2

	

	searche.focus_set()

	main1.create_oval(x_-150-15,10, x_-150+15,40,fill="#ffffff",outline="#ffffff")
	main1.create_oval(x_+150-15,10, x_+150+15,40,fill="#ffffff",outline="#ffffff")

	main1.create_rectangle(x_-150,10, x_+150,40,fill="#ffffff",outline="#ffffff")




	se=ImageTk.PhotoImage(file="data/search.png")

	main1.create_image(x_+150+50-30,15,image=se,anchor="nw")






	searche.place(in_=root,x=x_-148,y=14)



	x_=90+(wd-90-1020)/2



	cali=ImageTk.PhotoImage(file="data/calendar.png")


	main1.create_image(x_,10,image=cali,anchor="nw")





	date__=main1.create_text(x_+40,25,text=daten,font=("FreeMono",13),anchor="w",fill="#ffffff")

	rr_.place(in_=root,x=x_,y=50)


	dbsales=db.connect("data/sales.db")
	cur=dbsales.cursor()


	cur.execute("SELECT * FROM sales_ ORDER BY sales_id DESC")

	rows=cur.fetchall()

	yv=31

	st=0
	c=0
	for row in rows:

		if not str(row[1].lower()).find(searche.get().lower())==-1:

			

			_yy=int(daten.split("-")[2])
			_mm=int(daten.split("-")[1])
			_dd=daten.split("-")[0]

			if not _dd=="*":
				_dd=int(daten.split("-")[0])

				

			yy=int(str(row[5]).split(" ")[0].split("-")[0])
			mm=int(str(row[5]).split(" ")[0].split("-")[1])
			dd=int(str(row[5]).split(" ")[0].split("-")[2])



			if _dd=="*":

				if _mm==mm and _yy==yy:
					pass
				else:
					continue

			else:

				if _dd==dd and _mm==mm and _yy==yy:
					pass
				else:
					continue

			c+=1


			date=str(row[5].split(" ")[1].split(".")[0])+"/"+str(dd)+"-"+str(mm)+"-"+str(yy)

			var=[str(row[1].lower())[:15],add_comma(str(row[2])[:15]),add_comma(str(row[3])[:15]),add_comma(str(row[4])[:15]),str(date),add_comma(str(row[6])[:15]),add_comma(str(row[7])[:15]) ]


			tot1+=int(row[6])
			tot2+=int(row[7])
			v=1000/7
			xv=x_+v

			if st==1:
				main2.create_rectangle(x_,yv,x_+1020,yv+25,fill="#f3f3f3",outline="#f3f3f3")
				st=0
			elif st==0:
				st=1
				main2.create_rectangle(x_,yv,x_+1020,yv+25,fill="#ffffff",outline="#ffffff")

			for a in range(7):

				if a==4:
					xv+=10
				main2.create_text(xv-v/2,yv+12.5,text=var[a],font=("FreeMono",13),fill="#000000")

				if a==4:
					xv+=10
				xv+=v

			yv+=25



	if c==0:
		rr_.place_forget()


		vbar1.pack_forget()


		main2.create_text(90+(wd-90)/2,ht/2-50,text="No Record",fill="#333333",font=("FreeMono",25),anchor="c")


		return


	main2.create_line(x_,yv,x_+1020,yv,fill="#000000")

	v=1000/7
	xv=x_+v
	for a in range(6):

		if a==3:
			xv-=1

		if a==4:
			xv+=20
		main2.create_line(xv+1,30,xv+1,yv,fill="#ffffff")
		main2.create_line(xv,30,xv,yv,fill="#000000")

		xv+=v

	x=x_+v/2+v*5
	main2.create_text(x+20,yv+12.5,font=("FreeMono",13),fill="#000000",text=add_comma(str(tot1)))

	x=x_+v/2+v*6
	main2.create_text(x+20,yv+12.5,font=("FreeMono",13),fill="#000000",text=add_comma(str(tot2)))


	yvar=yv+100
	main2["scrollregion"]=(0,0,wd,yvar)

	

	#print(yvar)


def unse(e):
	global ems

	ems.focus_set()

def emse(e):
	global cons

	cons.focus_set()

def conse(e):
	global pss

	pss.focus_set()


uns=tk.Entry(width=24,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,font=("FreeMono","13"))
uns.bind("<Return>",unse)
ems=tk.Entry(width=24,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,font=("FreeMono","13"))
ems.bind("<Return>",emse)
cons=tk.Entry(width=24,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,font=("FreeMono","13"))
cons.bind("<Return>",conse	)
pss=tk.Entry(show="*",width=24,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,font=("FreeMono","13"))

photo1=()
photo2=()

admin_st1=1
admin_st2=0
admin_st2_1=0
admin_st2_2=0
prof_st="myprofile"
prof0=""
prof1=""
prof2=0
myp=[]

myp2=[]
myp3=[]
mypv=0

sss2=()


user_array=[]
def draw_profiles():
	global main1,main2,dvar2
	global wd,ht,diw2,logw,prof_st,uns,ems,cons,pss,photo1,photo2,qu,admin_st1,admin_st2_1,admin_st2_2,prof0,prof1,myp2,myp3,myp

	global info
	global userframe,yvar3,userc,user_array
	global cirw,cirr,cirb,sqr,sqb

	global showp,dshowp,pst,sss2

	main2.delete("all")

	

	main2["bg"]="#222222"

	draw_main1()



	x_,y_=90+(wd-800-90)/2,((ht-50)-500)/2



	main2.create_oval(x_+20,y_+500-20-20,x_+40,y_+500-20,fill="#ffffff",outline="#ffffff")
	main2.create_oval(x_-20+800-20,y_+500-20-20,x_-20+800,y_+500-20,fill="#ffffff",outline="#ffffff")
	main2.create_oval(x_-20+800-20,y_+50,x_-20+800,y_+50+20,fill="#ffffff",outline="#ffffff")

	main2.create_polygon(x_+20,y_+50, x_+20,y_+500-10-20, x_+30, y_+500-20, x_-20+800-10, y_+500-20,
		x_-20+800,y_+500-20-10, x_-20+800,y_+50+10-1, x_-20+800-10,y_+50, x_+20+280,y_+50,fill="#ffffff",outline="#ffffff")
    

	photo1=ImageTk.PhotoImage(file="data/userd.png")
	
	qu=ImageTk.PhotoImage(file="data/remove.png")

	cirw=ImageTk.PhotoImage(file="data/circlew.png")
	cirr=ImageTk.PhotoImage(file="data/circler.png")
	cirb=ImageTk.PhotoImage(file="data/circleb.png")

	sqr=ImageTk.PhotoImage(file="data/squarer.png")
	sqb=ImageTk.PhotoImage(file="data/squareb.png")

	if prof_st==0:





		main2.create_oval(x_+20,y_+20, x_+40,y_+40,fill="#ffffff",outline="#ffffff")
		main2.create_oval(x_+280-140,y_+20, x_+20+140,y_+40,fill="#ffffff",outline="#ffffff")

		main2.create_rectangle(x_+20+10,y_+20, x_+20+140-10,y_+30,fill="#ffffff",outline="#ffffff")
		main2.create_rectangle(x_+20,y_+30, x_+20+140,y_+50-1,fill="#ffffff",outline="#ffffff")



		




		main2.create_oval(x_+20+140+2,y_+20, x_+40+140+2,y_+40,fill="#222222",outline="#222222")
		main2.create_oval(x_+280+2,y_+20, x_+20+280+2,y_+40,fill="#222222",outline="#222222")

		main2.create_rectangle(x_+20+140+10+2,y_+20, x_+20+280-10+2,y_+30,fill="#222222",outline="#222222")
		main2.create_rectangle(x_+20+140+2,y_+30, x_+20+280+2,y_+50-1,fill="#222222",outline="#222222")





		main2.create_oval(x_+20+140+140+2+2,y_+20, x_+40+140+140+2+2,y_+40,fill="#222222",outline="#222222")
		main2.create_oval(x_+280+140+2+2,y_+20, x_+20+280+140+2+2,y_+40,fill="#222222",outline="#222222")

		main2.create_rectangle(x_+20+140+10+140+2+2,y_+20, x_+20+280-10+140+2+2,y_+30,fill="#222222",outline="#222222")
		main2.create_rectangle(x_+20+140+140+2+2,y_+30, x_+20+280+140+2+2,y_+50-1,fill="#222222",outline="#222222")

		ar=[x_+20+140,y_+50]

		cx,cy=x_+20+140+10,y_+50-10

		a_=0

		for a in range(90):
			x=10*math.sin(math.radians(a_))+cx
			y=10*math.cos(math.radians(a_))+cy

			ar.append(x)
			ar.append(y)

			a_-=1

		main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")



		#x 55
		#y 37

		main2.create_text(x_+20+70,y_+20+15,text="My Profile",fill="#000000",font=("FreeMono",13,"bold"))
		main2.create_text(x_+20+70+140,y_+20+15,text="New User",fill="#ffffff",font=("FreeMono",13))
		main2.create_text(x_+20+70+140+140,y_+20+15,text="Users",fill="#ffffff",font=("FreeMono",13))

       

		av=60
		main2.create_text(x_+40+10+55-40,y_+50+50+10-20+37,text="User Name",anchor="w",fill="#000000",
                          font=("FreeMono",13))
		main2.create_text(x_+40+10+55-40,y_+50+50+av+10-20+37,text="Email",anchor="w",fill="#000000",
                          font=("FreeMono",13))

		main2.create_text(x_+40+10+55-40,y_+50+50+av*2+10-20+37,text="Contact",anchor="w",fill="#000000",
                          font=("FreeMono",13))
		main2.create_text(x_+40+10+55-40,y_+50+50+av*3+10-20+37,text="Password",anchor="w",fill="#000000",
                          font=("FreeMono",13))


		main2.create_arc(x_+171-4+55-40,y_+100-10-4+10-20+37, x_+171-4+10+55-40,y_+100-10-4+10+10-20+37,style="arc",start=90,extent=90,
			outline="#000000")
		main2.create_arc(x_+171-4+55-40,y_+100-10+21+4-10+10-20+37, x_+171-4+10+55-40,y_+100-10+21+4+10-20+37,style="arc",start=180,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10-4+10-20+37, x_+171+164+4+55-40+53,y_+100-10-4+10+10-20+37,style="arc",start=0,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10+21+4-10+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4+10-20+37,style="arc",start=270,extent=90,
			outline="#000000")

		main2.create_line(x_+171-4+5+55-40,y_+100-10-4+10-20+37, x_+171+164+4-5+1+55-40+53,y_+100-10-4+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+5+55-40,y_+100-10+21+4+10-20+37, x_+171+164+4-5+55-40+53,y_+100-10+21+4+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+55-40,y_+100-10-4+5+10-20+37, x_+171-4+55-40,y_+100-10+21+4-5+10-20+37,fill="#000000")
		main2.create_line(x_+171+164+4+55-40+53,y_+100-10-4+5+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4-5+10-20+37,fill="#000000")


		main2.create_arc(x_+171-4+55-40,y_+100-10-4+av+10-20+37, x_+171-4+10+55-40,y_+100-10-4+10+av+10-20+37,style="arc",start=90,extent=90,
			outline="#000000")
		main2.create_arc(x_+171-4+55-40,y_+100-10+21+4-10+av+10-20+37, x_+171-4+10+55-40,y_+100-10+21+4+av+10-20+37,style="arc",start=180,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10-4+av+10-20+37, x_+171+164+4+55-40+53,y_+100-10-4+10+av+10-20+37,style="arc",start=0,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10+21+4-10+av+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4+av+10-20+37,style="arc",start=270,extent=90,
			outline="#000000")

		main2.create_line(x_+171-4+5+55-40,y_+100-10-4+av+10-20+37, x_+171+164+4-5+1+55-40+53,y_+100-10-4+av+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+5+55-40,y_+100-10+21+4+av+10-20+37, x_+171+164+4-5+55-40+53,y_+100-10+21+4+av+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+55-40,y_+100-10-4+5+av+10-20+37, x_+171-4+55-40,y_+100-10+21+4-5+av+10-20+37,fill="#000000")
		main2.create_line(x_+171+164+4+55-40+53,y_+100-10-4+5+av+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4-5+av+10-20+37,fill="#000000")


		main2.create_arc(x_+171-4+55-40,y_+100-10-4+av*2+10-20+37, x_+171-4+10+55-40,y_+100-10-4+10+av*2+10-20+37,style="arc",start=90,extent=90,
			outline="#000000")
		main2.create_arc(x_+171-4+55-40,y_+100-10+21+4-10+av*2+10-20+37, x_+171-4+10+55-40,y_+100-10+21+4+av*2+10-20+37,style="arc",start=180,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10-4+av*2+10-20+37, x_+171+164+4+55-40+53,y_+100-10-4+10+av*2+10-20+37,style="arc",start=0,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10+21+4-10+av*2+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4+av*2+10-20+37,style="arc",start=270,extent=90,
			outline="#000000")

		main2.create_line(x_+171-4+5+55-40,y_+100-10-4+av*2+10-20+37, x_+171+164+4-5+1+55-40+53,y_+100-10-4+av*2+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+5+55-40,y_+100-10+21+4+av*2+10-20+37, x_+171+164+4-5+55-40+53,y_+100-10+21+4+av*2+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+55-40,y_+100-10-4+5+av*2+10-20+37, x_+171-4+55-40,y_+100-10+21+4-5+av*2+10-20+37,fill="#000000")
		main2.create_line(x_+171+164+4+55-40+53,y_+100-10-4+5+av*2+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4-5+av*2+10-20+37,fill="#000000")



		main2.create_arc(x_+171-4+55-40,y_+100-10-4+av*3+10-20+37, x_+171-4+10+55-40,y_+100-10-4+10+av*3+10-20+37,style="arc",start=90,extent=90,
			outline="#000000")
		main2.create_arc(x_+171-4+55-40,y_+100-10+21+4-10+av*3+10-20+37, x_+171-4+10+55-40,y_+100-10+21+4+av*3+10-20+37,style="arc",start=180,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10-4+av*3+10-20+37, x_+171+164+4+55-40+53,y_+100-10-4+10+av*3+10-20+37,style="arc",start=0,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10+21+4-10+av*3+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4+av*3+10-20+37,style="arc",start=270,extent=90,
			outline="#000000")


		main2.create_line(x_+171-4+5+55-40,y_+100-10-4+av*3+10-20+37, x_+171+164+4-5+1+55-40+53,y_+100-10-4+av*3+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+5+55-40,y_+100-10+21+4+av*3+10-20+37, x_+171+164+4-5+55-40+53,y_+100-10+21+4+av*3+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+55-40,y_+100-10-4+5+av*3+10-20+37, x_+171-4+55-40,y_+100-10+21+4-5+av*3+10-20+37,fill="#000000")
		main2.create_line(x_+171+164+4+55-40+53,y_+100-10-4+5+av*3+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4-5+av*3+10-20+37,fill="#000000")



		uns.delete(0,tk.END)
		ems.delete(0,tk.END)
		cons.delete(0,tk.END)
		pss.delete(0,tk.END)

		uns.focus_set()

		uns.place(in_=root,x=x_+171+55-40,y=y_+100-10+50+10-20+37)
		ems.place(in_=root,x=x_+171+55-40,y=y_+100-10+50+av+10-20+37)
		cons.place(in_=root,x=x_+171+55-40,y=y_+100-10+50+av*2+10-20+37)		
		pss.place(in_=root,x=x_+171+55-40,y=y_+100-10+50+av*3+10-20+37)

		uns.insert(0,myp3[0])
		ems.insert(0,myp3[1])
		cons.insert(0,myp3[2])
		pss.insert(0,myp3[3])


		if prof2==0:


			if myp[4]==0:

				main2.create_image(x_+400+55,y_+100-40+30-10+37-4,image=photo1,anchor="nw")


			if myp[4]==1:
				photo2=ImageTk.PhotoImage(file="Images/"+"pp_"+str(myp[0])+"l.jpg")
				main2.create_image(x_+400+55,y_+100-40+30-10+37-4,image=photo2,anchor="nw")

		elif prof2==1:

			if prof0=="":

				main2.create_image(x_+400+55,y_+100-40+30-10+37-4,image=photo1,anchor="nw")


			else:
				main2.create_image(x_+400+55,y_+100-40+30-10+37-4,image=prof0,anchor="nw")


		ar1=[x_+400+120+55,y_+100-40+120+30-10+37-4]
		

		cx=x_+400+60+55
		cy=y_+100-40+60+37-4

		a=0

		for a in range(180):

			x=60*math.sin(math.radians(a))+cx
			y=60*math.cos(math.radians(a))+cy+30-10

			ar1.append(x)
			ar1.append(y)

		ar1.append(x_+400+120+55)
		ar1.append(y_+100-40+30-10+37-4)		

		main2.create_polygon(ar1,fill="#ffffff",outline="#ffffff")


		ar2=[x_+400+55,y_+100-40+30-10+37-4]

		a_=180

		for a in range(180):

			x=60*math.sin(math.radians(a_))+cx
			y=60*math.cos(math.radians(a_))+cy+30-10


			ar2.append(x)
			ar2.append(y)

			a_+=1

		ar2.append(x_+400+55)
		ar2.append(y_+100-40+120+30-10+37-4)		

		main2.create_polygon(ar2,fill="#ffffff",outline="#ffffff")





		main2.create_image(x_+400+120+55,y_+100+120-20-50+30-10+37-4,image=qu,anchor="nw")

		main2.create_text(x_+400+120+20+55,y_+100-20+10+30-10+37-4,text="Profile Picture",fill="#000000",
			font=("FreeMono",13),anchor="w")


		#main2.create_rectangle(x_+400+120+20+50,y_+100-20+10+30-10, x_+400+120+20+50+100-13,y_+100-20+10+30+10,
		#	fill="#000000",outline="#000000")


		main2.create_text(x_+400+120+20+55,y_+100-20+10+30+30-10+37-4,text="Add Picture",fill="red",
			font=("FreeMono",13),anchor="w")

		main2.create_text(x_+400+50-410+10+55-40,y_+250+150-30-20+37,text="Set Admin",fill="#000000",
			font=("FreeMono",13),anchor="w")


		if admin_st2_1==0:
			
			main2.create_image(x_+400+50+100-410+55-40,y_+250-12.5+150-30-20+37,image=cirb,anchor="nw")
			main2.create_image(x_+400+50+100-410+25+55-40,y_+250-12.5+150-30-20+37,image=cirb,anchor="nw")
			main2.create_image(x_+400+50+100-410+12.5+55-40,y_+250-12.5+150-30-20+37,image=sqb,anchor="nw")
			main2.create_image(x_+400+50+100-410+5+55-40,y_+250-12.5+150+5-30-20+37,image=cirw,anchor="nw")


		elif admin_st2_1==1:
			main2.create_image(x_+400+50+100-410+55-40,y_+250-12.5+150-30-20+37,image=cirr,anchor="nw")
			main2.create_image(x_+400+50+100-410+25+55-40,y_+250-12.5+150-30-20+37,image=cirr,anchor="nw")
			main2.create_image(x_+400+50+100-410+12.5+55-40,y_+250-12.5+150-30-20+37,image=sqr,anchor="nw")
			main2.create_image(x_+400+50+100-410+25+5+55-40,y_+250-12.5+150+5-30-20+37,image=cirw,anchor="nw")


		if pst==0:
			showp=ImageTk.PhotoImage(file="data/show.png")

			sss2=main2.create_image(x_+171+164+4+55-40+53+10,y_+100-10-4+av*3+10-20+37,image=showp,anchor="nw")
			pss["show"]="*"
		elif pst==1:
			dshowp=ImageTk.PhotoImage(file="data/dshow.png")

			sss2=main2.create_image(x_+171+164+4+55-40+53+10,y_+100-10-4+av*3+10-20+37,image=dshowp,anchor="nw")
			pss["show"]=""



		main2.create_arc(x_+400-90,y_+500-10-30-20, x_+400-90+30,y_+500-10-20,start=90,extent=180,outline="#000000",style="arc")
		main2.create_arc(x_+400+90-30,y_+500-10-30-20, x_+400+90,y_+500-10-20,start=270,extent=180,outline="#000000",style="arc")

		main2.create_line(x_+400-90+15,y_+500-10-30-20, x_+400+90-15,y_+500-10-30-20,fill="#000000")
		main2.create_line(x_+400-90+15-1,y_+500-10-20, x_+400+90-15,y_+500-10-20,fill="#000000")

		main2.create_text(x_+400,y_+500-10-30-20+15,text="Save",font=("FreeMono",13),fill="#000000")



	elif prof_st==1:

		main2.create_oval(x_+20+140-140,y_+20, x_+40+140-140,y_+40,fill="#222222",outline="#222222")
		main2.create_oval(x_+280-140,y_+20, x_+20+280-140,y_+40,fill="#222222",outline="#222222")

		main2.create_rectangle(x_+20+140+10-140,y_+20, x_+20+280-10-140,y_+30,fill="#222222",outline="#222222")
		main2.create_rectangle(x_+20+140-140,y_+30, x_+20+280-140,y_+50-1,fill="#222222",outline="#222222")



		main2.create_oval(x_+20+140+2,y_+20, x_+40+140+2,y_+40,fill="#ffffff",outline="#ffffff")
		main2.create_oval(x_+280+2,y_+20, x_+20+280+2,y_+40,fill="#ffffff",outline="#ffffff")

		main2.create_rectangle(x_+20+140+10+2,y_+20, x_+20+280-10,y_+30,fill="#ffffff",outline="#ffffff")
		main2.create_rectangle(x_+20+140+2,y_+30, x_+20+280+2,y_+50-1,fill="#ffffff",outline="#ffffff")



		main2.create_oval(x_+20+140+2+140+2,y_+20, x_+40+140+2+140+2,y_+40,fill="#222222",outline="#222222")
		main2.create_oval(x_+280+2+140+2,y_+20, x_+20+280+2+140+2,y_+40,fill="#222222",outline="#222222")

		main2.create_rectangle(x_+20+140+10+2+140+2,y_+20, x_+20+280-10+140+2,y_+30,fill="#222222",outline="#222222")
		main2.create_rectangle(x_+20+140+2+140+2,y_+30, x_+20+280+2+140+2,y_+50-1,fill="#222222",outline="#222222")

		main2.create_text(x_+20+70,y_+20+15,text="My Profile",fill="#ffffff",font=("FreeMono",13))
		main2.create_text(x_+20+70+140+1,y_+20+15,text="New User",fill="#000000",font=("FreeMono",13,"bold"))
		main2.create_text(x_+20+70+140+1+140,y_+20+15,text="Users",fill="#ffffff",font=("FreeMono",13))



		ar=[x_+20+140+2+140,y_+50]

		cx,cy=x_+20+140+10+2+140,y_+50-10

		a_=0

		for a in range(90):
			x=10*math.sin(math.radians(a_))+cx
			y=10*math.cos(math.radians(a_))+cy

			ar.append(x)
			ar.append(y)

			a_-=1

		main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")


		ar=[x_+20+140+2,y_+50]

		cx,cy=x_+20+140-10+2,y_+50-10

		a_=0

		for a in range(90):
			x=10*math.sin(math.radians(a_))+cx
			y=10*math.cos(math.radians(a_))+cy

			ar.append(x)
			ar.append(y)

			a_+=1

		main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")

		if myp[-1]==0:

			info=ImageTk.PhotoImage(file="data/info.png")
			uns.place_forget()
			ems.place_forget()
			cons.place_forget()	
			pss.place_forget()



			main2.create_image(x_+200+30,y_+250-50,image=info,anchor="nw")

			main2.create_text(x_+200+100+30+30,y_+250,text="Login as Administrator",font=("FreeMono",15),anchor="w")



			return

		av=60


		main2.create_text(x_+40+10+55-40,y_+50+50+10-20+37,text="User Name",anchor="w",fill="#000000",
                          font=("FreeMono",13))
		main2.create_text(x_+40+10+55-40,y_+50+50+av+10-20+37,text="Email",anchor="w",fill="#000000",
                          font=("FreeMono",13))

		main2.create_text(x_+40+10+55-40,y_+50+50+av*2+10-20+37,text="Contact",anchor="w",fill="#000000",
                          font=("FreeMono",13))
		main2.create_text(x_+40+10+55-40,y_+50+50+av*3+10-20+37,text="Password",anchor="w",fill="#000000",
                          font=("FreeMono",13))


		main2.create_arc(x_+171-4+55-40,y_+100-10-4+10-20+37, x_+171-4+10+55-40,y_+100-10-4+10+10-20+37,style="arc",start=90,extent=90,
			outline="#000000")
		main2.create_arc(x_+171-4+55-40,y_+100-10+21+4-10+10-20+37, x_+171-4+10+55-40,y_+100-10+21+4+10-20+37,style="arc",start=180,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10-4+10-20+37, x_+171+164+4+55-40+53,y_+100-10-4+10+10-20+37,style="arc",start=0,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10+21+4-10+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4+10-20+37,style="arc",start=270,extent=90,
			outline="#000000")

		main2.create_line(x_+171-4+5+55-40,y_+100-10-4+10-20+37, x_+171+164+4-5+1+55-40+53,y_+100-10-4+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+5+55-40,y_+100-10+21+4+10-20+37, x_+171+164+4-5+55-40+53,y_+100-10+21+4+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+55-40,y_+100-10-4+5+10-20+37, x_+171-4+55-40,y_+100-10+21+4-5+10-20+37,fill="#000000")
		main2.create_line(x_+171+164+4+55-40+53,y_+100-10-4+5+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4-5+10-20+37,fill="#000000")


		main2.create_arc(x_+171-4+55-40,y_+100-10-4+av+10-20+37, x_+171-4+10+55-40,y_+100-10-4+10+av+10-20+37,style="arc",start=90,extent=90,
			outline="#000000")
		main2.create_arc(x_+171-4+55-40,y_+100-10+21+4-10+av+10-20+37, x_+171-4+10+55-40,y_+100-10+21+4+av+10-20+37,style="arc",start=180,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10-4+av+10-20+37, x_+171+164+4+55-40+53,y_+100-10-4+10+av+10-20+37,style="arc",start=0,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10+21+4-10+av+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4+av+10-20+37,style="arc",start=270,extent=90,
			outline="#000000")

		main2.create_line(x_+171-4+5+55-40,y_+100-10-4+av+10-20+37, x_+171+164+4-5+1+55-40+53,y_+100-10-4+av+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+5+55-40,y_+100-10+21+4+av+10-20+37, x_+171+164+4-5+55-40+53,y_+100-10+21+4+av+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+55-40,y_+100-10-4+5+av+10-20+37, x_+171-4+55-40,y_+100-10+21+4-5+av+10-20+37,fill="#000000")
		main2.create_line(x_+171+164+4+55-40+53,y_+100-10-4+5+av+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4-5+av+10-20+37,fill="#000000")


		main2.create_arc(x_+171-4+55-40,y_+100-10-4+av*2+10-20+37, x_+171-4+10+55-40,y_+100-10-4+10+av*2+10-20+37,style="arc",start=90,extent=90,
			outline="#000000")
		main2.create_arc(x_+171-4+55-40,y_+100-10+21+4-10+av*2+10-20+37, x_+171-4+10+55-40,y_+100-10+21+4+av*2+10-20+37,style="arc",start=180,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10-4+av*2+10-20+37, x_+171+164+4+55-40+53,y_+100-10-4+10+av*2+10-20+37,style="arc",start=0,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10+21+4-10+av*2+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4+av*2+10-20+37,style="arc",start=270,extent=90,
			outline="#000000")

		main2.create_line(x_+171-4+5+55-40,y_+100-10-4+av*2+10-20+37, x_+171+164+4-5+1+55-40+53,y_+100-10-4+av*2+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+5+55-40,y_+100-10+21+4+av*2+10-20+37, x_+171+164+4-5+55-40+53,y_+100-10+21+4+av*2+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+55-40,y_+100-10-4+5+av*2+10-20+37, x_+171-4+55-40,y_+100-10+21+4-5+av*2+10-20+37,fill="#000000")
		main2.create_line(x_+171+164+4+55-40+53,y_+100-10-4+5+av*2+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4-5+av*2+10-20+37,fill="#000000")



		main2.create_arc(x_+171-4+55-40,y_+100-10-4+av*3+10-20+37, x_+171-4+10+55-40,y_+100-10-4+10+av*3+10-20+37,style="arc",start=90,extent=90,
			outline="#000000")
		main2.create_arc(x_+171-4+55-40,y_+100-10+21+4-10+av*3+10-20+37, x_+171-4+10+55-40,y_+100-10+21+4+av*3+10-20+37,style="arc",start=180,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10-4+av*3+10-20+37, x_+171+164+4+55-40+53,y_+100-10-4+10+av*3+10-20+37,style="arc",start=0,extent=90,
			outline="#000000")
		main2.create_arc(x_+171+164+4-10+55-40+53,y_+100-10+21+4-10+av*3+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4+av*3+10-20+37,style="arc",start=270,extent=90,
			outline="#000000")

		main2.create_line(x_+171-4+5+55-40,y_+100-10-4+av*3+10-20+37, x_+171+164+4-5+1+55-40+53,y_+100-10-4+av*3+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+5+55-40,y_+100-10+21+4+av*3+10-20+37, x_+171+164+4-5+55-40+53,y_+100-10+21+4+av*3+10-20+37,fill="#000000")
		main2.create_line(x_+171-4+55-40,y_+100-10-4+5+av*3+10-20+37, x_+171-4+55-40,y_+100-10+21+4-5+av*3+10-20+37,fill="#000000")
		main2.create_line(x_+171+164+4+55-40+53,y_+100-10-4+5+av*3+10-20+37, x_+171+164+4+55-40+53,y_+100-10+21+4-5+av*3+10-20+37,fill="#000000")



		uns.delete(0,tk.END)
		ems.delete(0,tk.END)
		cons.delete(0,tk.END)
		pss.delete(0,tk.END)

		uns.focus_set()

		uns.place(in_=root,x=x_+171+55-40,y=y_+100-10+50+10-20+37)
		ems.place(in_=root,x=x_+171+55-40,y=y_+100-10+50+av+10-20+37)
		cons.place(in_=root,x=x_+171+55-40,y=y_+100-10+50+av*2+10-20+37)		
		pss.place(in_=root,x=x_+171+55-40,y=y_+100-10+50+av*3+10-20+37)


		if len(myp2)>0:
			uns.insert(0,myp2[0])
			ems.insert(0,myp2[1])
			cons.insert(0,myp2[2])
			pss.insert(0,myp2[3])

		uns.focus_set()






		if prof1=="":
			main2.create_image(x_+400+55,y_+100-40+20+37-4,image=photo1,anchor="nw")
		else:
			main2.create_image(x_+400+55,y_+100-40+20+37-4,image=prof1,anchor="nw")

		ar1=[x_+400+120+55,y_+100-40+120+20+37-4]
		

		cx=x_+400+60+55
		cy=y_+100-40+60+20+37-4

		a=0

		for a in range(180):

			x=60*math.sin(math.radians(a))+cx
			y=60*math.cos(math.radians(a))+cy

			ar1.append(x)
			ar1.append(y)

		ar1.append(x_+400+120+55)
		ar1.append(y_+100-40+20+37-4)		

		main2.create_polygon(ar1,fill="#ffffff",outline="#ffffff")


		ar2=[x_+400+55,y_+100-40+20+37-4]

		a_=180

		for a in range(180):

			x=60*math.sin(math.radians(a_))+cx
			y=60*math.cos(math.radians(a_))+cy

			ar2.append(x)
			ar2.append(y)

			a_+=1

		ar2.append(x_+400+55)
		ar2.append(y_+100-40+120+20+37-4)		

		main2.create_polygon(ar2,fill="#ffffff",outline="#ffffff")





		main2.create_image(x_+400+120+55,y_+100+120-20-50+20+37-4,image=qu,anchor="nw")

		main2.create_text(x_+400+120+20+55,y_+100-20+10+20+37-4,text="Profile Picture",fill="#000000",
			font=("FreeMono",13),anchor="w")


		#main2.create_rectangle(x_+400+120+20+50,y_+100-20+10+30-10, x_+400+120+20+50+100-13,y_+100-20+10+30+10,
		#	fill="#000000",outline="#000000")


		main2.create_text(x_+400+120+20+55,y_+100-20+10+30+20+37-4,text="Add Picture",fill="red",
			font=("FreeMono",13),anchor="w")

		main2.create_text(x_+400+60-410+55-40,y_+250+150-30-20+37,text="Set Admin",fill="#000000",
			font=("FreeMono",13),anchor="w")

		if admin_st2_2==0:
			
			main2.create_image(x_+400+50+100-410+55-40,y_+250-12.5+150-30-20+37,image=cirb,anchor="nw")
			main2.create_image(x_+400+50+100-410+25+55-40,y_+250-12.5+150-30-20+37,image=cirb,anchor="nw")
			main2.create_image(x_+400+50+100-410+12.5+55-40,y_+250-12.5+150-30-20+37,image=sqb,anchor="nw")
			main2.create_image(x_+400+50+100-410+5+55-40,y_+250-12.5+150+5-30-20+37,image=cirw,anchor="nw")


		elif admin_st2_2==1:
			main2.create_image(x_+400+50+100-410+55-40,y_+250-12.5+150-30-20+37,image=cirr,anchor="nw")
			main2.create_image(x_+400+50+100-410+25+55-40,y_+250-12.5+150-30-20+37,image=cirr,anchor="nw")
			main2.create_image(x_+400+50+100-410+12.5+55-40,y_+250-12.5+150-30-20+37,image=sqr,anchor="nw")
			main2.create_image(x_+400+50+100-410+25+5+55-40,y_+250-12.5+150+5-30-20+37,image=cirw,anchor="nw")


		if pst==0:
			showp=ImageTk.PhotoImage(file="data/show.png")

			sss2=main2.create_image(x_+171+164+4+55-40+53+10,y_+100-10-4+av*3+10-20+37,image=showp,anchor="nw")
			pss["show"]="*"
		elif pst==1:
			dshowp=ImageTk.PhotoImage(file="data/dshow.png")

			sss2=main2.create_image(x_+171+164+4+55-40+53+10,y_+100-10-4+av*3+10-20+37,image=dshowp,anchor="nw")
			pss["show"]=""


		main2.create_arc(x_+400-90,y_+500-10-30-20, x_+400-90+30,y_+500-10-20,start=90,extent=180,outline="#000000",style="arc")
		main2.create_arc(x_+400+90-30,y_+500-10-30-20, x_+400+90,y_+500-10-20,start=270,extent=180,outline="#000000",style="arc")

		main2.create_line(x_+400-90+15,y_+500-10-30-20, x_+400+90-15,y_+500-10-30-20,fill="#000000")
		main2.create_line(x_+400-90+15-1,y_+500-10-20, x_+400+90-15,y_+500-10-20,fill="#000000")

		main2.create_text(x_+400,y_+500-10-30-20+15,text="Save",font=("FreeMono",13),fill="#000000")



	elif prof_st==2:

		main2.create_oval(x_+20+140-140,y_+20, x_+40+140-140,y_+40,fill="#222222",outline="#222222")
		main2.create_oval(x_+280-140,y_+20, x_+20+280-140,y_+40,fill="#222222",outline="#222222")

		main2.create_rectangle(x_+20+140+10-140,y_+20, x_+20+280-10-140,y_+30,fill="#222222",outline="#222222")
		main2.create_rectangle(x_+20+140-140,y_+30, x_+20+280-140,y_+50-1,fill="#222222",outline="#222222")




		main2.create_oval(x_+20+140-140+2+140,y_+20, x_+40+140-140+2+140,y_+40,fill="#222222",outline="#222222")
		main2.create_oval(x_+280-140+2+140,y_+20, x_+20+280-140+2+140,y_+40,fill="#222222",outline="#222222")

		main2.create_rectangle(x_+20+140+10-140+2+140,y_+20, x_+20+280-10-140+2+140,y_+30,fill="#222222",outline="#222222")
		main2.create_rectangle(x_+20+140-140+2+140,y_+30, x_+20+280-140+2+140,y_+50-1,fill="#222222",outline="#222222")




		main2.create_oval(x_+20+140-140+2+140+2+140,y_+20, x_+40+140-140+2+140+2+140,y_+40,fill="#ffffff",outline="#ffffff")
		main2.create_oval(x_+280-140+2+140+2+140,y_+20, x_+20+280-140+2+140+2+140,y_+40,fill="#ffffff",outline="#ffffff")

		main2.create_rectangle(x_+20+140+10-140+2+140+2+140,y_+20, x_+20+280-10-140+2+140+2+140,y_+30,fill="#ffffff",outline="#ffffff")
		main2.create_rectangle(x_+20+140-140+2+140+2+140,y_+30, x_+20+280-140+2+140+2+140,y_+50-1,fill="#ffffff",outline="#ffffff")



		main2.create_text(x_+20+70,y_+20+15,text="My Profile",fill="#ffffff",font=("FreeMono",13))
		main2.create_text(x_+20+70+140+1,y_+20+15,text="New User",fill="#ffffff",font=("FreeMono",13))
		main2.create_text(x_+20+70+140+1+140,y_+20+15,text="Users",fill="#000000",font=("FreeMono",13,"bold"))



		ar=[x_+20+140+2+2+140,y_+50]

		cx,cy=x_+20+140-10+2+2+140,y_+50-10

		a_=0

		for a in range(90):
			x=10*math.sin(math.radians(a_))+cx
			y=10*math.cos(math.radians(a_))+cy

			ar.append(x)
			ar.append(y)

			a_+=1

		main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")

		uns.place_forget()
		ems.place_forget()
		cons.place_forget()		
		pss.place_forget()


		ar=[x_+20+140*3+2+2,y_+50]

		cx,cy=x_+20+140*3+2+2+10,y_+50-10

		a_=0

		for a in range(90):
			x=10*math.sin(math.radians(a_))+cx
			y=10*math.cos(math.radians(a_))+cy

			ar.append(x)
			ar.append(y)

			a_-=1

		main2.create_polygon(ar,fill="#ffffff",outline="#ffffff")


		if myp[-1]==0:

			info=ImageTk.PhotoImage(file="data/info.png")
			uns.place_forget()
			ems.place_forget()
			cons.place_forget()	
			pss.place_forget()



			main2.create_image(x_+200+30,y_+250-50,image=info,anchor="nw")

			main2.create_text(x_+200+100+30+30,y_+250,text="Login as Administrator",font=("FreeMono",15),anchor="w")



			return

		xx=x_+20+10



		main2.create_oval(xx,y_+50+20+5, xx+20,y_+50+20+20,fill="#222222",outline="#222222")
		main2.create_oval(xx+572+50-20,y_+50+20+5, xx+572+50,y_+50+20+20,fill="#222222",outline="#222222")

		main2.create_rectangle(xx+10,y_+50+20+5, xx+572+50-10,y_+50+20+10+5,fill="#222222",outline="#222222")
		main2.create_rectangle(xx,y_+50+20+10+5, xx+572+50,y_+50+20+30,fill="#222222",outline="#222222")

		x_=xx+143
		for x in range(3):
			#main2.create_line(x_,y_+50+20+5, x_,y_+50+20+30,fill="#ffffff")
			main2.create_line(x_-1,y_+50+20+5, x_-1,y_+50+20+30,fill="#999999")


			if x==0:
				main2.create_text(xx-143/2+143,y_+50+20+5+12.5,text="User Name",font=("FreeMono",13),fill="#ffffff")
				x_+=143+50
			else:
				x_+=143

			if x==1:
				main2.create_text(xx+96.5+143,y_+50+20+5+12.5,text="Email",font=("FreeMono",13),fill="#ffffff")


			if x==2:
				main2.create_text(xx+193+143/2+143,y_+50+20+5+12.5,text="Contact",font=("FreeMono",13),fill="#ffffff")
				main2.create_text(xx+193+143/2+143+143,y_+50+20+5+12.5,text="Admin",font=("FreeMono",13),fill="#ffffff")

		main2.create_line(xx,y_+50+20+30, xx,y_+500-20-10, xx+680+42+18,y_+500-20-10, xx+680+42+18,y_+50+20+30
			,xx+680+42+18-140+22,y_+50+20+30, xx,y_+50+20+30,fill="#999999")
		userframe.place(in_=root,x=xx+1,y=y_+50+20+30+1+50)

		userc.delete("all")


		dbuser=db.connect('data/users.db')
		cur=dbuser.cursor()


		cur.execute("SELECT * FROM user")
		rows=cur.fetchall()

		st=0

		yvar3=0
		yy=30

		user_array=[]
		for row in rows:
			#print(row)

			if st==0:
				col="#ffffff"
				st=1
			elif st==1:
				col="#f3f3f3"
				st=0

			if row[0]==profileid:
				col="cyan"



			userc.create_rectangle(0,yy-30,680+42,yy,fill=col,outline=col)

			userc.create_text(142/2,yy-15,text=row[1][:15],fill="#000000",font=("FreeMono",13),anchor="c")

			if len(row[2])>21:
				
				userc.create_text(142+193/2,yy-15,text=row[2][:21-3]+"...",fill="#000000",font=("FreeMono",13),anchor="c")
			else:
				userc.create_text(142+193/2,yy-15,text=row[2],fill="#000000",font=("FreeMono",13),anchor="c")
			userc.create_text(142+193+143/2,yy-15,text=row[3][:15],fill="#000000",font=("FreeMono",13),anchor="c")
			

			if row[-1]==0:
				
				userc.create_image(525.5,yy-(30-((30-25)/2)),image=cirb,anchor="nw")
				userc.create_image(525.5+25,yy-(30-((30-25)/2)),image=cirb,anchor="nw")
				userc.create_image(525.5+12.5,yy-(30-((30-25)/2)),image=sqb,anchor="nw")
				userc.create_image(525.5+5,yy-(30-((30-25)/2))+5,image=cirw,anchor="nw")


			elif row[-1]==1:
				userc.create_image(525.5,yy-(30-((30-25)/2)),image=cirr,anchor="nw")
				userc.create_image(525.5+25,yy-(30-((30-25)/2)),image=cirr,anchor="nw")
				userc.create_image(525.5+12.5,yy-(30-((30-25)/2)),image=sqr,anchor="nw")
				userc.create_image(525.5+25+5,yy-(30-((30-25)/2))+5,image=cirw,anchor="nw")

			userc.create_image(622+37.5,yy-(30-((30-20)/2)),image=qu,anchor="nw")


			user_array.append([row[0],[525.5,yy-(30-((30-25)/2)),525.5+25+25,yy-(30-((30-25)/2))+25],[622+37.5+12.5,yy-(30-((30-20)/2))+10],row[-1]])

			


			

			yvar3+=30
			yy+=30

		xv=143-1
		for x in range(4):

			userc.create_line(xv,0, xv,yvar3,fill="#ffffff")
			userc.create_line(xv-1,0, xv-1,yvar3,fill="#999999")

			if x==0:
				xv+=143+50
			else:
				xv+=143

		userc.create_line(0,yvar3, 680+42,yvar3,fill="#999999")

		yvar3+=50

		userc["scrollregion"]=(0,0,680+42,yvar3)

	    


prof_st=0

def search():
	global svar,dashb_state,searche,si_con,ms_con,lvar

	

	if not lvar==0:

		if not searche.get()==svar:

			if dashb_state=="sell_items" and si_con==0:
				draw_sellitems()

			if dashb_state=="stock" and ms_con==0:
				draw_stock()

			if dashb_state=="reports":
				draw_reports()

			svar=searche.get()

		

	root.after(1,search)
 
svar=""


def checkscroll():


	global main2,cscroll

	if not cscroll==main2.canvasy(0):

		if dashb_state=="sell_items" and si_con==0:
			draw_sellitems()
			cscroll=main2.canvasy(0)

		if dashb_state=="stock" and ms_con==0:
			draw_stock()

			cscroll=main2.canvasy(0)

	root.after(100,checkscroll)





cscroll=0



rr_=tk.Canvas(height=30,width=1021,bg="#000000",relief="flat", highlightthickness=0,border=0)


rr_.create_line(0,0,1021,0,fill="#ffffff")
vv=["Item Name","Selling Price","Price Sold","Quantity","Date","Total","Profit"]
v=1000/7
x=v
for a in range(7):

	if a==4:
		x+=20

	rr_.create_line(x,0,x,30,fill="#ffffff")

	if a==4:
		rr_.create_text(x-10-v/2,15,text=vv[a],font=("FreeMono",13),fill="#ffffff")
	else:
		rr_.create_text(x-v/2,15,text=vv[a],font=("FreeMono",13),fill="#ffffff")


	x+=v

searche=tk.Entry(width=33,relief="flat",highlightthickness=0,border=0,bg="#ffffff",font=("FreeMono",13)
,fg="#000000",insertbackground="#000000" )






def month_str(m):
	global cal_year

	if m==1:
		mm="January"
		d=31
	elif m==2:
		mm="Febraury"

		if cal_year%4==0:
			d=29
		else:
			d=28

	elif m==3:
		mm="March"
		d=31

	elif m==4:
		mm="April"
		d=30
	elif m==5:
		mm="May"
		d=31
	elif m==6:
		mm="June"
		d=30
	elif m==7:
		mm="July"
		d=31
	elif m==8:
		mm="August"
		d=31
	elif m==9:
		mm="September"
		d=30
	elif m==10:
		mm="October"
		d=31
	elif m==11:
		mm="November"
		d=30

	elif m==12:
		mm="December"
		d=31

	return [mm,d]

def cal_commands(e):

	global cal_year,cal_month,cal_day,main1,date__,daten,days_array,dvar2,cal_st

	con=0

	if 15-3<=e.x<=25+3:
		if 10<=e.y<=30:
			cal_year-=1
			cal_day=1
			con=1
			cal_st=0



	if 73-3<=e.x<=83+3:
		if 10<=e.y<=30:
			cal_year+=1
			cal_day=1
			con=1
			cal_st=0

	if 95-3-80<=e.x<=105+3-80:
		if 30+10<=e.y<=50+10:

			cal_month-=1
			cal_day=1
			cal_st=0

			if cal_month==0:
				cal_month=12
				cal_year-=1
			con=1


	if 195-3-80<=e.x<=205+3-80:
		if 30+10<=e.y<=50+10:
			cal_month+=1
			cal_day=1
			cal_st=0

			if cal_month==13:
				cal_month=1
				cal_year+=1

			con=1

	for d in days_array:

		if d[1]<=e.x<=d[3]:
			if d[2]<=e.y<=d[4]:
				cal_day=int(d[0])
				cal_st=0

				con=1





	con2=0

	300-40+20+10

	cx,cy=300-40+10,10+10
	r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

	if r<=10:
		con2=1

	if con2==0:
		cx,cy=300-40+10+10,10+10
		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=10:
			con2=1

	if con2==0:

		if 300-40+10<=e.x<=300-40+20:
			if 10<=e.y<=30:
				con2=1



	if con2==1:
		if cal_st==0:
			cal_st=1
		elif cal_st==1:
			cal_st=0

		if cal_st==1:
			cal_day="*"

		elif cal_st==0:
			cal_day=1

	draw_cal()
	daten=str(cal_day)+"-"+str(cal_month)+"-"+str(cal_year)

	main1.delete(date__)

	if dvar2==1:
		x_=250+(wd-250-1000)/2
	elif dvar2==0:
		x_=(wd-1000)/2

	date__=main1.create_text(x_+40,25,text=daten,font=("FreeMono",13),anchor="w",fill="#ffffff")

	main2["scrollregion"]=(0,0,wd,ht-50)
	draw_reports()

cal_st=0
def draw_cal():
	global cal,cal_day,cal_month,cal_year,days_array,cal_st

	days_array=[]


	cal.delete("all")

	cal.create_text(300-50,20,text="All days",fill="#ffffff",font=("FreeMono",13),anchor="e")
	cal.create_arc(300-40,10,300-40+20,30,outline="#ffffff",style="arc",start=90,extent=180)
	cal.create_arc(300-40+10,10,300-40+20+10,30,outline="#ffffff",style="arc",start=270,extent=180)
	cal.create_line(300-40+10,10, 300-40+20,10,fill="#ffffff")
	cal.create_line(300-40+10-1,30, 300-40+20,30,fill="#ffffff")

	if cal_st==0:
		cal.create_oval(300-40+3,10+3,300-40+20-3,30-3,fill="#ffffff",outline="#ffffff")
	elif cal_st==1:
		cal.create_oval(300-40+10+3,10+3,300-40+20+10-3,30-3,outline="#ffffff",fill="#ffffff")

	cal.create_text(50,20,anchor="c",text=str(cal_year),font=("FreeMono",13),fill="#ffffff")

	cal.create_text(20,20,text="<",font=("FreeMono",13),anchor="c",fill="#ffffff")
	cal.create_text(78,20,text=">",font=("FreeMono",13),anchor="c",fill="#ffffff")

	cal.create_text(150-80,50,text=month_str(cal_month)[0],font=("FreeMono",13),anchor="c",fill="#ffffff")

	cal.create_text(100-80,50,text="<",font=("FreeMono",13),anchor="c",fill="#ffffff")
	cal.create_text(200-80,50,text=">",font=("FreeMono",13),anchor="c",fill="#ffffff")

	days=["mon","tue","wed","thur","fri","sat","sun",]

	v=(300/7)/2

	for d in days:

		cal.create_text(v,80,text=d,font=("FreeMono",13),anchor="c",fill="#ffffff")

		v+=300/7


	cal.create_line(0,90,300,90,fill="#ffffff")


	d_=month_str(cal_month)[1]

	day=datetime.date(int(cal_year),int(cal_month),1)

	d2=day.weekday()


	dy=120

	c=1

	for ddd in range(d_):

		con=0

		if not cal_day=="*":
			if ddd+1==int(cal_day):
				con=1
				cal.create_rectangle((300/7/2)+(300/7)*d2-(300/7/2),dy-(300/7/2),
					(300/7/2)+(300/7)*d2+(300/7/2),dy+(300/7/2),fill="#fa677f",outline="#fa677f")
				cal.create_text((300/7/2)+(300/7)*d2,dy,text=str(ddd+1),font=("FreeMono",13),fill="#000000")

		if con==0:
			cal.create_text((300/7/2)+(300/7)*d2,dy,text=str(ddd+1),font=("FreeMono",13),fill="#ffffff")

		days_array.append([ddd+1,(300/7/2)+(300/7)*d2-(300/7/2),dy-(300/7/2),(300/7/2)+(300/7)*d2+(300/7/2),dy+(300/7/2)])

		
		if d2==6:
			d2=0

			dy+=300/7
			c+=1
		else:
			d2+=1




		if c==6:
			dy=120







now=datetime.datetime.now()
yy=now.year
mm=now.month
dd=now.day
daten=str(dd)+"-"+str(mm)+"-"+str(yy)

date__=()
days_array=[]

cal_year=int(yy)
cal_month=int(mm)
cal_day=int(dd)


cart_array=[]
cart=tk.Canvas(width=wd,height=50,bg="#000000",highlightthickness=0,border=0,relief="flat")



cal_con=0
cal=tk.Canvas(height=313,width=300,bg="#000000",relief="flat", highlightthickness=0,border=0)
cal.bind("<Button-1>",cal_commands)
draw_cal()



cartc_array=[]


def cartc_commands(e):
	global cart_array,cartc_array,cv,si_con,cartframe,cartc,ht


	for a in cartc_array:
		
		cx,cy=a[1],a[2]
		y=cartc.canvasy(e.y)
		r=math.sqrt((e.x-cx)**2 + (y-cy)**2)

		if r<=10:

			cart_array.pop(a[0])

			dashb.delete(cv)
			yy=ht-140-40-20
			cv=dashb.create_text(100+15-10,yy+33.5,text=str(len(cart_array)),fill="#32fca7",font=("FreeMono",13),anchor="w")

			if len(cart_array)==0:
				si_con=0
				cartframe.place_forget()
			draw_sellitems()


cartframe=tk.Frame(width=1000-60,height=419,bg="#ffffff")

yvar2=0
cartc=tk.Canvas(cartframe,width=1000-18-60,height=419,bg="#ffffff",relief="flat",highlightthickness=0,border=0,
	scrollregion=(0,0,982,419))
cartc.bind("<Button-1>",cartc_commands)
cartc.bind_all("<MouseWheel>",_on_mousewheel)
cartc.create_line(0,0,0,100,fill="blue")

vbar2=tk.Scrollbar(cartframe,orient=tk.VERTICAL)
vbar2.pack(side=tk.RIGHT,fill=tk.Y)
vbar2.config(command=cartc.yview)

cartc.config(yscrollcommand=vbar2.set)

cartc.pack(side=tk.RIGHT)




def user_comm(e):

	global dvar,dvar2,dashb_state,main2,as_im,as_image,ax,ay,intro,lvar,si_con,ms_con
	global si_quantity,psoldat,si_desc,as_n,as_bp,as_sp,as_q,as_de,rr_,searche,cart,cal_con,wd,cartframe,cart_array
	global ascon2,as_image,ascon,uns,ems,cons,pss,userframe
	global user_array,userc,myp,profileid,yvar3,admin_st1,admin_st2_1,barc,pst,main2



	#user_array.append([row[0],[525.5,yy-32.5,525.5+25+25,yy-32.5+25],[622+17.5+12.5,yy-32.5+12.5]])

	x=userc.canvasx(e.x)
	y=userc.canvasy(e.y)

	for i in user_array:
		if i[1][0]<=x<=i[1][2]:
			if i[1][1]<=y<=i[1][3]:


				if i[-1]==0:
					v=1
				elif i[-1]==1:
					v=0


				dbuser=db.connect('data/users.db')
				cur=dbuser.cursor()
				cur.execute("UPDATE user SET admin='"+str(v)+"' WHERE user_id="+str(i[0])+" ")

				dbuser.commit()


				
				cur=dbuser.cursor()

				cur.execute("SELECT * FROM user WHERE user_id="+str(profileid))
				rows=cur.fetchall()

				for row in rows:

			
					myp=[]

					for i in row:
						myp.append(i)


					admin_st1=row[-1]
					admin_st2_1=row[-1]

					myp3=[row[1],row[2],row[3],row[-2]]

				userframe.place_forget()

				draw_profiles()
				message(main2,90+(wd-800-90)/2+400,(ht-50)/2+250+20,1,"Admin status changed!")
				return

		cx,cy=i[2]

		r=math.sqrt( ((cx-x)**2)+((cy-y)**2) )

		if r<=12.5:
			dbuser=db.connect('data/users.db')
			cur=dbuser.cursor()

			cur.execute("DELETE FROM user WHERE user_id="+str(i[0])+"")

			dbuser.commit()


			if yvar3<=368:

				userc["scrollregion"]=(0,0,680,368)

			if profileid==i[0]:
				barc=[]

				ascon2=0
				as_image=""
				ascon=0
				dvar=0
				dvar2=1




				uns.place_forget()
				ems.place_forget()
				cons.place_forget()
				pss.place_forget()

				userframe.place_forget()


				cartframe.place_forget()
				cart_array=[]

				si_quantity.place_forget()
				psoldat.place_forget()
				si_desc.place_forget()
				cart.place_forget()
				cart_array=[]

				as_n.place_forget()
				as_bp.place_forget()
				as_sp.place_forget()
				as_q.place_forget()
				as_de.place_forget()

				rr_.place_forget()

				searche.place_forget()

				searche.delete(0,tk.END)


				x_,y_=(wd/2)-350/2,(ht-200)/2
				lvar=0
				searche.place_forget()
				intro.place(in_=root,x=0,y=0)
				un.place(in_=root,x=x_+150-10,y=y_+30)
				pw.place(in_=root,x=x_+150-10,y=y_+30+50)
				pst=0
				show()

				cal.place_forget()


				ms_con=0
				si_con=0

				un.focus_set()
			else:
				draw_profiles()

				message(main2,90+(wd-800-90)/2+400,(ht-50)/2+250+20,1,"User removed!")
				return
userframe=tk.Frame(width=620+18+60+42,height=368,bg="#ffffff")

yvar3=0
userc=tk.Canvas(userframe,width=620+60+42,height=368,bg="#ffffff",relief="flat",highlightthickness=0,border=0,
	scrollregion=(0,0,620+60+42,368))
userc.bind("<Button-1>",user_comm)
userc.bind_all("<MouseWheel>",_on_mousewheel)
userc.create_line(0,0,0,100,fill="blue")

vbar3=tk.Scrollbar(userframe,orient=tk.VERTICAL)
vbar3.pack(side=tk.RIGHT,fill=tk.Y)
vbar3.config(command=userc.yview)

userc.config(yscrollcommand=vbar3.set)

userc.pack(side=tk.RIGHT)


def draw_main1(aaa=0):
	global main1,logw,myp,pp



	main1.delete("all")

	logw=ImageTk.PhotoImage(file="data/logoutw.png")
	main1.create_image(wd-20-25,10,image=logw,anchor="nw")

	name=myp[1]

	pic=myp[4]

	if pic==1:
		pp=ImageTk.PhotoImage(file="Images/pp_"+str(myp[0])+"s.jpg")
	else:
		pp=ImageTk.PhotoImage(file="data/userd2.png")

	main1.create_image(10+aaa,5,image=pp,anchor="nw")

	cx,cy=30+aaa,25

	ar=[50+aaa,5]


	a_=180
	for a in range(180):

		x=20*math.sin(math.radians(a_))+cx
		y=20*math.cos(math.radians(a_))+cy

		ar.append(x)
		ar.append(y)

		a_-=1

	ar.append(50+aaa)
	ar.append(45)


	main1.create_polygon(ar,fill="#222222",outline="#222222")

	ar=[10+aaa,5]


	a_=180
	for a in range(180):

		x=20*math.sin(math.radians(a_))+cx
		y=20*math.cos(math.radians(a_))+cy

		ar.append(x)
		ar.append(y)

		a_+=1

	ar.append(10+aaa)
	ar.append(45)


	main1.create_polygon(ar,fill="#222222",outline="#222222")


	main1.create_text(10+40+10+aaa,25,text=name[:22],anchor="w",font=("FreeMono",13),fill="#ffffff")


pp=()


try:
	dbstock=db.connect('data/stock.db')
	cur=dbstock.cursor()
	cur.execute("""CREATE TABLE items(
		items_id INT,
		name VARCHAR(255),
		bp INT,
		sp INT,
		quantity INT,
		description VARCHAR(255),
		picture INT);""")
	dbstock.close()


except:
	pass


_start_time=0

m1=0
m2=0
m3=0
m4=0
m5=0
def message(c,x,y,c1,txt):
	global m1,m2,m3,m4,m5,_start_time

	m5=c

	c.delete(m1)
	c.delete(m2)
	c.delete(m3)
	c.delete(m4)

	if c1==0:
		col="#ee6b6e"
	elif c1==1:
		col="#5bd75b"

	m1=c.create_rectangle(x-120,y-15, x+120,y+15,fill=col,outline=col)
	m2=c.create_oval(x-120-15,y-15, x-120+15,y+15,fill=col,outline=col)
	m3=c.create_oval(x+120-15,y-15, x+120+15,y+15,fill=col,outline=col)
	m4=c.create_text(x,y,text=txt,fill="#000000",font=("FreeMono",13))

	_start_time=time.time()


def timeout():
	global _start_time
	global m1,m2,m3,m4,m5

	try:

		if time.time()>=_start_time+2:

			m5.delete(m1)
			m5.delete(m2)
			m5.delete(m3)
			m5.delete(m4)
	except:
		pass

	root.after(1,timeout)




try:
	dbsales=db.connect('data/sales.db')
	cur=dbsales.cursor()	
	cur.execute("""CREATE TABLE sales_(
		sales_id INT,
		name VARCHAR(255),
		sp INT,
		ps INT,
		quantity INT,
		date_ VARCHAR(255),
		total INT,
		profit INT );""")

	dbsales.close()
except:
	pass


try:
	dbuser=db.connect('data/users.db')
	cur=dbuser.cursor()	
	cur.execute("""CREATE TABLE user(
		user_id INT,
		name VARCHAR(255),
		email VARCHAR(255),
		contact VARCHAR(255),
		pic INT,
		password VARCHAR(255),
		admin INT);""")

	dbuser.close()
except:
	pass


def add_comma(v):

	n=int(len(str(v))/3)




	ar=[]

	c=-1
	c2=0




	if n>=1:
		for a in range(len(str(v))):
			ar.append(str(v)[c])

			c-=1
			c2+=1

			if not a==len(str(v))-1:

				if c2==3:
					ar.append(",")
					c2=0
	else:
		return str(v)




    

	result=""

	c=-1

	for i in range(len(ar)):
		result+=ar[c]
		c-=1

	return result




barc=[]
bc=()
info=()


carti=()





cl=()

profw=()
profb=()
sellw=()
sellb=()
neww=()
newb=()
maniw=()
manib=()
repw=()
repb=()

diw=()
diw2=()
dib=()

logw=()
logb=()

cali=()

rem=()
qq=()

cirw=()
cirr=()
cirb=()

recr=()
recb=()


xvarray=[]

for a in range(500):
	xvarray.append(a)


lvar=0

draw_dashb()
search()
gentotal()
checkscroll()
un.focus_set()
invalide()


timeout()
root.mainloop()