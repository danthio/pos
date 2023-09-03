import tkinter as tk
import math
from tkinter import filedialog
from PIL import Image,ImageTk,ImageEnhance
import sqlite3 as db
import xv
import os

import datetime


def login(e):
	global intro,un,pw,lvar,state,dvar,dvar2,dashb_state,main2
	global cal_year,cal_month,cal_day,daten


	x_,y_=(wd/2)-350/2,200
	#87.5 262.5
	#150 175
	if x_+87.5<=e.x<=x_+262.5:
		if y_+150<=e.y<=y_+175:



			if un.get()=="admin" and pw.get()=="pass":
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

				move_dashb()


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


def move_dashb():
	global dx,dashb,dvar

	if dvar==1:
		dvar=0
		dashb.place(in_=root,x=-250,y=0)

	elif dvar==2:
		dvar=0
		dashb.place(in_=root,x=0,y=0)








root=tk.Tk()

wd=root.winfo_screenwidth()#-15
ht=root.winfo_screenheight()-75


root.resizable(0,0)
root.title("Point of Sale")
root.geometry(str(wd)+"x"+str(ht)+"+0+0")



########################

def main1_commands(e):
	global dvar,dvar2,dashb_state,main2,as_im,as_image,ax,ay,intro,lvar,si_con,ms_con
	global si_quantity,psoldat,si_desc,as_n,as_bp,as_sp,as_q,as_de,rr_,searche,cart,cal_con,wd

	if 10<=e.x<=35:
		if 12.5<=e.y<=37.5:
			dvar=2
			dvar2=1

			if dashb_state=="sell_items":
				main2["scrollregion"]=(0,0,wd,ht)
				draw_sellitems()
			elif dashb_state=="add_stock":
				draw_addstock()
				main2["scrollregion"]=(0,0,wd,ht-50)

				if not as_image=="":
					main2.delete(as_im)

					if dvar2==1:
						x_,y_=250+(wd-250-800)/2,30
					elif dvar2==0:
						x_,y_=(wd-800)/2,30
					
					as_im=main2.create_image(x_+400-20+ax,y_+20+ay,image=as_image,anchor="nw")


			elif dashb_state=="stock":
				main2["scrollregion"]=(0,0,wd,ht-50)
				draw_stock()
			elif dashb_state=="reports":
				main2["scrollregion"]=(0,0,wd,ht-50)
				draw_reports()

				if cal_con==1:

					x_=250+(wd-250-1000)/2
						
					cal.place(in_=root,x=x_+40,y=40)
			elif dashb_state=="settings":
				draw_settings()				

			move_dashb()
	if wd-20-25<=e.x<=wd-20:
		if 10<=e.y<=35:

			dvar=0
			dvar2=1

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


			x_,y_=(wd/2)-350/2,200
			lvar=0
			searche.place_forget()
			intro.place(in_=root,x=0,y=0)
			un.place(in_=root,x=x_+150,y=y_+30)
			pw.place(in_=root,x=x_+150,y=y_+30+50)

			cal.place_forget()


			ms_con=0
			si_con=0

			un.focus_set()

	if dashb_state=="reports":


		if dvar2==1:
			x_=250+(wd-250-1000)/2
		elif dvar2==0:
			x_=(wd-1000)/2


		if x_<=e.x<=x_+30:
			if 10<=e.y<=40:

				if cal_con==0:
					cal.place(in_=root,x=x_+40,y=40)
					cal_con=1

				elif cal_con==1:

					cal.place_forget()
					cal_con=0

def _on_mousewheel(e):
	global main2,dashb_state,si_con,ms_con,yvar,ht

	if dashb_state=="sell_items" and si_con==0 and yvar>ht-50:
		main2.yview_scroll(int(-1*(e.delta/120)), "units")

	if dashb_state=="stock" and ms_con==0 and yvar>ht-50:
		main2.yview_scroll(int(-1*(e.delta/120)), "units")

	if dashb_state=="reports" and yvar>ht-50:
		main2.yview_scroll(int(-1*(e.delta/120)), "units")


