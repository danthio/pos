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

#+254769167904

"""

db_items=database.connect("data/items.db")
cur=db_items.cursor()


cur.execute("SELECT * FROM items")
rows=cur.fetchall()



for row in rows:
	print(row)

"""


def check_root_sz():
	global width,height
	global cur_sz
	global st_


	sz=root.geometry().split("+")[0].split("x")
	w,h=int(sz[0]),int(sz[1])

	if not cur_sz==[w,h]:

		width,height=w,h

		if st_=="main":

			print("ok")
			draw_db()
			main(1)

		elif st_=="login":
			login(1)
		elif st_=="register":
			draw_registration(1)

		cur_sz=[w,h]


	root.after(1,check_root_sz)


def forget_widgets(except_=None):
	global t_widgets

	entries=t_widgets["entries"]

	for e in entries:

		e.place_forget()

	text=t_widgets["text"]

	for t in text:

		t.place_forget()

	canvas=t_widgets["canvas"]

	for c in canvas:

		if c==except_:
			continue

		c.place_forget()


def delete_widgets():
	global t_widgets

	entries=t_widgets["entries"]

	for e in entries:

		e.delete(0,tk.END)


	text=t_widgets["text"]

	for t in text:

		t.delete(0.0, tk.END)


def entries_show_reset():
	global t_widgets

	entries=t_widgets["entries"]

	for e in entries:

		e["show"]=""


sel_item_ent_d=[]
def check_sel_item():
	global can
	global st_,sel_item
	global sel_err1,sel_err2
	global sel_total
	global sel_item_ent_d
	global ent1,ent2

	if sel_item!=None and st_=="main":

		data=[ent1.get(),ent2.get()]

		if sel_item_ent_d!=data:

			con=0

			try:
				v1=int(ent1.get())

				can.itemconfig(sel_err1,text="")

			except:
				con=1
				can.itemconfig(sel_err1,text="error")



			try:
				v2=int(ent2.get())

				can.itemconfig(sel_err2,text="")

			except:
				con=1
				can.itemconfig(sel_err2,text="error")



			
			if con==1:
				can.itemconfig(sel_total,text="Invalid")
			elif con==0:
				can.itemconfig(sel_total,text=f"Ksh.{v1*v2}")


			sel_item_ent_d=data

	root.after(1,check_sel_item)



		




sel_err1=0
sel_err2=0
sel_total=0
qp=None
add_c_coord=[]
def draw_selected_item(id_):
	global can,sel_item,sell_items_ims
	global dashboard,can,can2,can3,can4
	global quit,qp
	global ent1,ent2
	global add_c_coord
	global sel_err1,sel_err2,sel_total
	global sel_item_ent_d

	f=font.Font(family="FreeMono",size=13)


	im=Image.new("RGBA",(int(can["width"]),int(can["height"])),(0,0,0,128))
	sell_items_ims["can_overlay"]=ImageTk.PhotoImage(im)

	sell_items_ims["can_overlay_"]=can.create_image(0,can.canvasy(0),image=sell_items_ims["can_overlay"],anchor="nw")



	im=Image.new("RGBA",(int(can2["width"]),int(can2["height"])),(0,0,0,128))
	sell_items_ims["can2_overlay"]=ImageTk.PhotoImage(im)

	sell_items_ims["can2_overlay_"]=can2.create_image(0,0,image=sell_items_ims["can2_overlay"],anchor="nw")



	im=Image.new("RGBA",(int(can3["width"]),int(can3["height"])),(0,0,0,128))
	sell_items_ims["can3_overlay"]=ImageTk.PhotoImage(im)

	sell_items_ims["can3_overlay_"]=can3.create_image(0,0,image=sell_items_ims["can3_overlay"],anchor="nw")



	im=Image.new("RGBA",(int(can4["width"]),int(can4["height"])),(0,0,0,128))
	sell_items_ims["can4_overlay"]=ImageTk.PhotoImage(im)

	sell_items_ims["can4_overlay_"]=can4.create_image(can4.canvasx(0),can4.canvasy(0),image=sell_items_ims["can4_overlay"],anchor="nw")





	x=int(dashboard.place_info()["x"])+int(dashboard["width"])

	xx,yy=int(can["width"])-int(dashboard["width"])-60,int(int(can["height"])*0.6)





	x=x+((int(can["width"])-x)-xx)/2
	y=can.canvasy(40+((int(can["height"])-40)-yy)/2)




	v=len(sell_items_ims)+1

	x1,y1,x2,y2=x,y-20, x+xx,y+yy-20

	im=draw_round_rect(15,x1,y1,x2,y2, "#ffffff","#ffffff",alpha=1,width=1)
	sell_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x,y-20,image=sell_items_ims[v],anchor="nw")

	can.create_image(x2-5-25,y1+5,image=quit,anchor="nw")

	qp=[x2-5-25,y1+5]



	sel_item=id_

	
	db_items=database.connect("data/items.db")
	cur=db_items.cursor()


	cur.execute(f"SELECT * FROM items WHERE item_id={id_}")
	rows=cur.fetchall()



	for row in rows:
		name=row[1]
		bp=row[2]
		sp=row[3]
		qt=row[4]
		desc=row[5]
		im_=row[6]



	can.create_text(x1+((x2-270)-x1)/2,y1+15,text=name,font=("FreeMono",13),fill="#0000ff",anchor="c")

	can.create_line(x2-270, y1+10, x2-270,y2-10,fill="#000000")
	

	x1_,y1_,x2_,y2_=x1+10,y1+30,x2-270-10,y2-50

	#can.create_rectangle(x1_,y1_,x2_,y2_, outline="#aaaaaa")

	if im_!="":

		im=Image.open(f"data/images/{im_}")
		_x,_y=im.size

		if _x/_y>(x2_-x1_)/(y2_-y1_):

			x_=(x2_-x1_)
			y_=x_*_y/_x

		elif _x/_y<(x2_-x1_)/(y2_-y1_):

			y_=(y2_-y1_)
			x_=y_*_x/_y

		else:
			x_=(x2_-x1_)
			y_=(y2_-y1_)

		x_=int(round(x_,0))
		y_=int(round(y_,0))

		im=im.resize((x_,y_))


		__x=((x2_-x1_)-x_)/2
		__y=((y2_-y1_)-y_)/2

		v+=1
		sell_items_ims[v]=ImageTk.PhotoImage(im)

		can.create_image(x1_+__x,y1_+__y,image=sell_items_ims[v],anchor="nw")

	else:
		can.create_text(x1_+(x2_-x1_)/2,y1_+(y2_-y1_)/2,text="No Image",font=("FreeMono",13),fill="#000000",anchor="c")

	can.create_text(x1+((x2-270)-x1)/2,y2-25,text=desc,fill="#000000",font=("FreeMono",13),anchor="c")




	can.create_text(x2-270+10,y1+30+30, text="Selling Price", font=("FreeMono",13),fill="#000000",anchor="w")
	can.create_text(x2-270+10+f.measure("Selling Price")+30,y1+30+30,text=f"Ksh.{sp}", font=("FreeMono",13),fill="#ff0000",anchor="w")


	can.create_text(x2-270+10,y1+30+30+40, text="Items Left", font=("FreeMono",13),fill="#000000",anchor="w")
	can.create_text(x2-270+10+f.measure("Selling Price")+30,y1+30+30+40,text=str(qt), font=("FreeMono",13),fill="#ff0000",anchor="w")


	yy1=y1+30+30+40

	



	yy2=y2-10-30-10-30

	yy3=31+10+31


	_y_=yy1+((yy2-yy1)-yy3)/2
	
	x1,y1,x2,y2=x2-270+10+f.measure("Sold at")+30,_y_, x2-270+10+f.measure("Sold at")+30+166,_y_+31,

	can.create_text(x+xx-270+10,y1+31/2, text="Sold at", font=("FreeMono",13),fill="#000000",anchor="w")

	v+=1

	im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	sell_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=sell_items_ims[v],anchor="nw")

	ent1.delete(0,tk.END)
	ent1.insert(tk.END,str(sp))


	ent1.place(in_=root,x=x1+5,y=_y_+5+40-can.canvasy(0))

	sel_err1=can.create_text(x1,y2+5,text="",fill="#ff0000",font=("FreeMono",9),anchor="w")





	v+=1

	im=draw_round_rect(5,x1,y1+40+10,x2,y2+40+10, "#000000",alpha=1,width=1)
	sell_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1+40+10,image=sell_items_ims[v],anchor="nw")

	ent2.delete(0,tk.END)
	ent2.insert(tk.END,str(1))


	ent2.place(in_=root,x=x1+5,y=y1+5+40-can.canvasy(0)+40+10)

	sel_err2=can.create_text(x1,y2+40+10+5,text="",fill="#ff0000",font=("FreeMono",9),anchor="w")

	can.create_text(x+xx-270+10,y1+40+10+31/2, text="Quantity", font=("FreeMono",13),fill="#000000",anchor="w")

	sel_item_ent_d=[ent1.get(),ent2.get()]




	x1,y1,x2,y2=x,y-20, x+xx,y+yy-20

	




	can.create_text(x2-270+10,y2-10-30-10-30, text="Total", font=("FreeMono",13),fill="#000000",anchor="w")


	sel_total=can.create_text(x2-10,y2-10-30-10-30, text=f"Ksh.{int(ent1.get())*int(ent2.get())}", font=("FreeMono",13),fill="#ff0000",anchor="e")



	v+=1

	

	x1,y1,x2,y2=x2-270+10, y2-10-30, x2-10,y2-10

	im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#000000",alpha=1,width=1)
	sell_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=sell_items_ims[v],anchor="nw")

	can.create_text(x1+(x2-x1)/2, y1+15,text="Add to Cart",fill="#ffffff",font=("FreeMono",13),anchor="c")


	add_c_coord=[x1,y1,x2,y2]


	ent1.focus_set()


def man_items_delete():
	global man_item


	db_items=database.connect("data/items.db")
	cur=db_items.cursor()

	cur.execute(f"DELETE FROM items WHERE item_id={man_item}")

	db_items.commit()

	man_item=None

	main(1)


def man_items_save():
	global man_item
	global ent1,ent2,ent3,ent4,text1






	name=ent1.get()
	bp=ent2.get()
	sp=ent3.get()
	qt=ent4.get()

	if name=="" or bp=="" or sp=="" or qt=="":

		return [0,"Fill essential fields!"]



	try:
		v=int(bp)
	except:
		return [0,"Some fields must be numbers!"]

	try:
		v=int(sp)
	except:
		return [0,"Some fields must be numbers!"]

	try:
		v=int(qt)
	except:
		return [0,"Some fields must be numbers!"]

	



	desc=text1.get("1.0",tk.END).replace("\n"," ")

	db_items=database.connect("data/items.db")
	cur=db_items.cursor()

	cur.execute(f"UPDATE items SET name='{name}' WHERE item_id={man_item}")
	cur.execute(f"UPDATE items SET bp={bp} WHERE item_id={man_item}")
	cur.execute(f"UPDATE items SET sp={sp} WHERE item_id={man_item}")
	cur.execute(f"UPDATE items SET quantity={qt} WHERE item_id={man_item}")
	cur.execute(f"UPDATE items SET description='{desc}' WHERE item_id={man_item}")

	if man_items_ims["image"]!=0:

		os.makedirs("data/images",exist_ok=True)

		man_items_ims["image"].save(f"data/images/{man_item}.png")

		scale_down_im(f"{man_item}.png",1,140,85)


		cur.execute(f"UPDATE items SET image='"+str(f"{man_item}.png")+f"' WHERE item_id={man_item}")
	else:
		cur.execute(f"UPDATE items SET image='' WHERE item_id={man_item}")

		ar=os.listdir("data/images")

		try:

			v=ar.index(f"{man_item}.png")

			os.remove(f"data/images/{man_item}.png")

		except:
			pass



		try:

			v=ar.index(f"{man_item}_1.png")

			os.remove(f"data/images/{man_item}_1.png")

		except:
			pass




	db_items.commit()


	return [1,"Item details saved!"]



