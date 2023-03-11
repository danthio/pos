from tkinter import *
from win32api import GetSystemMetrics as gsm
import math
from tkinter import filedialog
from PIL import Image,ImageTk,ImageGrab
import sqlite3 as db
import win32gui
import imagevar


def validate():
	global wd,un_,pw_,err,intro,frame

	un=un_.get()
	pw=pw_.get()


	if un=="admin" and pw=="pass":
		pw_.delete(0,END)
		un_.delete(0,END)

		frame.focus_set()

		intro.place_forget()
		un_.place_forget()
		pw_.place_forget()
		

	else:

		pw_.delete(0,END)
		un_.delete(0,END)


		intro.delete(err)
		err=intro.create_text((wd/2),440,anchor="c",text="Invalid entry",font=("FreeMono",13),fill="red")

		intro.focus_set()

def login(e):

	

	if (wd/2)-85 <= e.x <= (wd/2)+85:
		if 380<= e.y <=410:
			validate()



def cerr(e):
	global intro,err

	intro.delete(err)

def j1(e):
	global pw_

	pw_.focus_set()
def j2(e):

	validate()

def getcoord(e):
	global main2

	x=main2.canvasx(e.x)
	y=main2.canvasy(e.y)


def _on_mousewheel(e):
	global main2
	main2.yview_scroll(int(-1*(e.delta/120)), "units")



def main1e(e):
	global con_dashb,_dashb_,main2,ht,state

	def checkC(x,y):
		cx,cy=25,25

		val=math.sqrt((x-cx)**2+(y-cy)**2)

		if val<=15:
			return 1
		else:
			return 0

	if checkC(e.x,e.y)==1:
		con_dashb=1
		_dashb_=0

		if state=="items":
			draw_items()
		elif state=="addstock":
			draw_addstock()
		elif state=="reports":
			draw_reports()
		elif state=="summary":
			draw_summary()



def move_dashb():
	global con_dashb,_dashb,_dashb_

	if con_dashb==1:

		if _dashb_==0:
			_dashb+=2

			if _dashb==0:
				con_dashb=0

		elif _dashb_==1:
			_dashb-=2

			if _dashb==-300:
				con_dashb=0


		dashb.place(in_=root,x=_dashb,y=0)

	root.after(1,move_dashb)



def db_commands(e):
	global main1,con_dashb,_dashb_,state

	def checkC(x,y):
		cx,cy=275,25

		val=math.sqrt((x-cx)**2+(y-cy)**2)

		if val<=15:
			return 1
		else:
			return 0

	if 10<= e.x <=290:
		if 55<=e.y<=85:
			draw_items()
			state="items"

	if 10<= e.x <=290:
		if 105<=e.y<=135:
			draw_reports()
			state="reports"
			
	if 10<= e.x <=290:
		if 155<=e.y<=185:
			draw_summary()
			state="summary"

	if 10<= e.x <=290:
		if 205<=e.y<=235:
			draw_addstock()
			state="addstock"

	if checkC(e.x,e.y)==1:
		con_dashb=1
		_dashb_=1

		if state=="items":
			draw_items()
		elif state=="addstock":
			draw_addstock()
		elif state=="reports":
			draw_reports()
		elif state=="summary":
			draw_summary()
	#if e.x


