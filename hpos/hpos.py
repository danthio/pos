import tkinter as tk
from tkinter import font
from PIL import Image,ImageTk,ImageDraw
import math

import sqlite3 as database

import time

from tkinter import filedialog

import os
import datetime


"""
def linear_regression(y_values):
    n = len(y_values)

    # x values are simply 1, 2, 3, ...
    x_values = list(range(1, n + 1))

    x_mean = sum(x_values) / n
    y_mean = sum(y_values) / n

    # Calculate slope (b1)
    numerator = sum(
        (x - x_mean) * (y - y_mean)
        for x, y in zip(x_values, y_values)
    )

    denominator = sum(
        (x - x_mean) ** 2
        for x in x_values
    )

    b1 = numerator / denominator

    # Calculate intercept (b0)
    b0 = y_mean - b1 * x_mean

    return b0, b1


# Example
y = [45, 50, 60, 65, 72]

b0, b1 = linear_regression(y)

print("Intercept:", b0)
print("Slope:", b1)

# Predict the next value (x = 6)
x = 6
prediction = b0 + b1 * x

print("Prediction:", prediction)

θ=tan−1(1)=45∘

"""


add_items_ims={}

add_items_coords={}

add_item_im=0

#+254769167904
"""


db_reports=database.connect("data/reports.db")
cur=db_reports.cursor()


cur.execute("SELECT * FROM reports")
rows=cur.fetchall()



for row in rows:
	print(row)

"""
def formart_number(no,x,con=0):

	f=font.Font(family="FreeMono",size=13)

	if con==1:

		l=f.measure(str(no))+f.measure("Ksh.")
	else:
		l=f.measure(str(no))

	if l>x:


		no=int(no)


		if no>=1000000000:

			return f"{round(no/1000000000,1)} B"

		elif no>=1000000:
			return f"{round(no/1000000,1)} B"

		elif no>=1000:
			return f"{round(no/1000,1)} K"

		else:
			return f"{no}"

	else:
		return f"{no}"


def format_text(txt,x):

	f=font.Font(family="FreeMono",size=13)


	if f.measure(txt)<=x:

		return txt


	else:

		_txt_=""

		for t in txt:


			if f.measure(_txt_+"...")>x:


				return _txt_[:-1]+"..."

			else:

				_txt_+=t


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
	global sel_totalx

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
				can.itemconfig(sel_total,text=f"Ksh.{formart_number(v1*v2,sel_totalx,1)}")


			sel_item_ent_d=data

	root.after(1,check_sel_item)



		




sel_err1=0
sel_err2=0
sel_total=0
qp=None
add_c_coord=[]
sel_totalx=0
def draw_selected_item(id_,con):
	global can,sel_item,sell_items_ims
	global dashboard,can,can2,can3,can4
	global quit,qp
	global ent1,ent2
	global add_c_coord
	global sel_err1,sel_err2,sel_total
	global sel_item_ent_d
	global sel_totalx

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

	xx,yy=int(can["width"])-int(dashboard["width"])-60,int(int(can["height"])*0.7)





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



	can.create_text(x1+((x2-270)-x1)/2,y1+20,text=format_text(name,(x2-270)-x1-20),font=("FreeMono",13),fill="#0000ff",anchor="c")

	can.create_line(x2-270, y1+10, x2-270,y2-10,fill="#000000")
	

	x1_,y1_,x2_,y2_=x1+10,y1+40,x2-270-10,y2-50

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

	can.create_text(x1+((x2-270)-x1)/2,y2-25,text=format_text(desc.replace("\n",""),(x2-270)-x1-20),fill="#000000",font=("FreeMono",13),anchor="c")




	can.create_text(x2-270+10,y1+30+30, text="Selling Price", font=("FreeMono",13),fill="#000000",anchor="w")
	can.create_text(x2-270+10+f.measure("Selling Price")+30,y1+30+30,text=f"Ksh.{formart_number(sp,((x2-10)-(x2-270+10+f.measure("Selling Price")+30)),1)}", font=("FreeMono",13),fill="#ff0000",anchor="w")


	can.create_text(x2-270+10,y1+30+30+40, text="Items Left", font=("FreeMono",13),fill="#000000",anchor="w")
	can.create_text(x2-270+10+f.measure("Selling Price")+30,y1+30+30+40,text=str(formart_number(qt,((x2-10)-(x2-270+10+f.measure("Selling Price")+30)))), font=("FreeMono",13),fill="#ff0000",anchor="w")


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

	if con==0:
		ent1.delete(0,tk.END)
		ent1.insert(tk.END,str(sp))


	ent1.place(in_=root,x=x1+5,y=_y_+5+40-can.canvasy(0))

	sel_err1=can.create_text(x1,y2+5,text="",fill="#ff0000",font=("FreeMono",9),anchor="w")





	v+=1

	im=draw_round_rect(5,x1,y1+40+10,x2,y2+40+10, "#000000",alpha=1,width=1)
	sell_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1+40+10,image=sell_items_ims[v],anchor="nw")


	if con==0:
		ent2.delete(0,tk.END)
		ent2.insert(tk.END,str(1))


	ent2.place(in_=root,x=x1+5,y=y1+5+40-can.canvasy(0)+40+10)

	sel_err2=can.create_text(x1,y2+40+10+5,text="",fill="#ff0000",font=("FreeMono",9),anchor="w")

	can.create_text(x+xx-270+10,y1+40+10+31/2, text="Quantity", font=("FreeMono",13),fill="#000000",anchor="w")

	sel_item_ent_d=[ent1.get(),ent2.get()]




	x1,y1,x2,y2=x,y-20, x+xx,y+yy-20

	




	can.create_text(x2-270+10,y2-10-30-10-30, text="Total", font=("FreeMono",13),fill="#000000",anchor="w")


	sel_total=can.create_text(x2-10,y2-10-30-10-30, text=f"Ksh.{formart_number(int(ent1.get())*int(ent2.get()),((x2-10)-(x2-270+10+f.measure("Total")+30)),1)}", font=("FreeMono",13),fill="#ff0000",anchor="e")

	sel_totalx=((x2-10)-(x2-270+10+f.measure("Total")+30))


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

	



	desc=text1.get("1.0",tk.END)

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
	global save_im,delete2,reset_im
	global man_item_crop_v
	global man_item_crop_coord_norm



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


	

	man_items_coords["imagep"]=[x1+15,y1+15, x2-15,y2-15]






	can.create_image(x2-25,y2+5,image=delete,anchor="nw")
	man_items_coords["delete"]=[x2-25,y2+5]



	if man_item_crop_v[0]==False:
	

		can.create_image(x2-25-10-25,y2+5,image=crop2,anchor="nw")

	elif man_item_crop_v[0]==True:

		if len(man_item_crop_v[1])>0:

			if len(man_item_crop_v[1][-1])==2:

				x_,y_=man_item_crop_coord_norm

				x_+=x
				y_+=y
				man_item_crop_v[1][-1]=[x_,y_]



		can.create_image(x2-25-10-25,y2+5,image=crop1,anchor="nw")


	man_items_coords["crop"]=[x2-25-10-25,y2+5]
	can.create_image(x2-25-10-25-10-25,y2+5,image=refresh,anchor="nw")
	man_items_coords["refresh"]=[x2-25-10-25-10-25,y2+5]

	#print((y2+5+25+10+30+10)-y,"h")

	if con==0:

		if im_!="":


			man_items_ims["image"]=Image.open(f"data/images/{im_}")
			man_items_ims["_image_"]=man_items_ims["image"]

		else:

			man_items_ims["image"]=0


		man_item_crop_v=[False,[]]


	if not man_items_ims["image"]==0:

		process_man_item_im(man_items_ims["image"])

		man_items_coords["add_image"]=None

		can.create_rectangle(man_items_coords["imagep_"],outline="#000000")

	else:


		v+=1

		cx,cy=x1+(x2-x1)/2,y1+(y2-y1-80-20-15)/2+40

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

	_x=x1+((x2-x1)-(20+10+f.measure("Reset")))/2

	can.create_image(_x,y+yy-10-15-20-10,image=reset_im,anchor="nw")

	can.create_text(_x+20+10, y+yy-10-15-20, text="Reset", font=("FreeMono",13),fill="#ffffff",anchor="w")

	man_items_coords["reset"]=[x1,y1,x2,y2]


	v+=1

	x1,y1,x2,y2=x+x_*2-80,y+yy-10-30-20, x+x_*2+80,y+yy-10-20

	im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#000000",alpha=1,width=1)
	man_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=man_items_ims[v],anchor="nw")

	_x=x1+((x2-x1)-(20+10+f.measure("Delete")))/2

	can.create_image(_x,y+yy-10-15-20-10,image=delete2,anchor="nw")


	can.create_text(_x+20+10, y+yy-10-15-20, text="Delete", font=("FreeMono",13),fill="#ffffff",anchor="w")

	man_items_coords["_delete_"]=[x1,y1,x2,y2]



	v+=1

	x1,y1,x2,y2=x+x_*3-80,y+yy-10-30-20, x+x_*3+80,y+yy-10-20

	im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#000000",alpha=1,width=1)
	man_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=man_items_ims[v],anchor="nw")


	_x=x1+((x2-x1)-(20+10+f.measure("Save")))/2

	can.create_image(_x,y+yy-10-15-20-10,image=save_im,anchor="nw")

	can.create_text(_x+20+10, y+yy-10-15-20, text="Save", font=("FreeMono",13),fill="#ffffff",anchor="w")

	man_items_coords["save"]=[x1,y1,x2,y2]


	ent1.focus_set()



cb_v=""
def check_balance():
	global pay_st
	global bal_,_total_
	global ent1
	global cb_v


	if pay_st=="Cash":

		if cb_v!=ent1.get():

			try:

				v_=int(ent1.get())


				can.itemconfig(bal_,text=f"Ksh.{int(int(ent1.get())-_total_)}")



			except:

				can.itemconfig(bal_,text="")


			cb_v=ent1.get()



	root.after(1,check_balance)





def complete_payment():

	global cart_ar
	global user_name


	con=0

	try:


		date_time=datetime.datetime.now()




		for i in cart_ar:




			id_,sold_at,quantity=i

			db_items=database.connect("data/items.db")
			cur=db_items.cursor()


			cur.execute("SELECT * FROM items WHERE item_id="+str(id_)+"")

			row=cur.fetchall()[0]

			name=row[1]
			bp=row[2]
			sp=row[3]
			q=row[4]



			db_reports=database.connect("data/reports.db")
			cur2=db_reports.cursor()

			cur2.execute(f"INSERT INTO reports VALUES('{name}','{date_time}','{user_name}',{quantity},{bp},{sp},{sold_at})")

			db_reports.commit()


			cur.execute(f"UPDATE items SET quantity={int(q)-int(quantity)} WHERE item_id={id_}")
			db_items.commit()



		con=1



	except Exception as e:

		print(e)
		pass



	return con




	





pay_st=None
bal_=0
_total_=0

sell_items_coords={}