def main2_commands(e):
	global file_path,as_image,main2,as_im,ascon,ax,ay,ascon2,sellarray, si_con,seli, msarray,ms_con
	global as_n,as_bp,as_sp,as_q,as_de,msimage,msi,msf,mscon,mscon2,vbar1,cal_con,cal,cart_array,cv,dashb



	if dashb_state=="stock":
		y=main2.canvasy(e.y)
		yy=main2.canvasy(0)

		for v in msarray:

			if v[1]<=e.x<=v[3]:
				if v[2]<=y<=v[4]:
					

					if ms_con==0:
						ms_con=1
						seli=v[0]
						draw_stock()

		if dvar2==1:
			x1,y1=250+(wd-250-800)/2,50+yy
		elif dvar2==0:
			x1,y1=(wd-800)/2,50+yy

		cx,cy=x1+785-5+40,y1+15

		r=math.sqrt((e.x-cx)**2 + (y-cy)**2)

		if r<=15:
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

		if x1+255<=e.x<=x1+385:
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
							ext=a.split(".")[1]


							if os.path.isfile("Images/"+a):
								os.remove("Images/"+a)

							ff="Images/"+str(seli)+"_s."+ext
							if os.path.isfile(ff):
								os.remove(ff)    							

							ff="Images/"+str(seli)+"_sd."+ext
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
									ext=a.split(".")[1]


									if os.path.isfile("Images/"+a):
										os.remove("Images/"+a)

									ff="Images/"+str(seli)+"_s."+ext
									if os.path.isfile(ff):
										os.remove(ff)    							

									ff="Images/"+str(seli)+"_sd."+ext
									if os.path.isfile(ff):
										os.remove(ff) 

							im=Image.open(msf)
							im.save("Images/"+str(seli)+"."+msf.split(".")[1])


							x,y=im.size



							def darken(im,v):
								px=im.load()

								list_=[]

								for y_ in range(200):
									for x_ in range(300):
										coord=px[x_,y_]	

										r=int(coord[0]/3)
										b=int(coord[1]/3)
										g=int(coord[2]/3)

										list_.append(r)
										list_.append(b)
										list_.append(g)	


								colors = bytes(list_)
								img = Image.frombytes('RGB', (300, 200), colors)
								img.save("Images/"+str(v)+"_sd."+msf.split(".")[1])	


							if (x/y)>(300/200):
								bx=x-(x*((300/200)/(x/y) ) )
								im=im.crop((bx,0,x-bx,y))
								im=im.resize((300,200))
								im.save("Images/"+str(seli)+"_s."+msf.split(".")[1])
								darken(im,seli)

							elif (x/y)<(300/200):
								by=(y-(y*((x/y)/(300/200))  ))/2

								im=im.crop((0,by,x,y-by))
								im=im.resize((300,200))
								im.save("Images/"+str(seli)+"_s."+msf.split(".")[1])
								darken(im,seli)
							elif (x/y)==(1.5):
								im=im.resize((300,200))
								im.save("Images/"+str(seli)+"_s."+msf.split(".")[1])
								darken(im,seli)


				elif pic==0:
					if not msimage=="":
						dbstock=db.connect('data/stock.db')
						cur=dbstock.cursor()

						cur.execute("UPDATE items SET picture=1 WHERE items_id="+str(seli)+" ")
						dbstock.commit()	


						im=Image.open(msf)
						im.save("Images/"+str(seli)+"."+msf.split(".")[1])


						x,y=im.size



						def darken(im,v):
							px=im.load()

							list_=[]

							for y_ in range(200):
								for x_ in range(300):
									coord=px[x_,y_]	

									r=int(coord[0]/3)
									b=int(coord[1]/3)
									g=int(coord[2]/3)

									list_.append(r)
									list_.append(b)
									list_.append(g)	


							colors = bytes(list_)
							img = Image.frombytes('RGB', (300, 200), colors)
							img.save("Images/"+str(v)+"_sd."+msf.split(".")[1])	


						if (x/y)>(300/200):
							bx=x-(x*((300/200)/(x/y) ) )
							im=im.crop((bx,0,x-bx,y))
							im=im.resize((300,200))
							im.save("Images/"+str(seli)+"_s."+msf.split(".")[1])
							darken(im,seli)

						elif (x/y)<(300/200):
							by=(y-(y*((x/y)/(300/200))  ))/2

							im=im.crop((0,by,x,y-by))
							im=im.resize((300,200))
							im.save("Images/"+str(seli)+"_s."+msf.split(".")[1])
							darken(im,seli)
						elif (x/y)==(1.5):
							im=im.resize((300,200))
							im.save("Images/"+str(seli)+"_s."+msf.split(".")[1])
							darken(im,seli)




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



		if x1+415<=e.x<=x1+545:
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
							ext=a.split(".")[1]


							if os.path.isfile("Images/"+a):
								os.remove("Images/"+a)

							ff="Images/"+str(seli)+"_s."+ext
							if os.path.isfile(ff):
								os.remove(ff)    							

							ff="Images/"+str(seli)+"_sd."+ext
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

		cx,cy=x1+580,y1+220+10

		r=math.sqrt((e.x-cx)**2 + (y-cy)**2)


		if r<=40 and msimage=="":
			msf=filedialog.askopenfilename()

			im=Image.open(msf)
			mscon2=1
			mscon=1

			ext=msf.split(".")[1]

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

			msi=main2.create_image(x1+400-20+ax,y1+20+ay+10,image=msimage,anchor="nw")
		cx,cy=x1+765+5,y1+435+10

		r=math.sqrt((e.x-cx)**2 + (y-cy)**2)

		if r<=15:
			if not msimage=="":

				main2.delete(msi)
				msimage=""
				mscon=0
				mscon2=0
				msf=""
			

	elif dashb_state=="sell_items":
		y=main2.canvasy(e.y)
		yy=main2.canvasy(0)





		if dvar2==1:
			x1,y1=250+(wd-250-800)/2,50+yy
		elif dvar2==0:
			x1,y1=(wd-800)/2,50+yy


		if si_con==2:

			cx,cy=x1+785-5+40,y1+15

			r=math.sqrt((e.x-cx)**2 + (y-cy)**2)

			if r<=15:
				si_con=0
				vbar1.pack_forget()
				main2.pack_forget()

				vbar1.pack(side=tk.RIGHT,fill=tk.Y)
				main2.pack(side=tk.LEFT)
				draw_sellitems()

		for v in sellarray:

			if v[1]<=e.x<=v[3]:
				if v[2]<=y<=v[4]:
					

					if si_con==0:
						si_con=1
						seli=v[0]
						draw_sellitems()
						

		cx,cy=x1+785-5+40,y1+15

		r=math.sqrt((e.x-cx)**2 + (y-cy)**2)

		if r<=15:
			si_con=0

			vbar1.pack_forget()
			main2.pack_forget()

			vbar1.pack(side=tk.RIGHT,fill=tk.Y)
			main2.pack(side=tk.LEFT)
			draw_sellitems()

		if x1+555<=e.x<=x1+745:
			if y1+420<=y<=y1+450:
				#add to cart
				print("sell items")


				ps=psoldat.get()
				quantity=si_quantity.get()


				try:
					ps=int(ps)
					quantity=int(quantity)
				except:
					return

				cart_array.append([seli,int(ps),int(quantity)])

				dashb.delete(cv)
				cv=dashb.create_text(110,ht-200+12.5,text=str(len(cart_array)),fill="#ffffff",font=("FreeMono",13),anchor="w")


				"""






				dbsales=db.connect("sales.db")
				cur=dbsales.cursor()

				cur.execute("SELECT MAX(sales_id) FROM sales_")

				rows=cur.fetchall()

				v=0

				for row in rows:
					v=row[0]


				if v==None:
					v=1
				else:
					v+=1




				dbstock=db.connect("stock.db")
				cur=dbstock.cursor()

				cur.execute("SELECT * FROM items WHERE items_id="+str(seli)+"")
				rows=cur.fetchall()

				for row in rows:
					name=row[1]
					sp=row[3]
					bp=row[2]

					q=row[4]


				import datetime

				date_=datetime.datetime.now()

				total=ps*quantity

				profit=total-(int(bp)*quantity)




				sales_(v,name,sp,ps,quantity,date_,total,profit)


				dbstock=db.connect('stock.db')
				cur=dbstock.cursor()

				cur.execute("UPDATE items SET quantity='"+str(q-quantity)+"' WHERE items_id="+str(seli)+" ")

				dbstock.commit()"""

				si_con=0

				psoldat.delete(0,tk.END)
				si_quantity.delete(0,tk.END)

				psoldat.place_forget()
				si_quantity.place_forget()


				vbar1.pack_forget()
				main2.pack_forget()

				vbar1.pack(side=tk.RIGHT,fill=tk.Y)
				main2.pack(side=tk.LEFT)

				draw_sellitems()






	elif dashb_state=="add_stock":
		if dvar2==1:
			x_,y_=250+(wd-250-800)/2,30
		elif dvar2==0:
			x_,y_=(wd-800)/2,30


		cx,cy=x_+580,y_+220

		r=math.sqrt((e.x-cx)**2 + (main2.canvasy(e.y)-cy)**2)


		if r<=40 and ascon==0:
			file_path=filedialog.askopenfilename()

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

		cx,cy=x_+765+5,y_+435

		r=math.sqrt((e.x-cx)**2 + (e.y-cy)**2)

		if r<=15:
			as_image=""
			file_path=""
			ascon=0

			main2.delete(as_im)


		if x_+325<=e.x<=x_+475:
			if y_+460<=e.y<=y_+490:

				name=as_n.get()
				bp=as_bp.get()
				sp=as_sp.get()
				q=as_q.get()
				de=as_de.get(0.0, tk.END)


				de=de.split("\n")[0]

				if name=="" or bp=="" or sp=="":
					ascon2=1
					draw_addstock()

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



					def darken(im,v):
						px=im.load()

						list_=[]

						for y_ in range(200):
							for x_ in range(300):
								coord=px[x_,y_]	

								r=int(coord[0]/3)
								b=int(coord[1]/3)
								g=int(coord[2]/3)

								list_.append(r)
								list_.append(b)
								list_.append(g)	


						colors = bytes(list_)
						img = Image.frombytes('RGB', (300, 200), colors)
						img.save("Images/"+str(v)+"_sd."+file_path.split(".")[1])	


					if (x/y)>(300/200):
						bx=x-(x*((300/200)/(x/y) ) )
						im=im.crop((bx,0,x-bx,y))
						im=im.resize((300,200))
						im.save("Images/"+str(var)+"_s."+file_path.split(".")[1])
						darken(im,var)

					elif (x/y)<(300/200):
						by=(y-(y*((x/y)/(300/200))  ))/2

						im=im.crop((0,by,x,y-by))
						im=im.resize((300,200))
						im.save("Images/"+str(var)+"_s."+file_path.split(".")[1])
						darken(im,var)
					elif (x/y)==(1.5):
						im=im.resize((300,200))
						im.save("Images/"+str(var)+"_s."+file_path.split(".")[1])
						darken(im,var)




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


file_path=""
as_image=""
as_im=()
ax,ay=0,0
frame=tk.Frame(width=wd,height=ht,bg="#ffffff")
frame.pack()

main1=tk.Canvas(frame,width=wd,height=50,relief="flat",highlightthickness=0,border=0,bg="#ffffff")
main1.bind("<Button-1>",main1_commands)
main1.pack(side=tk.TOP)

main1.create_line( 13,8, 21,16, 13,24,fill="#000000",width=2)






fmain2=tk.Frame(frame,width=wd,height=ht-50,bg="#ffffff")
fmain2.pack(side=tk.TOP)

main2=tk.Canvas(fmain2,width=wd,height=ht-50,bg="#ffffff",relief="flat",highlightthickness=0,border=0,
	scrollregion=(0,0,wd,ht-50))
main2.bind("<Button-1>",main2_commands)
main2.bind_all("<MouseWheel>",_on_mousewheel)



vbar1=tk.Scrollbar(fmain2,orient=tk.VERTICAL)
vbar1.pack(side=tk.RIGHT,fill=tk.Y)
vbar1.config(command=main2.yview)

main2.config(yscrollcommand=vbar1.set)

main2.pack(side=tk.LEFT)

###################

def dashb_commands(e):

	global dvar,dashb,dashb_state,dvar2,as_im,as_image,ax,ay,si_con,ms_con,cal,cal_con
	global as_n,as_bp,as_sp,as_q,as_de,ht,wd,main2,si_quantity,psoldat,si_desc,searche,vbar1,cart
	global cart_array

	if 250-20-2-10<=e.x<=250:
		if 0<=e.y<=20+8-5+10:

			dvar=1
			dvar2=0

			if dashb_state=="sell_items":
				main2["scrollregion"]=(0,0,wd,ht-50)
				draw_sellitems()
			elif dashb_state=="add_stock":
				main2["scrollregion"]=(0,0,wd,ht-50)


				draw_addstock()

				if not as_image=="":
					main2.delete(as_im)

					if dvar2==1:
						x_,y_=250+(wd-250-800)/2,30
					elif dvar2==0:
						x_,y_=(wd-800)/2,30
					
					as_im=main2.create_image(x_+400-20+ax,y_+20+ay,image=as_image,anchor="nw")

			elif dashb_state=="stock":
				main2["scrollregion"]=(0,0,wd,ht-50)
				draw_stock()
			elif dashb_state=="reports":
				main2["scrollregion"]=(0,0,wd,ht-50)
				draw_reports()

				if cal_con==1:

					x_=(wd-1000)/2	
						
					cal.place(in_=root,x=x_+40,y=40)
			elif dashb_state=="settings":
				draw_settings()
			move_dashb()



	if 53<=e.y<=53+30:
		dashb_state="sell_items"
		draw_dashb()
		main2["scrollregion"]=(0,0,wd,ht-50)

		cal.place_forget()
		cal_con=0

		si_con=0

		vbar1.pack_forget()
		main2.pack_forget()

		vbar1.pack(side=tk.RIGHT,fill=tk.Y)
		main2.pack(side=tk.LEFT)

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
		move_dashb()
	elif 86<=e.y<=86+30:

		dashb_state="add_stock"
		main2["scrollregion"]=(0,0,wd,ht-50)
		draw_dashb()
		draw_addstock()
		searche.delete(0,tk.END)
		cart.place_forget()

		cal.place_forget()
		cal_con=0
		rr_.place_forget()

		vbar1.pack_forget()

		si_quantity.place_forget()
		psoldat.place_forget()
		si_desc.place_forget()

		searche.place_forget()
		move_dashb()

	elif 119<=e.y<=119+30:
		dashb_state="stock"

		ms_con=0
		draw_dashb()
		main2["scrollregion"]=(0,0,wd,ht-50)
		searche.delete(0,tk.END)

		cart.place_forget()
		cal.place_forget()
		cal_con=0
		vbar1.pack_forget()
		main2.pack_forget()

		vbar1.pack(side=tk.RIGHT,fill=tk.Y)
		main2.pack(side=tk.LEFT)

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
		move_dashb()
	elif 152<=e.y<=152+30:

		dashb_state="reports"
		vbar1.pack_forget()
		main2.pack_forget()
		cart.place_forget()
		cal.place_forget()
		cal_con=0

		vbar1.pack(side=tk.RIGHT,fill=tk.Y)
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

		draw_reports()

		move_dashb()

	elif 185<=e.y<=215:

		dashb_state="settings"
		vbar1.pack_forget()
		main2.pack_forget()
		cart.place_forget()
		cal.place_forget()
		cal_con=0

		rr_.place_forget()

		vbar1.pack(side=tk.RIGHT,fill=tk.Y)
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

		draw_settings()

		move_dashb()

	if dashb_state=="sell_items":

		if 23<=e.x<=113:
			if ht-150<=e.y<=ht-125:

				si_con=0

				cart_array=[]
				draw_dashb()
				draw_sellitems()


		if 136<=e.x<=226:
			if ht-150<=e.y<=ht-125:

				if len(cart_array)>0:
					si_con=2
					draw_sellitems()


