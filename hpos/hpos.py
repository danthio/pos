import tkinter as tk
from tkinter import font
from PIL import Image,ImageTk,ImageDraw
import math

import sqlite3 as database

import time

from tkinter import filedialog

import os

add_items_ims={}

add_items_coords={}

add_item_im=0



db_items=database.connect("data/items.db")
cur=db_items.cursor()


cur.execute("SELECT * FROM items")
rows=cur.fetchall()



for row in rows:
	print(row)


sell_items_ims={}

def main(con=0):

	global st,st_
	global can
	global add_items_ims
	global dashboard
	global name,bp,sp,qt,desc
	global delete,crop1,crop2,refresh
	global add_items_coords
	global add_item_im
	global sell_items_ims

	st_="main"

	f=font.Font(family="FreeMono",size=13)

	if st=="Sell Items":


		can["width"]=width
		can["height"]=height
		can["scrollregion"]=(0,0,width,height)
		can["bg"]="#ffffff"

		name.place_forget()
		bp.place_forget()
		sp.place_forget()
		qt.place_forget()
		desc.place_forget()


		can.delete("all")

		db_items=database.connect("data/items.db")
		cur=db_items.cursor()

		cur.execute("SELECT * FROM items")

		rows=cur.fetchall()


		x=int(dashboard.place_info()["x"])+int(dashboard["width"])

		x+=20

		y=30


		xx=150
		yy=200

		v=0

		for row in rows:

			x1,y1,x2,y2=x,y,x+xx,y+yy


			im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#ffffff",alpha=1,width=1)

			sell_items_ims[v]=ImageTk.PhotoImage(im)

			can.create_image(x1,y1,image=sell_items_ims[v],anchor="nw")

			

			x1_,y1_,x2_,y2_=x1+5,y1+15, x2-5,y2-25-25-25-25

			if not row[-1]=="":

				im=Image.open(f"data/images/{row[-1]}")
				_x,_y=im.size

				if _x/_y>(x2_-x1_)/(y2_-y1_):

					x_=(x2_-x1_)
					y_=x_*_y/_x

				elif _x/_y<(x2_-x1_)/(y2_-y1_):

					y_=(y2_-y1_)
					x_=y_*_x/_y

				else:

					y_=(x2_-x1_)
					x_=(y2_-y1_)

				x_=int(x_)
				y_=int(y_)

				im=im.resize((x_,y_))


				v+=1

				sell_items_ims[v]=ImageTk.PhotoImage(im)

				__x=((x2_-x1_)-x_)/2
				__y=((y2_-y1_)-y_)/2

				can.create_image(x1_+__x,y1_+__y,image=sell_items_ims[v],anchor="nw")
			else:
				can.create_text(x1_+(x2_-x1_)/2, y1_+(y2_-y1_)/2,text="No Image",font=("FreeMono",13),fill="#000000",anchor="c")

			can.create_rectangle(x1+5,y1+15, x2-5,y2-25-25-25-25,outline="#aaaaaa")





			can.create_text(x1+10,y2-25-25-25, text=f"{row[1]}",font=("FreeMono",13),fill="#ff0000",anchor="w")
			can.create_text(x1+10,y2-25-25, text=f"Ksh. {row[3]}",font=("FreeMono",13),fill="#000000",anchor="w")
			can.create_text(x1+10,y2-25, text=f"{row[4]} items left",font=("FreeMono",13),fill="#000000",anchor="w")


			v+=1



			x+=xx+20


	elif st=="Add Items":


		can["width"]=width
		can["height"]=height
		can["scrollregion"]=(0,0,width,height)
		can["bg"]="#ffffff"


		can.delete("all")

		v=0

		im=Image.new("RGBA",(width,height),(0,0,0,128))

		add_items_ims[v]=ImageTk.PhotoImage(im)

		can.create_image(0,0,image=add_items_ims[v],anchor="nw")


		xx,yy=700,410

		x=int(dashboard.place_info()["x"])+int(dashboard["width"])

		x=x+((width-x)-xx)/2
		y=40+((height-40)-yy)/2

		



		v+=1

		x1,y1,x2,y2=x,y, x+xx,y+yy

		im=draw_round_rect(15,x1,y1,x2,y2, "#ffffff","#ffffff",alpha=1,width=1)
		add_items_ims[v]=ImageTk.PhotoImage(im)
		can.create_image(x,y,image=add_items_ims[v],anchor="nw")




		if con==0:

			name.delete(0,tk.END)
			bp.delete(0,tk.END)
			sp.delete(0,tk.END)	
			qt.delete(0,tk.END)	
			desc.delete(0.0,tk.END)	



		

		can.create_text(x+10+10,y+20+15, text="Item Name",font=("FreeMono",13), anchor="w",fill="#000000")

		v+=1

		x1,y1,x2,y2=x+150-5-20+10,y+20+15-10-5,x+150-5+100+60+6-20+10,y+20+15-10-5+25+6

		im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
		add_items_ims[v]=ImageTk.PhotoImage(im)
		can.create_image(x1,y1,image=add_items_ims[v],anchor="nw")

		name.place(in_=root,x=x+150-20+10,y=y+20+15-10)

		add_items_coords["item name"]=[x1,y1,x2,y2]

		

		can.create_text(x+10+10,y+20+15+50, text="Buying Price",font=("FreeMono",13), anchor="w",fill="#000000")

		v+=1

		x1,y1,x2,y2=x+150-5-20+10,y+20+15-10-5+50,x+150-5+100+60+6-20+10,y+20+15-10-5+25+6+50

		im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
		add_items_ims[v]=ImageTk.PhotoImage(im)
		can.create_image(x1,y1,image=add_items_ims[v],anchor="nw")

		bp.place(in_=root,x=x+150-20+10,y=y+20+15-10+50)


		add_items_coords["bp"]=[x1,y1,x2,y2]

		can.create_text(x+10+10,y+20+15+50*2, text="Selling Price",font=("FreeMono",13), anchor="w",fill="#000000")

		v+=1

		x1,y1,x2,y2=x+150-5-20+10,y+20+15-10-5+50*2,x+150-5+100+60+6-20+10,y+20+15-10-5+25+6+50*2

		im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
		add_items_ims[v]=ImageTk.PhotoImage(im)
		can.create_image(x1,y1,image=add_items_ims[v],anchor="nw")

		sp.place(in_=root,x=x+150-20+10,y=y+20+15-10+50*2)
	

		add_items_coords["sp"]=[x1,y1,x2,y2]	


		can.create_text(x+10+10,y+20+15+50*3, text="Quantity",font=("FreeMono",13), anchor="w",fill="#000000")

		v+=1

		x1,y1,x2,y2=x+150-5-20+10,y+20+15-10-5+50*3,x+150-5+100+60+6-20+10,y+20+15-10-5+25+6+50*3

		im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
		add_items_ims[v]=ImageTk.PhotoImage(im)
		can.create_image(x1,y1,image=add_items_ims[v],anchor="nw")

		qt.place(in_=root,x=x+150-20+10,y=y+20+15-10+50*3)

		add_items_coords["q"]=[x1,y1,x2,y2]



		v+=1

		x1,y1,x2,y2=x+10+10,y+20+15-10-5+50*4+10,x+150-5+100+60+6-20+10,y+20+15-10-5++50*4+10+100

		im=draw_round_rect(10,x1,y1,x2,y2, "#000000",alpha=1,width=1)
		draw=ImageDraw.Draw(im)

		draw.rectangle((10,-5, 10+5+f.measure("Description")+5,5),fill=(0,0,0,0),outline=(0,0,0,0))

		add_items_ims[v]=ImageTk.PhotoImage(im)
		can.create_image(x1,y1,image=add_items_ims[v],anchor="nw")

		can.create_text(x1+10+5,y1, text="Description",font=("FreeMono",13),fill="#000000", anchor="w")

		add_items_coords["desc"]=[x1,y1,x2,y2]

		desc.place(in_=root,x=x1+15,y=y1+15,)


		v+=1

		x1,y1,x2,y2=x+150-5+100+60+6-20+10+20,y+20+15-10-5,x+xx-20,y2

		im=draw_round_rect(15,x1,y1,x2,y2, "#000000",alpha=1,width=1)
		add_items_ims[v]=ImageTk.PhotoImage(im)
		can.create_image(x1,y1,image=add_items_ims[v],anchor="nw")


		can.create_rectangle(x1+15,y1+15, x2-15,y2-15,outline="#aaaaaa")

		add_items_coords["imagep"]=[x1+15,y1+15, x2-15,y2-15]






		can.create_image(x2-25,y2+5,image=delete,anchor="nw")
		add_items_coords["delete"]=[x2-25,y2+5]
		can.create_image(x2-25-10-25,y2+5,image=crop2,anchor="nw")
		add_items_coords["crop"]=[x2-25-10-25,y2+5]
		can.create_image(x2-25-10-25-10-25,y2+5,image=refresh,anchor="nw")
		add_items_coords["refresh"]=[x2-25-10-25-10-25,y2+5]

		#print((y2+5+25+10+30+10)-y,"h")

		



		if con==0:
			add_items_ims["image"]=0


		if not add_items_ims["image"]==0:

			process_add_item_im(add_items_ims["image"])

			add_items_coords["add_image"]=None

		else:


			v+=1

			cx,cy=x1+(x2-x1)/2,y1+(y2-y1)/2

			x1,y1,x2,y2=cx-40,cy-40, cx+40,cy+40,

			im=draw_round_rect(40,x1,y1,x2,y2, "#000000",alpha=1,width=1)
			add_items_ims[v]=ImageTk.PhotoImage(im)
			can.create_image(x1,y1,image=add_items_ims[v],anchor="nw")

			can.create_line(cx-20,cy, cx+20,cy,fill="#000000")
			can.create_line(cx,cy-20, cx,cy+20,fill="#000000")

			can.create_text(cx,cy+40+20,text="Add Image", font=("FreeMono",13),fill="#000000",anchor="c")

			add_items_coords["add_image"]=[cx,cy]




		v+=1

		x1,y1,x2,y2=x+xx/2-80,y+yy-10-30, x+xx/2+80,y+yy-10

		im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#000000",alpha=1,width=1)
		add_items_ims[v]=ImageTk.PhotoImage(im)
		can.create_image(x1,y1,image=add_items_ims[v],anchor="nw")

		can.create_text(x+xx/2, y+yy-10-15, text="Save", font=("FreeMono",13),fill="#ffffff",anchor="c")

		add_items_coords["save"]=[x1,y1,x2,y2]

		name.focus_set()