v4,h4=0,0
def pay_with_cash(con):
	global sell_items_ims
	global pay_st
	global can,can2,can3,can4,can5
	global quit,qp
	global sel_sb
	global cart_im
	global bal_,_total_
	global sell_items_coords
	global v4,h4



	pay_st="Cash"

	if con==0:
		ent1.delete(0,tk.END)






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

	sell_items_ims["can4_overlay_"]=can4.create_image(0,can4.canvasy(0),image=sell_items_ims["can4_overlay"],anchor="nw")



	x=int(dashboard.place_info()["x"])+int(dashboard["width"])

	xx,yy=int(can["width"])-int(dashboard["width"])-60,int(int(can["height"])*0.7)



	v=len(sell_items_ims)+1



	x=x+((int(can["width"])-x)-xx)/2
	y=can.canvasy(40+((int(can["height"])-40)-yy)/2)


	x1,y1,x2,y2=x,y,x+xx,y+yy

	im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#ffffff",alpha=1,width=1)

	sell_items_ims[v]=ImageTk.PhotoImage(im)

	can.create_image(x1,y1,image=sell_items_ims[v],anchor="nw")


	can.create_polygon(x1+(x2-x1)/2-100,y1+2, x1+(x2-x1)/2+100,y1+2,
		x1+(x2-x1)/2+100-15,y1+32, x1+(x2-x1)/2-100+15,y1+32,fill="#000000",outline="#000000")



	can.create_text(x+xx/2,y1+1+15,text="Pay with Cash",font=("FreeMono",13),fill="#ffffff",anchor="c")


	can.create_line(x1+(x2-x1)/2-200,y1+2, x1+(x2-x1)/2+200,y1+2,fill="#000000")


	can.create_image(x2-5-25,y1+5,image=quit,anchor="nw")

	qp=[x2-5-25,y1+5]

	can.create_line(x2-270,y1+40, x2-270,y2-15)


	


	x1,y1,x2,y2=x1+15,y1+35+30,x2-270-4-10-4,y2-15-4-10-4

	x_=x1+((x2-x1)-(25+10+f.measure("Cart")))/2

	can.create_image(x_,y1-30+(30-25)/2,image=cart_im,anchor="nw")
	can.create_text(x_+25+10,y1-30+15,text="Cart",font=("FreeMono",13),fill="#000000",anchor="w")

	v+=1

	im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#ffffff",alpha=1,width=1)

	sell_items_ims[v]=ImageTk.PhotoImage(im)

	can.create_image(x1,y1,image=sell_items_ims[v],anchor="nw")


	can5["width"]=int(x2-x1)-2
	can5["height"]=int(y2-y1)-15-15

	can5["bg"]="#ffffff"

	can5.place(in_=root,x=x1+1,y=y1+15-can.canvasy(0)+40)


	can5["scrollregion"]=(0,0,int(can5["width"]),int(can5["height"]))

	can5.delete("all")

	

	dict_={"widget": can5,
			"sb_widget":can,
			"sb_st":"both",
			"sb_sz":10,
			"v_sb_coord":[(y1+15,y1+15+int(can5["height"]),x2+4,x2+4+10,0),0],
			"h_sb_coord":[(x1+1,x1+1+int(can5["width"]),y2+4,y2+4+10),0],
			"_y":int(can5["height"]),
			"v":v4,
			"h_":h4,
			"w":int(can5["width"]),
			"h":int(can5["height"]),
			"_x":int(can5["width"]),
			"_x2":int(can5["width"]),
			"scrollregion":can5["scrollregion"],
			"v_drag_st":0,
			"h_drag_st":0,
			"v_var":0,
			"h_var":0


			}

	_scroll_["cart2"]=dict_


	db_items=database.connect("data/items.db")
	cur=db_items.cursor()


	_y=0

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


		can5.create_text(5,_y+15,text=name,font=("FreeMono",13),fill="#0000ff",anchor="w")

		if int(quantity)==1:
			q="Unit"
		else:
			q="Units"
		can5.create_text(5,_y+15+30+10,text=q,font=("FreeMono",13),fill="#000000",anchor="w")
		can5.create_text(5+f.measure("Total")+20,_y+15+30+10,text=str(formart_number(quantity,(int(can4["width"]))-(5+f.measure("Total")+20))),font=("FreeMono",13),fill="#ff0000",anchor="w")
		can5.create_text(5,_y+15+30+10+30,text="Total",font=("FreeMono",13),fill="#000000",anchor="w")
		can5.create_text(5+f.measure("Total")+20,_y+15+30+10+30,text=f"Ksh.{formart_number(int(sold_at)*int(quantity),(int(can4["width"]))-(5+f.measure("Total")+20),1)}",font=("FreeMono",13),fill="#ff0000",anchor="w")

		_y+=15+30+10+30+20

		can5.create_line(0,_y, int(can5["width"]),_y,fill="#000000")


		no_items+=int(quantity)
		total+=int(sold_at)*int(quantity)
		discount+=(int(sp)-int(sold_at))*int(quantity)


	_y+=10





	if _y<=int(can5["height"]):

		_scroll_["cart"]["_y"]=int(can5["height"])

		can5["scrollregion"]=(0,0,int(can5["width"]),int(can5["height"]))


	else:

		can5["scrollregion"]=(0,0,int(can5["width"]),_y)

		_scroll_["cart2"]["_y"]=_y





	can.create_text((x+xx)-270+10,y+35+15,text="Sub Total",font=("FreeMono",13),fill="#000000",anchor="w")
	can.create_text((x+xx)-10,y+35+15,text="Ksh."+str(total),font=("FreeMono",13),fill="#ff0000",anchor="e")

	_total_=total

	can.create_text((x+xx)-270+10,y+40+15+40,text="Cash",font=("FreeMono",13),fill="#000000",anchor="w")




	#can.create_text(x+10+10,y+20+15+50*3, text="Quantity",font=("FreeMono",13), anchor="w",fill="#000000")

	v+=1



	x1,y1,x2,y2=(x+xx)-270+10+150-5+10-100+29,y+40+15+40-15,(x+xx)-270+10+150-5+10+100+60+6-100+29,y+40+15+40-15+25+6


	im=draw_round_rect(5,x1,y1,x2,y2, "#000000",alpha=1,width=1)
	sell_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=sell_items_ims[v],anchor="nw")

	__y1=y2

	ent1["bg"]="#ffffff"

	ent1.place(in_=root,x=x1+5,y=y1+5+40-can.canvasy(0))


	v+=1


	x1,y1,x2,y2=x+xx-270+10,y+yy-15-30, x+xx-10,y+yy-15	

	im=draw_round_rect(15,x1,y1,x2,y2, "#000000","#000000",alpha=1,width=1)
	sell_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y1,image=sell_items_ims[v],anchor="nw")


	can.create_text(x1+(x2-x1)/2,y1+15,text="Complete Payment",fill="#ffffff",font=("FreeMono",13),anchor="c")


	sell_items_coords["complete payment"]=x1,y1,x2,y2


	__y2=y1

	_scroll_["cart2"]["v_sb_coord"][-1]=0
	_scroll_["cart2"]["h_sb_coord"][-1]=0

	draw_v_sb("cart2")
	draw_h_sb("cart2")

	sel_sb=["cart2","vertical"]


	y__=__y1+(__y2-__y1-100)/2

	v+=1


	x1,y1,x2,y2=x1,y__,x2,y__+100

	im=draw_round_rect(15,x1,y1,x2,y2, "#009900",alpha=1,width=1)

	draw=ImageDraw.Draw(im)

	draw.rectangle((15,-5,15+5+f.measure("Balance")+5,+5),fill=(0,0,0,0),outline=(0,0,0,0))

	sell_items_ims[v]=ImageTk.PhotoImage(im)
	can.create_image(x1,y__,image=sell_items_ims[v],anchor="nw")


	can.create_text(x1+15+5,y__,text="Balance",fill="#009900",font=("FreeMono",13),anchor="w")




	can.delete(bal_)

	try:

		v_=int(ent1.get())



		bal_=can.create_text(x1+(x2-x1)/2, y1+(y2-y1)/2, text=f"Ksh.{int(int(ent1.get())-_total_)}",
			font=("FreeMono",15),fill="#009900",anchor="c")

	except:

		bal_=can.create_text(x1+(x2-x1)/2, y1+(y2-y1)/2, text="",
			font=("FreeMono",15),fill="#009900",anchor="c")


	ent1.focus_set()


def pay_with_mpesa():
	pass
	


def linear_regression(y_values,x_values):
    n = len(y_values)

    # x values are simply 1, 2, 3, ...
    #x_values = list(range(1, n + 1))

    x_mean = sum(x_values) / n
    y_mean = sum(y_values) / n

    # Calculate slope (b1)
    numerator = sum(
        (x - x_mean) * (y - y_mean)
        for x, y in zip(x_values, y_values)
    )

    denominator = sum(
        (x - x_mean) ** 2
        for x in x_values
    )

    b1 = numerator / denominator

    # Calculate intercept (b0)
    b0 = y_mean - b1 * x_mean

    return b0, b1



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
add_item_crop_v=[False,[]]
add_item_crop_coord_norm=[]
man_item_crop_v=[False,[]]
man_item_crop_coord_norm=[]

rep_items_ims={}
_date_=""

v5,h5=0,0
v6,h6=0,0

cal_st=0

rep_items_coord={}
all_by=None
graph_coords={}

