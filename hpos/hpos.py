import tkinter as tk
from tkinter import font
from PIL import Image,ImageTk,ImageDraw


db=0
sell_items_im,reports_im,manage_items_im,add_items_im,profiles_im=0,0,0,0,0
sell_items_im2,reports_im2,manage_items_im2,add_items_im2,profiles_im2=0,0,0,0,0
log_out_im=0
def load_im():
	global db
	global sell_items_im,reports_im,manage_items_im,add_items_im,profiles_im
	global sell_items_im2,reports_im2,manage_items_im2,add_items_im2,profiles_im2
	global log_out_im


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
			["Add Item",add_items_im,add_items_im2],["Profiles", profiles_im,profiles_im2]]


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




root=tk.Tk()


width,height=root.winfo_screenwidth()-50,root.winfo_screenheight()-50

root.geometry(f"{width}x{height}+0+0")


can=tk.Canvas(width=width,height=height,relief="flat",bg="#ffffff",highlightthickness=0,border=0)
can.place(in_=root,x=0,y=0)


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

		if i[1]<=e.y<=i[1]+40:

			st=i[0]

			draw_db()

			return

def move_db():
	global dashboard
	global db_st


	if not db_st==0:



		x=int(dashboard.place_info()["x"])


		if db_st==1:

			if x==0:

				db_st=0

			else:

				x+=1

				dashboard.place(in_=root,x=x,y=0)






		elif db_st==2:



			if x==-int(dashboard["width"])+5+25+5:

				db_st=0
			else:

				x-=1


				dashboard.place(in_=root,x=x,y=0)





	root.after(1,move_db)


dashboard=tk.Canvas(width=200,height=height,relief="flat",bg="#000000",highlightthickness=0,border=0)
dashboard.bind("<Button-1>",dashboard_b1)

dashboard.place(in_=root,x=0,y=0)

st="Sell Items"

load_im()

draw_db()

move_db()

root.mainloop()