def draw_items():
	global main2,main1,_dashb_,wd,ht
	global as_name,as_price,as_no,items_image



	main1.create_line(0,49,wd,49,fill="#323232")

	arr=[]

	conn=db.connect("stock.db")
	v=conn.execute("SELECT * FROM stock_data ORDER BY item_name ASC ;")

	for a in v:
		arr.append(a)



	main2["bg"]="#ffffff"
	main1["bg"]="#ffffff"

	as_name.place_forget()
	as_price.place_forget()
	as_no.place_forget()
	main2.pack_forget()

	vbar1.pack(side=RIGHT,fill=Y)
	main2.pack(side=LEFT)


	main2["scrollregion"]=(0,0,wd,ht-50)

	main2.delete("all")

	n=1010

	w_=gsm(0)

	if w_==1366:
		d1,d2=25.2,31.5
	elif w_==1440:
		d1,d2=48,60


	ar=[]

	if _dashb_==1:
		x=d1

		v=int(str(float(n/4)).split(".")[0])
		v2=int(str(float(n/4)).split(".")[1])

		if v2>0:
			v+=1

		sc=20+(220*v)
		main2["scrollregion"]=(0,0,wd,sc)

	elif _dashb_==0:
		x=d2+300

		v=int(str(float(n/3)).split(".")[0])
		v2=int(str(float(n/3)).split(".")[1])

		if v2>0:
			v+=1

		sc=20+(220*v)
		main2["scrollregion"]=(0,0,wd,sc)




	y=20

	if not len(arr)==0:
		for a in range(len(arr)):

			im=arr[a][4]
			

			main2.create_rectangle(x,y,x+300,y+200,fill="grey",outline="grey")


			if not im=="_":
				imagevar.items_arr[a]=ImageTk.PhotoImage(file="images1/"+str(im)+"_s.jpg")

				im=Image.open("images1/"+str(im)+"_s.jpg")
				w,h=im.size

				vx,vy=0,0

				if w==300:
					if not h==200:
						vy=(200-h)/2
				if h==200:
					if not w==300:
						vx=(300-w)/2

				main2.create_image(x+vx,y+vy,image=imagevar.items_arr[a],anchor="nw")

			if _dashb_==1:
				x+=300+d1
			elif _dashb_==0:
				x+=300+d2

			if _dashb_==1:
				if x==d1+(300+d1)*4:
					x=d1
					y+=220
			elif _dashb_==0:
				if x==d2+300+(300+d2)*3:
					x=d2+300
					y+=220

def draw_reports():
	global as_name,as_price,as_no,main2

	main2["bg"]="#ffffff"
	main1["bg"]="#ffffff"

	as_name.place_forget()
	as_price.place_forget()
	as_no.place_forget()

	main2.delete("all")


def draw_summary():
	global as_name,as_price,as_no,main2

	main2["bg"]="#ffffff"
	main1["bg"]="#ffffff"

	as_name.place_forget()
	as_price.place_forget()
	as_no.place_forget()

	main2.delete("all")