def process_add_item_im(im):
	global add_items_coords
	global add_items_ims
	global add_item_im

	_x,_y=im.size

	x1,y1,x2,y2=add_items_coords["imagep"]

	if _x/_y>(x2-x1)/(y2-y1):

		x_=x2-x1
		y_=x_*_y/_x

	elif _x/_y<(x2-x1)/(y2-y1):
		y_=(y2-y1)
		x_=y_*_x/_y


	else:
		y_=(y2-y1)
		x_=(x2-x1)

	x_=int(x_)
	y_=int(y_)

	im=im.resize((x_,y_))

	add_items_ims["image_"]=ImageTk.PhotoImage(im)

	can.delete(add_item_im)

	__x=((x2-x1)-x_)/2
	__y=((y2-y1)-y_)/2

	add_item_im=can.create_image(x1+__x,y1+__y,image=add_items_ims["image_"],anchor="nw")




def hex_to_rgb(col):

	col=col.replace("#","")

	r=col[:2]
	g=col[2:4]
	b=col[4:6]


	return (int(r,16),int(g,16),int(b,16))

db=0
sell_items_im,reports_im,manage_items_im,add_items_im,profiles_im=0,0,0,0,0
sell_items_im2,reports_im2,manage_items_im2,add_items_im2,profiles_im2=0,0,0,0,0
log_out_im=0