man_items_ims={}
man_items_coords={}
def draw_manage_item(id_,con):
	global man_item
	global ent1,ent2,ent3,ent4,text1
	global can,dashboard
	global man_items_ims,man_items_coords
	global qp


	f=font.Font(family="FreeMono",size=13)


	im=Image.new("RGBA",(int(can["width"]),int(can["height"])),(0,0,0,128))
	man_items_ims["can_overlay"]=ImageTk.PhotoImage(im)

	man_items_ims["can_overlay_"]=can.create_image(0,can.canvasy(0),image=man_items_ims["can_overlay"],anchor="nw")



	im=Image.new("RGBA",(int(can2["width"]),int(can2["height"])),(0,0,0,128))
	man_items_ims["can2_overlay"]=ImageTk.PhotoImage(im)

	man_items_ims["can2_overlay_"]=can2.create_image(0,0,image=man_items_ims["can2_overlay"],anchor="nw")



	im=Image.new("RGBA",(int(can3["width"]),int(can3["height"])),(0,0,0,128))
	man_items_ims["can3_overlay"]=ImageTk.PhotoImage(im)

	man_items_ims["can3_overlay_"]=can3.create_image(0,0,image=man_items_ims["can3_overlay"],anchor="nw")




	"""
	forget_widgets(except_=dashboard)
	delete_widgets()
	entries_show_reset()"""

	man_item=id_

	
	db_items=database.connect("data/items.db")
	cur=db_items.cursor()


	cur.execute(f"SELECT * FROM items WHERE item_id={id_}")
	rows=cur.fetchall()



	for row in rows:
		name=row[1]
		bp=row[2]
		sp=row[3]
		qt=row[4]
		desc=row[5]
		im_=row[6]




	xx,yy=700,430

	x=int(dashboard.place_info()["x"])+int(dashboard["width"])

	x=x+((width-x)-xx)/2
	y=can.canvasy(((height-40)-yy)/2)

	yv=can.canvasy(0)

	#print(y,"yy")

	
	v=len(man_items_ims)


	v+=1

	x1,y1,x2,y2=x,y, x+xx,y+yy

	im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#ffffff",alpha=1,width=1)
	man_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x,y,image=man_items_ims[v],anchor="nw")

	can.create_image(x2-5-25,y1+5,image=quit,anchor="nw")

	qp=[x2-5-25,y1+5]


	can.create_polygon(x1+(x2-x1)/2-100,y1+2, x1+(x2-x1)/2+100,y1+2,
		x1+(x2-x1)/2+100-15,y1+32, x1+(x2-x1)/2-100+15,y1+32,fill="#000000",outline="#000000")



	can.create_text(x+xx/2,y1+1+15,text="Manage Item",font=("FreeMono",13),fill="#ffffff",anchor="c")






	y+=20



	

	can.create_text(x+10+10,y+20+15, text="Item Name",font=("FreeMono",13), anchor="w",fill="#000000")

	v+=1


	x1,y1,x2,y2=x+150-5-20+10,y+20+15-10-5,x+150-5+100+60+6-20+10,y+20+15-10-5+25+6

	im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	man_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=man_items_ims[v],anchor="nw")

	ent1.place(in_=root,x=x+150-20+10,y=y+20+15-10+40-yv)


	man_items_coords["item name"]=[x1,y1,x2,y2]

	

	can.create_text(x+10+10,y+20+15+50, text="Buying Price",font=("FreeMono",13), anchor="w",fill="#000000")

	v+=1

	x1,y1,x2,y2=x+150-5-20+10,y+20+15-10-5+50,x+150-5+100+60+6-20+10,y+20+15-10-5+25+6+50

	im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	man_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=man_items_ims[v],anchor="nw")

	ent2.place(in_=root,x=x+150-20+10,y=y+20+15-10+50+40-yv)




	man_items_coords["bp"]=[x1,y1,x2,y2]

	can.create_text(x+10+10,y+20+15+50*2, text="Selling Price",font=("FreeMono",13), anchor="w",fill="#000000")

	v+=1

	x1,y1,x2,y2=x+150-5-20+10,y+20+15-10-5+50*2,x+150-5+100+60+6-20+10,y+20+15-10-5+25+6+50*2

	im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	man_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=man_items_ims[v],anchor="nw")

	ent3.place(in_=root,x=x+150-20+10,y=y+20+15-10+50*2+40-yv)




	man_items_coords["sp"]=[x1,y1,x2,y2]	


	can.create_text(x+10+10,y+20+15+50*3, text="Quantity",font=("FreeMono",13), anchor="w",fill="#000000")

	v+=1

	x1,y1,x2,y2=x+150-5-20+10,y+20+15-10-5+50*3,x+150-5+100+60+6-20+10,y+20+15-10-5+25+6+50*3

	im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	man_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=man_items_ims[v],anchor="nw")

	ent4.place(in_=root,x=x+150-20+10,y=y+20+15-10+50*3+40-yv)



	man_items_coords["q"]=[x1,y1,x2,y2]



	v+=1

	x1,y1,x2,y2=x+10+10,y+20+15-10-5+50*4+10,x+150-5+100+60+6-20+10,y+20+15-10-5++50*4+10+100

	im=draw_round_rect(10,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	draw=ImageDraw.Draw(im)

	draw.rectangle((10,-5, 10+5+f.measure("Description")+5,5),fill=(0,0,0,0),outline=(0,0,0,0))

	man_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=man_items_ims[v],anchor="nw")

	can.create_text(x1+10+5,y1, text="Description",font=("FreeMono",13),fill="#000000", anchor="w")

	text1.place(in_=root,x=x1+15,y=y1+15+40-yv)


	man_items_coords["desc"]=[x1,y1,x2,y2]




	if con==0:
		ent1.delete(0,tk.END)
		ent2.delete(0,tk.END)
		ent3.delete(0,tk.END)
		ent4.delete(0,tk.END)
		text1.delete(0.0, tk.END)

		ent1.insert(tk.END,name)
		ent2.insert(tk.END,bp)
		ent3.insert(tk.END,sp)
		ent4.insert(tk.END,qt)
		text1.insert(tk.END,desc)

	else:


		name=ent1.get()
		bp=ent2.get()
		sp=ent3.get()
		qt=ent4.get()
		desc=text1.get("1.0",tk.END)



		ent1.delete(0,tk.END)
		ent2.delete(0,tk.END)
		ent3.delete(0,tk.END)
		ent4.delete(0,tk.END)
		text1.delete(0.0, tk.END)

		ent1.insert(tk.END,name)
		ent2.insert(tk.END,bp)
		ent3.insert(tk.END,sp)
		ent4.insert(tk.END,qt)
		text1.insert(tk.END,desc)

	v+=1

	x1,y1,x2,y2=x+150-5+100+60+6-20+10+20,y+20+15-10-5,x+xx-20,y2

	im=draw_round_rect(15,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	man_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=man_items_ims[v],anchor="nw")


	can.create_rectangle(x1+15,y1+15, x2-15,y2-15,outline="#aaaaaa")

	man_items_coords["imagep"]=[x1+15,y1+15, x2-15,y2-15]






	can.create_image(x2-25,y2+5,image=delete,anchor="nw")
	man_items_coords["delete"]=[x2-25,y2+5]
	can.create_image(x2-25-10-25,y2+5,image=crop2,anchor="nw")
	man_items_coords["crop"]=[x2-25-10-25,y2+5]
	can.create_image(x2-25-10-25-10-25,y2+5,image=refresh,anchor="nw")
	man_items_coords["refresh"]=[x2-25-10-25-10-25,y2+5]

	#print((y2+5+25+10+30+10)-y,"h")

	if con==0:

		if im_!="":


			man_items_ims["image"]=Image.open(f"data/images/{im_}")

		else:

			man_items_ims["image"]=0


	if not man_items_ims["image"]==0:

		process_man_item_im(man_items_ims["image"])

		man_items_coords["add_image"]=None

	else:


		v+=1

		cx,cy=x1+(x2-x1)/2,y1+(y2-y1)/2

		x1,y1,x2,y2=cx-40,cy-40, cx+40,cy+40,

		im=draw_round_rect(40,x1,y1,x2,y2, "#000000",alpha=1,width=1)
		man_items_ims[v]=ImageTk.PhotoImage(im)
		can.create_image(x1,y1,image=man_items_ims[v],anchor="nw")

		can.create_line(cx-20,cy, cx+20,cy,fill="#000000")
		can.create_line(cx,cy-20, cx,cy+20,fill="#000000")

		can.create_text(cx,cy+40+20,text="Add Image", font=("FreeMono",13),fill="#000000",anchor="c")

		man_items_coords["add_image"]=[cx,cy]





	x_=xx/4


	v+=1

	x1,y1,x2,y2=x+x_-80,y+yy-10-30-20, x+x_+80,y+yy-10-20

	im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#000000",alpha=1,width=1)
	man_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=man_items_ims[v],anchor="nw")

	can.create_text(x1+(x2-x1)/2, y+yy-10-15-20, text="Reset", font=("FreeMono",13),fill="#ffffff",anchor="c")

	man_items_coords["reset"]=[x1,y1,x2,y2]


	v+=1

	x1,y1,x2,y2=x+x_*2-80,y+yy-10-30-20, x+x_*2+80,y+yy-10-20

	im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#000000",alpha=1,width=1)
	man_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=man_items_ims[v],anchor="nw")

	can.create_text(x1+(x2-x1)/2, y+yy-10-15-20, text="Delete", font=("FreeMono",13),fill="#ffffff",anchor="c")

	man_items_coords["_delete_"]=[x1,y1,x2,y2]



	v+=1

	x1,y1,x2,y2=x+x_*3-80,y+yy-10-30-20, x+x_*3+80,y+yy-10-20

	im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#000000",alpha=1,width=1)
	man_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=man_items_ims[v],anchor="nw")

	can.create_text(x1+(x2-x1)/2, y+yy-10-15-20, text="Save", font=("FreeMono",13),fill="#ffffff",anchor="c")

	man_items_coords["save"]=[x1,y1,x2,y2]


	ent1.focus_set()



sell_items_ims={}

_scroll_={}
v1,h1=0,0
v2,h2=0,0
v3,h3=0,0