def draw_dashb():
	global dashb,dashb_state
	global settw,settb,sellw,sellb,neww,newb,maniw,manib,repw,repb,diw,carti,cv
	global cart_array


	if dashb_state=="sell_items":

		col1,col1_="#ffffff","#000000"
		col2,col2_="#000000","#ffffff"
		col3,col3_="#000000","#ffffff"
		col4,col4_="#000000","#ffffff"
		col5,col5_="#000000","#ffffff"

		v1,v2,v3,v4,v5=1,0,0,0,0




	elif dashb_state=="add_stock":

		col1,col1_="#000000","#ffffff"
		col2,col2_="#ffffff","#000000"
		col3,col3_="#000000","#ffffff"
		col4,col4_="#000000","#ffffff"
		col5,col5_="#000000","#ffffff"

		v1,v2,v3,v4,v5=0,1,0,0,0

	elif dashb_state=="stock":

		col1,col1_="#000000","#ffffff"
		col2,col2_="#000000","#ffffff"
		col3,col3_="#ffffff","#000000"
		col4,col4_="#000000","#ffffff"
		col5,col5_="#000000","#ffffff"

		v1,v2,v3,v4,v5=0,0,1,0,0

	elif dashb_state=="reports":

		col1,col1_="#000000","#ffffff"
		col2,col2_="#000000","#ffffff"
		col3,col3_="#000000","#ffffff"
		col4,col4_="#ffffff","#000000"
		col5,col5_="#000000","#ffffff"

		v1,v2,v3,v4,v5=0,0,0,1,0

	elif dashb_state=="settings":

		col1,col1_="#000000","#ffffff"
		col2,col2_="#000000","#ffffff"
		col3,col3_="#000000","#ffffff"
		col4,col4_="#000000","#ffffff"
		col5,col5_="#ffffff","#000000"

		v1,v2,v3,v4,v5=0,0,0,0,1

	settw=ImageTk.PhotoImage(file="data/settingsw.png")
	settb=ImageTk.PhotoImage(file="data/settingsb.png")
	sellw=ImageTk.PhotoImage(file="data/selliw.png")
	sellb=ImageTk.PhotoImage(file="data/sellib.png")
	neww=ImageTk.PhotoImage(file="data/newiw.png")
	newb=ImageTk.PhotoImage(file="data/newib.png")
	maniw=ImageTk.PhotoImage(file="data/maniw.png")
	manib=ImageTk.PhotoImage(file="data/manib.png")
	repw=ImageTk.PhotoImage(file="data/reportsw.png")
	repb=ImageTk.PhotoImage(file="data/reportsb.png")

	diw=ImageTk.PhotoImage(file="data/dashw.png")

	dashb.create_rectangle(0,0, 250,50,fill="#000000",outline="#000000")

	#dashb.create_image(10,10,image=sett,anchor="nw")

	dashb.create_image(250-10-25,10,image=diw,anchor="nw")

	dashb.create_rectangle(0,50+3,250,80+3,fill=col1,outline=col1)
	dashb.create_text(50+10,65+3,text="Sell Items",fill=col1_,font=("FreeMono",13),anchor="w")

	dashb.create_rectangle(0,86,250,80+30+6,fill=col2,outline=col2)
	dashb.create_text(50+10,65+30+6,text="New Stock",fill=col2_,font=("FreeMono",13),anchor="w")

	dashb.create_rectangle(0,119,250,80+2*30+9,fill=col3,outline=col3)
	dashb.create_text(50+10,65+9+2*30,text="Manage Stock",fill=col3_,font=("FreeMono",13),anchor="w")

	dashb.create_rectangle(0,152,250,80+3*30+12,fill=col4,outline=col4)
	dashb.create_text(50+10,65+12+3*30,text="Reports",fill=col4_,font=("FreeMono",13),anchor="w")

	dashb.create_rectangle(0,185,250,80+4*30+15,fill=col5,outline=col5)
	dashb.create_text(50+10,65+15+4*30,text="Settings",fill=col5_,font=("FreeMono",13),anchor="w")

	dashb.create_rectangle(0,80+4*30+15+3,250,ht,fill="#000000",outline="#000000")



	dashb.create_text(10,ht-20,text="Hepta ©",fill="#ffffff",anchor="w",font=("FreeMono",12))

	if v1==0:

		dashb.create_image(15,50+3+5,image=sellw,anchor="nw")
	elif v1==1:
		dashb.create_image(15,50+3+5,image=sellb,anchor="nw")


	if v2==0:

		dashb.create_image(15,86+5,image=neww,anchor="nw")
	elif v2==1:
		dashb.create_image(15,86+5,image=newb,anchor="nw")


	if v3==0:

		dashb.create_image(15,119+5,image=maniw,anchor="nw")
	elif v3==1:
		dashb.create_image(15,119+5,image=manib,anchor="nw")


	if v4==0:

		dashb.create_image(15,152+5,image=repw,anchor="nw")
	elif v4==1:
		dashb.create_image(15,152+5,image=repb,anchor="nw")


	if v5==0:

		dashb.create_image(15,185+5,image=settw,anchor="nw")
	elif v5==1:
		dashb.create_image(15,185+5,image=settb,anchor="nw")

	if v1==1:
		carti=ImageTk.PhotoImage(file="data/cart.png")

		dashb.create_image(15,ht-200,image=carti,anchor="nw")
		dashb.create_text(50,ht-200+12.5,text="Cart",fill="#ffffff",font=("FreeMono",13),anchor="w")
		cv=dashb.create_text(100,ht-200+12.5,text=str(len(cart_array)),fill="#ffffff",font=("FreeMono",13),anchor="w")


		dashb.create_oval(35-12,ht-200+30+20, 35+25-12,ht-200+30+25+20,fill="#ffffff",outline="#ffffff")
		dashb.create_oval(113-25,ht-200+30+20, 113,ht-200+30+25+20,fill="#ffffff",outline="#ffffff")
		dashb.create_rectangle(35+12.5-12,ht-200+30+20,113-12.5,ht-200+30+25+20,fill="#ffffff",outline="#ffffff")
		dashb.create_text(68,ht-200+30+20+12.5,text="clear",fill="#000000",font=("FreeMono",13),anchor="c")


		dashb.create_oval(136,ht-200+30+20,161,ht-200+30+25+20,fill="#ffffff",outline="#ffffff")
		dashb.create_oval(201,ht-200+30+20, 226,ht-200+30+25+20,fill="#ffffff",outline="#ffffff")
		dashb.create_rectangle(136+12.5,ht-200+30+20, 213.5,ht-200+30+25+20,fill="#ffffff",outline="#ffffff")
		dashb.create_text(181,ht-200+30+20+12.5,text="sell",fill="#000000",font=("FreeMono",13),anchor="c")




cv=()
dvar=0
dvar2=1
dx=0
dashb_state="sell_items"

dashb=tk.Canvas(relief="flat",width=250,height=ht,bg="#222222",highlightthickness=0,border=0)
dashb.bind("<Button-1>",dashb_commands)
dashb.place(in_=root,x=0,y=0)








################


intro=tk.Canvas(width=wd,height=ht,bg="#999999",highlightthickness=0,border=0,relief="flat")
intro.bind("<Button-1>",login)
intro.place(in_=root,x=0,y=0)



x_,y_=(wd/2)-350/2,200
#87.5 262.5
#150 175


intro.create_polygon(x_+10,y_, x_+350-10,y_, x_+350,y_+10, x_+350,y_+220, x_+340,y_+230, x_+10,y_+230,
	x_,y_+220, x_,y_+10,fill="#ffffff",outline="#ffffff")