show_p,dshow_p=0,0

delete=0
crop1,crop2=0,0
refresh=0


def load_im():
	global db
	global sell_items_im,reports_im,manage_items_im,add_items_im,profiles_im
	global sell_items_im2,reports_im2,manage_items_im2,add_items_im2,profiles_im2
	global log_out_im
	global show_p,dshow_p
	global delete
	global crop1,crop2
	global refresh


	#db

	im=Image.open("data/icons/db.png")
	im=im.resize((25,25))
	db=ImageTk.PhotoImage(im)


	#sell items


	im=Image.open("data/icons/sell_items.png")
	im=im.resize((25,25))
	sell_items_im=ImageTk.PhotoImage(im)


	im=Image.open("data/icons/sell_items2.png")
	im=im.resize((25,25))
	sell_items_im2=ImageTk.PhotoImage(im)


	#reports


	im=Image.open("data/icons/reports.png")
	im=im.resize((25,25))
	reports_im=ImageTk.PhotoImage(im)


	im=Image.open("data/icons/reports2.png")
	im=im.resize((25,25))
	reports_im2=ImageTk.PhotoImage(im)

	#add items


	im=Image.open("data/icons/add_items.png")
	im=im.resize((25,25))
	add_items_im=ImageTk.PhotoImage(im)


	im=Image.open("data/icons/add_items2.png")
	im=im.resize((25,25))
	add_items_im2=ImageTk.PhotoImage(im)


	#manage items


	im=Image.open("data/icons/manage_items.png")
	im=im.resize((25,25))
	manage_items_im=ImageTk.PhotoImage(im)


	im=Image.open("data/icons/manage_items2.png")
	im=im.resize((25,25))
	manage_items_im2=ImageTk.PhotoImage(im)


	#profile


	im=Image.open("data/icons/profiles.png")
	im=im.resize((25,25))
	profiles_im=ImageTk.PhotoImage(im)


	im=Image.open("data/icons/profiles2.png")
	im=im.resize((25,25))
	profiles_im2=ImageTk.PhotoImage(im)

	#log out


	im=Image.open("data/icons/log_out.png")
	im=im.resize((25,25))
	log_out_im=ImageTk.PhotoImage(im)

	# show password

	im=Image.open("data/icons/show.png")
	show_p=ImageTk.PhotoImage(im)

	# don't show password

	im=Image.open("data/icons/dshow.png")
	dshow_p=ImageTk.PhotoImage(im)


	#delete

	im=Image.open("data/icons/delete.png")
	im=im.resize((25,25))
	delete=ImageTk.PhotoImage(im)


	#crop1

	im=Image.open("data/icons/crop.png")
	im=im.resize((25,25))
	crop1=ImageTk.PhotoImage(im)

	#crop2

	im=Image.open("data/icons/crop2.png")
	im=im.resize((25,25))
	crop2=ImageTk.PhotoImage(im)


	#refresh

	im=Image.open("data/icons/refresh.png")
	im=im.resize((25,25))
	refresh=ImageTk.PhotoImage(im)



