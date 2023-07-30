import tkinter as tk
import math
from tkinter import filedialog
from PIL import Image,ImageTk,ImageEnhance
import sqlite3 as db
import xv
import os


def login(e):
	global intro,un,pw

	if 595.5<=e.x<=770.5:
		if 350<=e.y<=375:



			if un.get()=="admin" and pw.get()=="pass":
				un.place_forget()
				pw.place_forget()

				intro.place_forget()


def move_dashb():
	global dx,dashb,dvar

	if dvar==1:
		dvar=0
		dashb.place(in_=win,x=-250,y=0)

	elif dvar==2:
		dvar=0
		dashb.place(in_=win,x=0,y=0)






	win.after(1,move_dashb)




wd,ht=1366,768

win=tk.Tk()
win.resizable(0,0)
win.title("Precious collections")
win.geometry(str(wd)+"x"+str(ht)+"+0+0")



########################

def main1_commands(e):
	global dvar,dvar2,dashb_state,main2,as_im,as_image,ax,ay

	if 0<=e.x<=32:
		if 0<=e.y<=32:
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
	global as_n,as_bp,as_sp,as_q,as_de,msimage,msi,msf,mscon,mscon2,vbar1

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

		cx,cy=x1+785-5,y1+15

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

				dbstock=db.connect('stock.db')
				cur=dbstock.cursor()

				cur.execute("UPDATE items SET name='"+str(n)+"' WHERE items_id="+str(seli)+" ")
				cur.execute("UPDATE items SET bp="+str(bp)+" WHERE items_id="+str(seli)+"  ")
				cur.execute("UPDATE items SET sp="+str(sp)+" WHERE items_id="+str(seli)+" ")
				cur.execute("UPDATE items SET quantity="+str(q)+" WHERE items_id="+str(seli)+" ")
				cur.execute("UPDATE items SET description='"+str(de)+"' WHERE items_id="+str(seli)+" ")	

				dbstock.commit()			




				dbstock=db.connect('stock.db')
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
						dbstock=db.connect('stock.db')
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





		if x1+415<=e.x<=x1+545:
			if y1+460<=y<=y1+490:




				dbstock=db.connect('stock.db')
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

			im.save("msi."+ext)

			msimage=ImageTk.PhotoImage(file="msi."+ext)

			msi=main2.create_image(x1+400-20+ax,y1+20+ay+10,image=msimage,anchor="nw")
		cx,cy=x1+765,y1+435+10

		r=math.sqrt((e.x-cx)**2 + (y-cy)**2)

		if r<=15:
			if not msimage=="":

				main2.delete(msi)
				msimage=""
				mscon=0
			

	elif dashb_state=="sell_items":
		y=main2.canvasy(e.y)
		yy=main2.canvasy(0)





		if dvar2==1:
			x1,y1=250+(wd-250-800)/2,50+yy
		elif dvar2==0:
			x1,y1=(wd-800)/2,50+yy

		for v in sellarray:

			if v[1]<=e.x<=v[3]:
				if v[2]<=y<=v[4]:
					

					if si_con==0:
						si_con=1
						seli=v[0]
						draw_sellitems()
						

		cx,cy=x1+785-5,y1+15

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
				print("sell items")


				ps=psoldat.get()
				quantity=si_quantity.get()


				try:
					ps=int(ps)
					quantity=int(quantity)
				except:
					return



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

				dbstock.commit()

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

		r=math.sqrt((e.x-cx)**2 + (e.y-cy)**2)


		if r<=40 and ascon==0:
			file_path=filedialog.askopenfilename()

			try:
				im=Image.open(file_path)

				x,y=im.size

				if x>y:
					bx=400
					by=int(y*(400/x))

					im2=im.resize((bx,by))
					im2.save("mod."+file_path.split(".")[1])
					ax,ay=0,(400-by)/2
				elif y>x:
					bx=int(x*(400/y))
					by=400

					im2=im.resize((bx,by))
					im2.save("mod."+file_path.split(".")[1])
					ax,ay=(400-bx)/2,0

				elif x==y:
					bx,by=400,400
					ax,ay=0,0

					im2=im.resize((bx,by))
					im2.save("mod."+file_path.split(".")[1])


				as_image=ImageTk.PhotoImage(file="mod."+file_path.split(".")[1])

				
				as_im=main2.create_image(x_+400-20+ax,y_+20+ay,image=as_image,anchor="nw")

				ascon=1
			except:
				file_path=""

		cx,cy=x_+765,y_+435

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

				if name=="" or bp=="" or sp=="":
					ascon2=1
					draw_addstock()

					return

				


				dbstock=db.connect('stock.db')
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


	dbstock=db.connect('stock.db')
	cur=dbstock.cursor()


	cur.execute("INSERT INTO 	items VALUES("+str(id_)+",'"+name+"',"+str(bp)+","+str(sp)+","+str(quantity)+",'"+desc+"',"+pic+")")

	dbstock.commit()