cart_ar=[]
items_ar=[]
sel_item=None
man_item=None

cart_buttons_coords={}

search_val=""
search_coords=[]

man_reset_st=False
def main(con=0):

	global st,st_
	global can,can2,can3
	global add_items_ims
	global dashboard
	global ent1,ent2,ent3,ent4,ent_search,text1
	global delete,crop1,crop2,refresh
	global add_items_coords
	global add_item_im
	global sell_items_ims
	global _scroll_
	global v1,h1
	global v2,h2
	global cart_ar
	global items_ar
	global sel_item
	global added
	global width,height
	global cart_im,clear_cart
	global cart_buttons_coords
	global mpesa_logo
	global search
	global search_val,search_focus,search_coords
	global user_id
	global no_profile_im
	global no_record
	global man_items_ims
	global man_item
	global man_reset_st

	st_="main"

	f=font.Font(family="FreeMono",size=13)

	if st=="Sell Items":



		items_ar=[]

		cart_buttons_coords={}


		forget_widgets(except_=dashboard)
		entries_show_reset()
		if con==0:
			sel_item=None
			search_val=""
			delete_widgets()

		can["width"]=width-400
		can["height"]=height-40
		can["scrollregion"]=(0,0,width,height-40)
		can["bg"]="#ffffff"

		can["scrollregion"]=(0,0,width-400,height-40)


		if con==0:

			dict_={"widget": can,
					"sb_widget":can3,
					"sb_st":"vertical",
					"sb_sz":10,
					"v_sb_coord":[(0,height-40,0,10),0],
					"_y":height-40,
					"v":v1,
					"h_":h1,
					"w":int(can["width"]),
					"h":int(can["height"]),
					"_x":width-400,
					"_x2":width-400,
					"scrollregion":can["scrollregion"],
					"v_drag_st":0,
					"h_drag_st":0,
					"v_var":0,
					"h_var":0


					}

		else:

			dict_={"widget": can,
					"sb_widget":can3,
					"sb_st":"vertical",
					"sb_sz":10,
					"v_sb_coord":[(0,height-40,0,10),_scroll_["can"]["v_sb_coord"][-1]],
					"_y":height-40,
					"v":v1,
					"h_":h1,
					"w":int(can["width"]),
					"h":int(can["height"]),
					"_x":width-400,
					"_x2":width-400,
					"scrollregion":can["scrollregion"],
					"v_drag_st":0,
					"h_drag_st":0,
					"v_var":0,
					"h_var":0


					}			

		_scroll_["can"]=dict_


		can.place(in_=root,x=0,y=40)

		can2["width"]=width
		can2["height"]=40
		can2["bg"]="#ffffff"

		can2.delete("all")

		can2.create_line(0,0,width,0,fill="#000000")
		#can2.create_line(0,39,width,39,fill="#dddddd")

		can2.place(in_=root,x=0,y=0)


		can3["width"]=400
		can3["height"]=height-40
		can3["bg"]="#ffffff"

		can3.delete("all")
		can3.place(in_=root,x=width-400,y=40)

		v=0


		_x_=400-10



		if int(dashboard.place_info()["x"])<0:
			_x=5+25+5
		else:
			_x=int(dashboard["width"])
		x_=_x+(int(can["width"])-_x-_x_)/2

		x1,y1,x2,y2=x_,5,x_+_x_,5+30


		im=draw_round_rect(15,x1,y1,x2,y2, "#000000",alpha=1,width=1)

		sell_items_ims[v]=ImageTk.PhotoImage(im)

		can2.create_image(x1,y1,image=sell_items_ims[v],anchor="nw")

		ent_search["width"]=40

		if search_focus==False:
			if search_val=="":

				can2.create_text(x1+15,y1+15,text="Search",font=("FreeMono",13),fill="#000000",anchor="w")

				can2.create_image(x1+15+f.measure("Search")+10,y1+2.5,image=search,anchor="nw")

			else:

				can2.create_text(x1+15+1,y1+15,text=search_val,font=("FreeMono",13),fill="#000000",anchor="w")


		can2.create_image(x2+5,y1+2.5,image=quit,anchor="nw")



		search_coords=[x1,y1,x2,y2,[x2+5,y1+2.5]]

		if search_focus==True:


			ent_search.place(in_=root,x=x1+15,y=y1+4.5)

			ent_search.focus_set()




		db_users=database.connect("data/users.db")
		cur=db_users.cursor()


		cur.execute(f"SELECT * FROM users WHERE user_id={user_id}")

		row=cur.fetchall()[0]


		can2.create_text(width-5-25-15,20, text=row[1],fill="#000000",font=("FreeMono",13),anchor="e")

		if row[4]=="":

			can2.create_image(width-5-25,7.5,image=no_profile_im,anchor="nw")


		else:

			#process profile picture
			pass





		


		can.delete("all")

		db_items=database.connect("data/items.db")
		cur=db_items.cursor()

		cur.execute("SELECT * FROM items")

		rows=cur.fetchall()

		


		x=int(dashboard.place_info()["x"])+int(dashboard["width"])

		

		xx=150
		yy=200


		#det space between items

		_x_=int(can["width"])-x

		n=len(rows)

		n_=n

		con_n=0
		for _n in range(n):

			xv=(_x_-(n_*xx))/(n_+1)

			if xv<30:
				n_-=1
				con_n=1
			else:

				_n_=[n_,xv]

				break

		if con_n==0:
			_n_=[n,20]


		def det_selected(id_):
			global cart_ar

			con=0

			for i in cart_ar:


				if i[0]==id_:

					con=1
					break

			return con








		y=20


		v+=1

		_x_=x


		_x_=x+_n_[1]


		rc=1

		con_=0

		for row in rows:


			if row[1].lower().find(search_val.lower())==-1 and row[5].lower().find(search_val.lower())==-1:

				continue

			con_=1




			x1,y1,x2,y2=_x_,y,_x_+xx,y+yy

			col="#000000"

			if det_selected(row[0])==1:
				col="#ff0000"
				can.create_image(x2+5,y1,image=added,anchor="nw")


			items_ar.append([row[0],x1,y1,x2,y2])


			im=draw_round_rect(15,x1,y1,x2,y2, col,"#ffffff",alpha=1,width=1)

			sell_items_ims[v]=ImageTk.PhotoImage(im)

			can.create_image(x1,y1,image=sell_items_ims[v],anchor="nw")

			

			x1_,y1_,x2_,y2_=x1+5,y1+15, x2-5,y2-25-25-25-25


			if not row[-1]=="":

				im=Image.open(f"data/images/{row[-1].replace(".png","_1.png")}")
				_x,_y=im.size

				x_=int(_x)
				y_=int(_y)



				v+=1

				sell_items_ims[v]=ImageTk.PhotoImage(im)

				__x=((x2_-x1_)-x_)/2
				__y=((y2_-y1_)-y_)/2

				can.create_image(x1_+__x,y1_+__y,image=sell_items_ims[v],anchor="nw")
			else:
				can.create_text(x1_+(x2_-x1_)/2, y1_+(y2_-y1_)/2,text="No Image",font=("FreeMono",13),fill="#000000",anchor="c")

			can.create_rectangle(x1+5,y1+15, x2-5,y2-25-25-25-25,outline="#aaaaaa")





			can.create_text(x1+10,y2-25-25-25, text=f"{row[1]}",font=("FreeMono",13),fill="#0000ff",anchor="w")
			can.create_text(x1+10,y2-25-25, text=f"Ksh.{row[3]}",font=("FreeMono",13),fill="#000000",anchor="w")
			can.create_text(x1+10,y2-25, text=f"{row[4]} items left",font=("FreeMono",13),fill="#000000",anchor="w")


			v+=1


			if rc==_n_[0]:

				y+=yy+20
				_x_=x+_n_[1]

				rc=1

			else:
				_x_+=xx+_n_[1]

				rc+=1


		if con_==0:

			im=no_record

			im=im.resize((250,250))

			v+=1

			sell_items_ims[v]=ImageTk.PhotoImage(im)


			if int(dashboard.place_info()["x"])<0:
				_x=5+25+5
			else:
				_x=int(dashboard["width"])
			x_=_x+(int(can["width"])-_x)/2

			can.create_image(x_,int(can["height"])/2,image=sell_items_ims[v],anchor="c")

			can.create_text(x_,int(can["height"])/2+250/2+10+15,text="No Record",font=("FreeMono",13),fill="#000000",anchor="c")



		if rc-1==0:
			_y=y
		else:
			_y=y+yy+20

		if _y<=int(can["height"]):

			y_=int(can["height"])

		else:

			y_=_y
			can["scrollregion"]=(0,0,int(can["width"]),int(y_))



		_scroll_["can"]["_y"]=y_

		if con==0:

			_scroll_["can"]["v_sb_coord"][-1]=0


		draw_v_sb("can")


		v+=1

		x1,y1,x2,y2=10+5,5,int(can3["width"])-5,int(can3["height"])-5

		im=draw_round_rect(20,x1,y1,x2,y2, "#000000","#00fffff",alpha=1,width=1)
		sell_items_ims[v]=ImageTk.PhotoImage(im)

		can3.create_image(x1,y1, image=sell_items_ims[v],anchor="nw")


		_x=(int(can3["width"])-(10+25+f.measure("Cart")))/2
		can3.create_image(_x,5+35/2,image=cart_im,anchor="w")
		can3.create_text(_x+25+10,5+35/2, text="Cart", font=("FreeMono",13),fill="#000000",anchor="w")





		v+=1

		x1,y1,x2,y2=10+5+10,40,int(can3["width"])-4-10-4-5,int(can3["height"])-10-30-(10+30)*2-30*2-15-10-30-10-4-10

		im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#ffffff",alpha=1,width=1)
		sell_items_ims[v]=ImageTk.PhotoImage(im)

		can3.create_image(x1,y1, image=sell_items_ims[v],anchor="nw")


		#cart

		can4["width"]=(x2-x1)-2
		can4["height"]=(y2-y1)-15-15

		can4["bg"]="#ffffff"

		can4.delete("all")

		_x=int(can3.place_info()["x"])

		can4.place(in_=root,x=_x+x1+1,y=y1+40+15)

		can4["scrollregion"]=(0,0,int(can4["width"]),int(can4["height"]))

		

		dict_={"widget": can4,
				"sb_widget":can3,
				"sb_st":"both",
				"sb_sz":10,
				"v_sb_coord":[(y1+15,y1+15+int(can4["height"]),x2+4,x2+4+10,0),0],
				"h_sb_coord":[(x1+1,x1+1+int(can4["width"]),y2+4,y2+4+10),0],
				"_y":int(can4["height"]),
				"v":v2,
				"h_":h2,
				"w":int(can4["width"]),
				"h":int(can4["height"]),
				"_x":int(can4["width"]),
				"_x2":int(can4["width"]),
				"scrollregion":can4["scrollregion"],
				"v_drag_st":0,
				"h_drag_st":0,
				"v_var":0,
				"h_var":0


				}

		_scroll_["cart"]=dict_


		db_items=database.connect("data/items.db")
		cur=db_items.cursor()


		y=0

		#can4.create_line(0,y, int(can4["width"]),y,fill="#000000")


		total=0
		discount=0
		no_items=0

		con2_=0

		for i in cart_ar:

			con2_=1

			id_,sold_at,quantity=i





			cur.execute(f"SELECT * FROM items WHERE item_id={id_}")
			rows=cur.fetchall()



			for row in rows:
				name=row[1]
				sp=row[3]


			can4.create_text(5,y+15,text=name,font=("FreeMono",13),fill="#0000ff",anchor="w")

			if int(quantity)==1:
				q="Unit"
			else:
				q="Units"
			can4.create_text(5,y+15+30+10,text=q,font=("FreeMono",13),fill="#000000",anchor="w")
			can4.create_text(5+f.measure("Total")+20,y+15+30+10,text=str(quantity),font=("FreeMono",13),fill="#ff0000",anchor="w")
			can4.create_text(5,y+15+30+10+30,text="Total",font=("FreeMono",13),fill="#000000",anchor="w")
			can4.create_text(5+f.measure("Total")+20,y+15+30+10+30,text=f"Ksh.{int(sold_at)*int(quantity)}",font=("FreeMono",13),fill="#ff0000",anchor="w")
	
			y+=15+30+10+30+20

			can4.create_line(0,y, int(can4["width"]),y,fill="#000000")


			no_items+=int(quantity)
			total+=int(sold_at)*int(quantity)
			discount+=(int(sp)-int(sold_at))*int(quantity)
		y+=10



		if con2_==0:

			im=no_record

			im=im.resize((100,100))

			v+=1

			sell_items_ims[v]=ImageTk.PhotoImage(im)

			can4.create_image(int(can4["width"])/2,int(can4["height"])/2,image=sell_items_ims[v],anchor="c")

			can4.create_text(int(can4["width"])/2,int(can4["height"])/2+50+10+15,text="No Record",font=("FreeMono",13),fill="#000000",anchor="c")




		if y<=int(can4["height"]):

			_scroll_["cart"]["_y"]=int(can4["height"])

			can4["scrollregion"]=(0,0,int(can4["width"]),int(can4["height"]))


		else:

			can4["scrollregion"]=(0,0,int(can4["width"]),y)

			_scroll_["cart"]["_y"]=y






		

		_scroll_["cart"]["v_sb_coord"][-1]=1
		_scroll_["cart"]["h_sb_coord"][-1]=0

		draw_v_sb("cart")
		draw_h_sb("cart")



		v+=1

		x1,y1,x2,y2=10+5+10,int(can3["height"])-10-30-(10+30)*2-30*2-15-10-30,10+5+10+15+25+10+f.measure("Clear Cart")+15,int(can3["height"])-10-30-(10+30)*2-30*2-15-10

		im=draw_round_rect(15,x1,y1,x2,y2, "#ff0000","#ff0000",alpha=1,width=1)
		sell_items_ims[v]=ImageTk.PhotoImage(im)

		can3.create_image(x1,y1, image=sell_items_ims[v],anchor="nw")
		can3.create_image(x1+15,y1+2.5,image=clear_cart,anchor="nw")
		can3.create_text(x1+15+25+10,y1+15, text="Clear Cart",fill="#ffffff",font=("FreeMono",13),anchor="w")


		cart_buttons_coords["clear_cart"]=[x1,y1,x2,y2]


		if int(no_items)==1:
			i="Item"
		else:
			i="Items"

		can3.create_text(10+5+10, int(can3["height"])-10-30-(10+30)*2-30*2, text=i, font=("FreeMono",13),fill="#000000",anchor="w")
		can3.create_text(int(can3["width"])-10-5, int(can3["height"])-10-30-(10+30)*2-30*2, text=str(no_items), font=("FreeMono",13),fill="#ff0000",anchor="e")		

		can3.create_text(10+5+10, int(can3["height"])-10-30-(10+30)*2-30, text="Discount", font=("FreeMono",13),fill="#000000",anchor="w")
		can3.create_text(int(can3["width"])-10-5, int(can3["height"])-10-30-(10+30)*2-30, text=f"Ksh.{discount}", font=("FreeMono",13),fill="#ff0000",anchor="e")		

		can3.create_text(10+5+10, int(can3["height"])-10-30-(10+30)*2, text="Sub Total", font=("FreeMono",13),fill="#000000",anchor="w")
		can3.create_text(int(can3["width"])-10-5, int(can3["height"])-10-30-(10+30)*2, text=f"Ksh.{total}", font=("FreeMono",13),fill="#ff0000",anchor="e")		



		v+=1

		x1,y1,x2,y2=10+5+10,int(can3["height"])-10-30-10-30-5,int(can3["width"])-5-10,int(can3["height"])-10-10-30-5

		im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#000000",alpha=1,width=1)
		sell_items_ims[v]=ImageTk.PhotoImage(im)

		can3.create_image(x1,y1, image=sell_items_ims[v],anchor="nw")

		can3.create_text(x1+(x2-x1)/2, y1+15, text="Pay with Cash", font=("FreeMono",13),fill="#ffffff",anchor="c")


		


		cart_buttons_coords["pay_with_cash"]=[x1,y1,x2,y2]



		v+=1

		x1,y1,x2,y2=10+5+10,int(can3["height"])-10-30-5,int(can3["width"])-5-10,int(can3["height"])-10-5

		im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#0fb621",alpha=1,width=1)
		sell_items_ims[v]=ImageTk.PhotoImage(im)

		can3.create_image(x1,y1, image=sell_items_ims[v],anchor="nw")


		im=mpesa_logo

		w,h=im.size



		h_=25
		w_=int(round(h_*w/h,0))

		im=im.resize((w_,h_))

		w,h=im.size

		x_=x1+15+((x2-x1)-(f.measure("Pay with")+w+10+30))/2


		can3.create_text(x_, y1+15, text="Pay with", font=("FreeMono",13),fill="#ffffff",anchor="w")

		v+=1

		sell_items_ims[v]=ImageTk.PhotoImage(im)

		can3.create_image(x_+f.measure("Pay with")+10,y1+2.5,image=sell_items_ims[v],anchor="nw")



		cart_buttons_coords["pay_with_mpesa"]=[x1,y1,x2,y2]

		if sel_item!=None:

			draw_selected_item(sel_item)

	elif st=="Manage items":

		items_ar=[]


		forget_widgets(except_=dashboard)
		entries_show_reset()
		if con==0:
			man_item=None
			man_reset_st=False
			search_val=""
			delete_widgets()

		can["width"]=width-4-10
		can["height"]=height-40
		can["scrollregion"]=(0,0,width-4-10,height-40)
		can["bg"]="#ffffff"

		can["scrollregion"]=(0,0,width-4-10,height-40)


		if con==0:

			dict_={"widget": can,
					"sb_widget":can3,
					"sb_st":"vertical",
					"sb_sz":10,
					"v_sb_coord":[(0,height-40,0,10),0],
					"_y":height-40,
					"v":v3,
					"h_":h3,
					"w":int(can["width"]),
					"h":int(can["height"]),
					"_x":int(can["width"]),
					"_x2":int(can["width"]),
					"scrollregion":can["scrollregion"],
					"v_drag_st":0,
					"h_drag_st":0,
					"v_var":0,
					"h_var":0


					}

		else:

			dict_={"widget": can,
					"sb_widget":can3,
					"sb_st":"vertical",
					"sb_sz":10,
					"v_sb_coord":[(0,height-40,0,10),_scroll_["can"]["v_sb_coord"][-1]],
					"_y":height-40,
					"v":v3,
					"h_":h3,
					"w":int(can["width"]),
					"h":int(can["height"]),
					"_x":int(can["width"]),
					"_x2":int(can["width"]),
					"scrollregion":can["scrollregion"],
					"v_drag_st":0,
					"h_drag_st":0,
					"v_var":0,
					"h_var":0


					}			

		_scroll_["can"]=dict_


		can.place(in_=root,x=0,y=40)

		can2["width"]=width
		can2["height"]=40
		can2["bg"]="#ffffff"

		can2.delete("all")

		can2.create_line(0,0,width,0,fill="#000000")
		#can2.create_line(0,39,width,39,fill="#dddddd")

		can2.place(in_=root,x=0,y=0)


		can3["width"]=14
		can3["height"]=height-40
		can3["bg"]="#ffffff"

		can3.delete("all")
		can3.place(in_=root,x=width-14,y=40)

		v=0


		_x_=400-10



		if int(dashboard.place_info()["x"])<0:
			_x=5+25+5
		else:
			_x=int(dashboard["width"])
		x_=_x+(int(can["width"])-_x-_x_)/2

		x1,y1,x2,y2=x_,5,x_+_x_,5+30


		im=draw_round_rect(15,x1,y1,x2,y2, "#000000",alpha=1,width=1)

		man_items_ims[v]=ImageTk.PhotoImage(im)

		can2.create_image(x1,y1,image=man_items_ims[v],anchor="nw")

		ent_search["width"]=40

		if search_focus==False:
			if search_val=="":

				can2.create_text(x1+15,y1+15,text="Search",font=("FreeMono",13),fill="#000000",anchor="w")

				can2.create_image(x1+15+f.measure("Search")+10,y1+2.5,image=search,anchor="nw")

			else:

				can2.create_text(x1+15+1,y1+15,text=search_val,font=("FreeMono",13),fill="#000000",anchor="w")


		can2.create_image(x2+5,y1+2.5,image=quit,anchor="nw")



		search_coords=[x1,y1,x2,y2,[x2+5,y1+2.5]]

		if search_focus==True:


			ent_search.place(in_=root,x=x1+15,y=y1+4.5)

			ent_search.focus_set()




		db_users=database.connect("data/users.db")
		cur=db_users.cursor()


		cur.execute(f"SELECT * FROM users WHERE user_id={user_id}")

		row=cur.fetchall()[0]


		can2.create_text(width-5-25-15,20, text=row[1],fill="#000000",font=("FreeMono",13),anchor="e")

		if row[4]=="":

			can2.create_image(width-5-25,7.5,image=no_profile_im,anchor="nw")


		else:

			#process profile picture
			pass





		


		can.delete("all")

		db_items=database.connect("data/items.db")
		cur=db_items.cursor()

		cur.execute("SELECT * FROM items")

		rows=cur.fetchall()

		


		x=int(dashboard.place_info()["x"])+int(dashboard["width"])

		

		xx=150
		yy=200


		#det space between items

		_x_=int(can["width"])-x

		n=len(rows)

		n_=n

		con_n=0
		for _n in range(n):

			xv=(_x_-(n_*xx))/(n_+1)

			if xv<30:
				n_-=1
				con_n=1
			else:

				_n_=[n_,xv]

				break

		if con_n==0:
			_n_=[n,20]









		y=20


		v+=1

		_x_=x


		_x_=x+_n_[1]


		rc=1

		con_=0

		for row in rows:


			if row[1].lower().find(search_val.lower())==-1 and row[5].lower().find(search_val.lower())==-1:

				continue

			con_=1




			x1,y1,x2,y2=_x_,y,_x_+xx,y+yy

			col="#000000"



			items_ar.append([row[0],x1,y1,x2,y2])


			im=draw_round_rect(15,x1,y1,x2,y2, col,"#ffffff",alpha=1,width=1)

			man_items_ims[v]=ImageTk.PhotoImage(im)

			can.create_image(x1,y1,image=man_items_ims[v],anchor="nw")

			

			x1_,y1_,x2_,y2_=x1+5,y1+15, x2-5,y2-25-25-25-25


			if not row[-1]=="":

				im=Image.open(f"data/images/{row[-1].replace(".png","_1.png")}")
				_x,_y=im.size

				x_=int(_x)
				y_=int(_y)



				v+=1

				man_items_ims[v]=ImageTk.PhotoImage(im)

				__x=((x2_-x1_)-x_)/2
				__y=((y2_-y1_)-y_)/2

				can.create_image(x1_+__x,y1_+__y,image=man_items_ims[v],anchor="nw")
			else:
				can.create_text(x1_+(x2_-x1_)/2, y1_+(y2_-y1_)/2,text="No Image",font=("FreeMono",13),fill="#000000",anchor="c")

			can.create_rectangle(x1+5,y1+15, x2-5,y2-25-25-25-25,outline="#aaaaaa")





			can.create_text(x1+10,y2-25-25-25, text=f"{row[1]}",font=("FreeMono",13),fill="#0000ff",anchor="w")
			can.create_text(x1+10,y2-25-25, text=f"Ksh.{row[3]}",font=("FreeMono",13),fill="#000000",anchor="w")
			can.create_text(x1+10,y2-25, text=f"{row[4]} items left",font=("FreeMono",13),fill="#000000",anchor="w")


			v+=1


			if rc==_n_[0]:

				y+=yy+20
				_x_=x+_n_[1]

				rc=1

			else:
				_x_+=xx+_n_[1]

				rc+=1


		if con_==0:

			im=no_record

			im=im.resize((250,250))

			v+=1

			man_items_ims[v]=ImageTk.PhotoImage(im)


			if int(dashboard.place_info()["x"])<0:
				_x=5+25+5
			else:
				_x=int(dashboard["width"])
			x_=_x+(int(can["width"])-_x)/2

			can.create_image(x_,int(can["height"])/2,image=man_items_ims[v],anchor="c")

			can.create_text(x_,int(can["height"])/2+250/2+10+15,text="No Record",font=("FreeMono",13),fill="#000000",anchor="c")



		if rc-1==0:
			_y=y
		else:
			_y=y+yy+20

		if _y<=int(can["height"]):

			y_=int(can["height"])

		else:

			y_=_y
			can["scrollregion"]=(0,0,int(can["width"]),int(y_))



		_scroll_["can"]["_y"]=y_

		if con==0:

			_scroll_["can"]["v_sb_coord"][-1]=0


		draw_v_sb("can")


		if man_item!=None:


			if man_reset_st:
				draw_manage_item(man_item,0)
			else:
				draw_manage_item(man_item,1)


			man_reset_st=False


			


	elif st=="Add Items":

		search_val=""

		forget_widgets(except_=dashboard)
		entries_show_reset()
		if con==0:
			delete_widgets()


		can["width"]=width
		can["height"]=height-40
		can["scrollregion"]=(0,0,width,height-40)
		can["bg"]="#ffffff"

		can.place(in_=root,x=0,y=40)


		can2["width"]=width
		can2["height"]=40

		can2.delete("all")
		can2.place(in_=root,x=0,y=0)





		v=0

		im=Image.new("RGBA",(width,40),(0,0,0,128))

		add_items_ims[v]=ImageTk.PhotoImage(im)

		can2.create_image(0,0,image=add_items_ims[v],anchor="nw")









		can.delete("all")

		v+=1

		im=Image.new("RGBA",(width,height),(0,0,0,128))

		add_items_ims[v]=ImageTk.PhotoImage(im)

		can.create_image(0,0,image=add_items_ims[v],anchor="nw")


		xx,yy=700,430

		x=int(dashboard.place_info()["x"])+int(dashboard["width"])

		x=x+((width-x)-xx)/2
		y=((height-40)-yy)/2

		#print(y,"yy")

		



		v+=1

		x1,y1,x2,y2=x,y, x+xx,y+yy

		im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#ffffff",alpha=1,width=1)
		add_items_ims[v]=ImageTk.PhotoImage(im)
		can.create_image(x,y,image=add_items_ims[v],anchor="nw")


		can.create_polygon(x1+(x2-x1)/2-100,y1+2, x1+(x2-x1)/2+100,y1+2,
			x1+(x2-x1)/2+100-15,y1+32, x1+(x2-x1)/2-100+15,y1+32,fill="#000000",outline="#000000")



		can.create_text(x+xx/2,y1+1+15,text="Add Item",font=("FreeMono",13),fill="#ffffff",anchor="c")




		if con==0:

			#delete ent/txt

			pass


		y+=20



		

		can.create_text(x+10+10,y+20+15, text="Item Name",font=("FreeMono",13), anchor="w",fill="#000000")

		v+=1


		x1,y1,x2,y2=x+150-5-20+10,y+20+15-10-5,x+150-5+100+60+6-20+10,y+20+15-10-5+25+6

		im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
		add_items_ims[v]=ImageTk.PhotoImage(im)
		can.create_image(x1,y1,image=add_items_ims[v],anchor="nw")

		ent1.place(in_=root,x=x+150-20+10,y=y+20+15-10+40)

		add_items_coords["item name"]=[x1,y1,x2,y2]

		

		can.create_text(x+10+10,y+20+15+50, text="Buying Price",font=("FreeMono",13), anchor="w",fill="#000000")

		v+=1

		x1,y1,x2,y2=x+150-5-20+10,y+20+15-10-5+50,x+150-5+100+60+6-20+10,y+20+15-10-5+25+6+50

		im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
		add_items_ims[v]=ImageTk.PhotoImage(im)
		can.create_image(x1,y1,image=add_items_ims[v],anchor="nw")

		ent2.place(in_=root,x=x+150-20+10,y=y+20+15-10+50+40)


		add_items_coords["bp"]=[x1,y1,x2,y2]

		can.create_text(x+10+10,y+20+15+50*2, text="Selling Price",font=("FreeMono",13), anchor="w",fill="#000000")

		v+=1

		x1,y1,x2,y2=x+150-5-20+10,y+20+15-10-5+50*2,x+150-5+100+60+6-20+10,y+20+15-10-5+25+6+50*2

		im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
		add_items_ims[v]=ImageTk.PhotoImage(im)
		can.create_image(x1,y1,image=add_items_ims[v],anchor="nw")

		ent3.place(in_=root,x=x+150-20+10,y=y+20+15-10+50*2+40)
	

		add_items_coords["sp"]=[x1,y1,x2,y2]	


		can.create_text(x+10+10,y+20+15+50*3, text="Quantity",font=("FreeMono",13), anchor="w",fill="#000000")

		v+=1

		x1,y1,x2,y2=x+150-5-20+10,y+20+15-10-5+50*3,x+150-5+100+60+6-20+10,y+20+15-10-5+25+6+50*3

		im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
		add_items_ims[v]=ImageTk.PhotoImage(im)
		can.create_image(x1,y1,image=add_items_ims[v],anchor="nw")

		ent4.place(in_=root,x=x+150-20+10,y=y+20+15-10+50*3+40)

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

		text1.place(in_=root,x=x1+15,y=y1+15+40)


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

		x1,y1,x2,y2=x+xx/2-80,y+yy-10-30-20, x+xx/2+80,y+yy-10-20

		im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#000000",alpha=1,width=1)
		add_items_ims[v]=ImageTk.PhotoImage(im)
		can.create_image(x1,y1,image=add_items_ims[v],anchor="nw")

		can.create_text(x+xx/2, y+yy-10-15-20, text="Save", font=("FreeMono",13),fill="#ffffff",anchor="c")

		add_items_coords["save"]=[x1,y1,x2,y2]




		ent1.focus_set()