db_items=[]
def draw_db():
	global dashboard
	global db
	global sell_items_im,reports_im,manage_items_im,add_items_im,profiles_im
	global sell_items_im2,reports_im2,manage_items_im2,add_items_im2,profiles_im2
	global log_out_im
	global width,height
	global st
	global db_items

	dashboard.delete("all")

	db_items=[]


	dashboard.create_image(int(dashboard["width"])-5-25,5,image=db,anchor="nw")



	items=[["Sell Items",sell_items_im,sell_items_im2],["Reports",reports_im,reports_im2],["Manage items",manage_items_im,manage_items_im2],
			["Add Items",add_items_im,add_items_im2],["Profiles", profiles_im,profiles_im2]]


	y=5+25+20


	for i in items:

		if st==i[0]:

			dashboard.create_rectangle(0,y, int(dashboard["width"]),y+40, fill="#ffffff",outline="#ffffff")

			dashboard.create_text(10,y+20,text=i[0],font=("FreeMono",13),fill="#000000",anchor="w")

			dashboard.create_image(int(dashboard["width"])-5-25,y+7.5, image=i[2],anchor="nw")
 
		else:


			dashboard.create_text(10,y+20,text=i[0],font=("FreeMono",13),fill="#ffffff",anchor="w")

			dashboard.create_image(int(dashboard["width"])-5-25,y+7.5, image=i[1],anchor="nw")

		db_items.append([i[0],y])

		y+=40



	dashboard.create_text(10,height-20,text="Log Out", font=("FreeMono",13),fill="#ffffff",anchor="w")
	dashboard.create_image(int(dashboard["width"])-5-25,height-40+7.5, image=log_out_im,anchor="nw")



def draw_round_rect(r,x1,y1,x2,y2, col1,col2=None,alpha=1,width=1):

    w,h=int(round(abs(x2-x1),0)),int(round(abs(y2-y1),0))
    w_=w*4
    h_=int(round(w_*h/w,0))



    im=Image.new("RGBA",(w_,h_),(0,0,0,0))
    draw=ImageDraw.Draw(im)


    ar=[]

    r*=4

    cx,cy=r,r
    a_=180

    for a in range(90):

        x=int(round(r*math.sin(math.radians(a_))+cx,0))
        y=int(round(r*math.cos(math.radians(a_))+cy,0))

        ar.append((x,y))

        a_+=1



    cx,cy=r,h_-r-1
    a_=270

    for a in range(90):

        x=int(round(r*math.sin(math.radians(a_))+cx,0))
        y=int(round(r*math.cos(math.radians(a_))+cy,0))

        ar.append((x,y))

        a_+=1

    cx,cy=w_-r-1,h_-r-1
    a_=0

    for a in range(90):

        x=int(round(r*math.sin(math.radians(a_))+cx,0))
        y=int(round(r*math.cos(math.radians(a_))+cy,0))

        ar.append((x,y))

        a_+=1



    cx,cy=w_-r-1,r
    a_=90

    for a in range(90):

        x=int(round(r*math.sin(math.radians(a_))+cx,0))
        y=int(round(r*math.cos(math.radians(a_))+cy,0))

        ar.append((x,y))

        a_+=1



    if col2==None:
        draw.polygon(ar,outline=col1,width=int((round(4*width,0))))

    else:

        draw.polygon(ar,fill=(*hex_to_rgb(col2),int(round(255*alpha,0))),outline=col1,width=int((round(4*width,0))))




    im=im.resize((w,h))

    return im


login_im1=0
login_im2=0
login_im3=0
login_im4=0

un_login_coord=[]
pw1_login_coord=[]

login_coord=[]
register_coord=[]



st_=None
_show_=0