def sales_(id_,name,sp,ps,quantity,date_,total,profit):


	dbs=db.connect('sales.db')
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

	global dvar,dashb,dashb_state,dvar2,as_im,as_image,ax,ay
	global as_n,as_bp,as_sp,as_q,as_de,ht,wd,main2,si_quantity,psoldat,si_desc,searche,vbar1

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



	if 53<=e.y<=53+30:
		dashb_state="sell_items"
		draw_dashb()
		main2["scrollregion"]=(0,0,wd,ht-50)

		vbar1.pack_forget()
		main2.pack_forget()

		vbar1.pack(side=tk.RIGHT,fill=tk.Y)
		main2.pack(side=tk.LEFT)
		as_n.place_forget()
		as_bp.place_forget()
		as_sp.place_forget()
		as_q.place_forget()
		as_de.place_forget()

		rr_.place_forget()

		searche.place_forget()

		searche.delete(0,tk.END)


		draw_sellitems()
	elif 86<=e.y<=86+30:

		dashb_state="add_stock"
		main2["scrollregion"]=(0,0,wd,ht-50)
		draw_dashb()
		draw_addstock()
		searche.delete(0,tk.END)
		rr_.place_forget()

		vbar1.pack_forget()

		si_quantity.place_forget()
		psoldat.place_forget()
		si_desc.place_forget()

		searche.place_forget()

	elif 119<=e.y<=119+30:
		dashb_state="stock"
		draw_dashb()
		main2["scrollregion"]=(0,0,wd,ht-50)
		searche.delete(0,tk.END)

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
	elif 152<=e.y<=152+30:

		dashb_state="reports"
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
def draw_dashb():
	global dashb,dashb_state


	if dashb_state=="sell_items":

		col1,col1_="#ffffff","#000000"
		col2,col2_="#000000","#ffffff"
		col3,col3_="#000000","#ffffff"
		col4,col4_="#000000","#ffffff"

	elif dashb_state=="add_stock":

		col1,col1_="#000000","#ffffff"
		col2,col2_="#ffffff","#000000"
		col3,col3_="#000000","#ffffff"
		col4,col4_="#000000","#ffffff"
	elif dashb_state=="stock":

		col1,col1_="#000000","#ffffff"
		col2,col2_="#000000","#ffffff"
		col3,col3_="#ffffff","#000000"
		col4,col4_="#000000","#ffffff"

	elif dashb_state=="reports":

		col1,col1_="#000000","#ffffff"
		col2,col2_="#000000","#ffffff"
		col3,col3_="#000000","#ffffff"
		col4,col4_="#ffffff","#000000"

	dashb.create_rectangle(0,0, 250,50,fill="#000000",outline="#000000")

	dashb.create_rectangle(0,50+3,250,80+3,fill=col1,outline=col1)
	dashb.create_text(50,65+3,text="Sell Items",fill=col1_,font=("FreeMono",14),anchor="w")

	dashb.create_rectangle(0,86,250,80+30+6,fill=col2,outline=col2)
	dashb.create_text(50,65+30+6,text="New Stock",fill=col2_,font=("FreeMono",14),anchor="w")

	dashb.create_rectangle(0,119,250,80+2*30+9,fill=col3,outline=col3)
	dashb.create_text(50,65+9+2*30,text="Manage Stock",fill=col3_,font=("FreeMono",14),anchor="w")

	dashb.create_rectangle(0,152,250,80+3*30+12,fill=col4,outline=col4)
	dashb.create_text(50,65+12+3*30,text="Reports",fill=col4_,font=("FreeMono",14),anchor="w")

	dashb.create_rectangle(0,80+3*30+12+3,250,ht,fill="#000000",outline="#000000")

	dashb.create_line(250-20-2,20-5, 250-20+8-2,20-8-5,fill="#ffffff",width=2)
	dashb.create_line(250-20-2,20-5, 250-20+8-2,20+8-5,fill="#ffffff",width=2)



dvar=0
dvar2=1
dx=0
dashb_state="sell_items"

dashb=tk.Canvas(relief="flat",width=250,height=ht,bg="#111111",highlightthickness=0,border=0)
dashb.bind("<Button-1>",dashb_commands)
dashb.place(in_=win,x=0,y=0)






draw_dashb()

################


intro=tk.Canvas(width=wd,height=ht,bg="#111111",highlightthickness=0,border=0,relief="flat")
intro.bind("<Button-1>",login)
intro.place(in_=win,x=0,y=0)