intro.create_oval(x_,y_,x_+20,y_+20,fill="#ffffff",outline="#ffffff")
intro.create_oval(x_,y_+230-20,x_+20,y_+230,fill="#ffffff",outline="#ffffff")
intro.create_oval(x_+350-20,y_+230-20,x_+350,y_+230,fill="#ffffff",outline="#ffffff")
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


intro.create_text(x_+30+10,y_+40, anchor="w",text="User name",fill="#000000",font=("FreeMono","13"))
intro.create_text(x_+30+10,y_+40+50, anchor="w",text="Password",fill="#000000",font=("FreeMono","13"))


intro.create_rectangle(x_+150-2,y_+30-2, x_+150+168,y_+30+20+5,fill="#ffffff",outline="#000000")
intro.create_rectangle(x_+150-2,y_+30-2+50, x_+150+168,y_+30+20+5+50,fill="#ffffff",outline="#000000")

un=tk.Entry(width=15,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,font=("FreeMono","13"))
un.place(in_=root,x=x_+150,y=y_+30)
un.bind("<Return>",eun)

pw=tk.Entry(width=15,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,font=("FreeMono","13"),show="*")
pw.place(in_=root,x=x_+150,y=y_+30+50)


intro.create_rectangle(x_+100,y_+130+20, x_+250,y_+130+25+20, fill="#333333",outline="#333333")
intro.create_oval(x_+100-(25/2), y_+130+20, x_+100+(25/2), y_+130+20+25,fill="#333333",outline="#333333")

intro.create_oval(x_+250-(25/2), y_+130+20, x_+250+(25/2), y_+130+20+25,fill="#333333",outline="#333333")

intro.create_text(x_+350/2,y_+130+20+(25/2),text="Login",font=("FreeMono","13"),fill="#ffffff")

# sell items

im=Image.open("data/search.png")
im=im.resize((20,20))
im.save("data/search.png"		)

se=()