sb_dict1={}
sb_dict2={}

def draw_v_sb(widget):
    global _scroll_
    global can,can2,can3
    global sb_dict1




    widget_=_scroll_[widget]["widget"]
    sb_widget=_scroll_[widget]["sb_widget"]
    sb_sz=_scroll_[widget]["sb_sz"]
    v_sb_coord=_scroll_[widget]["v_sb_coord"]
    _y=_scroll_[widget]["_y"]
    v=_scroll_[widget]["v"]
    w=_scroll_[widget]["w"]
    h=_scroll_[widget]["h"]

    x=v_sb_coord[0][2]
    y=v_sb_coord[0][0]


    p=v_sb_coord[-1]*h
    sz=h*h/_y







    if p+sz>v_sb_coord[0][1]-y:


        v_sb_coord[-1]=(v_sb_coord[0][1]-(v_sb_coord[0][1]-sz))/h
        v_sb_coord[-1]=1-v_sb_coord[-1]

        _scroll_[widget]["v_sb_coord"]=v_sb_coord
        p=v_sb_coord[-1]*h



    

    try:

        v_=sb_dict1[widget]

    except:

        sb_dict1[widget]=0







    x1,y1,x2,y2=x,y+p, x+sb_sz,y+p+sz

    im=draw_round_rect(5,x1,y1,x2,y2, "#000000","#000000",1)

    sb_dict1[widget]=ImageTk.PhotoImage(im)








    if v==0:

        v=sb_widget.create_image(x,y+p, image=sb_dict1[widget],anchor="nw")


        _scroll_[widget]["v"]=v

    else:

        sb_widget.coords(_scroll_[widget]["v"],x,y+p)



        x1,y1,x2,y2=x,y+p, x+sb_sz,y+p+sz

        im=draw_round_rect(5,x1,y1,x2,y2,"#000000","#000000",1)

        sb_dict1[widget]=ImageTk.PhotoImage(im)


        sb_widget.itemconfig(_scroll_[widget]["v"],image=sb_dict1[widget])



    widget_.yview_moveto(v_sb_coord[-1])


    return [p,p+sz]