graph_st=""
graph_ims={}
forecast_st=""
forecast_ims={}
forecast_coords={}
fp,fs=0,0
def main(con=0):

	global st,st_
	global can,can2,can3,can4
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
	global sel_sb
	global add_item_crop_v,man_item_crop_v
	global add_item_crop_coord_norm,man_item_crop_coord_norm
	global pay_st
	global user_name
	global calendar,_date_
	global rep_items_ims
	global v5,h5
	global v6,h6
	global cal_st
	global rep_items_coord
	global all_by
	global graph_coords
	global graph_st
	global previous2,next2
	global graph_ims
	global forecast_st
	global forecast_ims
	global forecast_coords
	global fp,fs

	st_="main"

	if con==0:

		sel_sb=None

	f=font.Font(family="FreeMono",size=13)

	if st=="Sell Items":



		items_ar=[]

		cart_buttons_coords={}


		forget_widgets(except_=dashboard)
		entries_show_reset()
		if con==0:
			sell_items_ims={}
			sel_item=None
			search_val=""
			search_focus=False
			delete_widgets()

		can["width"]=width-450
		can["height"]=height-40
		can["scrollregion"]=(0,0,width,height-40)
		can["bg"]="#ffffff"

		can["scrollregion"]=(0,0,width-450,height-40)


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
					"_x":width-450,
					"_x2":width-450,
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
					"_x":width-450,
					"_x2":width-450,
					"scrollregion":can["scrollregion"],
					"v_drag_st":0,
					"h_drag_st":0,
					"v_var":0,
					"h_var":0


					}			

		_scroll_["can"]=dict_

		sel_sb=["can","vertical"]


		can.place(in_=root,x=0,y=40)

		can2["width"]=width
		can2["height"]=40
		can2["bg"]="#ffffff"

		can2.delete("all")

		can2.create_line(0,0,width,0,fill="#000000")
		#can2.create_line(0,39,width,39,fill="#eeeeee")

		can2.place(in_=root,x=0,y=0)


		can3["width"]=450
		can3["height"]=height-40
		can3["bg"]="#ffffff"

		can3.delete("all")
		can3.place(in_=root,x=width-450,y=40)

		can3["scrollregion"]=(0,0,int(can3["width"]),int(can3["height"]))

		v=0


		_x_=450-10



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

		user_name=row[1]


		can2.create_text(width-5-25-15,20, text=user_name,fill="#000000",font=("FreeMono",13),anchor="e")

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





			can.create_text(x1+10,y2-25-25-25, text=format_text(f"{row[1]}",x2-x1-20),font=("FreeMono",13),fill="#0000ff",anchor="w")
			can.create_text(x1+10,y2-25-25, text=f"Ksh.{formart_number(row[3],x2-x1-20,1)}",font=("FreeMono",13),fill="#ff0000",anchor="w")
			can.create_text(x1+10,y2-25, text=f"{formart_number(row[4],x2-x1-20)} items left",font=("FreeMono",13),fill="#000000",anchor="w")


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

			can.create_image(x_,int(can["height"])/2-(10+30)/2,image=sell_items_ims[v],anchor="c")

			can.create_text(x_,int(can["height"])/2+250/2+10+15-(10+30)/2,text="No Record",font=("FreeMono",13),fill="#000000",anchor="c")



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

		im=draw_round_rect(20,x1,y1,x2,y2, "#000000","#eeeeee",alpha=1,width=1)
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
			can4.create_text(5+f.measure("Total")+20,y+15+30+10,text=str(formart_number(quantity,(int(can4["width"]))-(5+f.measure("Total")+20))),font=("FreeMono",13),fill="#ff0000",anchor="w")
			can4.create_text(5,y+15+30+10+30,text="Total",font=("FreeMono",13),fill="#000000",anchor="w")
			can4.create_text(5+f.measure("Total")+20,y+15+30+10+30,text=f"Ksh.{formart_number(int(sold_at)*int(quantity),(int(can4["width"]))-(5+f.measure("Total")+20),1)}",font=("FreeMono",13),fill="#ff0000",anchor="w")
	
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

			can4.create_image(int(can4["width"])/2,int(can4["height"])/2-(10+30)/2,image=sell_items_ims[v],anchor="c")

			can4.create_text(int(can4["width"])/2,int(can4["height"])/2+50+10+15-(10+30)/2,text="No Record",font=("FreeMono",13),fill="#000000",anchor="c")




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

		x1,y1,x2,y2=10+5+10,int(can3["height"])-10-30-(10+30)*2-30*2-15-10-30,int(can3["width"])-10-5,int(can3["height"])-10-30-(10+30)*2-30*2-15-10

		im=draw_round_rect(15,x1,y1,x2,y2, "#ff0000","#ff0000",alpha=1,width=1)
		sell_items_ims[v]=ImageTk.PhotoImage(im)

		can3.create_image(x1,y1, image=sell_items_ims[v],anchor="nw")
		can3.create_image(x1+(x2-x1-25-f.measure("Clear Cart")-10)/2,y1+2.5,image=clear_cart,anchor="nw")
		can3.create_text(x1+(x2-x1-25-f.measure("Clear Cart")-10)/2+25+10,y1+15, text="Clear Cart",fill="#ffffff",font=("FreeMono",13),anchor="w")


		cart_buttons_coords["clear_cart"]=[x1,y1,x2,y2]


		if int(no_items)==1:
			i="Item"
		else:
			i="Items"

		can3.create_text(10+5+10, int(can3["height"])-10-30-(10+30)*2-30*2, text=i, font=("FreeMono",13),fill="#000000",anchor="w")
		can3.create_text(int(can3["width"])-10-5, int(can3["height"])-10-30-(10+30)*2-30*2, text=str(formart_number(no_items,(int(can3["width"])-10-5)-(10+5+10+f.measure("Sub Total")))), font=("FreeMono",13),fill="#ff0000",anchor="e")		

		can3.create_text(10+5+10, int(can3["height"])-10-30-(10+30)*2-30, text="Discount", font=("FreeMono",13),fill="#000000",anchor="w")
		can3.create_text(int(can3["width"])-10-5, int(can3["height"])-10-30-(10+30)*2-30, text=f"Ksh.{formart_number(discount,(int(can3["width"])-10-5)-(10+5+10+f.measure("Sub Total")),1)}", font=("FreeMono",13),fill="#ff0000",anchor="e")		

		can3.create_text(10+5+10, int(can3["height"])-10-30-(10+30)*2, text="Sub Total", font=("FreeMono",13),fill="#000000",anchor="w")
		can3.create_text(int(can3["width"])-10-5, int(can3["height"])-10-30-(10+30)*2, text=f"Ksh.{formart_number(total,(int(can3["width"])-10-5)-(10+5+10+f.measure("Sub Total")),1)}", font=("FreeMono",13),fill="#ff0000",anchor="e")		



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

			draw_selected_item(sel_item,con)

		elif pay_st=="Cash":
			pay_with_cash(1)
		elif pay_st=="MPESA":
			pay_with_mpesa()

	elif st=="Reports":


		forget_widgets(except_=dashboard)
		entries_show_reset()
		if con==0:
			rep_items_ims={}
			search_val=""
			search_focus=False
			all_by=None
			delete_widgets()

			_date_=str(datetime.datetime.now()).split(" ")[0]



		can["width"]=width
		can["height"]=height-40

		can.place(in_=root,x=0,y=40)

		can["scrollregion"]=(0,0,int(can["width"]),int(can["height"]))

		can.delete("all")



		can2["width"]=width
		can2["height"]=40
		can2["bg"]="#ffffff"

		can2.place(in_=root,x=0,y=0)

		can2.delete("all")

		can2.create_line(0,0,width,0,fill="#000000")
		#can2.create_line(0,39,width,39,fill="#eeeeee")
		v=0


		_x_=450-10



		if int(dashboard.place_info()["x"])<0:
			_x=5+25+5
		else:
			_x=int(dashboard["width"])
		x_=_x+(int(can["width"])-_x-_x_)/2

		x1,y1,x2,y2=x_,5,x_+_x_,5+30


		im=draw_round_rect(15,x1,y1,x2,y2, "#000000",alpha=1,width=1)

		rep_items_ims[v]=ImageTk.PhotoImage(im)

		can2.create_image(x1,y1,image=rep_items_ims[v],anchor="nw")

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

		user_name=row[1]


		can2.create_text(width-5-25-15,20, text=user_name,fill="#000000",font=("FreeMono",13),anchor="e")

		if row[4]=="":

			can2.create_image(width-5-25,7.5,image=no_profile_im,anchor="nw")


		else:

			#process profile picture
			pass





		

		f=font.Font(family="FreeMono",size=13)



		ar=["Item Name","Date/Time","Sold By","Selling Price","Sold Price","Quantity","Discount","Profit","Total"]

		x_sz=[]

		for i in ar:

			sz=f.measure(i)
			x_sz.append(sz)



		xt2=0

		for x_ in x_sz:

			xt2+=x_+40


		total__=0
		tprofit=0






		data=[]

		db_reports=database.connect("data/reports.db")
		cur=db_reports.cursor()

		cur.execute("SELECT * FROM reports")

		rows=cur.fetchall()

		for row in rows:

			date_time=str(row[1])

			_y_,_m_,_d_=date_time.split(" ")[0].split("-")
			
			_y_2,_m_2,_d_2=_date_.split("-")

			if all_by==None:

				if date_time.split(" ")[0]!=_date_:
					continue

			elif all_by=="month":

				if _y_==_y_2 and _m_==_m_2:
					pass
				else:
					continue


			elif all_by=="year":

				if _y_==_y_2:
					pass
				else:
					continue

			item_name=str(row[0])
			
			sold_by=str(row[2])
			selling_price=str(row[5])
			buying_price=str(row[4])
			sold_at=str(row[6])
			quantity=str(row[3])
			discount=str((int(selling_price)*int(quantity))-(int(sold_at)*int(quantity)))
			profit=str((int(sold_at)*int(quantity))-(int(buying_price)*int(quantity)))
			total=str((int(sold_at)*int(quantity)))




			if item_name.lower().find(search_val.lower())==-1 and date_time.lower().find(search_val.lower())==-1 and sold_by.lower().find(search_val.lower())==-1:

				continue


			tprofit+=int(profit)
			total__+=int(total)

			data.append([item_name,date_time,sold_by,"Ksh."+selling_price,"Ksh."+sold_at,quantity,"Ksh."+discount,"Ksh."+profit,"Ksh."+total])

		for i in data:

			
			for _ in range(len(i)):


				if f.measure(i[_])>x_sz[_]:
					x_sz[_]=f.measure(i[_])

			


		for _ in range(len(x_sz)):

			x_sz[_]=x_sz[_]+40





		xt=0

		for x_ in x_sz:

			xt+=x_




		if xt2>(int(can["width"])-int(dashboard["width"]))-60:

			xx=(int(can["width"])-int(dashboard["width"]))-60

		else:

			xx=xt2



		if int(dashboard.place_info()["x"])<0:

			x_=5+25+5

		else:

			x_=int(dashboard["width"])



		_x_=x_+((int(can["width"])-x_)-xx)/2

		can3["width"]=xx
		can3["height"]=30

		can3["bg"]="#000000"
		can3.delete("all")

		can3["scrollregion"]=(0,0,int(can3["width"]),int(can3["height"]))

		can3.place(in_=root,x=_x_,y=40+40)

		_x=0
		for _ in range(len(ar)):


			can3.create_text(_x+x_sz[_]/2,15,text=ar[_],font=("FreeMono",13),fill="#ffffff",anchor="c")


			if _==len(ar)-1:
				pass
			else:
				can3.create_line(_x+x_sz[_],0, _x+x_sz[_],30, fill="#ffffff")

			_x+=x_sz[_]


		can4["width"]=xx
		can4["height"]=height-40-40-30-50-50

		can4["scrollregion"]=(0,0,int(can4["width"]),int(can4["height"]))

		can4.place(in_=root,x=_x_,y=40+40+30)
		can4.delete("all")





		_st_=0

		y=0

		p=len(data)-1
		for _ in range(len(data)):

			i=data[p]

			if _st_==1:

				can4.create_rectangle(0,y, xt,y+30, fill="#eeeeee",outline="#eeeeee")

			_x=0

			for _ in range(len(i)):

				txt=i[_]

				can4.create_text(_x+x_sz[_]/2,y+15,text=txt,font=("FreeMono",13),fill="#000000",anchor="c")



				_x+=x_sz[_]

				can4.create_line(_x,y, _x,y+30, fill="#000000")
			
			if _st_==0:
				_st_=1
			elif _st_==1:
				_st_=0




			#can4.create_line(0,y+30,int(can4["width"]),y+30,fill="#000000")

			p-=1


			y+=30

		can4.create_line(0,y, xt,y,fill="#000000")

		if len(data)==0:




			im=no_record

			im=im.resize((250,250))

			v+=1

			rep_items_ims[v]=ImageTk.PhotoImage(im)



			can4.create_image(int(can4["width"])/2,int(can4["height"])/2-(10+30)/2,image=rep_items_ims[v],anchor="c")

			can4.create_text(int(can4["width"])/2,int(can4["height"])/2+250/2+10+15-(10+30)/2,text="No Record",font=("FreeMono",13),fill="#000000",anchor="c")





		can.create_rectangle(_x_-1,40-1, _x_+int(can3["width"]),40+30+int(can4["height"]),outline="#000000")


		if xt<=int(can3["width"]):

			can3["scrollregion"]=(0,0, int(can3["width"]), int(can3["height"]))

			xxx=int(can3["width"])

		else:

			can3["scrollregion"]=(0,0, xt, int(can3["height"]))

			xxx=xt




		dict_={"widget": can3,
				"sb_widget":can,
				"sb_st":"horizontal",
				"sb_sz":10,
				"h_sb_coord":[(_x_,_x_+int(can4["width"]),40+30+int(can4["height"])+4,40+30+int(can4["height"])+4+10),0],
				"_y":height-40,
				"v":v5,
				"h_":h5,
				"w":int(can3["width"]),
				"h":int(can3["height"]),
				"_x":int(can3["width"]),
				"_x2":xxx,
				"scrollregion":can3["scrollregion"],
				"v_drag_st":0,
				"h_drag_st":0,
				"v_var":0,
				"h_var":0


				}			

		_scroll_["can3r"]=dict_

		draw_h_sb("can3r")


		if y<=int(can4["height"]):

			can4["scrollregion"]=(0,0,xxx,int(can4["height"]))

			yyy=int(can4["height"])

		else:

			can4["scrollregion"]=(0,0,xxx,y)

			yyy=y




		dict_={"widget": can4,
				"sb_widget":can,
				"sb_st":"both",
				"sb_sz":10,
				"v_sb_coord":[(40+30,40+30+int(can4["height"]),_x_+int(can3["width"])+4,_x_+int(can3["width"])+4+10),0],
				"h_sb_coord":[(_x_,_x_+int(can4["width"]),40+30+int(can4["height"])+4,40+30+int(can4["height"])+4+10),0],
				"_y":yyy,
				"v":v6,
				"h_":h6,
				"w":int(can4["width"]),
				"h":int(can4["height"]),
				"_x":int(can4["width"]),
				"_x2":xxx,
				"scrollregion":can4["scrollregion"],
				"v_drag_st":0,
				"h_drag_st":0,
				"v_var":0,
				"h_var":0


				}			

		_scroll_["can4r"]=dict_

		draw_v_sb("can4r")
		draw_h_sb("can4r")


		_x_-1,40-1

		can.create_image(_x_,(40-30)/2, image=calendar,anchor="nw")

		rep_items_coord["calendar"]=[_x_,(40-30)/2]

		if con==0:
			cal_st=0


		m=["January","February","March","April","May","June","July","August","September","October","November","December"]
			

		m_=m[int(_date_.split("-")[1])-1]



		can.create_text(_x_+30+15,20,text=str(_date_),font=("FreeMono",13),fill="#000000",anchor="w")

		v+=1

		can.create_text(_x_+30+15+f.measure(str(_date_))+50,20,text=f"All by Month ({m_})",font=("FreeMono",13),fill="#000000",anchor="w")


		x1,y1,x2,y2=_x_+30+15+f.measure(str(_date_))+50+f.measure(f"All by Month ({m_})")+20,20-15, _x_+30+15+f.measure(str(_date_))+50+f.measure(f"All by Month ({m_})")+20+50,20+15,
		
		rep_items_coord["all_by_month"]=[x1,y1,x2,y2]


		if all_by=="month":
			col="#00ff00"
		else:
			col="#ff0000"

		im=draw_round_rect(15,x1,y1,x2,y2, "#000000",alpha=1,width=1)

		rep_items_ims[v]=ImageTk.PhotoImage(im)

		can.create_image(x1,y1,image=rep_items_ims[v],anchor="nw")


		v+=1


		im=draw_round_rect(10,0,0,20,20, "#000000",col,alpha=1,width=1)

		rep_items_ims[v]=ImageTk.PhotoImage(im)




		if all_by=="month":

			can.create_image(x2-15,y1+15,image=rep_items_ims[v],anchor="c")

		else:

			can.create_image(x1+15,y1+15,image=rep_items_ims[v],anchor="c")



		v+=1

		can.create_text(_x_+30+15+f.measure(str(_date_))+50+f.measure(f"All by Month ({m_})")+20+50+40,20,text=f"All by Year ({_date_.split("-")[0]})",font=("FreeMono",13),fill="#000000",anchor="w")


		x1,y1,x2,y2=_x_+30+15+f.measure(str(_date_))+50+f.measure(f"All by Month ({m_})")+20+50+40+f.measure(f"All by Year ({_date_.split("-")[0]})")+20,20-15, _x_+30+15+f.measure(str(_date_))+50+f.measure(f"All by Month ({m_})")+20+50+40+f.measure(f"All by Year ({_date_.split("-")[0]})")+20+50,20+15,
		

		rep_items_coord["all_by_year"]=[x1,y1,x2,y2]

		if all_by=="year":
			col="#00ff00"
		else:
			col="#ff0000"


		im=draw_round_rect(15,x1,y1,x2,y2, "#000000",alpha=1,width=1)

		rep_items_ims[v]=ImageTk.PhotoImage(im)

		can.create_image(x1,y1,image=rep_items_ims[v],anchor="nw")
		

		v+=1


		im=draw_round_rect(10,0,0,20,20, "#000000",col,alpha=1,width=1)

		rep_items_ims[v]=ImageTk.PhotoImage(im)


		

		if all_by=="year":

			can.create_image(x2-15,y1+15,image=rep_items_ims[v],anchor="c")

		else:
			can.create_image(x1+15,y1+15,image=rep_items_ims[v],anchor="c")






		_x_+int(can3["width"]),40+30+int(can4["height"])

		x_=_x_+int(can3["width"])-f.measure(f"Ksh.{total__}")-30-f.measure("Total Profit")

		can.create_text(_x_+int(can3["width"]),40+30+int(can4["height"])+4+10+30+15-15,text=f"Ksh.{tprofit}",font=("FreeMono",13),
			fill="#ff0000",anchor="e")

		can.create_text(x_,40+30+int(can4["height"])+4+10+30+15-15,text="Total Profit",font=("FreeMono",13),fill="#000000",anchor="w")


		can.create_text(_x_+int(can3["width"]),40+30+int(can4["height"])+4+10+30+15+30-15,text=f"Ksh.{total__}",font=("FreeMono",13),
			fill="#ff0000",anchor="e")

		can.create_text(x_,40+30+int(can4["height"])+4+10+30+15+30-15,text="Total Sales",font=("FreeMono",13),fill="#000000",anchor="w")



		


		if con==0:

			sel_sb=["can4r","vertical"]


		if cal_st==1:

			draw_cal(rep_items_coord["calendar"][0]+30,rep_items_coord["calendar"][1]+30)










	elif st=="Graphs":


		forget_widgets(except_=dashboard)
		entries_show_reset()
		if con==0:

			cal_st=0

			_date_=str(datetime.datetime.now()).split(" ")[0]

			graph_st="Annually"

			
			delete_widgets()


		can["width"]=width
		can["height"]=height-40
		can["bg"]="#ffffff"
		can["scrollregion"]=(0,0,int(can["width"]),int(can["height"]))
		can.delete("all")

		can.place(in_=root,x=0,y=40)

		can2["width"]=width
		can2["height"]=40

		can2.place(in_=root,x=0,y=0)

		can2.delete("all")

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






		if int(dashboard.place_info()["x"])<0:

			x_=5+25+5

		else:

			x_=int(dashboard["width"])


		xx=int(can["width"])-int(dashboard["width"])-200


		_x_=x_+((int(can["width"])-x_)-xx)/2


		can.create_image(_x_,(40-30)/2, image=calendar,anchor="nw")

		graph_coords["calendar"]=[_x_,(40-30)/2]


		d=_date_.split("-")
		y=d[0]
		m=d[1]
		can.create_text(_x_+30+20,20,text=f"{y}-{m}",font=("FreeMono",13),fill="#000000",anchor="w")

		x1,y1,x2,y2=_x_,40,_x_+xx,int(can["height"])-40


		can.create_image(x2-20,(40-20)/2,image=next2,anchor="nw")

		graph_coords["next"]=x2-20,(40-20)/2

		can.create_text(x2-20-10-f.measure(graph_st),20,text=graph_st,font=("FreeMono",13),fill="#000000",anchor="w")

		can.create_image(x2-20-10-f.measure(graph_st)-10-20,(40-20)/2,image=previous2,anchor="nw")

		graph_coords["previous"]=x2-20-10-f.measure(graph_st)-10-20,(40-20)/2



		#can.create_rectangle(x1,y1,x2,y2,outline="#000000",fill="#eeeeee")

		v=0
		im=draw_round_rect(20,x1,y1,x2,y2, "#000000","#eeeeee",alpha=1,width=1)

		graph_ims[v]=ImageTk.PhotoImage(im)

		can.create_image(x1,y1,image=graph_ims[v],anchor="nw")

		if graph_st=="Annually":

			db_reports=database.connect("data/reports.db")
			cur=db_reports.cursor()

			cur.execute("SELECT * FROM reports")

			rows=cur.fetchall()

			data={1:{"month":"Jan","profit":0,"total sales":0},
				2:{"month":"Feb","profit":0,"total sales":0},
				3:{"month":"March","profit":0,"total sales":0},
				4:{"month":"April","profit":0,"total sales":0},
				5:{"month":"May","profit":0,"total sales":0},
				6:{"month":"June","profit":0,"total sales":0},
				7:{"month":"July","profit":0,"total sales":0},
				8:{"month":"Aug","profit":0,"total sales":0},
				9:{"month":"Sept","profit":0,"total sales":0},
				10:{"month":"Oct","profit":0,"total sales":0},
				11:{"month":"Nov","profit":0,"total sales":0},
				12:{"month":"Dec","profit":0,"total sales":0},
				}



			for row in rows:

				date_time=str(row[1])

				_y_,_m_,_d_=date_time.split(" ")[0].split("-")

				if y!=_y_:
					continue



				selling_price=str(row[5])
				buying_price=str(row[4])
				sold_at=str(row[6])
				quantity=str(row[3])
				discount=str((int(selling_price)*int(quantity))-(int(sold_at)*int(quantity)))
				profit=str((int(sold_at)*int(quantity))-(int(buying_price)*int(quantity)))
				total=str((int(sold_at)*int(quantity)))


				data[int(_m_)]["profit"]+=int(profit)
				data[int(_m_)]["total sales"]+=int(total)




			max_sales=0

			for i in data:

				if max_sales<data[i]["total sales"]:

					max_sales=data[i]["total sales"]






			can.create_rectangle(x1+150,y1+50, x2-50,y2-100-40, outline="#000000",fill="#ffffff")

			y_s=(((y2-100-40)-(y1+50))/10)

			y_=y2-100-40

			for _ in range(10):

				can.create_line(x1+150,y_,x2-50,y_,fill="#808080",dash=(1,3))

				y_-=y_s



			xr=((x2-50)-(x1+150))/12

			x__=x1+150+xr

			for _ in range(12):

				can.create_line(x__,y1+50,x__,y2-100-40,fill="#808080",dash=(1,3))

				x__+=xr


			can.create_rectangle(x1+150,y1+50, x2-50,y2-100-40, outline="#000000")

			x_=x1+150+xr/2


			xw=(xr-10-5)/2

			x__=(xr-xw*2-5)/2

			for i in data:

				p=data[i]["profit"]
				ts=data[i]["total sales"]


				if max_sales==0:
					y_1,y_2=0,0
				else:

					y_1=int(round((((y2-100-40)-(y1+50))-100)*p/max_sales,0))
					y_2=int(round((((y2-100-40)-(y1+50))-100)*ts/max_sales,0))

				if y_1!=0:

					can.create_rectangle(x_+x__-xr/2,y2-100-40, x_+x__+xw-xr/2,y2-100-40-y_1,fill="#ff0000",outline="#ff0000")
		
				if y_2!=0:

					can.create_rectangle(x_+x__+xw+5-xr/2,y2-100-40, x_+x__+xw+5+xw-xr/2,y2-100-40-y_2,fill="#0000ff",outline="#0000ff")


				can.create_text(x_,y2-100+30-40,text=data[i]["month"],font=("FreeMono",13),fill="#000000")

				x_+=xr



			can.create_text(x1+150+((x2-50)-(x1+150))/2,y2-100+30+40-40,text="Months",font=("FreeMono",13,"bold"),fill="#000000")
			can.create_text(x1+20,y1+50+((y2-100)-(y1+50))/2,text="Ksh",font=("FreeMono",13,"bold"),fill="#000000",anchor="w")


			

			y_=0

			y__=y2-100-40


			for _ in range(11):

				mx=max_sales

				if max_sales==0:

					mx=500000

				a=int(round((y_)/(((y2-100-40)-(y1+50))-100)*mx,0))



				can.create_text(x1+150-10,y__,text=formart_number(int(a),50),fill="#000000",anchor="e",font=("FreeMono",13))

				y_+=y_s
				y__-=y_s




			can.create_rectangle(x1+150,y2-10-30-10-5, x1+150+10,y2-10-30-10+10-5, fill="#ff0000",outline="#ff0000")
			can.create_text(x1+150+10+15,y2-10-30-10+5-5,text="Profits",fill="#000000",font=("FreeMono",13),anchor="w")


			can.create_rectangle(x1+150,y2-10-30-10+30-5, x1+150+10,y2-10-30-10+10+30-5, fill="#0000ff",outline="#0000ff")
			can.create_text(x1+150+10+15,y2-10-30-10+5+30-5,text="Total Sales",fill="#000000",font=("FreeMono",13),anchor="w")

			can.create_text(x1+150+((x2-50)-(x1+150))/2,y1+25,text=F"BAR GRAPH SHOWING YEAR {y} SALES.",font=("FreeMono",13,"bold"),fill="#000000")



		elif graph_st=="Monthly":


			db_reports=database.connect("data/reports.db")
			cur=db_reports.cursor()

			cur.execute("SELECT * FROM reports")

			rows=cur.fetchall()

			data={0:{"week":"Week 1","profit":0,"total sales":0},
				1:{"week":"Week 2","profit":0,"total sales":0},
				2:{"week":"Week 3","profit":0,"total sales":0},
				3:{"week":"Week 4","profit":0,"total sales":0},
				}


			for row in rows:

				date_time=str(row[1])

				_y_,_m_,_d_=date_time.split(" ")[0].split("-")

				if y!=_y_ or int(m)!=int(_m_):
					continue



				selling_price=str(row[5])
				buying_price=str(row[4])
				sold_at=str(row[6])
				quantity=str(row[3])
				discount=str((int(selling_price)*int(quantity))-(int(sold_at)*int(quantity)))
				profit=str((int(sold_at)*int(quantity))-(int(buying_price)*int(quantity)))
				total=str((int(sold_at)*int(quantity)))


				week=int(int(_d_)/7)

				if week>3:
					week=3




				data[week]["profit"]+=int(profit)
				data[week]["total sales"]+=int(total)




			max_sales=0

			for i in data:

				if max_sales<data[i]["total sales"]:

					max_sales=data[i]["total sales"]






			can.create_rectangle(x1+150,y1+50, x2-50,y2-100-40, outline="#000000",fill="#ffffff")

			y_s=(((y2-100-40)-(y1+50))/10)

			y_=y2-100-40

			for _ in range(10):

				can.create_line(x1+150,y_,x2-50,y_,fill="#808080",dash=(1,3))

				y_-=y_s

			


			xr=((x2-50)-(x1+150))/4
			x__=x1+150+xr

			for _ in range(4):

				can.create_line(x__,y1+50,x__,y2-100-40,fill="#808080",dash=(1,3))

				x__+=xr


			can.create_rectangle(x1+150,y1+50, x2-50,y2-100-40, outline="#000000")

			x_=x1+150+xr/2


			xw=(xr-60-5)/2

			x__=(xr-xw*2-5)/2

			for i in data:

				p=data[i]["profit"]
				ts=data[i]["total sales"]


				if max_sales==0:
					y_1,y_2=0,0
				else:

					y_1=int(round((((y2-100-40)-(y1+50))-100)*p/max_sales,0))
					y_2=int(round((((y2-100-40)-(y1+50))-100)*ts/max_sales,0))

				if y_1!=0:

					can.create_rectangle(x_+x__-xr/2,y2-100-40, x_+x__+xw-xr/2,y2-100-40-y_1,fill="#ff0000",outline="#ff0000")
		
				if y_2!=0:

					can.create_rectangle(x_+x__+xw+5-xr/2,y2-100-40, x_+x__+xw+5+xw-xr/2,y2-100-40-y_2,fill="#0000ff",outline="#0000ff")


				can.create_text(x_,y2-100+30-40,text=data[i]["week"],font=("FreeMono",13),fill="#000000")

				x_+=xr



			can.create_text(x1+150+((x2-50)-(x1+150))/2,y2-100+30+40-40,text="Week",font=("FreeMono",13,"bold"),fill="#000000")
			can.create_text(x1+20,y1+50+((y2-100)-(y1+50))/2,text="Ksh",font=("FreeMono",13,"bold"),fill="#000000",anchor="w")


			

			y_=0

			y__=y2-100-40


			for _ in range(11):

				mx=max_sales

				if max_sales==0:

					mx=500000

				a=int(round((y_)/(((y2-100-40)-(y1+50))-100)*mx,0))



				can.create_text(x1+150-10,y__,text=formart_number(int(a),50),fill="#000000",anchor="e",font=("FreeMono",13))

				y_+=y_s
				y__-=y_s




			can.create_rectangle(x1+150,y2-10-30-10-5, x1+150+10,y2-10-30-10+10-5, fill="#ff0000",outline="#ff0000")
			can.create_text(x1+150+10+15,y2-10-30-10+5-5,text="Profits",fill="#000000",font=("FreeMono",13),anchor="w")


			can.create_rectangle(x1+150,y2-10-30-10+30-5, x1+150+10,y2-10-30-10+10+30-5, fill="#0000ff",outline="#0000ff")
			can.create_text(x1+150+10+15,y2-10-30-10+5+30-5,text="Total Sales",fill="#000000",font=("FreeMono",13),anchor="w")

			m__=["January","February","March","April","May","June","July","August","September","October","November","December"]

			m_=m__[int(m)-1]

			can.create_text(x1+150+((x2-50)-(x1+150))/2,y1+25,text=f"BAR GRAPH SHOWING {m_.upper()} YEAR {y} SALES.",font=("FreeMono",13,"bold"),fill="#000000")
























		if cal_st==1:
						
			draw_cal(graph_coords["calendar"][0]+30,graph_coords["calendar"][1]+30)
				

	elif st=="Forecasts":



		forget_widgets(except_=dashboard)
		entries_show_reset()
		if con==0:

			forecast_ims={}

			forecast_st="Monthly"

			
			delete_widgets()


		can["width"]=width
		can["height"]=height-40
		can["bg"]="#ffffff"
		can["scrollregion"]=(0,0,int(can["width"]),int(can["height"]))
		can.delete("all")

		can.place(in_=root,x=0,y=40)

		can2["width"]=width
		can2["height"]=40

		can2.place(in_=root,x=0,y=0)

		can2.delete("all")

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


		if int(dashboard.place_info()["x"])<0:

			x_=5+25+5

		else:

			x_=int(dashboard["width"])


		xx=int(can["width"])-int(dashboard["width"])-200


		_x_=x_+((int(can["width"])-x_)-xx)/2



		v=0

		x1,y1,x2,y2=_x_,40,_x_+xx,int(can["height"])-40
		im=draw_round_rect(20,x1,y1,x2,y2, "#000000","#eeeeee",alpha=1,width=1)

		forecast_ims[v]=ImageTk.PhotoImage(im)

		can.create_image(x1,y1,image=forecast_ims[v],anchor="nw")

		x1_,y1_,x2_,y2_=x1+150,y1+50, x2-50,y2-100-40


		can3["width"]=int(x2_-x1_)
		can3["height"]=int(y2_-y1_)

		can3["bg"]="#ffffff"

		can3.delete("all")

		can3["scrollregion"]=(0,0,int(can3["width"]),int(can3["height"]))

		can3.place(in_=root,x=x1_,y=y1_+40)


		def det_next_day(date):

		    y,m,d=date.split("-")

		    y=int(y)
		    m=int(m)
		    d=int(d)



		    if y%4==0:
		        feb_=29
		    else:
		        feb_=28

		    months={
		    1:["January",31],
		    2:["February",feb_],
		    3:["March",31],
		    4:["April",30],
		    5:["May",31],
		    6:["June",30],
		    7:["July",31],
		    8:["August",31],
		    9:["September",30],
		    10:["October",31],
		    11:["November",30],
		    12:["December",31]
		    }


		    if d+1<=months[m][1]:

		        return f"{y}-{m}-{d+1}"

		    elif months[m][1]==d:

		        if m==12:

		            return f"{y+1}-{1}-{1}"

		        else:
		            return f"{y}-{m+1}-{1}"




		forecast_st="Daily"

		
		fx=[]

		start_date="2026-9-20"
		y_,m_,d_=str(datetime.datetime.now()).split(" ")[0].split("-")

		cur_date=f"{int(y_)}-{int(m_)}-{int(d_)}"

		x_=50

		fx.append([x_,start_date])


		can.create_rectangle(x1+150-1,y1+50-1,x1+150+int(can3["width"]),y1+50+int(can3["height"]))


		def det_total_daily_sales_n_profits(date):


			tprofit=0
			tsales=0


			db_reports=database.connect("data/reports.db")
			cur=db_reports.cursor()

			cur.execute("SELECT * FROM reports")

			rows=cur.fetchall()

			y_,m_,d_=date.split("-")

			y_=int(y_)
			m_=int(m_)
			d_=int(d_)

			for row in rows:

				date_time=str(row[1])

				_y_,_m_,_d_=date_time.split(" ")[0].split("-")

				_y_=int(_y_)
				_m_=int(_m_)
				_d_=int(_d_)



				if _y_==y_ and _m_==m_ and _d_==d_:


					selling_price=str(row[5])
					buying_price=str(row[4])
					sold_at=str(row[6])
					quantity=str(row[3])
					profit=(int(sold_at)*int(quantity))-(int(buying_price)*int(quantity))
					total=(int(sold_at)*int(quantity))


					tprofit+=profit
					tsales+=total


			return [tprofit,tsales]


		if forecast_st=="Daily":

			
			con_=0

			while 1:


			

				x_+=100


				date=det_next_day(fx[-1][1])


				if date==cur_date:
					con_=1




				fx.append([x_,date])

				if con_==1:
					break

			x_+=100
			for _ in range(30):

				date=det_next_day(fx[-1][1])

				fx.append([x_,date])

				x_+=100

			fy=[]

			for _ in range(len(fx)):





				fy.append(det_total_daily_sales_n_profits(fx[_][1]))


				if fx[_][1]==cur_date:

					break 






		max_sales=0

		for i in fy:

			if i[1]>max_sales:
				max_sales=i[1]

		

		x1,y1,x2,y2=0,0,10,10
		im=draw_round_rect(5,x1,y1,x2,y2, "#000000","#0000ff",alpha=1,width=1)

		fs=ImageTk.PhotoImage(im)
		

		x1,y1,x2,y2=0,0,10,10
		im=draw_round_rect(5,x1,y1,x2,y2, "#000000","#ff0000",alpha=1,width=1)

		fp=ImageTk.PhotoImage(im)

		can3.create_line(0,int(can3["height"])-50,fx[-1][0]+50,int(can3["height"])-50,fill="#000000")



		for _ in range(len(fx)):


			date=fx[_][1]
			x_=fx[_][0]

			can3.create_text(x_,int(can3["height"])-50+25,text=date,font=("FreeMono",13),fill="#000000",anchor="c")

			can3.create_line(x_,0,x_,int(can3["height"])-50,fill="#000000",dash=(1,3))


		x1,y1,x2,y2=_x_,40,_x_+xx,int(can["height"])-40

		y_s=(((y2-100-40-50)-(y1+50))/10)


		y_=0

		y__=y1_+int(can3["height"])-50


		for _ in range(11):

			mx=max_sales

			if max_sales==0:

				mx=500000

			a=y_*max_sales*2/(int(can3["height"])-50)



			can.create_text(x1+150-10,y__,text=formart_number(int(a),50),fill="#000000",anchor="e",font=("FreeMono",13))

			can3.create_line(0,y__-(y1+50),fx[-1][0]+50,y__-(y1+50),fill="#000000",dash=(1,3))


			y_+=y_s
			y__-=y_s




		c=0
		for s in fy:

			p=s[0]
			s=s[1]

			y_p=p*(int(can3["height"])-50)/max_sales/2
			y_s=s*(int(can3["height"])-50)/max_sales/2


			can3.create_image(fx[c][0], int(can3["height"])-50-y_p, image=fp, anchor="c")
			can3.create_image(fx[c][0], int(can3["height"])-50-y_s, image=fs, anchor="c")

			c+=1



		can.create_text(x1+150+int(can3["width"])/2,y1+50+int(can3["height"])+20,text="Days",font=("FreeMono",13,"bold"),fill="#000000")

		can.create_text(x1+20,y1+50+(int(can3["height"])-50)/2,text="Ksh",font=("FreeMono",13,"bold"),fill="#000000",anchor="w")

		#profit

		y_values=[]
		x_values=[]

		for _ in range(len(fy)):

			y_values.append(fy[_][0])
			x_values.append(fx[_][0])



		b0,b1=linear_regression(y_values,x_values)

		y1_=b0*(int(can3["height"])-50)/max_sales/2

		y2_=(b0 + b1 * fx[-1][0])*(int(can3["height"])-50)/max_sales/2


		can3.create_line(fx[0][0],int(can3["height"])-50-y1_, fx[-1][0],int(can3["height"])-50-y2_, fill="#ff0000")



		#sales

		y_values=[]
		x_values=[]

		for _ in range(len(fy)):

			y_values.append(fy[_][1])
			x_values.append(fx[_][0])



		b0,b1=linear_regression(y_values,x_values)

		y1_=b0*(int(can3["height"])-50)/max_sales/2

		y2_=(b0 + b1 * fx[-1][0])*(int(can3["height"])-50)/max_sales/2


		can3.create_line(fx[0][0],int(can3["height"])-50-y1_, fx[-1][0],int(can3["height"])-50-y2_, fill="#0000ff")


		can3["scrollregion"]=(0,0,fx[-1][0]+50,int(can3["height"]))


		can.create_image(x1+150-5-20,y1+50+int(can3["height"])-20,image=previous2,anchor="nw")
		forecast_coords["left"]=[x1+150-5-20,y1+50+int(can3["height"])-20]
		can.create_image(x1+150+int(can3["width"])+5,y1+50+int(can3["height"])-20,image=next2,anchor="nw")
		forecast_coords["right"]=[x1+150+int(can3["width"])+5,y1+50+int(can3["height"])-20]


		can.create_text(x1+150+int(can3["width"])/2,y1+25,text="LINREAR REGRESSION SHOWING POSSIBLE SALES ON FUTURE DAYS",
			font=("FreeMono",13,"bold"),fill="#000000")


		can.create_image(x1+150+5,y1+50+int(can3["height"])+30+20,image=fs)
		can.create_text(x1+150+5+10+10,y1+50+int(can3["height"])+30+20,text="Sales",font=("FreeMono",13),anchor="w",fill="#000000")


		can.create_line(x1+150+5+10+10+f.measure("Sales")+20,y1+50+int(can3["height"])+30+20, x1+150+5+10+10+f.measure("Sales")+20+15,y1+50+int(can3["height"])+30+20,fill="#0000ff",width=2)
		can.create_text(x1+150+5+10+10+f.measure("Sales")+20+15+10,y1+50+int(can3["height"])+30+20,
			text="Linear regression for Sales",font=("FreeMono",13),fill="#000000",anchor="w")


		can.create_image(x1+150+5,y1+50+int(can3["height"])+30+20+30,image=fp)
		can.create_text(x1+150+5+10+10,y1+50+int(can3["height"])+30+20+30,text="Profit",font=("FreeMono",13),anchor="w",fill="#000000")

		can.create_line(x1+150+5+10+10+f.measure("Sales")+20,y1+50+int(can3["height"])+30+20+30, x1+150+5+10+10+f.measure("Sales")+20+15,y1+50+int(can3["height"])+30+20+30,fill="#ff0000",width=2)
		can.create_text(x1+150+5+10+10+f.measure("Sales")+20+15+10,y1+50+int(can3["height"])+30+20+30,
			text="Linear regression for Profits",font=("FreeMono",13),fill="#000000",anchor="w")



	elif st=="Manage items":

		items_ar=[]


		forget_widgets(except_=dashboard)
		entries_show_reset()
		if con==0:

			man_items_ims={}
			man_item=None
			man_reset_st=False
			search_focus=False
			man_item_crop_v=[False,[]]
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

		sel_sb=["can","vertical"]


		can.place(in_=root,x=0,y=40)

		can2["width"]=width
		can2["height"]=40
		can2["bg"]="#ffffff"

		can2.delete("all")

		can2.create_line(0,0,width,0,fill="#000000")
		#can2.create_line(0,39,width,39,fill="#eeeeee")

		can2.place(in_=root,x=0,y=0)


		can3["width"]=14
		can3["height"]=height-40
		can3["bg"]="#ffffff"

		can3.delete("all")
		can3.place(in_=root,x=width-14,y=40)

		v=0


		_x_=450-10



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





			can.create_text(x1+10,y2-25-25-25, text=f"{format_text(row[1],x2-x1-20)}",font=("FreeMono",13),fill="#0000ff",anchor="w")
			can.create_text(x1+10,y2-25-25, text=f"Ksh.{formart_number(row[3],x2-x1-20,1)}",font=("FreeMono",13),fill="#ff0000",anchor="w")
			can.create_text(x1+10,y2-25, text=f"{formart_number(row[4],x2-x1-20)} items left",font=("FreeMono",13),fill="#000000",anchor="w")


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

			can.create_image(x_,int(can["height"])/2-(10+30)/2,image=man_items_ims[v],anchor="c")

			can.create_text(x_,int(can["height"])/2+250/2+10+15-(10+30)/2,text="No Record",font=("FreeMono",13),fill="#000000",anchor="c")



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
			add_items_ims={}
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


		

		add_items_coords["imagep"]=[x1+15,y1+15, x2-15,y2-15]






		can.create_image(x2-25,y2+5,image=delete,anchor="nw")
		add_items_coords["delete"]=[x2-25,y2+5]

		if add_item_crop_v[0]==False:
			can.create_image(x2-25-10-25,y2+5,image=crop2,anchor="nw")
		elif add_item_crop_v[0]==True:



			if len(add_item_crop_v[1])>0:

				if len(add_item_crop_v[1][-1])==2:

					x_,y_=add_item_crop_coord_norm

					x_+=x
					y_+=y
					add_item_crop_v[1][-1]=[x_,y_]



			can.create_image(x2-25-10-25,y2+5,image=crop1,anchor="nw")

		add_items_coords["crop"]=[x2-25-10-25,y2+5]
		can.create_image(x2-25-10-25-10-25,y2+5,image=refresh,anchor="nw")
		add_items_coords["refresh"]=[x2-25-10-25-10-25,y2+5]

		#print((y2+5+25+10+30+10)-y,"h")

		



		if con==0:
			add_items_ims["image"]=0

			add_item_crop_v=[False,[]]


		if not add_items_ims["image"]==0:

			process_add_item_im(add_items_ims["image"])

			add_items_coords["add_image"]=None

			can.create_rectangle(add_items_coords["imagep_"],outline="#000000")

		else:


			v+=1

			cx,cy=x1+(x2-x1)/2,y1+(y2-y1-80-20-15)/2+40

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
    global sel_sb
    global can3



    #terminal


    #vertical scroll

    if _scroll_[widget]["sb_st"]=="vertical" or _scroll_[widget]["sb_st"]=="both":


	    can3.focus_set()

	    x1=_scroll_[widget]["v_sb_coord"][0][2]
	    y1=_scroll_[widget]["v_sb_coord"][0][0]

	    x2,y2=x1+_scroll_[widget]["sb_sz"],y1+_scroll_[widget]["h"]

	    var=draw_v_sb(widget)




	    

	    if x1<=_x_<=x2:

	        if y1<=_y_<=y2:
	            sel_sb=[widget,"vertical"]	   
	            can3.focus_set()
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

	    
	    sb2=None

	    if widget=="can4r":
	    	sb2="can3r"

	    var=draw_h_sb(widget)

	    x1=_scroll_[widget]["h_sb_coord"][0][0]
	    y1=_scroll_[widget]["h_sb_coord"][0][2]

	    x2,y2=x1+_scroll_[widget]["w"],y1+4+_scroll_[widget]["sb_sz"]

	    if x1<=_x_<=x2:

	        if y1<=_y_<=y2:


	            sel_sb=[widget,"horizontal"]
	            _scroll_[widget]["h_drag_st"]=1


	            x=_x_-_scroll_[widget]["h_sb_coord"][0][0]

	            if var[0]<=x<=var[1]:

	                _scroll_[widget]["h_var"]=x-var[0]
	                return

	            _scroll_[widget]["h_sb_coord"][-1]=x/_scroll_[widget]["w"]


	            draw_h_sb(widget)


	            if sb2=="can3r":


		            sel_sb=["can3r","horizontal"]
		            _scroll_["can3r"]["h_drag_st"]=1



		            if var[0]<=x<=var[1]:

		                _scroll_["can3r"]["h_var"]=x-var[0]
		                return

		            _scroll_["can3r"]["h_sb_coord"][-1]=x/_scroll_["can3r"]["w"]


		            draw_h_sb("can3r")

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




	        sb2=None
	        if widget=="can4r":
	        	sb2="can3r"




	        x1=_scroll_[widget]["h_sb_coord"][0][0]
	        y1=_scroll_[widget]["h_sb_coord"][0][2]


	        x2,y2=x1+_scroll_[widget]["w"],y1+4+_scroll_[widget]["sb_sz"]

	        

	        #if y1<=_y_<=y2:

	        if x1<=_x_<=x2:

	            if x1<=_x_-_scroll_[widget]["h_var"]<=x2:



	                x=_x_-_scroll_[widget]["h_sb_coord"][0][0]-_scroll_[widget]["h_var"]

	                _scroll_[widget]["h_sb_coord"][-1]=x/_scroll_[widget]["w"]


	                draw_h_sb(widget)


	                if sb2=="can3r":



		                _scroll_["can3r"]["h_sb_coord"][-1]=x/_scroll_["can3r"]["w"]


		                draw_h_sb("can3r")



	                return

	        elif x1-10<_x_<x1:



	            _scroll_[widget]["h_sb_coord"][-1]=0


	            draw_h_sb(widget)

	            if sb2=="can3r":

		            _scroll_["can3r"]["h_sb_coord"][-1]=0


		            draw_h_sb("can3r")
	            return

	        elif x2+10>_x_>x2:



	            _scroll_[widget]["h_sb_coord"][-1]=1


	            draw_h_sb(widget)

	            if sb2=="can3r":


		            _scroll_["can3r"]["h_sb_coord"][-1]=1


		            draw_h_sb("can3r")


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

	x,y=im.size

	add_items_ims["image_"]=ImageTk.PhotoImage(im)

	can.delete(add_item_im)

	__x=((x2-x1)-x_)/2
	__y=((y2-y1)-y_)/2

	add_item_im=can.create_image(x1+__x,y1+__y,image=add_items_ims["image_"],anchor="nw")

	add_items_coords["imagep_"]=[x1+__x,y1+__y,x1+__x+x,y1+__y+y]


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

	x,y=im.size

	man_items_ims["image_"]=ImageTk.PhotoImage(im)

	can.delete(man_item_im)

	__x=((x2-x1)-x_)/2
	__y=((y2-y1)-y_)/2

	man_item_im=can.create_image(x1+__x,y1+__y,image=man_items_ims["image_"],anchor="nw")

	man_items_coords["imagep_"]=[x1+__x,y1+__y,x1+__x+x,y1+__y+y]





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