def login():
	global can
	global width,height
	global login_im1,login_im2,login_im3,login_im4
	global un,pw1,pw2
	global un_login_coord,pw1_login_coord
	global login_coord,register_coord
	global st_
	global show_p,dshow_p
	global _show_


	can.delete("all")
	un.delete(0,tk.END)
	pw1.delete(0,tk.END)
	pw2.delete(0,tk.END)


	pw1["show"]="*"

	pw2.place_forget()

	st_="login"




	can["width"]=width
	can["height"]=height
	can["scrollregion"]=(0,0,width,height)
	can["bg"]="#000000"


	xx,yy=350,200


	x=(width-xx)/2
	y=(height-yy)/2


	x1,y1,x2,y2=x,y,x+xx,y+yy


	im=draw_round_rect(15,x1,y1,x2,y2, "#ffffff",col2="#ffffff",alpha=1,width=1)
	login_im1=ImageTk.PhotoImage(im)
	can.create_image(x,y,image=login_im1,anchor="nw")

	
	#user name

	can.create_text(x+30+4.5,y+20+15, text="User Name",font=("FreeMono",13), anchor="w",fill="#000000")



	x1,y1,x2,y2=x+150-5+4.5,y+20+15-10-5,x+150-5+100+60+6+4.5,y+20+15-10-5+25+6

	im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	login_im2=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=login_im2,anchor="nw")

	un.place(in_=root,x=x+150+4.5,y=y+20+15-10)


	un_login_coord=[x1,y1,x2,y2]



	#password



	can.create_text(x+30+4.5,y+20+15+50, text="Password",font=("FreeMono",13), anchor="w",fill="#000000")



	x1,y1,x2,y2=x+150-5+4.5,y+20+15-10-5+50,x+150-5+100+60+6+4.5,y+20+15-10-5+25+6+50

	im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	login_im3=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=login_im3,anchor="nw")


	if pw1["show"]=="*":

		_show_=can.create_image(x2+(34.5-29)/2,y1+((y2-y1)-29)/2,image=show_p,anchor="nw")

	else:

		_show_=can.create_image(x2+(34.5-29)/2,y1+((y2-y1)-29)/2,image=dshow_p,anchor="nw")





	pw1.place(in_=root,x=x+150+4.5,y=y+20+15-10+50)


	pw1_login_coord=[x1,y1,x2,y2]


	#print(30-(xx-(x2-(x+30)))/2)

	#buttons


	x1,y1,x2,y2=x+1,y+yy-30,x+xx-1,y+yy-1

	im=draw_round_rect(15,x1,y1,x2,y2, "#000000",col2="#000000",alpha=1,width=1)
	login_im4=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=login_im4,anchor="nw")

	can.create_line(x+xx/2,y+yy-31, x+xx/2,y+yy, fill="#ffffff")


	_x=xx/4

	can.create_text(x+_x,y+yy-15,text="Login",font=("FreeMono",13),fill="#ffffff",anchor="c")
	can.create_text(x+xx-_x,y+yy-15,text="Register",font=("FreeMono",13),fill="#ffffff",anchor="c")

	login_coord=[x1,y1,x1+xx/2,y2]

	register_coord=[x1+xx/2,y1,x2,y2]


	un.focus_set()


cancel_coord=[]
confirm_coord=[]


login_im5=0

pw2_login_coord=[]
def draw_registration():

	global can
	global width,height
	global login_im1,login_im2,login_im3,login_im4,login_im5
	global un,pw1,pw2
	global un_login_coord,pw1_login_coord,pw2_login_coord
	global cancel_coord,confirm_coord
	global st_
	global _show_,show_p,dshow_p


	can.delete("all")
	un.delete(0,tk.END)
	pw1.delete(0,tk.END)
	pw2.delete(0,tk.END)

	pw1["show"]="*"
	pw2["show"]="*"


	st_="register"




	can["width"]=width
	can["height"]=height
	can["scrollregion"]=(0,0,width,height)
	can["bg"]="#000000"


	xx,yy=350,250


	x=(width-xx)/2
	y=(height-yy)/2


	x1,y1,x2,y2=x,y,x+xx,y+yy


	im=draw_round_rect(15,x1,y1,x2,y2, "#ffffff",col2="#ffffff",alpha=1,width=1)
	login_im1=ImageTk.PhotoImage(im)
	can.create_image(x,y,image=login_im1,anchor="nw")

	
	#user name

	can.create_text(x+30+4.5,y+20+15, text="User Name",font=("FreeMono",13), anchor="w",fill="#000000")



	x1,y1,x2,y2=x+150-5+4.5,y+20+15-10-5,x+150-5+100+60+6+4.5,y+20+15-10-5+25+6

	im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	login_im2=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=login_im2,anchor="nw")

	un.place(in_=root,x=x+150+4.5,y=y+20+15-10)


	un_login_coord=[x1,y1,x2,y2]



	#password



	can.create_text(x+30+4.5,y+20+15+50, text="Password",font=("FreeMono",13), anchor="w",fill="#000000")



	x1,y1,x2,y2=x+150-5+4.5,y+20+15-10-5+50,x+150-5+100+60+6+4.5,y+20+15-10-5+25+6+50

	im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	login_im3=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=login_im3,anchor="nw")


	if pw1["show"]=="*":

		_show_=can.create_image(x2+(34.5-29)/2,y1+((y2-y1)-29)/2,image=show_p,anchor="nw")

	else:

		_show_=can.create_image(x2+(34.5-29)/2,y1+((y2-y1)-29)/2,image=dshow_p,anchor="nw")




	pw1.place(in_=root,x=x+150+4.5,y=y+20+15-10+50)


	pw1_login_coord=[x1,y1,x2,y2]


	#password2



	can.create_text(x+30+4.5,y+20+15+50+50, text="Password",font=("FreeMono",13), anchor="w",fill="#000000")



	x1,y1,x2,y2=x+150-5+4.5,y+20+15-10-5+50+50,x+150-5+100+60+6+4.5,y+20+15-10-5+25+6+50+50

	im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	login_im5=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=login_im5,anchor="nw")

	pw2.place(in_=root,x=x+150+4.5,y=y+20+15-10+50+50)


	pw2_login_coord=[x1,y1,x2,y2]





	#print(30-(xx-(x2-(x+30)))/2)

	#buttons


	x1,y1,x2,y2=x+1,y+yy-30,x+xx-1,y+yy-1

	im=draw_round_rect(15,x1,y1,x2,y2, "#000000",col2="#000000",alpha=1,width=1)
	login_im4=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=login_im4,anchor="nw")

	can.create_line(x+xx/2,y+yy-31, x+xx/2,y+yy, fill="#ffffff")


	_x=xx/4

	can.create_text(x+_x,y+yy-15,text="Cancel",font=("FreeMono",13),fill="#ffffff",anchor="c")
	can.create_text(x+xx-_x,y+yy-15,text="Confirm",font=("FreeMono",13),fill="#ffffff",anchor="c")

	cancel_coord=[x1,y1,x1+xx/2,y2]

	confirm_coord=[x1+xx/2,y1,x2,y2]


	un.focus_set()