x_,y_=(wd/2)-350/2,200



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



intro.create_text(x_+20,y_+40, anchor="w",text="User name",fill="#000000",font=("FreeMono","14"))
intro.create_text(x_+20,y_+40+50, anchor="w",text="Password",fill="#000000",font=("FreeMono","14"))


intro.create_rectangle(x_+150-2,y_+30-2, x_+150+168,y_+30+20+5,fill="#000000")
intro.create_rectangle(x_+150-2,y_+30-2+50, x_+150+168,y_+30+20+5+50,fill="#000000")

un=tk.Entry(width=15,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,font=("FreeMono","14"))
un.place(in_=win,x=x_+150,y=y_+30)

pw=tk.Entry(width=15,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,font=("FreeMono","14"),show="*")
pw.place(in_=win,x=x_+150,y=y_+30+50)


intro.create_rectangle(x_+100,y_+130+20, x_+250,y_+130+25+20, fill="#111111",outline="#111111")
intro.create_oval(x_+100-(25/2), y_+130+20, x_+100+(25/2), y_+130+20+25,fill="#111111",outline="#111111")

intro.create_oval(x_+250-(25/2), y_+130+20, x_+250+(25/2), y_+130+20+25,fill="#111111",outline="#111111")

intro.create_text(x_+350/2,y_+130+20+(25/2),text="Login",font=("FreeMono","14"),fill="#ffffff")

# sell items