save_im=0
delete2=0
reset_im,reset_im2=0,0
calendar=0

previous,next_=0,0
previous2,next2=0,0
graph1,graph2=0,0
forecast1,forecast2=0,0
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
	global save_im,delete2,reset_im,reset_im2
	global calendar
	global previous,next_
	global previous2,next2
	global graph1,graph2
	global forecast1,forecast2


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


	#save

	im=Image.open("data/icons/save.png")
	im=im.resize((20,20))
	save_im=ImageTk.PhotoImage(im)

	#delete2

	im=Image.open("data/icons/delete2.png")
	im=im.resize((20,20))
	delete2=ImageTk.PhotoImage(im)

	#reset

	im=Image.open("data/icons/reset.png")

	im=im.resize((25,25))
	reset_im2=ImageTk.PhotoImage(im)
	im=im.resize((20,20))
	reset_im=ImageTk.PhotoImage(im)


	#calendar

	im=Image.open("data/icons/calendar.png")
	im=im.resize((30,30))
	calendar=ImageTk.PhotoImage(im)


	#previous

	im=Image.open("data/icons/previous.png")
	im=im.resize((20,20))
	previous=ImageTk.PhotoImage(im)



	#previous2

	im=Image.open("data/icons/previous2.png")
	im=im.resize((20,20))
	previous2=ImageTk.PhotoImage(im)

	#next

	im=Image.open("data/icons/next.png")
	im=im.resize((20,20))
	next_=ImageTk.PhotoImage(im)


	#next2

	im=Image.open("data/icons/next2.png")
	im=im.resize((20,20))
	next2=ImageTk.PhotoImage(im)

	#graph

	im=Image.open("data/icons/graph1.png")
	im=im.resize((25,25))
	graph1=ImageTk.PhotoImage(im)


	im=Image.open("data/icons/graph2.png")
	im=im.resize((25,25))
	graph2=ImageTk.PhotoImage(im)

	#forecast

	im=Image.open("data/icons/forecast1.png")
	im=im.resize((25,25))
	forecast1=ImageTk.PhotoImage(im)


	im=Image.open("data/icons/forecast2.png")
	im=im.resize((25,25))
	forecast2=ImageTk.PhotoImage(im)