def valdate_login():
	global can,dashboard
	global width,height
	global un,pw1,pw2


	xx,yy=350,200


	x=(width-xx)/2
	y=(height-yy)/2


	if un.get()=="" or pw1.get()=="":

		message(0,can,"Fill all fields!",x+xx/2,y+yy+10+15,xx,30)

		return


	db_user=database.connect("data/users.db")
	cur=db_user.cursor()
	cur.execute("SELECT * FROM users;")
	rows=cur.fetchall()


	con=0
	for row in rows:

		if row[1]==un.get() and row[5]==pw1.get():
			con=1

	

	if con==0:

		message(0,can,"Invalid Entry!",x+xx/2,y+yy+10+15,xx,30)

		return





	un.place_forget()
	pw1.place_forget()
	pw2.place_forget()

	can.delete("all")
	
	can["width"]=width
	can["height"]=width
	can["scrollregion"]=(0,0,width,height)
	can["bg"]="#ffffff"


	dashboard.place(in_=root,x=0,y=0)

	draw_db()

	main()

def validate_registration():
	global width,height
	global can
	global un,pw1,pw2

	xx,yy=350,250


	x=(width-xx)/2
	y=(height-yy)/2


	if un.get()=="" or pw1.get()=="" or pw2.get()=="":

		message(0,can,"Fill all fields!",x+xx/2,y+yy+10+15,xx,30)

		return

	if pw1.get()!=pw2.get():

		message(0,can,"Password doesn't match!",x+xx/2,y+yy+10+15,xx,30)

		return


	db_user=database.connect("data/users.db")
	cur=db_user.cursor()

	v=0

	cur.execute("SELECT * FROM users")
	rows=cur.fetchall()


	ids=[]


	for row in rows:
		if row[1].lower() == un.get().lower():

			message(0,can,"User name exists!",x+xx/2,y+yy+10+15,xx,30)

			return


		ids.append(row[0])

	if ids==[]:
		v=1
	else:

		max_id=max(ids)

		v=1
		for _ in range(max_id):

			try:
				v_=ids.index(v)
				v+=1
			except:
				break



			






	cur.execute("INSERT INTO users VALUES("+str(v)+",'"+un.get()+"','""','""',"+str(0)+",'"+str(pw1.get())+"',"+str(0)+")")

	db_user.commit()

	login()


	xx,yy=350,200


	x=(width-xx)/2
	y=(height-yy)/2

	message(1,can,"Accont Created!",x+xx/2,y+yy+10+15,xx,30)



def check_message():
	global mess_v
	global mess_con

	if mess_con==True:

		if time.time()-mess_v[4]>=3:

			mess_v[3].delete(mess_v[1])
			mess_v[3].delete(mess_v[2])

			mess_v=[0,0,0,0,0]

			mess_con=False

	root.after(1,check_message)

mess_v=[0,0,0,0,0]
mess_con=False
def message(con,_can_,mess,cx,cy,w,h):
	global mess_im
	global mess_con


	if con==0:
		col="#ff0000"
	elif con==1:
		col="#00ff00"


	x1,y1,x2,y2=cx-w/2,cy-h/2, cx+w/2,cy+h/2



	im=draw_round_rect(15,x1,y1,x2,y2, col,col2=col,alpha=1,width=1)
	mess_v[0]=ImageTk.PhotoImage(im)
	mess_v[1]=_can_.create_image(cx,cy,image=mess_v[0],anchor="c")
	mess_v[2]=_can_.create_text(cx,cy,text=mess,font=("FreeMono",13),fill="#000000")

	mess_v[3]=_can_
	mess_v[4]=time.time()

	mess_con=True


root=tk.Tk()


width,height=root.winfo_screenwidth()-80,root.winfo_screenheight()-100

root.geometry(f"{width}x{height}+0+0")