def draw_h_sb(widget):

    global _scroll_
    global can,can2,can3
    global h_sb
    global sb_dict2


    widget_=_scroll_[widget]["widget"]
    sb_widget=_scroll_[widget]["sb_widget"]
    sb_sz=_scroll_[widget]["sb_sz"]
    v_sb_coord=_scroll_[widget]["v_sb_coord"]
    h_sb_coord=_scroll_[widget]["h_sb_coord"]
    _y=_scroll_[widget]["_y"]
    h_=_scroll_[widget]["h_"]
    w=_scroll_[widget]["w"]
    h=_scroll_[widget]["h"]
    _x2=_scroll_[widget]["_x2"]

    y=h_sb_coord[0][2]
    x=h_sb_coord[0][0]


    p=h_sb_coord[-1]*w
    sz=w*w/_x2



    if p+sz>h_sb_coord[0][1]-x:


        h_sb_coord[-1]=(h_sb_coord[0][1]-(h_sb_coord[0][1]-sz))/w
        h_sb_coord[-1]=1-h_sb_coord[-1]

        _scroll_[widget]["h_sb_coord"]=h_sb_coord


        p=h_sb_coord[-1]*w





    try:

        v=sb_dict2[widget]

    except:

        sb_dict2[widget]=0



    x1,y1,x2,y2=x+p,y, x+p+sz,y+sb_sz

    im=draw_round_rect(5,x1,y1,x2,y2,"#000000","#000000",1)

    sb_dict2[widget]=ImageTk.PhotoImage(im)



    if _scroll_[widget]["h_"]==0:

        _scroll_[widget]["h_"]=sb_widget.create_image(x+p,y, image=sb_dict2[widget],anchor="nw")
    else:

        sb_widget.coords(_scroll_[widget]["h_"],x+p,y)


        x1,y1,x2,y2=x+p,y, x+p+sz,y+sb_sz

        im=draw_round_rect(5,x1,y1,x2,y2, "#000000","#000000",1)

        sb_dict2[widget]=ImageTk.PhotoImage(im)


        sb_widget.itemconfig(_scroll_[widget]["h_"],image=sb_dict2[widget])




    widget_.xview_moveto(h_sb_coord[-1])



    return [p,p+sz]