def draw_sellitems():
	global main1,main2,dvar2,wd, si_con,sellarray,seli,si_quantity,psoldat,total, pos,si_desc,yvar
	global searche,svar,vbar1
	main1.delete("all")
	main2.delete("all")



	if dvar2==1:
		x_=250+(wd-250)/2
	elif dvar2==0:
		x_=wd/2
	if si_con==0:
		col="#ffffff"
		pic_="s"
	elif si_con==1:

		col="#555555"
		pic_="sd"
		


	main1.create_rectangle(x_-150,10, x_+150,40,fill="#111111",outline="#111111")
	main1.create_oval(x_-150-15,10, x_-150+15,40,fill="#111111",outline="#111111")
	main1.create_oval(x_+150-15,10, x_+150+15,40,fill="#111111",outline="#111111")

	main1.create_line(x_+150+50-20+10,25, x_+150+50-20+10+15,25+15,fill="#111111",width=2)
	main1.create_oval(x_+150+50-20,15, x_+150+70-20,35,fill=col,outline="#111111",width=2)

	searche.place(in_=win,x=x_-148,y=13)

	si_quantity.place_forget()
	psoldat.place_forget()
	si_desc.place_forget()

	psoldat.delete(0,tk.END)
	si_quantity.delete(0,tk.END)

	sellarray=[]



	main1["bg"]=col
	main2["bg"]=col
	main1.create_line( 13,8, 21,16, 13,24,fill="#000000",width=2)
	n=0

	dbstock=db.connect('stock.db')
	cur=dbstock.cursor()

	cur.execute("SELECT * FROM items")

	rows=cur.fetchall()


	_items=[]
	for row in rows:

		if not row[1].lower().find(svar.lower())==-1:
			n+=1

			_items.append(row)
			

	if dvar2==1:
		xx=250
		e=3
		bx=(wd-250-(304*3))/4
	elif dvar2==0:
		xx=0
		e=4
		bx=(wd-(304*4))/5
		
		
	

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


			main2.create_arc(x+bx,y, x+bx+20,y+20, outline="#000000", style="arc", start=90, extent=90,width=2)
			main2.create_arc(x+bx,y+300-20, x+bx+20,y+300, outline="#000000", style="arc", start=180, extent=90,width=2)

			main2.create_arc(x+bx+304-20,y, x+bx+304,y+20, outline="#000000", style="arc", start=0, extent=90,width=2)
			main2.create_arc(x+bx+304-20,y+300-20, x+bx+304,y+300, outline="#000000", style="arc", start=270, extent=90,width=2)

			main2.create_line(x+bx+10,y, x+bx+304-10,y,fill="#000000",width=2)
			main2.create_line(x+bx+10,y+300, x+bx+304-10,y+300,fill="#000000",width=2)

			main2.create_line(x+bx,y+10, x+bx,y+300-10,fill="#000000",width=2)
			main2.create_line(x+bx+304,y+10, x+bx+304,y+300-10,fill="#000000",width=2)
			#x+bx,y, x+bx+304,y+300
					


			
			name=_items[count][1]
			price=_items[count][3]
			items_=_items[count][4]

			main2.create_text(x+bx+10,y+200+20,anchor="w",text=str(name),font=("FreeMono","14"))
			main2.create_text(x+bx+10,y+200+20+30,anchor="w",text=str(price)+" Ksh",font=("FreeMono","14"))
			main2.create_text(x+bx+10,y+200+20+60,anchor="w",text=str(items_)+" items left",font=("FreeMono","14"))

			x+=304+bx
			count+=1

			if count==n:
				con=1
				break
		y+=300+40
		if con==1:
			break


	yvar=y
	main2["scrollregion"]=(0,0,wd,yvar)

	if si_con==1:

		vbar1.pack_forget()

		searche.place_forget()
		yy=main2.canvasy(0)

		if dvar2==1:
			x1,y1=250+(wd-250-800)/2,50+yy
		elif dvar2==0:
			x1,y1=(wd-800)/2,50+yy

		dbstock=db.connect('stock.db')
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


		main2.create_line(x1+785-7-5,y1+15-7, x1+785+7-5,y1+15+7,fill="#000000",width=2)
		main2.create_line(x1+785-7-5,y1+15+7, x1+785+7-5,y1+15-7,fill="#000000",width=2)

		main2.create_line(x1+500,y1+50,x1+500,y1+450,fill="#000000")

		main2.create_text(x1+250,y1+20,text=name2.upper(),fill="#000000",font=("FreeMono",15,))

		main2.create_text(x1+500+20,y1+70, fill="#000000",font=("FreeMono",14),text="Price",anchor="w")
		main2.create_text(x1+500+20+90,y1+70, fill="darkred",font=("FreeMono",14),text=price,anchor="w")
		main2.create_text(x1+500+20,y1+70+40, fill="#000000",font=("FreeMono",14),text=quant+" items left"
			,anchor="w")

		main2.create_line(x1+500+30,y1+140, x1+800-30,y1+140,fill="#000000" )

		main2.create_text(x1+500+20,y1+170,fill="#000000",text="Sold at",font=("FreeMono",14),anchor="w")
		main2.create_text(x1+500+20,y1+170+40,fill="#000000",text="Quantity",font=("FreeMono",14),anchor="w")


		main2.create_rectangle(x1+500+120-2,y1+170-10-2, x1+500+120+200-90+3,y1+170-10+100-50-20-5,fill="#000000",outline="#000000")
		main2.create_rectangle(x1+500+120-2,y1+170-10-2+40, x1+500+120+200-90+3,y1+170-10+100-50-20-5+40,fill="#000000",outline="#000000")


		psoldat.place(in_=win,x=x1+500+120,y=100+170-10)
		si_quantity.place(in_=win,x=x1+500+120,y=100+170-10+40)

		si_desc.place(in_=win,x=x1+55,y=520)

		si_desc["text"]=desc[:26]



		pos=[x1,y1]


		main2.create_text(x1+500+20,y1+500-50-70,text="Total",fill="red",font=
			("FreeMono",20),anchor="w")

		total=main2.create_text(x1+500+20+80,y1+500-50-70,text="0",fill="#000000",font=
			("FreeMono",20),anchor="w")

		main2.create_rectangle(x1+500+40+30,y1+500-50-30, x1+800-40-30,y1+500-50,fill="#111111",outline="#111111")
		main2.create_oval(x1+500+40+30-15,y1+500-50-30, x1+500+40+30+15,y1+500-50,fill="#111111",outline="#111111")
		main2.create_oval(x1+800-40-30-15,y1+500-50-30, x1+800-40-30+15,y1+500-50,fill="#111111",outline="#111111" )
		main2.create_text(x1+500+150,y1+500-50-15,fill="#ffffff",text="Sell Item",font=("FreeMono",14))



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

			im.save("m."+ext)
			global se_image
			
			se_image=ImageTk.PhotoImage(file="m."+ext)

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
			total=main2.create_text(x+500+20+80,y+500-50-70,text=str(total_),fill="#000000",font=
			("FreeMono",20),anchor="w")
		except:
			x,y=pos[0],pos[1]
			main2.delete(total)
			total=main2.create_text(x+500+20+80,y+500-50-70,text="0",fill="#000000",font=
			("FreeMono",20),anchor="w")

	win.after(1,gentotal)
		
		



si_con=0
sellarray=[]
seli=0

se_image=""
total=()
total_=0
pos=[]



psoldat=tk.Entry(width=10,bg="#ffffff",relief="flat", highlightthickness=0,border=0,font=
	("FreeMono",14))
psoldat.bind("<KeyPress>",gentotal)


si_quantity=tk.Entry(width=10,bg="#ffffff",relief="flat", highlightthickness=0,border=0,font=
	("FreeMono",14))