def draw_addstock():

	global main2,_dashb_,as_i1,crop_region,coord,as_name,as_price,as_no,vbar1,s_as_n
	global as_i2,wd

	main2["bg"]="#ffffff"
	main1["bg"]="#ffffff"

	vbar1.pack_forget()

	main2.delete("all")

	as_name.place_forget()
	as_price.place_forget()
	as_no.place_forget()

	main2["scrollregion"]=(0,0,wd,ht-50)


	def draw_asn(sx,sy,qx,qy):
		main2.create_polygon(sx+10,sy, sx+10+qx,sy, sx+qx+20,sy+10,
			sx+qx+20,sy+qy+10, sx+qx+10,sy+qy+20, sx+10,sy+qy+20,
			sx,sy+qy+10, sx,sy+10,fill="#ffffff",outline="#ffffff")

		main2.create_oval(sx,sy, sx+20,sy+20,fill="#ffffff",outline="#ffffff")
		main2.create_oval(sx+qx,sy, sx+20+qx,sy+20,fill="#ffffff",outline="#ffffff")

		main2.create_oval(sx,sy+qy, sx+20,sy+20+qy,fill="#ffffff",outline="#ffffff")
		main2.create_oval(sx+qx,sy+qy, sx+20+qx,sy+20+qy,fill="#ffffff",outline="#ffffff")


		main2.create_oval(sx+qx-15,sy+5, sx+qx+15,sy+35,outline="darkred",fill="#ffffff")
		main2.create_line(sx+qx-7,sy+13, sx+qx+7,sy+27, fill="red",width=2)
		main2.create_line(sx+qx-7,sy+27, sx+qx+7,sy+13,fill="red",width=2)

		main2.create_text(sx+30,sy+70,text="Item Name",font=("FreeMono",14),fill="#323232",anchor="w")
		main2.create_rectangle(sx+159,sy+57, sx+339,sy+84,fill="#323232",outline="#323232",width=2 )
		as_name.place(in_=root,x=sx+160,y=sy+108)

		main2.create_text(sx+30,sy+130,text="Price",font=("FreeMono",14),fill="#323232",anchor="w")
		main2.create_rectangle(sx+159,sy+117, sx+339,sy+144,fill="#323232",outline="#323232",width=2 )
		as_price.place(in_=root,x=sx+160,y=sy+168)


		main2.create_text(sx+30,sy+50+120+20,text="Quantity",font=("FreeMono",14),fill="#323232",anchor="w")
		main2.create_rectangle(sx+159,sy+177, sx+343,sy+204,fill="#323232",outline="#323232",width=2 )
		as_no.place(in_=root,x=sx+160,y=sy+228)

		main2.create_rectangle(sx+(qx/2)-50,sy+258, sx+(qx/2)+50,sy+288, fill="#323232",outline="#323232")

		main2.create_oval(sx+(qx/2)-65,sy+258, sx+(qx/2)-35,sy+288, fill="#323232",outline="#323232")
		main2.create_oval(sx+(qx/2)+35,sy+258, sx+(qx/2)+65,sy+288, fill="#323232",outline="#323232")



		main2.create_text(sx+(qx/2),sy+273,text="Add Stock",fill="#ffffff",font=("FreeMono",14))

	vx=((wd-400)-853)/2
	qx,qy=360,290

	if _dashb_==0:

		if  s_as_n==11:
			main2.create_image(300,0,image=as_i2,anchor="nw")
			main2["bg"]="#4c4c4c"
			main1["bg"]="#4c4c4c"
			
			sx,sy=300+((wd-300)-qx)/2,200

			draw_asn(sx,sy,qx,qy)
			




		elif s_as_n==10:

			main2.create_image(150,0,image=as_i2,anchor="nw")
			sx,sy=300+((wd-300)-qx)/2,200
			main2["bg"]="#4c4c4c"
			main1["bg"]="#4c4c4c"			

			draw_asn(sx,sy,qx,qy)

		else:

			main2.create_rectangle(300+50,50, wd-50,650,fill="#b5b5b5",outline="#b5b5b5")

			cx,cy=300+50+(wd-400)/2,50+300
			main2.create_oval(cx-40,cy-40,cx+40,cy+40,fill="#b5b5b5",outline="#666666")
			main2.create_line(cx,cy-25,cx,cy+25,fill="#666666",width=2)
			main2.create_line(cx-25,cy,cx+25,cy,fill="#666666",width=2)

			main2.create_text(350+(wd-400)/2,200,text="Add Image",fill="#666666",font=("FreeMono",55))

			if not as_i1=="":
				main2.create_image(coord[0],coord[2],image=as_i1,anchor="nw")

			main2.create_oval(355,610+45, 390,645+45,fill="#ffffff",outline="#111111")
			main2.create_line(367,619+45-1,367,633+45,382,633+45,fill="#111111",width=2)
			main2.create_line(363,622+45, 378,622+45,378,638+45,fill="#111111",width=2)

			main2.create_oval(400,610+45, 435,645+45,fill="#ffffff",outline="#111111")
			main2.create_line(410.5,620.5+45, 424.5,634.5+45,fill="#111111",width=2)
			main2.create_line(410.5,634.5+45, 424.5,620.5+45,fill="#111111",width=2)

			main2.create_oval(350+(wd-400)-30,655, 350+(wd-400),655+30, fill="#323232",outline="#323232")
			main2.create_oval(350+(wd-400)-30-50+20,655, 350+(wd-400)-50+20,655+30, fill="#323232",outline="#323232")
			main2.create_rectangle(350+(wd-400)-30-50+15+20,655, 350+(wd-400)-15,655+30,fill="#323232",outline="#323232")
			main2.create_text(350+(wd-400)-40+10,655+15,text="Next",anchor="c",font=("FreeMono",14),fill="#ffffff")




		#main2.create_text()


	elif _dashb_==1:



		if  s_as_n==11:
			main2.create_image(150,0,image=as_i2,anchor="nw")

			sx,sy=(wd-qx)/2,200
			main2["bg"]="#4c4c4c"
			main1["bg"]="#4c4c4c"			

			draw_asn(sx,sy,qx,qy)

		elif  s_as_n==10:
			main2.create_image(0,0,image=as_i2,anchor="nw")
			main2["bg"]="#4c4c4c"
			main1["bg"]="#4c4c4c"
			sx,sy=(wd-qx)/2,200
			
			draw_asn(sx,sy,qx,qy)


		else:
			v=wd-400

			main2.create_rectangle(200,50,wd-200,650,fill="#b5b5b5",outline="#b5b5b5")

			cx,cy=200+(wd-400)/2,50+300
			main2.create_oval(cx-40,cy-40,cx+40,cy+40,fill="#b5b5b5",outline="#666666")
			main2.create_line(cx,cy-25,cx,cy+25,fill="#666666",width=2)
			main2.create_line(cx-25,cy,cx+25,cy,fill="#666666",width=2)

			main2.create_text(200+(wd-400)/2,200,text="Add Image",fill="#666666",font=("FreeMono",55))

			if not as_i1=="":
				main2.create_image(coord[1],coord[2],image=as_i1,anchor="nw")

			main2.create_oval(355-150,610+45, 390-150,645+45, fill="#ffffff",outline="#111111")
			main2.create_line(367-150,619+45-1, 367-150,633+45, 382-150,633+45,fill="#111111",width=2)
			main2.create_line(363-150,622+45, 378-150,622+45, 378-150,638+45,fill="#111111",width=2)

			main2.create_oval(400-150,610+45, 435-150,645+45,fill="#ffffff",outline="#111111")
			main2.create_line(410.5-150,620.5+45, 424.5-150,634.5+45,fill="#111111",width=2)
			main2.create_line(410.5-150,634.5+45, 424.5-150,620.5+45,fill="#111111",width=2)


			main2.create_oval(350+(wd-400)-30-150,655, 350+(wd-400)-150,655+30, fill="#323232",outline="#323232")
			main2.create_oval(350+(wd-400)-30-50-150+20,655, 350+(wd-400)-50-150+20,655+30, fill="#323232",outline="#323232")
			main2.create_rectangle(350+(wd-400)-30-50+15-150+20,655, 350+(wd-400)-15-150,655+30,fill="#323232",outline="#323232")
			main2.create_text(350+(wd-400)-40-150+10,655+15,text="Next",anchor="c",font=("FreeMono",14),fill="#ffffff")