def can_b1_sb(widget,_x_,_y_):

    global _scroll_



    #terminal


    #vertical scroll

    if _scroll_[widget]["sb_st"]=="vertical" or _scroll_[widget]["sb_st"]=="both":


	    
	    x1=_scroll_[widget]["v_sb_coord"][0][2]
	    y1=_scroll_[widget]["v_sb_coord"][0][0]

	    x2,y2=x1+_scroll_[widget]["sb_sz"],y1+_scroll_[widget]["h"]

	    var=draw_v_sb(widget)




	    

	    if x1<=_x_<=x2:

	        if y1<=_y_<=y2:

	            _scroll_[widget]["v_drag_st"]=1


	            y=_y_-_scroll_[widget]["v_sb_coord"][0][0]

	            if var[0]<=y<=var[1]:
	                _scroll_[widget]["v_var"]=y-var[0]

	                return

	            

	            _scroll_[widget]["v_sb_coord"][-1]=y/_scroll_[widget]["h"]


	            draw_v_sb(widget)

	            return


    #horizontal

    if _scroll_[widget]["sb_st"]=="horizontal" or _scroll_[widget]["sb_st"]=="both":

	    var=draw_h_sb(widget)



	    x1=_scroll_[widget]["h_sb_coord"][0][0]
	    y1=_scroll_[widget]["h_sb_coord"][0][2]

	    x2,y2=x1+_scroll_[widget]["w"],y1+4+_scroll_[widget]["sb_sz"]

	    if x1<=_x_<=x2:

	        if y1<=_y_<=y2:

	            _scroll_[widget]["h_drag_st"]=1

	            x=_x_-_scroll_[widget]["h_sb_coord"][0][0]

	            if var[0]<=x<=var[1]:

	                _scroll_[widget]["h_var"]=x-var[0]
	                return

	            _scroll_[widget]["h_sb_coord"][-1]=x/_scroll_[widget]["w"]


	            draw_h_sb(widget)

	            return



def sb_drag(widget,_x_,_y_):



    global _scroll_



    #terminal


    #vertical scroll

    if _scroll_[widget]["sb_st"]=="vertical" or _scroll_[widget]["sb_st"]=="both":

	    if _scroll_[widget]["v_drag_st"]==1:
	    
	        x1=_scroll_[widget]["v_sb_coord"][0][2]
	        y1=_scroll_[widget]["v_sb_coord"][0][0]

	        x2,y2=x1+_scroll_[widget]["sb_sz"],y1+_scroll_[widget]["h"]

	        #if x1<=_x_<=x2:

	        



	        if y1<=_y_<=y2:




	            if y1<=_y_-_scroll_[widget]["v_var"]<=y2:

	                y=_y_-_scroll_[widget]["v_sb_coord"][0][0]-_scroll_[widget]["v_var"]


	            

	                _scroll_[widget]["v_sb_coord"][-1]=y/_scroll_[widget]["h"]


	                draw_v_sb(widget)

	                return

	        elif y1-10<_y_<y1:


	            _scroll_[widget]["v_sb_coord"][-1]=0


	            draw_v_sb(widget)

	            return

	        elif y2+10>_y_>y2:


	            _scroll_[widget]["v_sb_coord"][-1]=1


	            draw_v_sb(widget)

	            return

    #horizontal

    if _scroll_[widget]["sb_st"]=="horizontal" or _scroll_[widget]["sb_st"]=="both":



	    if _scroll_[widget]["h_drag_st"]==1:





	        x1=_scroll_[widget]["h_sb_coord"][0][0]
	        y1=_scroll_[widget]["h_sb_coord"][0][2]

	        x2,y2=x1+_scroll_[widget]["w"],y1+4+_scroll_[widget]["sb_sz"]

	        

	        #if y1<=_y_<=y2:

	        if x1<=_x_<=x2:

	            if x1<=_x_-_scroll_[widget]["h_var"]<=x2:



	                x=_x_-_scroll_[widget]["h_sb_coord"][0][0]-_scroll_[widget]["h_var"]

	                _scroll_[widget]["h_sb_coord"][-1]=x/_scroll_[widget]["w"]


	                draw_h_sb(widget)


	                return

	        elif x1-10<_x_<x1:



	            _scroll_[widget]["h_sb_coord"][-1]=0


	            draw_h_sb(widget)

	            return

	        elif x2+10>_x_>x2:



	            _scroll_[widget]["h_sb_coord"][-1]=1


	            draw_h_sb(widget)

	            return





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


man_item_im=0
def process_man_item_im(im):
	global man_items_coords
	global man_items_ims
	global man_item_im

	_x,_y=im.size

	x1,y1,x2,y2=man_items_coords["imagep"]

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

	man_items_ims["image_"]=ImageTk.PhotoImage(im)

	can.delete(man_item_im)

	__x=((x2-x1)-x_)/2
	__y=((y2-y1)-y_)/2

	man_item_im=can.create_image(x1+__x,y1+__y,image=man_items_ims["image_"],anchor="nw")





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

quit=0
added=0
cart_im=0
clear_cart=0
mpesa_logo=0
search=0
no_profile_im=0
no_record=0
def load_im():
	global db
	global sell_items_im,reports_im,manage_items_im,add_items_im,profiles_im
	global sell_items_im2,reports_im2,manage_items_im2,add_items_im2,profiles_im2
	global log_out_im
	global show_p,dshow_p
	global delete
	global crop1,crop2
	global refresh
	global quit
	global added
	global cart_im,clear_cart
	global mpesa_logo
	global search
	global no_profile_im
	global no_record


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


	#quit

	im=Image.open("data/icons/quit.png")
	im=im.resize((25,25))
	quit=ImageTk.PhotoImage(im)


	#added

	im=Image.open("data/icons/added.png")
	im=im.resize((20,20))
	added=ImageTk.PhotoImage(im)


	#quit

	im=Image.open("data/icons/cart.png")
	im=im.resize((25,25))
	cart_im=ImageTk.PhotoImage(im)


	#clear_cart

	im=Image.open("data/icons/clear_cart.png")
	im=im.resize((25,25))
	clear_cart=ImageTk.PhotoImage(im)

	#mpesa logo

	mpesa_logo=Image.open("data/mpesa_logo.png")



	#search

	im=Image.open("data/icons/search.png")
	im=im.resize((25,25))
	search=ImageTk.PhotoImage(im)


	#no_profile_im

	im=Image.open("data/icons/no_profile_im.png")
	im=im.resize((25,25))
	no_profile_im=ImageTk.PhotoImage(im)

	#no_record
	no_record=Image.open("data/icons/no_record.png")

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


	dashboard["width"]=200
	dashboard["height"]=height

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


	if int(dashboard.place_info()["x"])<0:

		x=-int(dashboard["width"])+5+25+5

	else:
		x=0


	dashboard.place(in_=root,x=x,y=0)



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

def login(con=0):
	global can
	global width,height
	global login_im1,login_im2,login_im3,login_im4
	global ent1,ent2,ent3
	global un_login_coord,pw1_login_coord
	global login_coord,register_coord
	global st_
	global show_p,dshow_p
	global _show_



	forget_widgets()

	if con==0:
		delete_widgets()
		entries_show_reset()
		ent2["show"]="*"

	can.delete("all")




	st_="login"




	can["width"]=width
	can["height"]=height
	can["scrollregion"]=(0,0,width,height)
	can["bg"]="#000000"

	can.place(in_=root,x=0,y=0)


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

	ent1.place(in_=root,x=x+150+4.5,y=y+20+15-10)


	un_login_coord=[x1,y1,x2,y2]



	#password



	can.create_text(x+30+4.5,y+20+15+50, text="Password",font=("FreeMono",13), anchor="w",fill="#000000")



	x1,y1,x2,y2=x+150-5+4.5,y+20+15-10-5+50,x+150-5+100+60+6+4.5,y+20+15-10-5+25+6+50

	im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	login_im3=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=login_im3,anchor="nw")


	if ent2["show"]=="*":

		_show_=can.create_image(x2+(34.5-29)/2,y1+((y2-y1)-29)/2,image=show_p,anchor="nw")

	else:

		_show_=can.create_image(x2+(34.5-29)/2,y1+((y2-y1)-29)/2,image=dshow_p,anchor="nw")





	ent2.place(in_=root,x=x+150+4.5,y=y+20+15-10+50)


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


	ent1.focus_set()


cancel_coord=[]
confirm_coord=[]


login_im5=0

pw2_login_coord=[]
def draw_registration(con=0):

	global can
	global width,height
	global login_im1,login_im2,login_im3,login_im4,login_im5
	global ent1,ent2,ent3
	global un_login_coord,pw1_login_coord,pw2_login_coord
	global cancel_coord,confirm_coord
	global st_
	global _show_,show_p,dshow_p


	forget_widgets()

	if con==0:
		delete_widgets()
		entries_show_reset()
		ent2["show"]="*"
		ent3["show"]="*"	


	can.delete("all")

	can.place(in_=root,x=0,y=0)




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

	ent1.place(in_=root,x=x+150+4.5,y=y+20+15-10)


	un_login_coord=[x1,y1,x2,y2]



	#password



	can.create_text(x+30+4.5,y+20+15+50, text="Password",font=("FreeMono",13), anchor="w",fill="#000000")



	x1,y1,x2,y2=x+150-5+4.5,y+20+15-10-5+50,x+150-5+100+60+6+4.5,y+20+15-10-5+25+6+50

	im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	login_im3=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=login_im3,anchor="nw")


	if ent2["show"]=="*":

		_show_=can.create_image(x2+(34.5-29)/2,y1+((y2-y1)-29)/2,image=show_p,anchor="nw")

	else:

		_show_=can.create_image(x2+(34.5-29)/2,y1+((y2-y1)-29)/2,image=dshow_p,anchor="nw")




	ent2.place(in_=root,x=x+150+4.5,y=y+20+15-10+50)


	pw1_login_coord=[x1,y1,x2,y2]


	#password2



	can.create_text(x+30+4.5,y+20+15+50+50, text="Password",font=("FreeMono",13), anchor="w",fill="#000000")



	x1,y1,x2,y2=x+150-5+4.5,y+20+15-10-5+50+50,x+150-5+100+60+6+4.5,y+20+15-10-5+25+6+50+50

	im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	login_im5=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=login_im5,anchor="nw")

	ent3.place(in_=root,x=x+150+4.5,y=y+20+15-10+50+50)


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


	ent1.focus_set()