si_quantity.bind("<KeyPress>",gentotal)

si_desc=tk.Label(width=35,height=3,bg="#ffffff",relief="flat", highlightthickness=0,border=0,font=
	("FreeMono",14),justify="center")
# Add stock

def draw_addstock():
	global main1,main2,as_n,as_bp,as_sp,as_q,as_de,dvar2,ascon2,as_im
	global wd,ht,si_quantity,psoldat,ms_con

	as_n.delete(0,tk.END)
	as_bp.delete(0,tk.END)
	as_sp.delete(0,tk.END)
	as_q.delete(0,tk.END)
	as_de.delete(0.0,tk.END)

	main1.delete("all")
	main2.delete("all")

	main1["bg"]="#ffffff"
	main2["bg"]="#ffffff"

	main1.create_line( 13,8, 21,16, 13,24,fill="#000000",width=2)


	if dvar2==1:
		x_,y_=250+(wd-250-800)/2,30
	elif dvar2==0:
		x_,y_=(wd-800)/2,30

	main2.create_oval(x_,y_, x_+20,y_+20,fill="#111111",outline="#111111")
	main2.create_oval(x_-20+800,y_, x_+800,y_+20,fill="#111111",outline="#111111")
	main2.create_oval(x_,y_+500-20, x_+20,y_+500,fill="#111111",outline="#111111")
	main2.create_oval(x_-20+800,y_+500-20, x_+800,y_+500,fill="#111111",outline="#111111")

	main2.create_polygon(x_+10,y_, x_+800-10,y_, x_+800,y_+10, x_+800,y_+500-10,
		x_+800-10,y_+500, x_+10,y_+500, x_,y_+500-10, x_,y_+10,fill="#111111",outline="#111111")

	yy=50
	main2.create_text(x_+30,y_+40,text="Name",font=("FreeMono",14),fill="#ffffff",anchor="w")
	main2.create_text(x_+30,y_+40+yy,text="Buying Price",font=("FreeMono",14),fill="#ffffff",anchor="w")
	main2.create_text(x_+30,y_+40+yy*2,text="Selling Price",font=("FreeMono",14),fill="#ffffff",anchor="w")	
	main2.create_text(x_+30,y_+40+yy*3,text="Quantity",font=("FreeMono",14),fill="#ffffff",anchor="w")

	main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2-yy+y_, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_,fill="#777777",outline="#777777")
	main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2+y_, x_+170+170-2,40+yy+50-13-yy+28-3+y_,fill="#777777",outline="#777777")
	main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2+yy+y_, x_+170+170-2,40+yy+50-13-yy+28+yy-3+y_,fill="#777777",outline="#777777")	
	main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2+yy+yy+y_, x_+170+170-2,40+yy+50-13-yy+28+yy+yy-3+y_,fill="#777777",outline="#777777")

	as_n.place(in_=win,x=x_+170,y=40+yy+50-13-yy+y_)
	as_bp.place(in_=win,x=x_+170,y=40+yy+50-13+y_)
	as_sp.place(in_=win,x=x_+170,y=40+yy+50-13+yy+y_)
	as_q.place(in_=win,x=x_+170,y=40+yy+50-13+yy+yy+y_)



	#main2.create_rectangle(x_+30,y_+300, x_+30+320,y_+300+100,fill="red")

	main2.create_text(x_+50+5,y_+300+25,text="Description",anchor="sw",font=("FreeMono",14),fill="#ffffff")
	main2.create_line(x_+30+20,y_+300-5+25, x_+30,y_+300-5+25, x_+30, y_+300+95+25, x_+300+40, y_+300+95+25,
	x_+300+40, y_+300-5+25 ,x_+300+40-190+5, y_+300-5+25,  fill="#777777",width=2)

	as_de.place(in_=win,x=x_+30+5,y=y_+300+50+25)

	main2.create_rectangle(x_+400-20-1,y_+20-1, x_+400+400-20,y_+20+400,fill="#111111",outline="#555555")



	main2.create_text(x_-20+400+200,y_+100,text="Add Image",fill="#ffffff", font=("FreeMono",30))

	main2.create_oval(x_-20+400+200-40,y_+20+200-40, x_-20+400+200+40,y_+20+200+40, fill="#111111", outline="#ffffff",width=2 )

	main2.create_line(x_-20+400+200,y_+20+200-20, x_-20+400+200,y_+20+200+20,fill="#ffffff",width=2 )
	main2.create_line(x_-20+400-20+200,y_+20+200, x_-20+400+200+20,y_+20+200,fill="#ffffff",width=2 )

	main2.create_line(x_+400+400-20-15-7,y_+20+400+15-7, x_+400+400-20-15+7,y_+20+400+15+7,fill="#ffffff",width=2)
	main2.create_line(x_+400+400-20-15-7,y_+20+400+15+7, x_+400+400-20-15+7,y_+20+400+15-7,fill="#ffffff",width=2)

	if ascon2==1:
		main2.create_text(x_+400, y_+500-60,text="Fill all fields.",fill="red",font=("FreeMono",14))

	if not as_image=="":
		as_im=main2.create_image(x_+400-20+ax,y_+20+ay,image=as_image,anchor="nw")

	main2.create_rectangle(x_+400-60, y_+500-60+20, x_+400+60,y_+500-30+20,fill="#ffffff",outline="#ffffff")
	main2.create_oval(x_+400-60-15, y_+500-60+20, x_+400-60+15, y_+500-60+20+30,fill="#ffffff",outline="#ffffff")
	main2.create_oval(x_+400+60-15,y_+500-60+20, x_+400+60+15,y_+500-60+20+30,fill="#ffffff",outline="#ffffff")


	main2.create_text(x_+400,y_+500-30+20-15,text="Add Stock", fill="#000000",font=("FreeMono",14))