def main2e(e):
	global main2,state,_dashb_,as_i1,wd,as_i2,s_as_n
	global as_name,as_price,as_no, as_s_pic

	if state=="addstock":




		def checkc(x,y,cc,r_):
			cx,cy=cc[0],cc[1]

			r=math.sqrt((x-cx)**2 + (y-cy)**2)
			if r<=r_:
				return 1
			else:
				return 0


		if _dashb_==0:
			qx,qy=360,290
			sx,sy=300+((wd-300)-qx)/2,200
			if as_i1=="":
				if checkc(e.x,e.y,[300+50+(wd-400)/2,350],40)==1:
					file_path=filedialog.askopenfilename()
					get_image(file_path)

			if checkc(e.x,e.y,[372.5,627.5+45],17.5)==1:
				print("crop")

			if checkc(e.x,e.y,[417.5,627.5+45],17.5)==1:
				as_i1=""
				as_s_pic=0
				draw_addstock()


			if 350+(wd-400)-60<= e.x <= 350+(wd-400):
				if 655<= e.y<=685:
					hwnd=main2.winfo_id()
					rect=win32gui.GetWindowRect(hwnd)

					im=ImageGrab.grab(rect)
					im2=im.point(lambda p: int(p*0.3))
					w,h=im2.size
					im2=im2.crop((300,0,w,h))
					im2.save("as_i2.jpg")

					as_i2=ImageTk.PhotoImage(file="as_i2.jpg")

					pix=im2.load()
					crgb=pix[10,10]
					col=rgb_to_hex(crgb[0],crgb[1],crgb[2])


					s_as_n=11

					draw_addstock()


			if s_as_n==11 or s_as_n==10:#((wd-300)-qx)/2,200  qx,qy=360,290  sx+qx-15,sy+5, sx+qx+15,sy+35


				

				if checkc(e.x,e.y,[sx+qx,sy+20],15)==1:
					as_i1=""
					as_i2=""
					s_as_n=0
					as_s_pic=0

					as_name.delete(0,END)
					as_price.delete(0,END)

					main2.focus_set()

					draw_addstock()

			#sx+(qx/2)-65,sy+258    sx+(qx/2)+65,sy+288

			if  sx+(qx/2)-65<=e.x<=sx+(qx/2)+65:
				if   sy+258 <=e.y<=sy+288:
					conn=db.connect("stock.db")

					v=conn.execute("SELECT MAX(stockid) FROM stock_data;")

					for a in v:
						_id=a[0]


					an=as_name.get()


					if _id==None:
						_id=1
					else:
						_id+=1


					c1=0

					try:
						if not as_price=="":
							v=int(as_price.get())
					except:
						c1=1

					if as_name.get()=="" or as_price.get()=="":
						draw_addstock()
						main2.create_text(sx+qx/2,sy+20,text="Fill all fields!",fill="red",font=("FreeMono",14))
						as_name.delete(0,END)
						as_price.delete(0,END)
						as_name.focus_set()

					elif c1==1:
						draw_addstock()
						main2.create_text(sx+qx/2,sy+20,text="Price field must be a number!",fill="red",font=("FreeMono",14))
						as_price.delete(0,END)
						as_price.focus_set()	


					else:
						stockid=_id
						item_name="'"+str(as_name.get())+"'"
						price=int(as_price.get())
						quantity=int(as_no.get())

						if as_s_pic==1:
							picture="'stock"+str(stockid)+"'"
						else:
							picture="'_'"

						insert_to_stockdb(stockid,item_name,price,quantity,picture)


						if as_s_pic==1:
							#large 
							im=Image.open("mod.jpg")
							im.save("images1/stock"+str(stockid)+"_l.jpg")

							#small

							ax,ay=im.size

							r1=ax/ay
							r2=(300)/200

							if r2>r1:
								by=200
								bx=by*r1
							elif r1>r2:
								bx=300
								by=bx/r1
							elif r1==r2:
								bx=300
								by=200

							bx=int(bx)
							by=int(by)

							if bx>300:
								bx=300

							if by>200:
								by=200

							im2=im.resize((bx,by))
							im2.save("images1/stock"+str(stockid)+"_s.jpg")

							# small dark
							im3=im2.point(lambda p: int(p*0.3))
							im3.save("images1/stock"+str(stockid)+"_sd.jpg")


						as_i1=""
						as_i2=""
						s_as_n=0

						as_name.delete(0,END)
						as_price.delete(0,END)
						as_s_pic=0

						main2.focus_set()

						draw_addstock()

		elif _dashb_==1:
			qx,qy=360,290
			sx,sy=(wd-qx)/2,200
			if as_i1=="":
				if checkc(e.x,e.y,[200+(wd-400)/2,350],40)==1:

					file_path=filedialog.askopenfilename()
					get_image(file_path)

			if checkc(e.x,e.y,[222.5,627.5+45],17.5)==1:
				print("crop")

			if checkc(e.x,e.y,[267.5,627.5+45],17.5)==1:
				as_i1=""
				as_s_pic=0
				draw_addstock()

			if 350+(wd-400)-60-150<= e.x <= 350+(wd-400)-150:
				if 655<= e.y<=685:
					hwnd=main2.winfo_id()
					rect=win32gui.GetWindowRect(hwnd)

					im=ImageGrab.grab(rect)
					im2=im.point(lambda p: int(p*0.3))
					w,h=im2.size
					#im2=im2.crop((300,0,w,h))
					im2.save("as_i2.jpg")

					as_i2=ImageTk.PhotoImage(file="as_i2.jpg")
					pix=im2.load()
					crgb=pix[10,10]
					col=rgb_to_hex(crgb[0],crgb[1],crgb[2])




					s_as_n=10

					draw_addstock()


			if s_as_n==11 or s_as_n==10:#((wd-300)-qx)/2,200  qx,qy=360,290  sx+qx-15,sy+5, sx+qx+15,sy+35


				

				if checkc(e.x,e.y,[sx+qx,sy+20],15)==1:
					as_i1=""
					as_i2=""
					s_as_n=0

					as_name.delete(0,END)
					as_price.delete(0,END)
					as_s_pic=0

					main2.focus_set()

					draw_addstock()

			if  sx+(qx/2)-65<=e.x<=sx+(qx/2)+65:
				if   sy+258 <=e.y<=sy+288:
					conn=db.connect("stock.db")

					v=conn.execute("SELECT MAX(stockid) FROM stock_data;")

					for a in v:
						_id=a[0]


					an=as_name.get()

					if _id==None:
						_id=1
					else:
						_id+=1


					c1=0

					try:
						if not as_price=="":
							v=int(as_price.get())
					except:
						c1=1




					if as_name.get()=="" or as_price.get()=="":
						draw_addstock()
						main2.create_text(sx+qx/2,sy+20,text="Fill all fields!",fill="red",font=("FreeMono",14))
						as_name.delete(0,END)
						as_price.delete(0,END)
						as_name.focus_set()

					elif c1==1:
						draw_addstock()
						main2.create_text(sx+qx/2,sy+20,text="Price field must be a number!",fill="red",font=("FreeMono",14))
						as_price.delete(0,END)
						as_price.focus_set()						

					else:

						stockid=_id
						item_name="'"+str(as_name.get())+"'"
						price=int(as_price.get())
						quantity=int(as_no.get())

						if as_s_pic==1:
							picture="'stock"+str(stockid)+"'"
						else:
							picture="'_'"

						insert_to_stockdb(stockid,item_name,price,quantity,picture)


						if as_s_pic==1:
							#large 
							im=Image.open("mod.jpg")
							im.save("images1/stock"+str(stockid)+"_l.jpg")

							#small

							ax,ay=im.size

							r1=ax/ay
							r2=(300)/200

							if r2>r1:
								by=200
								bx=by*r1
							elif r1>r2:
								bx=300
								by=bx/r1
							elif r1==r2:
								bx=300
								by=200

							bx=int(bx)
							by=int(by)

							if bx>300:
								bx=300

							if by>200:
								by=200

							im2=im.resize((bx,by))
							im2.save("images1/stock"+str(stockid)+"_s.jpg")

							# small dark
							im3=im2.point(lambda p: int(p*0.3))
							im3.save("images1/stock"+str(stockid)+"_sd.jpg")

						as_i1=""
						as_i2=""
						s_as_n=0

						as_name.delete(0,END)
						as_price.delete(0,END)
						as_s_pic=0

						main2.focus_set()

						draw_addstock()