def draw_sellitems():
	global main1,main2,dvar2,wd, si_con,sellarray,seli,si_quantity,psoldat,total, pos,si_desc,yvar
	global searche,svar,vbar1,cart,cart_array,carti,diw2,dib,logw,logb,se
	main1.delete("all")
	main2.delete("all")


	#cart.delete("all")



	if dvar2==1:
		x_=250+(wd-250)/2



		
	elif dvar2==0:
		x_=wd/2
	if si_con==0:
		col="#ffffff"
		pic_="s"
		col2="#000000"
		col3="#dddddd"
		col4="#dddddd"
		v1=0
	if si_con==1 or si_con==2:

		col="#555555"
		pic_="sd"
		col2="#ffffff"
		col3="#323232"
		col4="#444444"
		v1=1

	diw2=ImageTk.PhotoImage(file="data/dashw.png")
	dib=ImageTk.PhotoImage(file="data/dashb.png")

	logw=ImageTk.PhotoImage(file="data/logoutw.png")
	logb=ImageTk.PhotoImage(file="data/logoutb.png")

	

	if v1==0:
		main1.create_image(10,12.5,image=dib,anchor="nw")
		main1.create_image(wd-20-25,10,image=logb,anchor="nw")
	elif v1==1:
		main1.create_image(10,12.5,image=diw2,anchor="nw")
		main1.create_image(wd-20-25,10,image=logw,anchor="nw")






	searche.focus_set()
	

	move_dashb()


	main1.create_oval(x_-150-15,10, x_-150+15,40,fill=col,outline=col)
	main1.create_oval(x_+150-15,10, x_+150+15,40,fill=col,outline=col)

	main1.create_rectangle(x_-150,10, x_+150,40,fill=col,outline=col)

	#main1.create_rectangle(x_-150,10, x_+150,40,fill=col,outline=col)
	main1.create_arc(x_-150-15,10, x_-150+15,40,fill=col,outline="#000000",style="arc",start=90,extent=180,width=1)
	main1.create_arc(x_+150-15,10, x_+150+15,40,fill=col,outline="#000000",style="arc",start=270,extent=180,width=1)

	main1.create_line(x_-150,10,x_+150,10,width=1,fill="#000000")
	main1.create_line(x_-150-1,40,x_+150,40,width=1,fill="#000000")



	se=ImageTk.PhotoImage(file="data/search.png")

	main1.create_image(x_+150+50-30,15,image=se,anchor="nw")









	searche.place(in_=root,x=x_-148,y=13)

	si_quantity.place_forget()
	psoldat.place_forget()
	si_desc.place_forget()

	psoldat.delete(0,tk.END)
	si_quantity.delete(0,tk.END)

	sellarray=[]



	main1["bg"]=col
	main2["bg"]=col
	n=0

	dbstock=db.connect('data/stock.db')
	cur=dbstock.cursor()

	cur.execute("SELECT * FROM items ORDER BY name ASC")

	rows=cur.fetchall()


	_items=[]
	for row in rows:

		if not row[1].lower().find(svar.lower())==-1:
			n+=1

			_items.append(row)
			

	if dvar2==1:
		xx=250
		e=3
		bx=(wd-250-(304*3)-18)/4
	elif dvar2==0:
		xx=0
		e=4
		bx=(wd-(304*4)-18)/5
		
		
	

	b=int(n/e)
	c=n%e

	if c>0:
		b+=1

	count=0

	
	y=30

	con=0
	for a in range(b):
		x=xx

		for s in range(e):

			sellarray.append([_items[count][0], x+bx,y,x+bx+304,y+300])
			

			if _items[count][6]==1:

				f="Images"
				dir_=os.listdir(f)


				for a in dir_:


					try:
						if int(a.split(".")[0])==_items[count][0]:
							ext=a.split(".")[1]

							xv.xvarray[count]=ImageTk.PhotoImage(file="Images/"+str(_items[count][0])+"_"+pic_+"."+ext)

							main2.create_image(x+bx+2,y+2,anchor="nw",image=xv.xvarray[count])

							cx,cy=x+bx+2+10,y+2+10
							ar=[]
							a_=180
							for a in range(90):
								x1=10*math.sin(math.radians(a_))+cx
								y1=10*math.cos(math.radians(a_))+cy

								ar.append(x1)
								ar.append(y1)

								a_+=1

							main2.create_polygon(x+bx+2,y+2,ar, x+bx+2,y+2,fill=col,outline=col)


							cx,cy=x+bx+2+10,y+200-10+2
							ar=[]
							a_=270
							for a in range(90):
								x1=10*math.sin(math.radians(a_))+cx
								y1=10*math.cos(math.radians(a_))+cy

								ar.append(x1)
								ar.append(y1)

								a_+=1

							main2.create_polygon(x+bx+2,y+202,ar,x+bx+2,y+202,fill=col,outline=col)


							cx,cy=x+bx+304-12,y+2+10
							ar=[]
							a_=90
							for a in range(90):
								x1=10*math.sin(math.radians(a_))+cx
								y1=10*math.cos(math.radians(a_))+cy

								ar.append(x1)
								ar.append(y1)

								a_+=1

							main2.create_polygon(x+bx+302,y+2,ar,x+bx+302,y+2,fill=col,outline=col)



							cx,cy=x+bx+304-12,y+200-10+2
							ar=[]
							a_=0
							for a in range(90):
								x1=10*math.sin(math.radians(a_))+cx
								y1=10*math.cos(math.radians(a_))+cy

								ar.append(x1)
								ar.append(y1)

								a_+=1

							main2.create_polygon(x+bx+302,y+202,ar,x+bx+302,y+202,fill=col,outline=col)


					except:
						pass


			coll="#000000"
			w=1

			for c in cart_array:


				if int(_items[count][0])==int(c[0]):

					if si_con==0:
						coll="#0288D1"
						w=1

						main2.create_oval(x+bx+304-5-27,y+300-5-27,x+bx+304-5-27+10,y+300-5-27+10,fill=coll,outline=coll)
						main2.create_oval(x+bx+304-5-27,y+300-5-10,x+bx+304-5-27+10,y+300-5,fill=coll,outline=coll)

						main2.create_oval(x+bx+304-5-10,y+300-5-27,x+bx+304-5,y+300-5-27+10,fill=coll,outline=coll)
						main2.create_oval(x+bx+304-5-10,y+300-5-10,x+bx+304-5,y+300-5,fill=coll,outline=coll)

						main2.create_polygon(x+bx+304-5-27+5,y+300-5-27, x+bx+304-5-5,y+300-5-27,
							x+bx+304-5,y+300-5-27+5, x+bx+304-5,y+300-5-5, x+bx+304-5-5,y+300-5,
							x+bx+304-5-27+5,y+300-5, x+bx+304-5-27,y+300-5-5, x+bx+304-5-27,y+300-5-27+5,fill=coll,outline=coll )

						main2.create_line(x+bx+304-5-27+3+1,y+300-5-27+13.5, x+bx+304-5-27+3+7+1,y+300-5-27+13.5+7
							,x+bx+304-5-4+1,y+300-5-27+8 ,fill="white",width=2 )

						#main2.create_rectangle(x+bx+304-5-27,y+300-5-27,x+bx+304-5,y+300-5,fill="blue")


			main2.create_arc(x+bx,y, x+bx+20,y+20, outline=coll, style="arc", start=90, extent=90,width=w)
			main2.create_arc(x+bx,y+300-20, x+bx+20,y+300, outline=coll, style="arc", start=180, extent=90,width=w)

			main2.create_arc(x+bx+304-20,y, x+bx+304,y+20, outline=coll, style="arc", start=0, extent=90,width=w)
			main2.create_arc(x+bx+304-20,y+300-20, x+bx+304,y+300, outline=coll, style="arc", start=270, extent=90,width=w)

			main2.create_line(x+bx+10,y, x+bx+304-10,y,fill=coll,width=w)
			main2.create_line(x+bx+10-1,y+300, x+bx+304-10,y+300,fill=coll,width=w)

			main2.create_line(x+bx,y+10-1, x+bx,y+300-10,fill=coll,width=w)
			main2.create_line(x+bx+304,y+10, x+bx+304,y+300-10,fill=coll,width=w)
			#x+bx,y, x+bx+304,y+300
					


			
			name=_items[count][1]
			price=_items[count][3]
			items_=_items[count][4]

			main2.create_text(x+bx+10,y+200+20,anchor="w",text=str(name),font=("FreeMono","13"))
			main2.create_text(x+bx+10,y+200+20+30,anchor="w",text=str(price)+" Ksh",font=("FreeMono","13"))
			main2.create_text(x+bx+10,y+200+20+60,anchor="w",text=str(items_)+" items left",font=("FreeMono","13"))

			x+=304+bx
			count+=1

			if count==n:
				con=1
				break
		y+=300+40
		if con==1:
			break


	yvar=y
	main2["scrollregion"]=(0,0,wd,yvar+50)

	if si_con==2:

		vbar1.pack_forget()

		searche.place_forget()
		yy=main2.canvasy(0)

		if dvar2==1:
			x1,y1=250+(wd-250-800)/2,50+yy
		elif dvar2==0:
			x1,y1=(wd-800)/2,50+yy


		main2.create_oval(x1,y1,x1+20,y1+20,fill="#ffffff",outline="#ffffff")
		main2.create_oval(x1,y1+480,x1+20,y1+500,fill="#ffffff",outline="#ffffff")

		main2.create_oval(x1+780,y1,x1+800,y1+20,fill="#ffffff",outline="#ffffff")
		main2.create_oval(x1+780,y1+480,x1+800,y1+500,fill="#ffffff",outline="#ffffff")

		main2.create_polygon(x1+10,y1, x1+790,y1, x1+800,y1+10, x1+800,y1+490,
			x1+790,y1+500, x1+10,y1+500,x1,y1+490, x1,y1+10,fill="#ffffff",outline="#ffffff")

		main2.create_oval(x1+785-5-15+40,y1,x1+785-5+15+40,y1+30,fill="#ffffff",outline="#ffffff")

		main2.create_line(x1+785-5-5+40,y1+15-5, x1+785+5-5+40,y1+15+5,fill="#000000",width=2)
		main2.create_line(x1+785-5-5+40,y1+15+5, x1+785+5-5+40,y1+15-5,fill="#000000",width=2)


	elif si_con==1:

		vbar1.pack_forget()

		searche.place_forget()
		yy=main2.canvasy(0)

		if dvar2==1:
			x1,y1=250+(wd-250-800)/2,50+yy
		elif dvar2==0:
			x1,y1=(wd-800)/2,50+yy

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

		main2.create_oval(x1+785-5-15+40,y1,x1+785-5+15+40,y1+30,fill="#ffffff",outline="#ffffff")

		main2.create_line(x1+785-5-5+40,y1+15-5, x1+785+5-5+40,y1+15+5,fill="#000000",width=2)
		main2.create_line(x1+785-5-5+40,y1+15+5, x1+785+5-5+40,y1+15-5,fill="#000000",width=2)

		main2.create_line(x1+500,y1+20,x1+500,y1+480,fill="#000000",width=1)

		main2.create_text(x1+250,y1+20,text=name2.upper(),fill="#000000",font=("FreeMono",15,))

		main2.create_text(x1+500+20,y1+70, fill="#000000",font=("FreeMono",13),text="Price",anchor="w")
		main2.create_text(x1+500+20+90,y1+70, fill="red",font=("FreeMono",13),text=price,anchor="w")
		main2.create_text(x1+500+20,y1+70+40, fill="#000000",font=("FreeMono",13),text="Items left"
			,anchor="w")

		main2.create_text(x1+500+20+90,y1+70+40, fill="red",font=("FreeMono",13),text=quant,anchor="w")

		main2.create_line(x1+500+30,y1+140, x1+800-30,y1+140,fill="#000000" )

		main2.create_text(x1+500+20,y1+170,fill="#000000",text="Sold at",font=("FreeMono",13),anchor="w")
		main2.create_text(x1+500+20,y1+170+40,fill="#000000",text="Quantity",font=("FreeMono",13),anchor="w")


		main2.create_rectangle(x1+500+120-2,y1+170-10-2, x1+500+120+200-90+3,y1+170-10+100-50-20-5,fill="#ffffff",outline="#000000")
		main2.create_rectangle(x1+500+120-2,y1+170-10-2+40, x1+500+120+200-90+3,y1+170-10+100-50-20-5+40,fill="#ffffff",outline="#000000")


		psoldat.delete(0,tk.END)
		si_quantity.delete(0,tk.END)

		psoldat.insert(0,price)
		si_quantity.insert(0,str(1))


		psoldat.focus_set()


		psoldat.place(in_=root,x=x1+500+120,y=100+170-10)
		si_quantity.place(in_=root,x=x1+500+120,y=100+170-10+40)

		si_desc.place(in_=root,x=x1+55,y=520)

		

		if len(desc)>35:

			si_desc["text"]=desc[:35]+"..."

		else:
			si_desc["text"]=desc





		pos=[x1,y1]

		#main2.create_rectangle(x1+500+20,y1+500-50-80,x1+500+300-20,y1+500-50-70+20,fill="#ffffff",outline="#000000",width=2)


		main2.create_text(x1+500+20,y1+500-50-70+5,text="Total",fill="red",font=
			("FreeMono",13),anchor="w")

		total=main2.create_text(x1+500+300-20,y1+500-50-70+5,text="0",fill="#000000",font=
			("FreeMono",13),anchor="e")

		main2.create_rectangle(x1+500+40+30,y1+500-50-30, x1+800-40-30,y1+500-50,fill="#333333",outline="#333333")
		main2.create_oval(x1+500+40+30-15,y1+500-50-30, x1+500+40+30+15,y1+500-50,fill="#333333",outline="#333333")
		main2.create_oval(x1+800-40-30-15,y1+500-50-30, x1+800-40-30+15,y1+500-50,fill="#333333",outline="#333333" )
		main2.create_text(x1+500+150,y1+500-50-15,fill="#ffffff",text="Add to cart",font=("FreeMono",13))



		if pic==1:

			f="Images"
			dir_=os.listdir(f)

			for a in dir_:
				if a.split(".")[0]==str(id_):
					ext=a.split(".")[1]

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
			total=main2.create_text(x+500+300-30,y+500-50-70+5,text=str(total_),fill="#000000",font=
			("FreeMono",13),anchor="e")
		except:
			x,y=pos[0],pos[1]
			main2.delete(total)
			total=main2.create_text(x+500+300-30,y+500-50-70+5,text="0",fill="#000000",font=
			("FreeMono",13),anchor="e")

	root.after(1,gentotal)
		
		



si_con=0
sellarray=[]
seli=0

se_image=""
total=()
total_=0
pos=[]



psoldat=tk.Entry(width=10,bg="#ffffff",relief="flat", highlightthickness=0,border=0,font=
	("FreeMono",13))
psoldat.bind("<KeyPress>",gentotal)


si_quantity=tk.Entry(width=10,bg="#ffffff",relief="flat", highlightthickness=0,border=0,font=
	("FreeMono",13))
si_quantity.bind("<KeyPress>",gentotal)

si_desc=tk.Label(width=35,height=3,bg="#ffffff",relief="flat", highlightthickness=0,border=0,font=
	("FreeMono",13),justify="center")
# Add stock