user_id=None

def valdate_login():
	global can,dashboard
	global width,height
	global ent1,ent2,ent3
	global st
	global user_id


	xx,yy=350,200


	x=(width-xx)/2
	y=(height-yy)/2


	if ent1.get()=="" or ent2.get()=="":

		message(0,can,"Fill all fields!",x+xx/2,y+yy+10+15,xx,30)

		return


	db_user=database.connect("data/users.db")
	cur=db_user.cursor()
	cur.execute("SELECT * FROM users;")
	rows=cur.fetchall()


	con=0
	for row in rows:

		if row[1]==ent1.get() and row[5]==ent2.get():
			user_id=row[0]
			con=1

	

	if con==0:

		message(0,can,"Invalid Entry!",x+xx/2,y+yy+10+15,xx,30)

		return





	forget_widgets()
	entries_show_reset()

	can.delete("all")
	
	can["width"]=width
	can["height"]=width
	can["scrollregion"]=(0,0,width,height)
	can["bg"]="#ffffff"


	dashboard.place(in_=root,x=0,y=0)

	st="Sell Items"

	draw_db()

	main()

def validate_registration():
	global width,height
	global can
	global ent1,ent2,ent3

	xx,yy=350,250


	x=(width-xx)/2
	y=(height-yy)/2


	if ent1.get()=="" or ent2.get()=="" or ent3.get()=="":

		message(0,can,"Fill all fields!",x+xx/2,y+yy+10+15,xx,30)

		return

	if ent2.get()!=ent3.get():

		message(0,can,"Password doesn't match!",x+xx/2,y+yy+10+15,xx,30)

		return


	db_user=database.connect("data/users.db")
	cur=db_user.cursor()

	v=0

	cur.execute("SELECT * FROM users")
	rows=cur.fetchall()


	ids=[]


	for row in rows:
		if row[1].lower() == ent1.get().lower():

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



			






	cur.execute("INSERT INTO users VALUES("+str(v)+",'"+ent1.get()+"','""','""','""','"+str(ent2.get())+"',"+str(0)+")")

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
	global mess_v

	try:


		mess_v[3].delete(mess_v[1])
		mess_v[3].delete(mess_v[2])

		mess_v=[0,0,0,0,0]

		mess_con=False

	except:
		pass


	if con==0:
		col="#ff0000"
		col2="#000000"
	elif con==1:
		col="#00ff00"
		col2="#000000"


	x1,y1,x2,y2=cx-w/2,cy-h/2, cx+w/2,cy+h/2



	im=draw_round_rect(15,x1,y1,x2,y2, col,col2=col,alpha=1,width=1)
	mess_v[0]=ImageTk.PhotoImage(im)
	mess_v[1]=_can_.create_image(cx,cy,image=mess_v[0],anchor="c")
	mess_v[2]=_can_.create_text(cx,cy,text=mess,font=("FreeMono",13),fill=col2)

	mess_v[3]=_can_
	mess_v[4]=time.time()

	mess_con=True


root=tk.Tk()


width_,height_=root.winfo_screenwidth(),root.winfo_screenheight()
width,height=width_-80,height_-100

root.geometry(f"{width}x{height}+0+0")

root.minsize(width,height)
root.maxsize(width_,height_)

sz=root.geometry().split("+")[0].split("x")
w,h=int(sz[0]),int(sz[1])
cur_sz=[w,h]

def can_b1(e):
	global can,dashboard
	global un_login_coord,	pw1_login_coord
	global ent1,ent2,ent3,ent4,text1
	global login_coord,register_coord
	global cancel_coord,confirm_coord
	global st_
	global _show_,show_p,dshow_p
	global add_items_coords,add_items_ims,add_item_im
	global items_ar
	global sel_item
	global man_item
	global qp
	global add_c_coord
	global cart_ar
	global search_focus
	global man_reset_st


	if st_=="main" and search_focus==True:

		if st=="Sell Items" or st=="Manage items": 

			search_focus=False


			main(1)




	


	if st_=="login":

		x,y=can.coords(_show_)

		if x<=e.x<=x+29:
			if y<=e.y<=y+29:

				if ent2["show"]=="*":
					ent2["show"]=""
					can.itemconfig(_show_,image=dshow_p)
				else:
					ent2["show"]="*"
					can.itemconfig(_show_,image=show_p)


				return


		x1,y1,x2,y2=un_login_coord

		if x1<=e.x<=x2:
			if y1<=e.y<=y2:

				ent1.focus_set()

				return


		x1,y1,x2,y2=pw1_login_coord

		if x1<=e.x<=x2:
			if y1<=e.y<=y2:

				ent2.focus_set()

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

				if ent2["show"]=="*":
					ent2["show"]=""
					ent3["show"]=""
					can.itemconfig(_show_,image=dshow_p)
				else:
					ent2["show"]="*"
					ent3["show"]="*"
					can.itemconfig(_show_,image=show_p)


				return



		x1,y1,x2,y2=un_login_coord

		if x1<=e.x<=x2:
			if y1<=e.y<=y2:

				ent1.focus_set()

				return


		x1,y1,x2,y2=pw1_login_coord

		if x1<=e.x<=x2:
			if y1<=e.y<=y2:

				ent2.focus_set()

				return




		x1,y1,x2,y2=pw2_login_coord

		if x1<=e.x<=x2:
			if y1<=e.y<=y2:

				ent3.focus_set()

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





		if st=="Sell Items":

			if sel_item==None:

				for i in items_ar:

					x1,y1,x2,y2=i[1:]

					if x1<=e.x<=x2:
						if y1<=can.canvasy(e.y)<=y2:

							draw_selected_item(i[0])

							return
			else:

				x,y=qp


				if x<=e.x<=x+25:
					if y<=can.canvasy(e.y)<=y+25:


						sel_item=None
						qp=None

						main(1)

						return



				x=int(dashboard.place_info()["x"])+int(dashboard["width"])


				xx,yy=int(can["width"])-int(dashboard["width"])-60,int(int(can["height"])*0.6)


				x=x+((int(can["width"])-x)-xx)/2
				y=can.canvasy(40+((int(can["height"])-40)-yy)/2)-20



				x1,y1,x2,y2=add_c_coord

				cx,cy=x1+15,y1+15

				r=math.sqrt((e.x-cx)**2+(can.canvasy(e.y)-cy)**2)

				if r<=15:

					try:
						v1=int(ent1.get())
						v2=int(ent2.get())

					except:

						message(0,can,"Invalid input!",x+xx/2,y+yy+10+15,350,30)

						return


					cart_ar.append([sel_item,ent1.get(),ent2.get()])

					#sel_item=None
					#qp=None

					main(1)

					message(1,can,"Item added to cart!",x+xx/2,y+yy+10+15,350,30)

					return

				cx,cy=x2-15,y1+15

				r=math.sqrt((e.x-cx)**2+(can.canvasy(e.y)-cy)**2)

				if r<=15:


					try:
						v1=int(ent1.get())
						v2=int(ent2.get())

					except:

						message(0,can,"Invalid input!",x+xx/2,y+yy+10+15,350,30)

						return


					cart_ar.append([sel_item,ent1.get(),ent2.get()])

					#sel_item=None
					#qp=None

					main(1)

					message(1,can,"Item added to cart!",x+xx/2,y+yy+10+15,350,30)

					return


				if x1+15<=e.x<=x2-15:
					if y1<=can.canvasy(e.y)<=y2:


						try:
							v1=int(ent1.get())
							v2=int(ent2.get())

						except:

							message(0,can,"Invalid input!",x+xx/2,y+yy+10+15,350,30)

							return


						cart_ar.append([sel_item,ent1.get(),ent2.get()])

						#sel_item=None
						#qp=None

						main(1)

						message(1,can,"Item added to cart!",x+xx/2,y+yy+10+15,350,30)


						return

		elif st=="Manage items":



			if man_item==None:

				for i in items_ar:

					x1,y1,x2,y2=i[1:]

					if x1<=e.x<=x2:
						if y1<=can.canvasy(e.y)<=y2:


							draw_manage_item(i[0],0)

							return
			else:

				x,y=qp


				if x<=e.x<=x+25:
					if y<=can.canvasy(e.y)<=y+25:


						man_item=None
						qp=None

						main(1)

						return

				xx,yy=700,430

				if int(dashboard.place_info()["x"])==0:

					x=int(dashboard["width"])

				else:
					x=5+25+5

				x=x+((width-x)-xx)/2
				y=can.canvasy(((height-40)-yy)/2)

				x1,y1,x2,y2=man_items_coords["item name"]

				if x1<=e.x<=x2:
					if y1<=e.y<=y2:
						ent1.focus_set()
						return

				x1,y1,x2,y2=man_items_coords["bp"]

				if x1<=e.x<=x2:
					if y2<=e.y<=y2:
						ent2.focus_set()
						return


				x1,y1,x2,y2=man_items_coords["sp"]

				if x1<=e.x<=x2:
					if y1<=e.y<=y2:
						ent3.focus_set()
						return

				x1,y1,x2,y2=man_items_coords["q"]

				if x1<=e.x<=x2:
					if y1<=e.y<=y2:
						ent4.focus_set()
						return

				x1,y1,x2,y2=man_items_coords["desc"]

				if x1<=e.x<=x2:
					if y1<=e.y<=y2:
						text1.focus_set()
						return

				if not man_items_coords["add_image"]==None:


					cx,cy=man_items_coords["add_image"]

					r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

					if r<=40:

						file=filedialog.askopenfilename()
						





						try:
							im=Image.open(file)

							man_items_ims["image"]=im

							main(1)


						except Exception as e:
							print(e)
							message(0,can,"Can't process image!",x+xx/2,y+yy+10+15,350,30)

						return
				x1,y1=man_items_coords["delete"]

				if x1<=e.x<=x1+25:
					if y1<=e.y<=y1+25:

						man_items_ims["image"]=0


						main(1)

						return

				#reset

				x1,y1,x2,y2=man_items_coords["reset"]

				cx,cy=x1+15,y1+15

				r=math.sqrt((e.x-cx)**2+(can.canvasy(e.y)-cy)**2)

				if r<=15:

					man_reset_st=True
					main(1)

					message(1,can,"Item details reseted!",x+xx/2,y+yy+10+15,350,30)
					return

				cx,cy=x2-15,y1+15

				r=math.sqrt((e.x-cx)**2+(can.canvasy(e.y)-cy)**2)

				if r<=15:

					man_reset_st=True
					main(1)
					message(1,can,"Item details reseted!",x+xx/2,y+yy+10+15,350,30)
					return

				if x1+15<=e.x<=x2-15:
					if y1<=can.canvasy(e.y)<=y2:
						man_reset_st=True
						main(1)
						message(1,can,"Item details reseted!",x+xx/2,y+yy+10+15,350,30)
						return



				#delete





				if int(dashboard.place_info()["x"])<0:
					_x=5+25+5
				else:
					_x=int(dashboard["width"])
				x_=_x+(int(can["width"])-_x)/2

				


				x1,y1,x2,y2=man_items_coords["_delete_"]

				cx,cy=x1+15,y1+15

				r=math.sqrt((e.x-cx)**2+(can.canvasy(e.y)-cy)**2)

				if r<=15:

					man_items_delete()
					main(1)

					message(1,can,"Item removed!",x_,can.canvasy(int(can["height"])-20-15),350,30)
					return

				cx,cy=x2-15,y1+15

				r=math.sqrt((e.x-cx)**2+(can.canvasy(e.y)-cy)**2)

				if r<=15:

					man_items_delete()
					main(1)
					message(1,can,"Item removed!",x_,can.canvasy(int(can["height"])-20-15),350,30)
					return

				if x1+15<=e.x<=x2-15:
					if y1<=can.canvasy(e.y)<=y2:
						man_items_delete()
						main(1)
						message(1,can,"Item removed!",x_,can.canvasy(int(can["height"])-20-15),350,30)
						return




				#save

				x1,y1,x2,y2=man_items_coords["save"]


				cx,cy=x1+15,y1+15

				r=math.sqrt((e.x-cx)**2+(can.canvasy(e.y)-cy)**2)

				if r<=15:




					res=man_items_save()

					if res[0]==1:

						main(1)

					message(res[0],can,res[1],x+xx/2,y+yy+10+15,350,30)

					return

				cx,cy=x2-15,y1+15

				r=math.sqrt((e.x-cx)**2+(can.canvasy(e.y)-cy)**2)

				if r<=15:

					res=man_items_save()

					if res[0]==1:

						main(1)

					message(res[0],can,res[1],x+xx/2,y+yy+10+15,350,30)
					return

				if x1+15<=e.x<=x2-15:
					if y1<=can.canvasy(e.y)<=y2:
						res=man_items_save()

						if res[0]==1:

							main(1)

						message(res[0],can,res[1],x+xx/2,y+yy+10+15,350,30)
						return







		elif st=="Add Items":

			xx,yy=700,430

			if int(dashboard.place_info()["x"])==0:

				x=int(dashboard["width"])

			else:
				x=5+25+5

			x=x+((width-x)-xx)/2
			y=((height-40)-yy)/2

			x1,y1,x2,y2=add_items_coords["item name"]

			if x1<=e.x<=x2:
				if y1<=e.y<=y2:
					ent1.focus_set()
					return

			x1,y1,x2,y2=add_items_coords["bp"]

			if x1<=e.x<=x2:
				if y2<=e.y<=y2:
					ent2.focus_set()
					return


			x1,y1,x2,y2=add_items_coords["sp"]

			if x1<=e.x<=x2:
				if y1<=e.y<=y2:
					ent3.focus_set()
					return

			x1,y1,x2,y2=add_items_coords["q"]

			if x1<=e.x<=x2:
				if y1<=e.y<=y2:
					ent4.focus_set()
					return

			x1,y1,x2,y2=add_items_coords["desc"]

			if x1<=e.x<=x2:
				if y1<=e.y<=y2:
					text1.focus_set()
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
	global ent1,ent2,ent3,ent4,text1
	global add_items_ims



	xx,yy=700,410

	if int(dashboard.place_info()["x"])==0:

		x=int(dashboard["width"])

	else:
		x=5+25+5

	x=x+((width-x)-xx)/2
	y=40+((height-40)-yy)/2

	

	if ent1.get()=="" or ent2.get()=="" or ent3.get()=="" or ent4.get()=="":

		message(0,can,"Fill essential fields!",x+xx/2,y+yy+10+15,350,30)

		return

	try:
		bp_=int(ent2.get())
	except:
		message(0,can,"Some fields must be a number!",x+xx/2,y+yy+10+15,350,30)
		return


	try:
		sp_=int(ent3.get())
	except:
		message(0,can,"Some fields must be a number!",x+xx/2,y+yy+10+15,350,30)
		return

	try:
		q_=int(ent4.get())
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
	name_=ent1.get()
	bp_=int(ent2.get())
	sp_=int(ent3.get())
	qt_=int(ent4.get())
	desc_=text1.get("1.0",tk.END)[:-1]


	if add_items_ims["image"]!=0:

		image=f"{item_id}.png"

	else:
		image=""





	cur.execute("INSERT INTO items VALUES("+str(item_id)+",'"+str(name_)+"',"+str(bp_)+","+str(sp_)+","+str(qt_)+",'"+str(desc_)+"','"+str(image)+"')")

	db_items.commit()


	if add_items_ims["image"]!=0:

		os.makedirs("data/images",exist_ok=True)

		add_items_ims["image"].save(f"data/images/{item_id}.png")

		scale_down_im(f"{item_id}.png",1,140,85)

	main()

	message(1,can,"Item added successfullly!",x+xx/2,y+yy+10+15,350,30)