def can_b1(e):
	global can,dashboard
	global un_login_coord,	pw1_login_coord
	global un,pw1,pw2
	global login_coord,register_coord
	global cancel_coord,confirm_coord
	global st_
	global _show_,show_p,dshow_p
	global add_items_coords,add_items_ims,add_item_im
	global name,bp,sp,qt,desc
	


	if st_=="login":

		x,y=can.coords(_show_)

		if x<=e.x<=x+29:
			if y<=e.y<=y+29:

				if pw1["show"]=="*":
					pw1["show"]=""
					can.itemconfig(_show_,image=dshow_p)
				else:
					pw1["show"]="*"
					can.itemconfig(_show_,image=show_p)


				return


		x1,y1,x2,y2=un_login_coord

		if x1<=e.x<=x2:
			if y1<=e.y<=y2:

				un.focus_set()

				return


		x1,y1,x2,y2=pw1_login_coord

		if x1<=e.x<=x2:
			if y1<=e.y<=y2:

				pw1.focus_set()

				return



		#login b

		x1,y1,x2,y2=login_coord

		cx,cy=x1+15,y1+15
		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:

			valdate_login()

		if x1+15<=e.x<=x2:
			if y1<=e.y<=y2:

				valdate_login()



		#register b

		x1,y1,x2,y2=register_coord

		cx,cy=x2-15,y1+15
		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:

			draw_registration()

		if x1<=e.x<=x2-15:
			if y1<=e.y<=y2:

				draw_registration()


	elif st_=="register":



		x,y=can.coords(_show_)

		if x<=e.x<=x+29:
			if y<=e.y<=y+29:

				if pw1["show"]=="*":
					pw1["show"]=""
					pw2["show"]=""
					can.itemconfig(_show_,image=dshow_p)
				else:
					pw1["show"]="*"
					pw2["show"]="*"
					can.itemconfig(_show_,image=show_p)


				return



		x1,y1,x2,y2=un_login_coord

		if x1<=e.x<=x2:
			if y1<=e.y<=y2:

				un.focus_set()

				return


		x1,y1,x2,y2=pw1_login_coord

		if x1<=e.x<=x2:
			if y1<=e.y<=y2:

				pw1.focus_set()

				return




		x1,y1,x2,y2=pw2_login_coord

		if x1<=e.x<=x2:
			if y1<=e.y<=y2:

				pw2.focus_set()

				return









		#cancel b

		x1,y1,x2,y2=cancel_coord

		cx,cy=x1+15,y1+15
		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:

			login()

		if x1+15<=e.x<=x2:
			if y1<=e.y<=y2:

				login()



		#confirm b

		x1,y1,x2,y2=confirm_coord

		cx,cy=x2-15,y1+15
		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:

			validate_registration()

		if x1<=e.x<=x2-15:
			if y1<=e.y<=y2:

				validate_registration()

	elif st_=="main":


		if st=="Add Items":

			xx,yy=700,410

			if int(dashboard.place_info()["x"])==0:

				x=int(dashboard["width"])

			else:
				x=5+25+5

			x=x+((width-x)-xx)/2
			y=40+((height-40)-yy)/2

			x1,y1,x2,y2=add_items_coords["item name"]

			if x1<=e.x<=x2:
				if y1<=e.y<=y2:
					name.focus_set()
					return

			x1,y1,x2,y2=add_items_coords["bp"]

			if x1<=e.x<=x2:
				if y1<=e.y<=y2:
					bp.focus_set()
					return


			x1,y1,x2,y2=add_items_coords["sp"]

			if x1<=e.x<=x2:
				if y1<=e.y<=y2:
					sp.focus_set()
					return

			x1,y1,x2,y2=add_items_coords["q"]

			if x1<=e.x<=x2:
				if y1<=e.y<=y2:
					qt.focus_set()
					return

			x1,y1,x2,y2=add_items_coords["desc"]

			if x1<=e.x<=x2:
				if y1<=e.y<=y2:
					desc.focus_set()
					return

			if not add_items_coords["add_image"]==None:


				cx,cy=add_items_coords["add_image"]

				r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

				if r<=40:

					file=filedialog.askopenfilename()
					





					try:
						im=Image.open(file)

						add_items_ims["image"]=im

						main(1)


					except Exception as e:
						print(e)
						message(0,can,"Can't process image!",x+xx/2,y+yy+10+15,350,30)

					return


			x1,y1=add_items_coords["delete"]

			if x1<=e.x<=x1+25:
				if y1<=e.y<=y1+25:

					add_items_ims["image"]=0


					main(1)

					return


			x1,y1,x2,y2=add_items_coords["save"]

			cx,cy=x1+15,y1+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:

				add_new_item()
				return

			cx,cy=x2-15,y1+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:

				add_new_item()
				return

			if x1+15<=e.x<=x2-15:
				if y1<=e.y<=y2:
					add_new_item()
					return






			