db_items_=[]
def draw_db():
	global dashboard
	global db
	global sell_items_im,reports_im,manage_items_im,add_items_im,profiles_im
	global sell_items_im2,reports_im2,manage_items_im2,add_items_im2,profiles_im2
	global log_out_im
	global width,height
	global st
	global db_items_
	global graph1,graph2
	global forecast1,forecast2


	dashboard["width"]=200
	dashboard["height"]=height

	dashboard.delete("all")

	db_items=[]


	dashboard.create_image(int(dashboard["width"])-5-25,5,image=db,anchor="nw")



	items=[["Sell Items",sell_items_im,sell_items_im2],["Reports",reports_im,reports_im2],["Graphs",graph1,graph2],["Forecasts",forecast1,forecast2],["Manage items",manage_items_im,manage_items_im2],
			["Add Items",add_items_im,add_items_im2],["Profiles", profiles_im,profiles_im2]]


	y=5+25+20


	for i in items:

		if st==i[0]:

			dashboard.create_rectangle(0,y, int(dashboard["width"]),y+50, fill="#ffffff",outline="#ffffff")

			dashboard.create_text(10,y+25,text=i[0],font=("FreeMono",13),fill="#000000",anchor="w")

			dashboard.create_image(int(dashboard["width"])-5-25,y+12.5, image=i[2],anchor="nw")
 
		else:


			dashboard.create_text(10,y+25,text=i[0],font=("FreeMono",13),fill="#ffffff",anchor="w")

			dashboard.create_image(int(dashboard["width"])-5-25,y+12.5, image=i[1],anchor="nw")

		db_items_.append([i[0],y])

		y+=50



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
user_name=""
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
		col2="#ffffff"
	elif con==1:
		col="#00ff00"
		col2="#000000"


	x1,y1,x2,y2=cx-w/2,cy-h/2, cx+w/2,cy+h/2



	im=draw_round_rect(15,x1,y1,x2,y2, "#000000",col2=col,alpha=1,width=1)
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
	global can,dashboard,can3
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
	global sel_sb
	global add_item_crop_v,add_item_crop_coord_norm
	global man_item_crop_v,man_item_crop_coord_norm
	global pay_st
	global sell_items_coords
	global _total_
	global cal_st
	global rep_items_coord
	global all_by
	global graph_coords
	global graph_st
	global forecast_coords




	if pay_st=="Cash":

		can_b1_sb("cart2",e.x,can.canvasy(e.y))

	if st_=="main" and st=="Reports":

		can_b1_sb("can4r",e.x,e.y)

	#sel_sb=None

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


			if pay_st==None:

				if sel_item==None:

					for i in items_ar:

						x1,y1,x2,y2=i[1:]

						if x1<=e.x<=x2:
							if y1<=can.canvasy(e.y)<=y2:

								draw_selected_item(i[0],0)

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


					xx,yy=int(can["width"])-int(dashboard["width"])-60,int(int(can["height"])*0.7)


					x=x+((int(can["width"])-x)-xx)/2
					y=can.canvasy(40+((int(can["height"])-40)-yy)/2)-20



					x1,y1,x2,y2=add_c_coord

					cx,cy=x1+15,y1+15

					r=math.sqrt((e.x-cx)**2+(can.canvasy(e.y)-cy)**2)

					db_items=database.connect("data/items.db")
					cur=db_items.cursor()

					cur.execute(f"SELECT * FROM items WHERE item_id={sel_item}")

					sp=float(cur.fetchall()[0][3])

					if r<=15:

						try:
							v1=int(ent1.get())
							v2=int(ent2.get())

						except:

							message(0,can,"Invalid input!",x+xx/2,y+yy+10+15,350,30)

							return

						if int(ent1.get())>sp:
							message(0,can,"Item can't be sold above selling price!",x+xx/2,y+yy+10+15,350,30)

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

						if int(ent1.get())>sp:
							message(0,can,"Item can't be sold above selling price!",x+xx/2,y+yy+10+15,350,30)

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

							if int(ent1.get())>sp:
								message(0,can,"Item can't be sold above selling price!",x+xx/2,y+yy+10+15,350,30)

								return


							cart_ar.append([sel_item,ent1.get(),ent2.get()])

							#sel_item=None
							#qp=None

							main(1)

							message(1,can,"Item added to cart!",x+xx/2,y+yy+10+15,350,30)


							return

			if pay_st=="Cash":
				x,y=qp


				if x<=e.x<=x+25:
					if y<=can.canvasy(e.y)<=y+25:


						pay_st=None
						qp=None

						main(1)

						return


				x=int(dashboard.place_info()["x"])+int(dashboard["width"])

				xx,yy=int(can["width"])-int(dashboard["width"])-60,int(int(can["height"])*0.7)


				x=x+((int(can["width"])-x)-xx)/2
				y=can.canvasy(40+((int(can["height"])-40)-yy)/2)


				if int(dashboard.place_info()["x"])<0:
					_x=5+25+5
				else:
					_x=int(dashboard["width"])
				x_=_x+(int(can["width"])-_x)/2

				x1,y1,x2,y2=sell_items_coords["complete payment"]

				cx,cy=x1+15,y1+15

				r=math.sqrt((e.x-cx)**2+(can.canvasy(e.y)-cy)**2)

				if r<=15:

					if ent1.get()=="":

						message(0,can,"Enter amount paid!",x+xx/2,y+yy+10+15,350,30)

						return

					try:

						v=int(ent1.get())
					except:


						message(0,can,"Amount paid must be a number!",x+xx/2,y+yy+10+15,350,30)

						return


					if int(ent1.get())<_total_:

						message(0,can,"Amount paid is less than sub total!",x+xx/2,y+yy+10+15,350,30)

						return


					if complete_payment()==1:

						pay_st=None
						cart_ar=[]
						main(1)

						message(1,can,"Purchase successfull!",x_,can.canvasy(int(can["height"])-20-15),350,30)

					else:
						message(0,can,"Purchase not successfull!",x+xx/2,y+yy+10+15,350,30)



				cx,cy=x2-15,y1+15

				r=math.sqrt((e.x-cx)**2+(can.canvasy(e.y)-cy)**2)

				if r<=15:

					if ent1.get()=="":

						message(0,can,"Enter amount paid!",x+xx/2,y+yy+10+15,350,30)

						return

					try:

						v=int(ent1.get())
					except:


						message(0,can,"Amount paid must be a number!",x+xx/2,y+yy+10+15,350,30)

						return


					if int(ent1.get())<_total_:

						message(0,can,"Amount paid is less than sub total!",x+xx/2,y+yy+10+15,350,30)

						return


					if complete_payment()==1:

						pay_st=None
						cart_ar=[]
						main(1)
						message(1,can,"Purchase successfull!",x_,can.canvasy(int(can["height"])-20-15),350,30)

					else:
						message(0,can,"Purchase not successfull!",x+xx/2,y+yy+10+15,350,30)

				if x1+15<=e.x<=x2-15:
					if y1<=can.canvasy(e.y)<=y2:



						if ent1.get()=="":

							message(0,can,"Enter amount paid!",x+xx/2,y+yy+10+15,350,30)

							return

						try:

							v=int(ent1.get())
						except:


							message(0,can,"Amount paid must be a number!",x+xx/2,y+yy+10+15,350,30)

							return


						if int(ent1.get())<_total_:

							message(0,can,"Amount paid is less than sub total!",x+xx/2,y+yy+10+15,350,30)

							return


						if complete_payment()==1:
							pay_st=None
							cart_ar=[]
							main(1)

							message(1,can,"Purchase successfull!",x_,can.canvasy(int(can["height"])-20-15),350,30)

						else:
							message(0,can,"Purchase not successfull!",x+xx/2,y+yy+10+15,350,30)


		elif st=="Reports":

			x_,y_=rep_items_coord["calendar"]

			if x_<=e.x<=x_+30:
				if y_<=e.y<=y_+30:

					if cal_st==0:
						cal_st=1
						draw_cal(rep_items_coord["calendar"][0]+30,rep_items_coord["calendar"][1]+30)
						return

					else:
						cal_st=0
						cal.place_forget()
						return


			x1,y1,x2,y2=rep_items_coord["all_by_month"]

			cx,cy=x1+15,y1+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:

				if all_by==None or all_by=="year":

					all_by="month"

					main(1)

					return

				elif all_by=="month":

					all_by=None
					main(1)

					return


			cx,cy=x2-15,y1+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:

				if all_by==None or all_by=="year":

					all_by="month"

					main(1)

					return

				elif all_by=="month":
					
					all_by=None
					main(1)

					return

			if x1+15<=e.x<=x2-15:
				if y1<=e.x<=y2:

					if all_by==None or all_by=="year":

						all_by="month"

						main(1)

						return

					elif all_by=="month":
						
						all_by=None
						main(1)

						return



			x1,y1,x2,y2=rep_items_coord["all_by_year"]


			cx,cy=x1+15,y1+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:

				if all_by==None or all_by=="month":

					all_by="year"

					main(1)

					return

				elif all_by=="year":

					all_by=None
					main(1)

					return


			cx,cy=x2-15,y1+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:

				if all_by==None or all_by=="month":

					all_by="year"

					main(1)

					return

				elif all_by=="year":
					
					all_by=None
					main(1)

					return

			if x1+15<=e.x<=x2-15:
				if y1<=e.x<=y2:

					if all_by==None or all_by=="month":

						all_by="year"

						main(1)

						return

					elif all_by=="year":
						
						all_by=None
						main(1)

						return

		elif st=="Graphs":

			x_,y_=graph_coords["calendar"]


			if x_<=e.x<=x_+30:
				if y_<=e.y<=y_+30:

					if cal_st==0:
						cal_st=1
						draw_cal(graph_coords["calendar"][0]+30,graph_coords["calendar"][1]+30)
						return

					else:
						cal_st=0
						cal.place_forget()
						return

			x_,y_=graph_coords["next"]

			if x_<=e.x<=x_+20:
				if y_<=e.y<=y_+20:

					if graph_st=="Annually":
						graph_st="Monthly"
					elif graph_st=="Monthly":
						graph_st="Annually"


					main(1)

					return




			x_,y_=graph_coords["previous"]

			if x_<=e.x<=x_+20:
				if y_<=e.y<=y_+20:

					if graph_st=="Annually":
						graph_st="Monthly"
					elif graph_st=="Monthly":
						graph_st="Annually"


					main(1)

					return

		elif st=="Forecasts":


			x_,y_=forecast_coords["left"]

			if x_<=e.x<=x_+20:

				if y_<=e.y<=y_+20:

					can3.xview_scroll(-1,"units")

					return



			x_,y_=forecast_coords["right"]

			if x_<=e.x<=x_+20:

				if y_<=e.y<=y_+20:

					can3.xview_scroll(1,"units")

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

						man_item_crop_v=[False,[]]


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
					if y1<=can.canvasy(e.y)<=y2:
						ent1.focus_set()
						return

				x1,y1,x2,y2=man_items_coords["bp"]

				if x1<=e.x<=x2:
					if y2<=can.canvasy(e.y)<=y2:
						ent2.focus_set()
						return


				x1,y1,x2,y2=man_items_coords["sp"]

				if x1<=e.x<=x2:
					if y1<=can.canvasy(e.y)<=y2:
						ent3.focus_set()
						return

				x1,y1,x2,y2=man_items_coords["q"]

				if x1<=e.x<=x2:
					if y1<=can.canvasy(e.y)<=y2:
						ent4.focus_set()
						return

				x1,y1,x2,y2=man_items_coords["desc"]

				if x1<=e.x<=x2:
					if y1<=can.canvasy(e.y)<=y2:
						text1.focus_set()
						return

				if not man_items_coords["add_image"]==None:


					cx,cy=man_items_coords["add_image"]

					r=math.sqrt((e.x-cx)**2+(can.canvasy(e.y)-cy)**2)

					if r<=40:

						file=filedialog.askopenfilename()

						if file=="":
							return
						





						try:
							im=Image.open(file)

							man_items_ims["image"]=im
							man_items_ims["_image_"]=im

							main(1)


						except Exception as e:
							print(e)
							message(0,can,"Can't process image!",x+xx/2,y+yy+10+15,350,30)

						return
				x1,y1=man_items_coords["delete"]

				if x1<=e.x<=x1+25:
					if y1<=can.canvasy(e.y)<=y1+25:

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

				x1,y1=man_items_coords["delete"]

				if x1<=e.x<=x1+25:
					if y1<=can.canvasy(e.y)<=y1+25:

						man_items_ims["image"]=0
						man_items_ims["_image_"]=0

						man_item_crop_v=[False,[]]



						main(1)

						return

				x1,y1=man_items_coords["crop"]

				if x1<=e.x<=x1+25:
					if y1<=can.canvasy(e.y)<=y1+25:


						if man_item_crop_v[0]==True:


							man_item_crop_v=[False,[]]

						else:



							if man_items_ims["image"]!=0:

								man_item_crop_v=[True,[]]

						


						main(1)

						return


				x1,y1=man_items_coords["refresh"]

				if x1<=e.x<=x1+25:
					if y1<=can.canvasy(e.y)<=y1+25:

						man_item_crop_v=[False,[]]

						if man_items_ims["image"]!=0:

							man_items_ims["image"]=man_items_ims["_image_"]



						main(1)

						return




				if man_item_crop_v[0]==True:

					_x_,_y_=e.x,can.canvasy(e.y)

					x1,y1,x2,y2=man_items_coords["imagep_"]


					if x1<=_x_<=x2:
						if y1<=_y_<=y2:


							if len(man_item_crop_v[1])==0:


								man_item_crop_v[1].append([_x_,_y_])

								man_item_crop_coord_norm=[_x_-x,_y_-y]



							else:

								if len(man_item_crop_v[1][-1])==2:

									man_item_crop_v[1][-1].append(_x_)
									man_item_crop_v[1][-1].append(_y_)


									x1_,y1_,x2_,y2_=man_item_crop_v[1][-1]

									_x,_y=man_items_ims["image"].size

									x_1=int(round((x1_-x1)*_x/(x2-x1),0))
									x_2=int(round((x2_-x1)*_x/(x2-x1),0))

									y_1=int(round((y1_-y1)*_y/(y2-y1),0))
									y_2=int(round((y2_-y1)*_y/(y2-y1),0))


									man_items_ims["image"]=man_items_ims["image"].crop((x_1,y_1,x_2,y_2))

									man_item_crop_v[0]=False

									main(1)




								elif len(man_item_crop_v[1][-1])==4:

									man_item_crop_v[1].append([_x_,_y_])

									man_item_crop_coord_norm=[_x_-x,_y_-y]






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
					



					if file=="":
						return


					try:
						im=Image.open(file)

						add_items_ims["_image_"]=im
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
					add_items_ims["_image_"]=0

					add_item_crop_v=[False,[]]



					main(1)

					return

			x1,y1=add_items_coords["crop"]

			if x1<=e.x<=x1+25:
				if y1<=e.y<=y1+25:

					if add_item_crop_v[0]==True:


						add_item_crop_v=[False,[]]

					else:


						if add_items_ims["image"]!=0:

							add_item_crop_v=[True,[]]

					


					main(1)

					return


			x1,y1=add_items_coords["refresh"]

			if x1<=e.x<=x1+25:
				if y1<=e.y<=y1+25:

					add_item_crop_v=[False,[]]

					if add_items_ims["image"]!=0:

						add_items_ims["image"]=add_items_ims["_image_"]



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




			if add_item_crop_v[0]==True:

				_x_,_y_=e.x,can.canvasy(e.y)

				x1,y1,x2,y2=add_items_coords["imagep_"]


				if x1<=_x_<=x2:
					if y1<=_y_<=y2:


						if len(add_item_crop_v[1])==0:


							add_item_crop_v[1].append([_x_,_y_])

							add_item_crop_coord_norm=[_x_-x,_y_-y]



						else:

							if len(add_item_crop_v[1][-1])==2:

								add_item_crop_v[1][-1].append(_x_)
								add_item_crop_v[1][-1].append(_y_)


								x1_,y1_,x2_,y2_=add_item_crop_v[1][-1]

								_x,_y=add_items_ims["image"].size

								x_1=int(round((x1_-x1)*_x/(x2-x1),0))
								x_2=int(round((x2_-x1)*_x/(x2-x1),0))

								y_1=int(round((y1_-y1)*_y/(y2-y1),0))
								y_2=int(round((y2_-y1)*_y/(y2-y1),0))


								add_items_ims["image"]=add_items_ims["image"].crop((x_1,y_1,x_2,y_2))

								add_item_crop_v[0]=False

								main(1)




							elif len(add_item_crop_v[1][-1])==4:

								add_item_crop_v[1].append([_x_,_y_])

								add_item_crop_coord_norm=[_x_-x,_y_-y]










			

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