def get_image(file):

	global main2,_dashb_,wd,as_i1,crop_region,coord,as_s_pic


	try:
		ar=[]

		im=Image.open(file)
		pix=im.load()
		crgb=pix[0,0]# get pixel value
		ax,ay=im.size

		r1=ax/ay
		r2=(wd-400)/600

		if r2>r1:
			by=600
			bx=by*r1
		elif r1>r2:
			bx=wd-400
			by=bx/r1
		elif r1==r2:
			bx=wd-400
			by=600

		bx=int(bx)
		by=int(by)

		if bx>(wd-400):
			bx=wd-400

		if by>600:
			by=600




		ni=im.resize((bx,by))
		ni.save("mod.jpg")

		y_=50

		if _dashb_==0:
			x_=300+50

		elif _dashb_==1:
			x_=200

		coord=[350,200,50]

		if bx<(wd-400):
			x_+=((wd-400)-bx)/2
			coord[0]=350+((wd-400)-bx)/2
			coord[1]=200+((wd-400)-bx)/2

		if by<600:
			y_+=(600-by)/2

			coord[2]=50+(600-by)/2


		

		crop_region=[x_,y_,x_+bx,y_+by]

		as_i1=ImageTk.PhotoImage(file="mod.jpg")
		draw_addstock()

		as_s_pic=1

	except:
		as_s_pic=0