can=tk.Canvas(width=width,height=height,relief="flat",bg="#ffffff",highlightthickness=0,border=0)
can.place(in_=root,x=0,y=0)
can.bind("<Button-1>",can_b1)


def can2_b1(e):
	global search_coords
	global search_focus
	global sel_item
	global search_val
	global st_,st

	if sel_item==None and st_=="main":

		if search_focus==False:


			x1,y1,x2,y2=search_coords[:-1]


			cx,cy=x1+15,y1+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:


				search_focus=True

				main(1)

				return



			cx,cy=x2-15,y1+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:


				search_focus=True

				main(1)

				return


			if x1+15<=e.x<=x2-15:

				if y1<=e.y<=y2:



					search_focus=True

					main(1)

					return




		x,y=search_coords[-1]


		if x<=e.x<=x+25:
			if y<=e.y<=y+25:

				search_val=""
				ent_search.delete(0,tk.END)
				search_focus=False

				main(1)

				return

		if search_focus==True:			

				search_focus=False

				main(1)




can2=tk.Canvas(width=width,height=40,relief="flat",bg="#ffffff",highlightthickness=0,border=0)
can2.bind("<Button-1>",can2_b1)
def can3_b1(e):
	global sel_item
	global man_item
	global cart_ar
	global cart_buttons_coords
	global can,dashboard
	global search_focus
	global st_,st

	if st_=="main" and search_focus==True:



		if st=="Sell Items" or st=="Manage items":

			search_focus=False

			main(1)


	if sel_item==None and man_item==None:

		can_b1_sb("can",e.x,e.y)
		can_b1_sb("cart",e.x,e.y)





	if sel_item==None:




		#clear cart

		if len(cart_ar)>0:


			if int(dashboard.place_info()["x"])<0:
				_x=5+25+5
			else:
				_x=int(dashboard["width"])
			x_=_x+(int(can["width"])-_x)/2



			x1,y1,x2,y2=cart_buttons_coords["clear_cart"]

			cx,cy=x1+15,y1+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:

				cart_ar=[]
				main(1)



				message(1,can,"Cart Cleared!",x_,can.canvasy(int(can["height"])-20-15),350,30)
				return

			cx,cy=x2-15,y1+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:

				cart_ar=[]
				main(1)
				message(1,can,"Cart Cleared!",x_,can.canvasy(int(can["height"])-20-15),350,30)
				return

			if x1+15<=e.x<=x2-15:
				if y1<=e.y<=y2:
					cart_ar=[]
					main(1)
					message(1,can,"Cart Cleared!",x_,can.canvasy(int(can["height"])-20-15),350,30)
					return


def can3_b1_motion(e):
	global sel_item

	if sel_item==None:	

		sb_drag("can",e.x,e.y)
		sb_drag("cart",e.x,e.y)

def can3_b1_sb_release(widget):

    global _scroll_


    _scroll_[widget]["v_drag_st"]=0
    _scroll_[widget]["h_drag_st"]=0

def can3_b1_release(e):

	can3_b1_sb_release("can")
	can3_b1_sb_release("cart")

can3=tk.Canvas(width=400,height=height-40,relief="flat",bg="#ffffff",highlightthickness=0,border=0)
can3.bind("<Button-1>",can3_b1)
can3.bind("<B1-Motion>",can3_b1_motion)
can3.bind("<ButtonRelease-1>",can3_b1_release)



can["scrollregion"]=(0,0,width,height)


can4=tk.Canvas(relief="flat",bg="#ffffff",highlightthickness=0,border=0)


db_st=0
def dashboard_b1(e):
	global dashboard
	global db_st
	global db_items
	global st
	global search_val
	global cart_ar

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

		search_val=""
		cart_ar=[]

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

def ent1_r(e):
	global ent2

	ent2.focus_set()


def ent2_r(e):
	global st_
	global ent3

	if st_=="login":
		valdate_login()
	elif st_=="register":

		ent3.focus_set()

def ent3_r(e):
	global st_
	global ent4

	if st_=="register":

		validate_registration()



ent1=tk.Entry(width=17, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,selectbackground="#000000",selectforeground="#ffffff")
ent1.bind("<Return>",ent1_r)

ent2=tk.Entry(width=17, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,show="*",selectbackground="#000000",selectforeground="#ffffff")
ent2.bind("<Return>",ent2_r)

ent3=tk.Entry(width=17, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,show="*",selectbackground="#000000",selectforeground="#ffffff")
ent3.bind("<Return>",ent3_r)


ent4=tk.Entry(width=17, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,selectbackground="#000000",selectforeground="#ffffff")
ent5=tk.Entry(width=17, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,selectbackground="#000000",selectforeground="#ffffff")
ent6=tk.Entry(width=17, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,selectbackground="#000000",selectforeground="#ffffff")
ent7=tk.Entry(width=17, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,selectbackground="#000000",selectforeground="#ffffff")

search_focus=False
def search_b1(e):
	global search_focus

	search_focus=True

	main(1)


def check_search_entry():

	global search_focus
	global search_val

	if search_focus==True:

		if search_val!=ent_search.get():

			search_val=ent_search.get()

			main(1)

	root.after(1,check_search_entry)



ent_search=tk.Entry(width=25, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,selectbackground="#000000",selectforeground="#ffffff")
ent_search.bind("<Button-1>",search_b1)

text1=tk.Text(width=28,height=4, font=("FreeMono",13),bg="#ffffff",relief="flat",highlightthickness=0,border=0,selectbackground="#000000",selectforeground="#ffffff")


t_widgets={"entries":[ent1,ent2,ent3,ent4,ent_search],
			"text":[text1],
			"canvas":[dashboard,can,can2,can3,can4]}

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
		pic VARCHAR(255),
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


def scale_down_im(im_,con,x,y,save_path="data/images"):

	x1_,y1_,x2_,y2_=0,0,x,y


	im=Image.open(f"data/images/{im_}")
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

	im.save(f"{save_path}/{im_.replace(".png",f"_{con}.png")}")


"""

db_items=database.connect("data/items.db")
cur=db_items.cursor()


cur.execute("SELECT * FROM items")
rows=cur.fetchall()



for row in rows:

	if row[6]!="":
	
		scale_down_im(row[6],1,140,85)


"""

st="Sell Items"

check_root_sz()
check_sel_item()
check_search_entry()
root.mainloop()