add_items_crop_v_=0
man_items_crop_v_=0
def can_motion(e):
	global st_,st
	global add_item_crop_v,man_item_crop_v
	global add_items_coords,man_items_coords
	global add_items_crop_v_,man_items_crop_v_

	if st_=="main":

		if st=="Add Items":

			if add_item_crop_v[0]==True:

				x,y=e.x,can.canvasy(e.y)

				x1,y1,x2,y2=add_items_coords["imagep_"]


				if x1<=x<=x2:
					if y1<=y<=y2:


						if len(add_item_crop_v[1])>0:

							if len(add_item_crop_v[1][-1])==2:

								x1_,y1_=add_item_crop_v[1][-1]

								can.delete(add_items_crop_v_)

								add_items_crop_v_=can.create_rectangle(x1_,y1_, x,y,outline="#ff0000")
			else:
				can.delete(add_items_crop_v_)


		elif st=="Manage items":

			if man_item_crop_v[0]==True:

				x,y=e.x,can.canvasy(e.y)

				x1,y1,x2,y2=man_items_coords["imagep_"]


				if x1<=x<=x2:
					if y1<=y<=y2:


						if len(man_item_crop_v[1])>0:

							if len(man_item_crop_v[1][-1])==2:

								x1_,y1_=man_item_crop_v[1][-1]

								can.delete(man_items_crop_v_)

								man_items_crop_v_=can.create_rectangle(x1_,y1_, x,y,outline="#ff0000")

			else:
				can.delete(man_items_crop_v_)								