def hex_to_rgb(hex):
	rgb=[]
	for i in (0,2,4):
		decimal=int(hex[i:i+2],16)
		rgb.append(decimal)

	return tuple(rgb)

def rgb_to_hex(r,g,b):
	return '#{:02x}{:02x}{:02x}'.format(r,g,b)



def insert_to_stockdb(stockid,item_name,price,quantity,picture):

	conn=db.connect("stock.db")

	conn.execute(""" INSERT INTO stock_data(stockid,item_name,price,quantity,picture) VALUES 
		("""+str(stockid)+""","""+item_name+""", """+str(price)+""", """+str(quantity)+""", """+picture+""");""")

	conn.commit()

	conn.close()


wd,ht=gsm(0)-20,gsm(1)-75
#wd=1366-20

con_dashb=0
_dashb=0
_dashb_=0

state=""
s_as_n=0
as_i1=""
as_i2=""

as_s_pic=0
crop_region=[]

coord=[350,200,50]

no_items=0

items_image=""
####################

conn=db.connect("stock.db")

try:
	conn.execute("""CREATE TABLE stock_data (stockid INT PRIMARY KEY NOT NULL,
			item_name VARCHAR NOT NULL, price INT NOT NULL, quantity INT NOT NULL, picture VARCHAR);""")