ascon=0
ascon2=0
as_n=tk.Entry(bg="#ffffff",width=15,font=("FreeMono",14),relief="flat",highlightthickness=0,border=0)
as_bp=tk.Entry(bg="#ffffff",width=15,font=("FreeMono",14),relief="flat",highlightthickness=0,border=0)
as_sp=tk.Entry(bg="#ffffff",width=15,font=("FreeMono",14),relief="flat",highlightthickness=0,border=0)
as_q=tk.Entry(bg="#ffffff",width=15,font=("FreeMono",14),relief="flat",highlightthickness=0,border=0)
as_de=tk.Text(bg="#ffffff",width=27,height=4,font=("FreeMono",14),relief="flat",highlightthickness=0,border=0)

# stock

def draw_stock():
	global main1,main2,dvar2,wd, si_con,msarray,ms_con,seli
	global as_n,as_bp,as_sp,as_q,as_de,msimage,msi,yvar,vbar1,svar,searche
	main1.delete("all")
	main2.delete("all")
	if ms_con==0:
		col="#ffffff"
		pic_="s"
	elif ms_con==1:

		col="#555555"
		pic_="sd"

	as_n.delete(0,tk.END)
	as_bp.delete(0,tk.END)
	as_sp.delete(0,tk.END)
	as_q.delete(0,tk.END)
	as_de.delete(0.0,tk.END)


	if dvar2==1:
		x_=250+(wd-250)/2
	elif dvar2==0:
		x_=wd/2

		


	main1.create_rectangle(x_-150,10, x_+150,40,fill="#111111",outline="#111111")
	main1.create_oval(x_-150-15,10, x_-150+15,40,fill="#111111",outline="#111111")
	main1.create_oval(x_+150-15,10, x_+150+15,40,fill="#111111",outline="#111111")

	main1.create_line(x_+150+50-20+10,25, x_+150+50-20+10+15,25+15,fill="#111111",width=2)
	main1.create_oval(x_+150+50-20,15, x_+150+70-20,35,fill=col,outline="#111111",width=2)

	searche.place(in_=win,x=x_-148,y=13)


	msarray=[]



	main1["bg"]=col
	main2["bg"]=col
	main1.create_line( 13,8, 21,16, 13,24,fill="#000000",width=2)
	n=0

	dbstock=db.connect('stock.db')
	cur=dbstock.cursor()

	cur.execute("SELECT * FROM items")

	rows=cur.fetchall()


	_items=[]
	for row in rows:

		if not row[1].lower().find(svar.lower())==-1:
			n+=1

			_items.append(row)
			

	if dvar2==1:
		xx=250
		e=3
		bx=(wd-250-(304*3))/4
	elif dvar2==0:
		xx=0
		e=4
		bx=(wd-(304*4))/5
		
		
	

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


			main2.create_arc(x+bx,y, x+bx+20,y+20, outline="#000000", style="arc", start=90, extent=90,width=2)
			main2.create_arc(x+bx,y+300-20, x+bx+20,y+300, outline="#000000", style="arc", start=180, extent=90,width=2)

			main2.create_arc(x+bx+304-20,y, x+bx+304,y+20, outline="#000000", style="arc", start=0, extent=90,width=2)
			main2.create_arc(x+bx+304-20,y+300-20, x+bx+304,y+300, outline="#000000", style="arc", start=270, extent=90,width=2)

			main2.create_line(x+bx+10,y, x+bx+304-10,y,fill="#000000",width=2)
			main2.create_line(x+bx+10,y+300, x+bx+304-10,y+300,fill="#000000",width=2)

			main2.create_line(x+bx,y+10, x+bx,y+300-10,fill="#000000",width=2)
			main2.create_line(x+bx+304,y+10, x+bx+304,y+300-10,fill="#000000",width=2)
			#x+bx,y, x+bx+304,y+300
					


			
			name=_items[count][1]
			price=_items[count][3]
			items_=_items[count][4]

			main2.create_text(x+bx+10,y+200+20,anchor="w",text=str(name),font=("FreeMono","14"))
			main2.create_text(x+bx+10,y+200+20+30,anchor="w",text=str(price)+" Ksh",font=("FreeMono","14"))
			main2.create_text(x+bx+10,y+200+20+60,anchor="w",text=str(items_)+" items left",font=("FreeMono","14"))

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


		dbstock=db.connect('stock.db')
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


		main2.create_line(x_+785-7-5,y_+15-7, x_+785+7-5,y_+15+7,fill="#000000",width=2)
		main2.create_line(x_+785-7-5,y_+15+7, x_+785+7-5,y_+15-7,fill="#000000",width=2)


		yy=50
		main2.create_text(x_+30,y_+40+10,text="Name",font=("FreeMono",14),fill="#000000",anchor="w")
		main2.create_text(x_+30,y_+40+yy+10,text="Buying Price",font=("FreeMono",14),fill="#000000",anchor="w")
		main2.create_text(x_+30,y_+40+yy*2+10,text="Selling Price",font=("FreeMono",14),fill="#000000",anchor="w")	
		main2.create_text(x_+30,y_+40+yy*3+10,text="Quantity",font=("FreeMono",14),fill="#000000",anchor="w")

		main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2-yy+y_+10, x_+170+170-2,40+yy+50-13-yy+28-yy-3+y_+10,fill="#777777",outline="#777777")
		main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2+y_+10, x_+170+170-2,40+yy+50-13-yy+28-3+y_+10,fill="#777777",outline="#777777")
		main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2+yy+y_+10, x_+170+170-2,40+yy+50-13-yy+28+yy-3+y_+10,fill="#777777",outline="#777777")	
		main2.create_rectangle(x_+170-2,40+yy+50-13-yy-2+yy+yy+y_+10, x_+170+170-2,40+yy+50-13-yy+28+yy+yy-3+y_+10,fill="#777777",outline="#777777")

		as_n.place(in_=win,x=x_+170,y=40+yy+50-13-yy+y_+10-main2.canvasy(0))
		as_bp.place(in_=win,x=x_+170,y=40+yy+50-13+y_+10-main2.canvasy(0))
		as_sp.place(in_=win,x=x_+170,y=40+yy+50-13+yy+y_+10-main2.canvasy(0))
		as_q.place(in_=win,x=x_+170,y=40+yy+50-13+yy+yy+y_+10-main2.canvasy(0))


		main2.create_text(x_+50+5,y_+300+25+10,text="Description",anchor="sw",font=("FreeMono",14),fill="#000000")
		main2.create_line(x_+30+20,y_+300-5+25+10, x_+30,y_+300-5+25+10, x_+30, y_+300+95+25+10, x_+300+40, y_+300+95+25+10,
		x_+300+40, y_+300-5+25+10 ,x_+300+40-190+5, y_+300-5+25+10,  fill="#777777",width=2)

		as_de.place(in_=win,x=x_+30+5,y=y_+300+50+25+10-main2.canvasy(0))

		main2.create_rectangle(x_+400-20-1,y_+20+10-1, x_+400+400-20,y_+20+400+10,fill="#ffffff",outline="#323232")

		main2.create_text(x_-20+400+200,y_+110,text="Add Image",fill="#111111", font=("FreeMono",30))
		main2.create_oval(x_-20+400+200-40,y_+20+200-40, x_-20+400+200+40,y_+20+200+40, fill="#ffffff", outline="#111111",width=2 )

		main2.create_line(x_-20+400+200,y_+20+200-20, x_-20+400+200,y_+20+200+20,fill="#111111",width=2 )
		main2.create_line(x_-20+400-20+200,y_+20+200, x_-20+400+200+20,y_+20+200,fill="#111111",width=2 )

		main2.create_line(x_+400+400-20-15-7,y_+20+400+15-7+10, x_+400+400-20-15+7,y_+20+400+15+7+10,fill="#111111",width=2)
		main2.create_line(x_+400+400-20-15-7,y_+20+400+15+7+10, x_+400+400-20-15+7,y_+20+400+15-7+10,fill="#111111",width=2)

		a=80
		main2.create_rectangle(x_+400-50-a,y_+500-50+10,x_+400+50-a,y_+500-20+10,fill="#111111",outline="#111111")
		main2.create_oval(x_+400-50-15-a,y_+500-50+10, x_+400-50+15-a,y_+500-20+10,fill="#111111",outline="#111111")
		main2.create_oval(x_+400+50-15-a,y_+500-50+10, x_+400+50+15-a,y_+500-20+10,fill="#111111",outline="#111111")
		main2.create_text(x_+400-a,y_+500-20-15+10,fill="#ffffff",text="Save",font=("FreeMono",14))

		main2.create_rectangle(x_+400-50+a,y_+500-50+10,x_+400+50+a,y_+500-20+10,fill="#111111",outline="#111111")
		main2.create_oval(x_+400-50-15+a,y_+500-50+10, x_+400-50+15+a,y_+500-20+10,fill="#111111",outline="#111111")
		main2.create_oval(x_+400+50-15+a,y_+500-50+10, x_+400+50+15+a,y_+500-20+10,fill="#111111",outline="#111111")
		main2.create_text(x_+400+a,y_+500-20-15+10,fill="#ffffff",text="Remove",font=("FreeMono",14))

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

					im.save("msi."+ext)

					msimage=ImageTk.PhotoImage(file="msi."+ext)

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
	global main1,main2,rr_,dvar2,yvar,svar

	main1.delete("all")
	main2.delete("all")

	main1["bg"]="#ffffff"
	main2["bg"]="#ffffff"


	if dvar2==1:
		x_=250+(wd-250)/2
	elif dvar2==0:
		x_=wd/2

		


	main1.create_rectangle(x_-150,10, x_+150,40,fill="#111111",outline="#111111")
	main1.create_oval(x_-150-15,10, x_-150+15,40,fill="#111111",outline="#111111")
	main1.create_oval(x_+150-15,10, x_+150+15,40,fill="#111111",outline="#111111")

	main1.create_line(x_+150+50-20+10,25, x_+150+50-20+10+15,25+15,fill="#111111",width=2)
	main1.create_oval(x_+150+50-20,15, x_+150+70-20,35,fill="#ffffff",outline="#111111",width=2)

	searche.place(in_=win,x=x_-148,y=13)


	main1.create_line( 13,8, 21,16, 13,24,fill="#000000",width=2)

	if dvar2==1:
		x_=250+(wd-250-1000)/2
	elif dvar2==0:
		x_=(wd-1000)/2

	rr_.place(in_=win,x=x_,y=50)


	dbsales=db.connect("sales.db")
	cur=dbsales.cursor()


	cur.execute("SELECT * FROM sales_ ORDER BY sales_id DESC")

	rows=cur.fetchall()

	yv=30

	st=0
	for row in rows:

		if not str(row[1].lower()).find(svar.lower())==-1:

			var=[str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]).split(" ")[0],str(row[6]),str(row[7]) ]

			v=1000/7
			xv=x_+v

			if st==1:
				main2.create_rectangle(x_,yv,x_+1000,yv+30,fill="#999999",outline="#999999")
				st=0
			elif st==0:
				st=1

			for a in range(7):
				main2.create_text(xv-v/2,yv+15,text=var[a],font=("FreeMono",14),fill="#000000")


				xv+=v

			yv+=30

	v=1000/7
	xv=x_+v
	for a in range(6):
		main2.create_line(xv,30,xv,yv,fill="#000000")

		xv+=v


	yvar=yv+50


def search():
	global svar,dashb_state,searche,si_con,ms_con

	svar=searche.get()



	if dashb_state=="sell_items" and si_con==0:
		draw_sellitems()

	if dashb_state=="stock" and ms_con==0:
		draw_stock()

	if dashb_state=="reports":
		draw_reports()

	win.after(10,search)

svar=""

rr_=tk.Canvas(height=30,width=1000,bg="#111111",relief="flat", highlightthickness=0,border=0)


vv=["Item Name","Selling Price","Price Sold","Quantity","Date","Total","Profit"]
v=1000/7
x=v
for a in range(7):

	rr_.create_line(x,0,x,30,fill="#ffffff")
	rr_.create_text(x-v/2,15,text=vv[a],font=("FreeMono",14),fill="#ffffff")

	x+=v

searche=tk.Entry(width=27,relief="flat",highlightthickness=0,border=0,bg="#111111",font=("FreeMono",14)
,fg="#ffffff",insertbackground="#ffffff" )


try:
	dbstock=db.connect('stock.db')
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
	dbstock=db.connect('sales.db')
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
search()
gentotal()
draw_sellitems()
move_dashb()
win.mainloop()