def can_drag(e):
	global pay_st
	global st_,st


	if pay_st=="Cash":

		sb_drag("cart2",e.x,can.canvasy(e.y))


	if st_=="main" and st=="Reports":

		sb_drag("can4r",e.x,e.y)



def can_b1_sb_release(widget):

    global _scroll_,pay_st

    if pay_st=="Cash":


	    _scroll_[widget]["v_drag_st"]=0
	    _scroll_[widget]["h_drag_st"]=0


def can_b1_release(e):

	can_b1_sb_release("cart2")




sel_sb=None
def scroll(e):
	global _scroll_
	global sel_sb
	global sel_item,man_item



	if sel_item==None and man_item==None:





		if not sel_sb==None:


			if sel_sb[1]=="vertical":


				var=-int(e.delta/120)


				_scroll_[sel_sb[0]]["widget"].yview_scroll(var,"units")

				h=_scroll_[sel_sb[0]]["_y"]

				y=_scroll_[sel_sb[0]]["widget"].canvasy(0)


				_scroll_[sel_sb[0]]["v_sb_coord"][-1]=y/h


				draw_v_sb(sel_sb[0])

			elif sel_sb[1]=="horizontal":

				sb2=None


				if sel_sb[0]=="can4r":
					sb2="can3r"


				
				var=-int(e.delta/120)


				_scroll_[sel_sb[0]]["widget"].xview_scroll(var,"units")

				w=_scroll_[sel_sb[0]]["_x2"]

				x=_scroll_[sel_sb[0]]["widget"].canvasx(0)


				_scroll_[sel_sb[0]]["h_sb_coord"][-1]=x/w


				draw_h_sb(sel_sb[0])

				if sb2!=None:

					_scroll_[sb2]["widget"].xview_scroll(var,"units")

					w=_scroll_[sb2]["_x2"]

					x=_scroll_[sb2]["widget"].canvasx(0)


					_scroll_[sb2]["h_sb_coord"][-1]=x/w


					draw_h_sb(sb2)