except:
	pass




root=Tk()

root.geometry(str(wd)+"x"+str(ht)+"+0+0")
root.resizable(0,0)


frame=Frame(root,width=wd,height=ht,bg="grey")
frame.pack()







main1=Canvas(frame,width=wd,height=50,relief="flat",highlightthickness=0,border=0,bg="#ffffff")
main1.pack(side=TOP)
main1.bind("<Button-1>",main1e)

#main1.create_rectangle(0,0,300,50,fill="#323232")
main1.create_oval(10,10, 40,40,fill="#ffffff",outline="#323232")
main1.create_line(10+7,25,40-7,25,fill="#323232",width=2)
main1.create_line(40-7,25, 40-7-7,25-7,fill="#323232",width=2)
main1.create_line(40-7,25, 40-7-7,25+7,fill="#323232",width=2)

main1.create_line(0,0,wd,0,fill="#323232")


fmain2=Frame(frame,width=wd,height=ht-50,bg="red")
fmain2.pack(side=TOP)

main2=Canvas(fmain2,width=wd,height=ht-50,bg="#ffffff",relief="flat",highlightthickness=0,border=0,
	scrollregion=(0,0,wd,ht-50))
main2.bind("<Button-1>",main2e)
main2.bind_all("<MouseWheel>",_on_mousewheel)

main2.create_rectangle(0,ht+100,50,ht+150,fill="red")


vbar1=Scrollbar(fmain2,orient=VERTICAL)
vbar1.pack(side=RIGHT,fill=Y)
vbar1.config(command=main2.yview)

main2.config(yscrollcommand=vbar1.set)

main2.pack(side=LEFT)

# end items

dashb=Canvas(width=300,height=ht,relief="flat",highlightthickness=0,border=0,bg="#323232")
dashb.place(in_=root,x=0,y=0)
dashb.bind("<Button-1>",db_commands)

dashb.create_oval(290-30,10, 290,40,fill="#323232",outline="#ffffff")
dashb.create_line(290-30+7,25,290-7,25,fill="#ffffff",width=2)
dashb.create_line(290-30+7,25, 290-30+7+7,25-7,fill="#ffffff",width=2)
dashb.create_line(290-30+7,25, 290-30+7+7,25+7,fill="#ffffff",width=2)


dashb.create_oval(10,5+50, 10+30,5+30+50, fill="#ffffff",outline="#ffffff")
dashb.create_oval(290-30,5+50, 290,5+30+50,fill="#ffffff",outline="#ffffff")
dashb.create_rectangle(10+15,5+50, 290-15,5+30+50,fill="#ffffff",outline="#ffffff")

dashb.create_text(150,70,fill="#323232",text="Items",font=("FreeMono",15),anchor="c")


dashb.create_oval(10,5+50+50, 10+30,5+30+50+50, fill="#ffffff",outline="#ffffff")
dashb.create_oval(290-30,5+50+50, 290,5+30+50+50,fill="#ffffff",outline="#ffffff")
dashb.create_rectangle(10+15,5+50+50, 290-15,5+30+50+50,fill="#ffffff",outline="#ffffff")

dashb.create_text(150,120,fill="#323232",text="Reports",font=("FreeMono",15),anchor="c")

dashb.create_oval(10,5+50+50*2, 10+30,5+50+30+50*2, fill="#ffffff",outline="#ffffff")
dashb.create_oval(290-30,5+50+50*2, 290,5+50+30+50*2,fill="#ffffff",outline="#ffffff")
dashb.create_rectangle(10+15,5+50+50*2, 290-15,5+50+30+50*2,fill="#ffffff",outline="#ffffff")

dashb.create_text(150,170,fill="#323232",text="Summary",font=("FreeMono",15),anchor="c")

dashb.create_oval(10,5+50+50*3, 10+30,5+50+30+50*3, fill="#ffffff",outline="#ffffff")
dashb.create_oval(290-30,5+50+50*3, 290,5+50+30+50*3,fill="#ffffff",outline="#ffffff")
dashb.create_rectangle(10+15,5+50+50*3, 290-15,5+50+30+50*3,fill="#ffffff",outline="#ffffff")

dashb.create_text(150,220,fill="#323232",text="Add Stock",font=("FreeMono",15),anchor="c")