def draw_addstock():
	global main1,main2,as_n,as_bp,as_sp,as_q,as_de,dvar2,ascon2,as_im
	global wd,ht,si_quantity,psoldat,ms_con,diw2,logw

	as_n.delete(0,tk.END)
	as_bp.delete(0,tk.END)
	as_sp.delete(0,tk.END)
	as_q.delete(0,tk.END)
	as_de.delete(0.0,tk.END)

	as_n.focus_set()

	main1.delete("all")
	main2.delete("all")

	main1["bg"]="#555555"
	main2["bg"]="#555555"

	diw2=ImageTk.PhotoImage(file="data/dashw.png")
	logw=ImageTk.PhotoImage(file="data/logoutw.png")
	main1.create_image(10,12.5,image=diw2,anchor="nw")
	main1.create_image(wd-20-25,10,image=logw,anchor="nw")


	if dvar2==1:
		x_,y_=250+(wd-250-800)/2,30
	elif dvar2==0:
		x_,y_=(wd-800)/2,30

	main2.create_oval(x_,y_, x_+20,y_+20,outline="#ffffff",fill="#ffffff")
	main2.create_oval(x_-20+800,y_, x_+800,y_+20,outline="#ffffff",fill="#ffffff")
	main2.create_oval(x_,y_+500-20, x_+20,y_+500,outline="#ffffff",fill="#ffffff")
	main2.create_oval(x_-20+800,y_+500-20, x_+800,y_+500,outline="#ffffff",fill="#ffffff")

	main2.create_polygon(x_+10,y_,x_+790,y_, x_+800,y_+10,x_+800,y_+490, x_+790,y_+500,
		x_+10,y_+500, x_,y_+490,x_,y_+10,fill="#ffffff",outline="#ffffff")


	yy=50
	main2.create_text(x_+30,y_+40,text="Name",font=("FreeMono",13),fill="#000000",anchor="w")
	main2.create_text(x_+30,y_+40+yy,text="Buying Price",font=("FreeMono",13),fill="#000000",anchor="w")
	main2.create_text(x_+30,y_+40+yy*2,text="Selling Price",font=("FreeMono",13),fill="#000000",anchor="w")	
	main2.create_text(x_+30,y_+40+yy*3,text="Quantity",font=("FreeMono",13),fill="#000000",anchor="w")

	main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2-yy+y_, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_,fill="#ffffff",outline="#000000")
	main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2+y_, x_+170+170-2,40+yy+50-13-yy+28-3+y_,fill="#ffffff",outline="#000000")
	main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2+yy+y_, x_+170+170-2,40+yy+50-13-yy+28+yy-3+y_,fill="#ffffff",outline="#000000")	
	main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2+yy+yy+y_, x_+170+170-2,40+yy+50-13-yy+28+yy+yy-3+y_,fill="#ffffff",outline="#000000")

	as_n.place(in_=root,x=x_+170,y=40+yy+50-13-yy+y_)
	as_bp.place(in_=root,x=x_+170,y=40+yy+50-13+y_)
	as_sp.place(in_=root,x=x_+170,y=40+yy+50-13+yy+y_)
	as_q.place(in_=root,x=x_+170,y=40+yy+50-13+yy+yy+y_)



	#main2.create_rectangle(x_+30,y_+300, x_+30+320,y_+300+100,fill="red")

	main2.create_text(x_+50+5,y_+300+25+2,text="Description",anchor="sw",font=("FreeMono",13),fill="#000000")
	main2.create_line(x_+30+20,y_+300-5+25, x_+30,y_+300-5+25, x_+30, y_+300+95+25, x_+300+40, y_+300+95+25,
	x_+300+40, y_+300-5+25 ,x_+300+40-190+5-15, y_+300-5+25,  fill="#000000",width=1)

	as_de.place(in_=root,x=x_+30+5,y=y_+300+50+25)

	main2.create_rectangle(x_+400-20-1,y_+20-1, x_+400+400-20,y_+20+400,fill="#bbbbbb",outline="#bbbbbb")



	main2.create_text(x_-20+400+200,y_+100+20,text="Add Image",fill="#ffffff", font=("FreeMono",30))

	main2.create_oval(x_-20+400+200-40,y_+20+200-40, x_-20+400+200+40,y_+20+200+40, fill="#bbbbbb", outline="#ffffff",width=1 )

	main2.create_line(x_-20+400+200,y_+20+200-20, x_-20+400+200,y_+20+200+20,fill="#ffffff",width=1 )
	main2.create_line(x_-20+400-20+200,y_+20+200, x_-20+400+200+20,y_+20+200,fill="#ffffff",width=1 )

	main2.create_line(x_+400+400-20-15-5+5,y_+20+400+15-5, x_+400+400-20-15+5+5,y_+20+400+15+5,fill="#000000",width=2)
	main2.create_line(x_+400+400-20-15-5+5,y_+20+400+15+5, x_+400+400-20-15+5+5,y_+20+400+15-5,fill="#000000",width=2)

	if ascon2==1:
		main2.create_text(x_+400, y_+500-60,text="Fill all fields.",fill="red",font=("FreeMono",13))

	if not as_image=="":
		as_im=main2.create_image(x_+400-20+ax,y_+20+ay,image=as_image,anchor="nw")

	main2.create_rectangle(x_+400-60, y_+500-60+20, x_+400+60,y_+500-30+20,fill="#333333",outline="#333333")
	main2.create_oval(x_+400-60-15, y_+500-60+20, x_+400-60+15, y_+500-60+20+30,fill="#333333",outline="#333333")
	main2.create_oval(x_+400+60-15,y_+500-60+20, x_+400+60+15,y_+500-60+20+30,fill="#333333",outline="#333333")


	main2.create_text(x_+400,y_+500-30+20-15,text="Add Stock", fill="#ffffff",font=("FreeMono",13))






ascon=0
ascon2=0
as_n=tk.Entry(bg="#ffffff",width=15,font=("FreeMono",13),relief="flat",highlightthickness=0,border=0)
as_bp=tk.Entry(bg="#ffffff",width=15,font=("FreeMono",13),relief="flat",highlightthickness=0,border=0)
as_sp=tk.Entry(bg="#ffffff",width=15,font=("FreeMono",13),relief="flat",highlightthickness=0,border=0)
as_q=tk.Entry(bg="#ffffff",width=15,font=("FreeMono",13),relief="flat",highlightthickness=0,border=0)
as_de=tk.Text(bg="#ffffff",width=27,height=4,font=("FreeMono",13),relief="flat",highlightthickness=0,border=0)

# stock