def add_new_item():
	global can,dashboard
	global name,bp,sp,qt,desc
	global add_items_ims



	xx,yy=700,410

	if int(dashboard.place_info()["x"])==0:

		x=int(dashboard["width"])

	else:
		x=5+25+5

	x=x+((width-x)-xx)/2
	y=40+((height-40)-yy)/2

	

	if name.get()=="" or bp.get()=="" or sp.get()=="" or qt.get()=="":

		message(0,can,"Fill essential fields!",x+xx/2,y+yy+10+15,350,30)

		return

	try:
		bp_=int(bp.get())
	except:
		message(0,can,"Some fields must be a number!",x+xx/2,y+yy+10+15,350,30)
		return


	try:
		sp_=int(sp.get())
	except:
		message(0,can,"Some fields must be a number!",x+xx/2,y+yy+10+15,350,30)
		return

	try:
		q_=int(qt.get())
	except:
		message(0,can,"Some fields must be a number!",x+xx/2,y+yy+10+15,350,30)
		return



	db_items=database.connect("data/items.db")
	cur=db_items.cursor()

	v=0

	cur.execute("SELECT * FROM items")
	rows=cur.fetchall()

	#print(rows)


	ids=[]


	for row in rows:

		ids.append(row[0])


	if ids==[]:
		v=1
	else:

		max_id=max(ids)

		v=1
		for _ in range(max_id):

			try:
				v_=ids.index(v)
				v+=1
			except:
				break






	item_id=v
	name_=name.get()
	bp_=int(bp.get())
	sp_=int(sp.get())
	qt_=int(qt.get())
	desc_=desc.get("1.0",tk.END)[:-1]


	if add_items_ims["image"]!=0:

		image=f"{item_id}.png"

	else:
		image=""





	cur.execute("INSERT INTO items VALUES("+str(item_id)+",'"+str(name_)+"',"+str(bp_)+","+str(sp_)+","+str(qt_)+",'"+str(desc_)+"','"+str(image)+"')")

	db_items.commit()


	if add_items_ims["image"]!=0:

		os.makedirs("data/images",exist_ok=True)

		add_items_ims["image"].save(f"data/images/{item_id}.png")

	main()

	message(1,can,"Item added successfullly!",x+xx/2,y+yy+10+15,350,30)



can=tk.Canvas(width=width,height=height,relief="flat",bg="#ffffff",highlightthickness=0,border=0)
can.place(in_=root,x=0,y=0)

can.bind("<Button-1>",can_b1)

can["scrollregion"]=(0,0,width,height)


db_st=0
def dashboard_b1(e):
	global dashboard
	global db_st
	global db_items
	global st

	if int(dashboard["width"])-5-25<=e.x<=int(dashboard["width"])-5:
		if 5<=e.y<=5+25:

			if int(dashboard.place_info()["x"])<0:

				db_st=1

			else:
				db_st=2

			return


	#select db

	for i in db_items:

		if i[1]<=e.y<=i[1]+50:

			st=i[0]

			main()

			draw_db()

			return


	if height-40<=e.y<=height:


		dashboard.place_forget()

		login()

def move_db():
	global dashboard
	global db_st


	if not db_st==0:



		x=int(dashboard.place_info()["x"])


		if db_st==1:

			if x==0:

				db_st=0

				main(1)

			else:

				x+=1

				dashboard.place(in_=root,x=x,y=0)








		elif db_st==2:



			if x==-int(dashboard["width"])+5+25+5:

				db_st=0
				main(1)
			else:

				x-=1


				dashboard.place(in_=root,x=x,y=0)





	root.after(1,move_db)


dashboard=tk.Canvas(width=200,height=height,relief="flat",bg="#000000",highlightthickness=0,border=0)
dashboard.bind("<Button-1>",dashboard_b1)

dashboard.place(in_=root,x=0,y=0)

def un_r(e):
	global pw1

	pw1.focus_set()


def pw1_r(e):
	global st_
	global pw2

	if st_=="login":
		valdate_login()
	elif st_=="register":

		pw2.focus_set()

def pw2_r(e):
	global st_
	global pw2

	if st_=="register":

		validate_registration()



un=tk.Entry(width=17, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,selectbackground="#000000",selectforeground="#ffffff")
un.bind("<Return>",un_r)

pw1=tk.Entry(width=17, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,show="*",selectbackground="#000000",selectforeground="#ffffff")
pw1.bind("<Return>",pw1_r)

pw2=tk.Entry(width=17, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,show="*",selectbackground="#000000",selectforeground="#ffffff")
pw2.bind("<Return>",pw2_r)


name=tk.Entry(width=17, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,selectbackground="#000000",selectforeground="#ffffff")
bp=tk.Entry(width=17, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,selectbackground="#000000",selectforeground="#ffffff")
sp=tk.Entry(width=17, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,selectbackground="#000000",selectforeground="#ffffff")
qt=tk.Entry(width=17, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,selectbackground="#000000",selectforeground="#ffffff")

desc=tk.Text(width=28,height=4, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,selectbackground="#000000",selectforeground="#ffffff")


load_im()


#draw_db()

move_db()


login()


check_message()

try:
	dbuser=database.connect('data/users.db')
	cur=dbuser.cursor()	
	cur.execute("""CREATE TABLE users(
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


try:
	dbuser=database.connect('data/items.db')
	cur=dbuser.cursor()	
	cur.execute("""CREATE TABLE items(
		item_id INT,
		name VARCHAR(255),
		bp INT,
		sp INT,
		quantity INT,
		description VARCHAR(255), 
		image VARCHAR(255));""")

	dbuser.close()
except:
	pass



st="Sell Items"



root.mainloop()