intro=Canvas(width=wd,height=ht,relief="flat",highlightthickness=0,border=0,bg="grey")
intro.place(in_=root,x=0,y=0)
intro.bind("<Button-1>",login)

#intro.create_rectangle((wd/2)-180,150+50,(wd/2)+180,410+50, fill="#ffffff",outline="#ffffff")

intro.create_oval((wd/2)-180,200, (wd/2)-160,220, fill="#ffffff",outline="#ffffff")
intro.create_oval((wd/2)+160,200, (wd/2)+180,220, fill="#ffffff",outline="#ffffff")

intro.create_oval((wd/2)-180,440, (wd/2)-160,460, fill="#ffffff",outline="#ffffff")
intro.create_oval((wd/2)+160,440, (wd/2)+180,460, fill="#ffffff",outline="#ffffff")

intro.create_polygon((wd/2)-170,200, (wd/2)+170,200, (wd/2)+180,210, (wd/2)+180,450,
(wd/2)+170,460, (wd/2)-170,460, (wd/2)-180,450, (wd/2)-180,210, (wd/2)-170,200, fill="#ffffff",outline="#ffffff" )

intro.create_arc((wd/2)-180,200, (wd/2)-160,220, fill="#ffffff",outline="#323232",start=90,extent=90,style="arc",width=2)
intro.create_arc((wd/2)+160,200, (wd/2)+180,220, fill="#ffffff",outline="#323232",start=0,extent=90,style="arc",width=2)

intro.create_arc((wd/2)-180,440, (wd/2)-160,460, fill="#ffffff",outline="#323232",start=180,extent=90,style="arc",width=2)
intro.create_arc((wd/2)+160,440, (wd/2)+180,460, fill="#ffffff",outline="#323232",start=270,extent=90,style="arc",width=2)

intro.create_line((wd/2)-170,200, (wd/2)+170,200, fill="#323232",width=2)
intro.create_line((wd/2)-170,460, (wd/2)+170,460, fill="#323232",width=2)

intro.create_line((wd/2)-180,210, (wd/2)-180,450, fill="#323232",width=2)
intro.create_line((wd/2)+180,210, (wd/2)+180,450, fill="#323232",width=2)

intro.create_text((wd/2)-150,250,text="User Name",fill="#323232",font=("FreeMono",15),anchor="nw")

intro.create_text((wd/2)-150,310,text="Password",fill="#323232",font=("FreeMono",15),anchor="nw")


intro.create_rectangle((wd/2)-41,249,(wd/2)+149,275,fill="#323232",outline="#323232")
intro.create_rectangle((wd/2)-41,309,(wd/2)+149,335,fill="#323232",outline="#323232")



un_=Entry(width=17,font=("FreeMono",15),relief="flat",border=0,highlightthickness=0)
un_.place(in_=root,x=(wd/2)-40,y=250)
un_.bind("<Button-1>",cerr)
un_.bind("<Return>",j1)

pw_=Entry(width=17,font=("FreeMono",15),relief="flat",border=0,highlightthickness=0,show="*")
pw_.place(in_=root,x=(wd/2)-40,y=310)
pw_.bind("<Button-1>",cerr)
pw_.bind("<Return>",j2)

intro.create_rectangle((wd/2)-70,380,(wd/2)+70,410,fill="#323232",outline="#323232")

intro.create_oval((wd/2)-85,380, (wd/2)-55,410,fill="#323232",outline="#323232")
intro.create_oval((wd/2)+55,380, (wd/2)+85,410,fill="#323232",outline="#323232")



intro.create_text((wd/2),395,anchor="c",text="Login",font=("FreeMono",14),fill="#ffffff")
err=()


#

as_name=Entry(width=16,relief="flat",highlightthickness=0,border=0,bg="#ffffff",font=("FreeMono",15)
	,fg="#323232",insertbackground="#323232")

as_price=Entry(width=16,relief="flat",highlightthickness=0,border=0,bg="#ffffff",font=("FreeMono",15)
	,fg="#323232",insertbackground="#323232")

as_no=Spinbox(width=15,relief="flat",font=("FreeMono",15),highlightthickness=0,border=0,bg="#ffffff",
	from_=0,to=1000,fg="#323232",insertbackground="#323232",textvariable=0)


un_.focus_set()
move_dashb()

root.mainloop()