def draw_stock():
	global main1,main2,dvar2,wd, si_con,msarray,ms_con,seli
	global as_n,as_bp,as_sp,as_q,as_de,msimage,msi,yvar,vbar1,svar,searche,diw2,dib,logw,logb,se
	main1.delete("all")
	main2.delete("all")
	if ms_con==0:
		col="#ffffff"
		pic_="s"
		col2="#000000"
		col4="#dddddd"
		v1=0
	elif ms_con==1:

		col="#555555"
		pic_="sd"
		col2="#ffffff"
		col4="#444444"
		v1=1

	as_n.delete(0,tk.END)
	as_bp.delete(0,tk.END)
	as_sp.delete(0,tk.END)
	as_q.delete(0,tk.END)
	as_de.delete(0.0,tk.END)


	if dvar2==1:
		x_=250+(wd-250)/2
	elif dvar2==0:
		x_=wd/2

	searche.focus_set()

	main1.create_oval(x_-150-15,10, x_-150+15,40,fill=col,outline=col)
	main1.create_oval(x_+150-15,10, x_+150+15,40,fill=col,outline=col)

	main1.create_rectangle(x_-150,10, x_+150,40,fill=col,outline=col)
		

	main1.create_arc(x_-150-15,10, x_-150+15,40,fill=col,outline="#000000",style="arc",start=90,extent=180,width=1)
	main1.create_arc(x_+150-15,10, x_+150+15,40,fill=col,outline="#000000",style="arc",start=270,extent=180,width=1)

	main1.create_line(x_-150,10,x_+150,10,width=1,fill="#000000")
	main1.create_line(x_-150-1,40,x_+150,40,width=1,fill="#000000")



	se=ImageTk.PhotoImage(file="data/search.png")

	main1.create_image(x_+150+50-30,15,image=se,anchor="nw")

	diw2=ImageTk.PhotoImage(file="data/dashw.png")
	dib=ImageTk.PhotoImage(file="data/dashb.png")

	logw=ImageTk.PhotoImage(file="data/logoutw.png")
	logb=ImageTk.PhotoImage(file="data/logoutb.png")

	if v1==0:
		main1.create_image(10,12.5,image=dib,anchor="nw")
		main1.create_image(wd-20-25,10,image=logb,anchor="nw")
	elif v1==1:
		main1.create_image(10,12.5,image=diw2,anchor="nw")
		main1.create_image(wd-20-25,10,image=logw,anchor="nw")



	searche.place(in_=root,x=x_-148,y=13)


	msarray=[]



	main1["bg"]=col
	main2["bg"]=col
	n=0

	dbstock=db.connect('data/stock.db')
	cur=dbstock.cursor()

	cur.execute("SELECT * FROM items ORDER BY name ASC")

	rows=cur.fetchall()


	_items=[]
	for row in rows:

		if not row[1].lower().find(svar.lower())==-1:
			n+=1

			_items.append(row)
			

	if dvar2==1:
		xx=250
		e=3
		bx=(wd-250-(304*3)-18)/4
	elif dvar2==0:
		xx=0
		e=4
		bx=(wd-(304*4)-18)/5
		
		
	

	b=int(n/e)
	c=n%e

	if c>0:
		b+=1

	count=0

	
	y=30

	con=0
	for a in range(b):
		x=xx

		for s in range(e):

			msarray.append([_items[count][0], x+bx,y,x+bx+304,y+300])
			

			if _items[count][6]==1:

				f="Images"
				dir_=os.listdir(f)


				for a in dir_:


					try:
						if int(a.split(".")[0])==_items[count][0]:
							ext=a.split(".")[1]

							xv.xvarray[count]=ImageTk.PhotoImage(file="Images/"+str(_items[count][0])+"_"+pic_+"."+ext)

							main2.create_image(x+bx+2,y+2,anchor="nw",image=xv.xvarray[count])

							cx,cy=x+bx+2+10,y+2+10
							ar=[]
							a_=180
							for a in range(90):
								x1=10*math.sin(math.radians(a_))+cx
								y1=10*math.cos(math.radians(a_))+cy

								ar.append(x1)
								ar.append(y1)

								a_+=1

							main2.create_polygon(x+bx+2,y+2,ar, x+bx+2,y+2,fill=col,outline=col)


							cx,cy=x+bx+2+10,y+200-10+2
							ar=[]
							a_=270
							for a in range(90):
								x1=10*math.sin(math.radians(a_))+cx
								y1=10*math.cos(math.radians(a_))+cy

								ar.append(x1)
								ar.append(y1)

								a_+=1

							main2.create_polygon(x+bx+2,y+202,ar,x+bx+2,y+202,fill=col,outline=col)


							cx,cy=x+bx+304-12,y+2+10
							ar=[]
							a_=90
							for a in range(90):
								x1=10*math.sin(math.radians(a_))+cx
								y1=10*math.cos(math.radians(a_))+cy

								ar.append(x1)
								ar.append(y1)

								a_+=1

							main2.create_polygon(x+bx+302,y+2,ar,x+bx+302,y+2,fill=col,outline=col)



							cx,cy=x+bx+304-12,y+200-10+2
							ar=[]
							a_=0
							for a in range(90):
								x1=10*math.sin(math.radians(a_))+cx
								y1=10*math.cos(math.radians(a_))+cy

								ar.append(x1)
								ar.append(y1)

								a_+=1

							main2.create_polygon(x+bx+302,y+202,ar,x+bx+302,y+202,fill=col,outline=col)


					except:
						pass


			main2.create_arc(x+bx,y, x+bx+20,y+20, outline="#000000", style="arc", start=90, extent=90,width=1)
			main2.create_arc(x+bx,y+300-20, x+bx+20,y+300, outline="#000000", style="arc", start=180, extent=90,width=1)

			main2.create_arc(x+bx+304-20,y, x+bx+304,y+20, outline="#000000", style="arc", start=0, extent=90,width=1)
			main2.create_arc(x+bx+304-20,y+300-20, x+bx+304,y+300, outline="#000000", style="arc", start=270, extent=90,width=1)

			main2.create_line(x+bx+10,y, x+bx+304-10,y,fill="#000000",width=1)
			main2.create_line(x+bx+10-1,y+300, x+bx+304-10,y+300,fill="#000000",width=1)

			main2.create_line(x+bx,y+10-1, x+bx,y+300-10,fill="#000000",width=1)
			main2.create_line(x+bx+304,y+10, x+bx+304,y+300-10,fill="#000000",width=1)
			#x+bx,y, x+bx+304,y+300
					


			
			name=_items[count][1]
			price=_items[count][3]
			items_=_items[count][4]

			main2.create_text(x+bx+10,y+200+20,anchor="w",text=str(name),font=("FreeMono","13"))
			main2.create_text(x+bx+10,y+200+20+30,anchor="w",text=str(price)+" Ksh",font=("FreeMono","13"))
			main2.create_text(x+bx+10,y+200+20+60,anchor="w",text=str(items_)+" items left",font=("FreeMono","13"))

			x+=304+bx
			count+=1

			if count==n:
				con=1
				break
		y+=300+40
		if con==1:
			break


	yvar=y
	main2["scrollregion"]=(0,0,wd,y)


	if ms_con==1:
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

		if dvar2==1:
			x_,y_=250+(wd-250-800)/2,50+main2.canvasy(0)
		elif dvar2==0:
			x_,y_=(wd-800)/2,50+main2.canvasy(0)

		main2.create_oval(x_,y_, x_+20,y_+20,fill="#ffffff",outline="#ffffff")
		main2.create_oval(x_-20+800,y_, x_+800,y_+20,fill="#ffffff",outline="#ffffff")
		main2.create_oval(x_,y_+500-20, x_+20,y_+500,fill="#ffffff",outline="#ffffff")
		main2.create_oval(x_-20+800,y_+500-20, x_+800,y_+500,fill="#ffffff",outline="#ffffff")

		main2.create_polygon(x_+10,y_, x_+800-10,y_, x_+800,y_+10, x_+800,y_+500-10,
			x_+800-10,y_+500, x_+10,y_+500, x_,y_+500-10, x_,y_+10,fill="#ffffff",outline="#ffffff")

		main2.create_oval(x_+785-5-15+40,y_,x_+785-5+15+40,y_+30,fill="#ffffff",outline="#ffffff")
		main2.create_line(x_+785-5-5+40,y_+15-5, x_+785+5-5+40,y_+15+5,fill="#000000",width=2)
		main2.create_line(x_+785-5-5+40,y_+15+5, x_+785+5-5+40,y_+15-5,fill="#000000",width=2)


		yy=50
		main2.create_text(x_+30,y_+40+10,text="Name",font=("FreeMono",13),fill="#000000",anchor="w")
		main2.create_text(x_+30,y_+40+yy+10,text="Buying Price",font=("FreeMono",13),fill="#000000",anchor="w")
		main2.create_text(x_+30,y_+40+yy*2+10,text="Selling Price",font=("FreeMono",13),fill="#000000",anchor="w")	
		main2.create_text(x_+30,y_+40+yy*3+10,text="Quantity",font=("FreeMono",13),fill="#000000",anchor="w")

		main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2-yy+y_+10, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_+10,fill="#ffffff",outline="#000000")
		main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2+y_+10, x_+170+170-2,40+yy+50-13-yy+28-3+y_+10,fill="#ffffff",outline="#000000")
		main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2+yy+y_+10, x_+170+170-2,40+yy+50-13-yy+28+yy-3+y_+10,fill="#ffffff",outline="#000000")	
		main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2+yy+yy+y_+10, x_+170+170-2,40+yy+50-13-yy+28+yy+yy-3+y_+10,fill="#ffffff",outline="#000000")

		as_n.place(in_=root,x=x_+170,y=40+yy+50-13-yy+y_+10-main2.canvasy(0))
		as_bp.place(in_=root,x=x_+170,y=40+yy+50-13+y_+10-main2.canvasy(0))
		as_sp.place(in_=root,x=x_+170,y=40+yy+50-13+yy+y_+10-main2.canvasy(0))
		as_q.place(in_=root,x=x_+170,y=40+yy+50-13+yy+yy+y_+10-main2.canvasy(0))


		main2.create_text(x_+50+5,y_+300+25+10+2,text="Description",anchor="sw",font=("FreeMono",13),fill="#000000")
		main2.create_line(x_+30+20,y_+300-5+25+10, x_+30,y_+300-5+25+10, x_+30, y_+300+95+25+10, x_+300+40, y_+300+95+25+10,
		x_+300+40, y_+300-5+25+10 ,x_+300+40-190+5-15, y_+300-5+25+10,  fill="#000000",width=1)

		as_de.place(in_=root,x=x_+30+5,y=y_+300+50+25+10-main2.canvasy(0))

		main2.create_rectangle(x_+400-20-1,y_+20+10-1, x_+400+400-20,y_+20+400+10,fill="#bbbbbb",outline="#bbbbbb")

		main2.create_text(x_-20+400+200,y_+110+20,text="Add Image",fill="#ffffff", font=("FreeMono",30))
		main2.create_oval(x_-20+400+200-40,y_+20+200-40, x_-20+400+200+40,y_+20+200+40, fill="#bbbbbb", outline="#ffffff",width=1 )

		main2.create_line(x_-20+400+200,y_+20+200-20, x_-20+400+200,y_+20+200+20,fill="#ffffff",width=1 )
		main2.create_line(x_-20+400-20+200,y_+20+200, x_-20+400+200+20,y_+20+200,fill="#ffffff",width=1 )

		main2.create_line(x_+400+400-20-15-5+5,y_+20+400+15-5+10, x_+400+400-20-15+5+5,y_+20+400+15+5+10,fill="#000000",width=2)
		main2.create_line(x_+400+400-20-15-5+5,y_+20+400+15+5+10, x_+400+400-20-15+5+5,y_+20+400+15-5+10,fill="#000000",width=2)

		a=80
		main2.create_rectangle(x_+400-50-a,y_+500-50+10,x_+400+50-a,y_+500-20+10,fill="#333333",outline="#333333")
		main2.create_oval(x_+400-50-15-a,y_+500-50+10, x_+400-50+15-a,y_+500-20+10,fill="#333333",outline="#333333")
		main2.create_oval(x_+400+50-15-a,y_+500-50+10, x_+400+50+15-a,y_+500-20+10,fill="#333333",outline="#333333")
		main2.create_text(x_+400-a,y_+500-20-15+10,fill="#ffffff",text="Save",font=("FreeMono",13))

		main2.create_rectangle(x_+400-50+a,y_+500-50+10,x_+400+50+a,y_+500-20+10,fill="#333333",outline="#333333")
		main2.create_oval(x_+400-50-15+a,y_+500-50+10, x_+400-50+15+a,y_+500-20+10,fill="#333333",outline="#333333")
		main2.create_oval(x_+400+50-15+a,y_+500-50+10, x_+400+50+15+a,y_+500-20+10,fill="#333333",outline="#333333")
		main2.create_text(x_+400+a,y_+500-20-15+10,fill="#ffffff",text="Delete",font=("FreeMono",13))

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

					msi=main2.create_image(x_+400-20+ax,y_+20+ay+10,image=msimage,anchor="nw")
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
	global main1,main2,rr_,dvar2,yvar,svar,dashb_state,daten,date__,cali,dib,logb,se


	main1.delete("all")
	main2.delete("all")

	main1["bg"]="#ffffff"
	main2["bg"]="#ffffff"

	tot1=0

	tot2=0


	if dvar2==1:
		x_=250+(wd-250)/2

	elif dvar2==0:
		x_=wd/2

	

	searche.focus_set()

	main1.create_oval(x_-150-15,10, x_-150+15,40,fill="#ffffff",outline="#ffffff")
	main1.create_oval(x_+150-15,10, x_+150+15,40,fill="#ffffff",outline="#ffffff")

	main1.create_rectangle(x_-150,10, x_+150,40,fill="#ffffff",outline="#ffffff")

	main1.create_arc(x_-150-15,10, x_-150+15,40,outline="#000000",style="arc",start=90,extent=180,width=1)
	main1.create_arc(x_+150-15,10, x_+150+15,40,outline="#000000",style="arc",start=270,extent=180,width=1)

	main1.create_line(x_-150,10, x_+150,10,fill="#000000",width=1)
	main1.create_line(x_-150-1,40, x_+150,40,fill="#000000",width=1 )


	se=ImageTk.PhotoImage(file="data/search.png")

	main1.create_image(x_+150+50-30,15,image=se,anchor="nw")



	dib=ImageTk.PhotoImage(file="data/dashb.png")

	logb=ImageTk.PhotoImage(file="data/logoutb.png")

	main1.create_image(10,12.5,image=dib,anchor="nw")
	main1.create_image(wd-20-25,10,image=logb,anchor="nw")



	searche.place(in_=root,x=x_-148,y=13)



	if dvar2==1:
		x_=250+(wd-250-1000)/2
	elif dvar2==0:
		x_=(wd-1000)/2



	cali=ImageTk.PhotoImage(file="data/calendar.png")


	main1.create_image(x_,10,image=cali,anchor="nw")





	date__=main1.create_text(x_+40,25,text=daten,font=("FreeMono",13),anchor="w")

	rr_.place(in_=root,x=x_,y=50)


	dbsales=db.connect("data/sales.db")
	cur=dbsales.cursor()


	cur.execute("SELECT * FROM sales_ ORDER BY sales_id DESC")

	rows=cur.fetchall()

	yv=30

	st=0
	for row in rows:

		if not str(row[1].lower()).find(svar.lower())==-1:

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


			date=str(dd)+"-"+str(mm)+"-"+str(yy)

			var=[str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(date),str(row[6]),str(row[7]) ]


			tot1+=int(row[6])
			tot2+=int(row[7])
			v=1000/7
			xv=x_+v

			if st==1:
				main2.create_rectangle(x_,yv,x_+1000,yv+25,fill="#bbbbbb",outline="#bbbbbb")
				st=0
			elif st==0:
				st=1

			for a in range(7):
				main2.create_text(xv-v/2,yv+12.5,text=var[a],font=("FreeMono",13),fill="#000000")


				xv+=v

			yv+=25

	main2.create_line(x_,yv,x_+1000,yv,fill="#000000")

	v=1000/7
	xv=x_+v
	for a in range(6):
		main2.create_line(xv+1,30,xv+1,yv,fill="#000000")

		xv+=v

	x=x_+v/2+v*5
	main2.create_text(x,yv+12.5,font=("FreeMono",13),fill="#000000",text=str(tot1))

	x=x_+v/2+v*6
	main2.create_text(x,yv+12.5,font=("FreeMono",13),fill="#000000",text=str(tot2))


	yvar=yv+100
	main2["scrollregion"]=(0,0,wd,yvar)

	

	#print(yvar)