can=tk.Canvas(width=width,height=height,relief="flat",bg="#ffffff",highlightthickness=0,border=0)
can.place(in_=root,x=0,y=0)
can.bind("<Button-1>",can_b1)
can.bind("<Motion>",can_motion)
can.bind("<B1-Motion>",can_drag)
can.bind_all("<MouseWheel>",scroll)
can.bind("<ButtonRelease-1>",can_b1_release)

def can2_b1(e):
	global search_coords
	global search_focus
	global sel_item
	global search_val
	global st_,st
	global sel_sb

	#sel_sb=None

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
	global sel_sb
	global pay_st

	#sel_sb=None

	if st_=="main" and search_focus==True:



		if st=="Sell Items" or st=="Manage items":

			search_focus=False

			main(1)


	if sel_item==None and man_item==None and pay_st==None:

		

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






			x1,y1,x2,y2=cart_buttons_coords["pay_with_cash"]


			cx,cy=x1+15,y1+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:
				pay_with_cash(0)


				return

			cx,cy=x2-15,y1+15

			r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

			if r<=15:

				pay_with_cash(0)


				return

			if x1+15<=e.x<=x2-15:
				if y1<=e.y<=y2:

					pay_with_cash(0)

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
can3.bind_all("<MouseWheel>",scroll)


can["scrollregion"]=(0,0,width,height)


def can4_b1(e):
	global sel_sb

	#sel_sb=None



	pass


can4=tk.Canvas(relief="flat",bg="#ffffff",highlightthickness=0,border=0)
can4.bind("<Button-1>",can4_b1)

can5=tk.Canvas(relief="flat",bg="#ffffff",highlightthickness=0,border=0)

db_st=0
def dashboard_b1(e):
	global dashboard
	global db_st
	global db_items_
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

	for i in db_items_:

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
	global sel_sb

	#sel_sb=None

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


cal_coord={}

days_ar=[]
def draw_cal(xx,yy):
	global cal
	global _date_
	global previous,next_
	global cal_coord
	global days_ar
	global reset_im2
	global st

	cal.delete("all")




	f=font.Font(family="FreeMono",size=13)

	year,month,day=_date_.split("-")
	year=int(year)
	month=int(month)
	day=int(day)

	if year%4==0:
		feb_=29
	else:
		feb_=28

	months={
	1:["January",31],
	2:["February",feb_],
	3:["March",31],
	4:["April",30],
	5:["May",31],
	6:["June",30],
	7:["July",31],
	8:["August",31],
	9:["September",30],
	10:["October",31],
	11:["November",30],
	12:["December",31]
	}


	cal.create_image(5,5,image=previous,anchor="nw")
	cal_coord["yp"]=[5,5]

	cal.create_text(5+20+5,5+10,text=str(year),font=("FreeMono",13),fill="#ffffff",anchor="w")

	cal.create_image(5+20+5+f.measure(str(year))+5,5,image=next_,anchor="nw")
	cal_coord["yn"]=[5+20+5+f.measure(str(year))+5,5]




	cal.create_image(5,5+20+15,image=previous,anchor="nw")
	cal_coord["mp"]=[5,5+20+15]



	cal.create_text(5+20+5,5+10+20+15,text=str(months[month][0]),font=("FreeMono",13),fill="#ffffff",anchor="w")

	cal.create_image(5+20+5+f.measure(str(months[month][0]))+5,5+20+15,image=next_,anchor="nw")

	cal_coord["mn"]=[5+20+5+f.measure(str(months[month][0]))+5,5+20+15]





	cal.place(in_=root,x=xx,y=yy+40)


	day_of_week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
	day_of_week2=["MON","TUE","WED","THUR","FRI","SAT","SUN"]



	y=5+20+15+40+30-20

	x=350/7/2
	for d in day_of_week2:

		cal.create_text(x,y,text=d,font=("FreeMono",13),fill="#ffffff",anchor="c")


		x+=350/7

	cal.create_line(0,y+15,350,y+15,fill="#ffffff")


	date_obj = datetime.date(year, month, 1)

	# Get the full weekday name
	day_name = date_obj.strftime('%A')

	
	i=day_of_week.index(day_name)
	n=months[month][1]




	x=350/7/2+(i)*350/7
	y=y+15+350/7/2

	d=1

	i_=i

	days_ar=[]

	for _ in range(n):
		col="#ffffff"




		if day==d and st=="Reports":

			cal.create_rectangle(x-350/7/2,y-350/7/2, x+350/7/2,y+350/7/2,fill="#ffffff",outline="#ffffff")

			col="#000000"

		cal.create_text(x,y,text=str(d),font=("FreeMono",13),fill=col,anchor="c")

		days_ar.append([d,[x-350/7/2,y-350/7/2, x+350/7/2,y+350/7/2]])

		i_+=1

		if i_==7:

			x=350/7/2
			y+=350/7

			i_=0

		else:

			x+=350/7



		d+=1

	y+=350/7/2

	cal["width"]=350

	cal["height"]=y

	cal.create_rectangle(0,0, int(cal["width"])-1,int(cal["height"])-1,outline="#ffffff")

	cal.create_image(int(cal["width"])-5-25,5,image=reset_im2,anchor="nw")

	cal_coord["reset"]=int(cal["width"])-5-25,5


def cal_b1(e):
	global cal
	global cal_coord
	global _date_
	global days_ar
	global all_by
	global st

	year,month,day=_date_.split("-")
	year=int(year)
	month=int(month)
	day=int(day)

	x,y=cal_coord["reset"]

	if x<=e.x<=x+20:
		if y<=e.y<=y+20:

			_date_=str(datetime.datetime.now()).split(" ")[0]

			all_by=None

			main(1)
			return


	x,y=cal_coord["yp"]

	if x<=e.x<=x+20:
		if y<=e.y<=y+20:
			year-=1

			month=str(month)

			if len(month)==1:
				month="0"+month



			_date_=f"{year}-{month}-01"

			all_by=None

			main(1)



			return


	x,y=cal_coord["yn"]

	if x<=e.x<=x+20:
		if y<=e.y<=y+20:
			year+=1


			month=str(month)

			if len(month)==1:
				month="0"+month

			_date_=f"{year}-{month}-01"

			all_by=None

			main(1)

			return


	x,y=cal_coord["mp"]

	if x<=e.x<=x+20:
		if y<=e.y<=y+20:

			month-=1

			if month<=0:
				month=12


			month=str(month)

			if len(month)==1:
				month="0"+month

			_date_=f"{year}-{month}-01"
			all_by=None

			main(1)

			return


	x,y=cal_coord["mn"]

	if x<=e.x<=x+20:
		if y<=e.y<=y+20:

			month+=1

			if month>12:
				month=1


			month=str(month)

			if len(month)==1:
				month="0"+month

			_date_=f"{year}-{month}-01"

			all_by=None

			main(1)

			return


	if st=="Reports":


		for i in days_ar:

			d=i[0]
			x1,y1,x2,y2=i[1]

			if x1<=e.x<=x2:
				if y1<=e.y<=y2:

					day=d


					month=str(month)

					if len(month)==1:
						month="0"+month


					day=str(day)

					if len(day)==1:
						day="0"+day


					_date_=f"{year}-{month}-{day}"

					all_by=None

					main(1)

					return






cal=tk.Canvas(bg="#000000",relief="flat",highlightthickness=0,border=0)

cal.bind("<Button-1>",cal_b1)

t_widgets={"entries":[ent1,ent2,ent3,ent4,ent_search],
			"text":[text1],
			"canvas":[dashboard,can,can2,can3,can4,can5,cal]}













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


try:
	dbuser=database.connect('data/reports.db')
	cur=dbuser.cursor()	
	cur.execute("""CREATE TABLE reports(
		item_name VARCHAR(255),
		date_time VARCHAR(255),
		sold_by VARCHAR(255),
		quantity INT,
		bp,INT
		sp INT,
		sold_at INT

		);""")

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
check_balance()
root.mainloop()