def draw_settings():
	global main1,main2,dvar2
	global wd,ht,diw2,logw


	main1.delete("all")
	main2.delete("all")

	main1["bg"]="#555555"
	main2["bg"]="#555555"

	diw2=ImageTk.PhotoImage(file="data/dashw.png")
	logw=ImageTk.PhotoImage(file="data/logoutw.png")
	main1.create_image(10,12.5,image=diw2,anchor="nw")
	main1.create_image(wd-20-25,10,image=logw,anchor="nw")


	if dvar2==1:
		x_,y_=250+(wd-250-800)/2,30
	elif dvar2==0:
		x_,y_=(wd-800)/2,30

	main2.create_oval(x_,y_, x_+20,y_+20,outline="#ffffff",fill="#ffffff")
	main2.create_oval(x_-20+800,y_, x_+800,y_+20,outline="#ffffff",fill="#ffffff")
	main2.create_oval(x_,y_+500-20, x_+20,y_+500,outline="#ffffff",fill="#ffffff")
	main2.create_oval(x_-20+800,y_+500-20, x_+800,y_+500,outline="#ffffff",fill="#ffffff")

	main2.create_polygon(x_+10,y_,x_+790,y_, x_+800,y_+10,x_+800,y_+490, x_+790,y_+500,
		x_+10,y_+500, x_,y_+490,x_,y_+10,fill="#ffffff",outline="#ffffff")




def search():
	global svar,dashb_state,searche,si_con,ms_con,lvar

	svar=searche.get()

	if not lvar==0:

		if dashb_state=="sell_items" and si_con==0:
			draw_sellitems()

		if dashb_state=="stock" and ms_con==0:
			draw_stock()

		if dashb_state=="reports":
			draw_reports()

		

	root.after(1000,search)
 
svar=" "

rr_=tk.Canvas(height=30,width=1000,bg="#111111",relief="flat", highlightthickness=0,border=0)


vv=["Item Name","Selling Price","Price Sold","Quantity","Date","Total","Profit"]
v=1000/7
x=v
for a in range(7):

	rr_.create_line(x,0,x,30,fill="#ffffff")
	rr_.create_text(x-v/2,15,text=vv[a],font=("FreeMono",13),fill="#ffffff")

	x+=v

searche=tk.Entry(width=27,relief="flat",highlightthickness=0,border=0,bg="#ffffff",font=("FreeMono",13)
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

	global cal_year,cal_month,cal_day,main1,date__,daten,days_array,dvar2

	con=0

	if 15<=e.x<=25:
		if 10<=e.y<=30:
			cal_year-=1
			cal_day="*"
			con=1


	if 73<=e.x<=83:
		if 10<=e.y<=30:
			cal_year+=1
			cal_day="*"
			con=1

	if 95<=e.x<=105:
		if 30<=e.y<=50:

			if not cal_month==1:
				cal_month-=1
				cal_day="*"
			con=1


	if 195<=e.x<=205:
		if 30<=e.y<=50:
			if not cal_month==12:
				cal_month+=1
				cal_day="*"
			con=1

	for d in days_array:

		if d[1]<=e.x<=d[3]:
			if d[2]<=e.y<=d[4]:
				cal_day=int(d[0])
				con=1
	if con==0:
		cal_day="*"

	draw_cal()
	daten=str(cal_day)+"-"+str(cal_month)+"-"+str(cal_year)

	main1.delete(date__)

	if dvar2==1:
		x_=250+(wd-250-1000)/2
	elif dvar2==0:
		x_=(wd-1000)/2

	date__=main1.create_text(x_+40,25,text=daten,font=("FreeMono",13),anchor="w")
	draw_reports()

def draw_cal():
	global cal,cal_day,cal_month,cal_year,days_array

	days_array=[]


	cal.delete("all")

	cal.create_text(50,20,anchor="c",text=str(cal_year),font=("FreeMono",13),fill="#ffffff")

	cal.create_text(20,20,text="<",font=("FreeMono",13),anchor="c",fill="#ffffff")
	cal.create_text(78,20,text=">",font=("FreeMono",13),anchor="c",fill="#ffffff")

	cal.create_text(150,40,text=month_str(cal_month)[0],font=("FreeMono",13),anchor="c",fill="#ffffff")

	cal.create_text(100,40,text="<",font=("FreeMono",13),anchor="c",fill="#ffffff")
	cal.create_text(200,40,text=">",font=("FreeMono",13),anchor="c",fill="#ffffff")

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
					(300/7/2)+(300/7)*d2+(300/7/2),dy+(300/7/2),fill="#ffffff",outline="#ffffff")
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
cal=tk.Canvas(height=313,width=300,bg="#111111",relief="flat", highlightthickness=0,border=0)
cal.bind("<Button-1>",cal_commands)
draw_cal()

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


try:
	dbstock=db.connect('data/sales.db')
	cur=dbstock.cursor()	
	cur.execute("""CREATE TABLE sales_(
		sales_id INT,
		name VARCHAR(255),
		sp INT,
		ps INT,
		quantity INT,
		date_ VARCHAR(255),
		total INT,
		profit INT );""")

	dbstock.close()
except:
	pass




carti=()


settw=()
settb=()
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





lvar=0

draw_dashb()
search()
gentotal()
move_dashb()

un.focus_set()

root.mainloop()