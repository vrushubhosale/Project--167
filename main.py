from tkinter import *

root= Tk()
root.title("DBASIC DRAWING APP")
root.geometry("600x600")

color_label=Label(root, text="Enter a color :")
color_label.place(relx=0.6, rely=0.9, anchor= CENTER)

input_box = Entry(root)
input_box.insert(0, "brown")
input_box.place(relx=0.8,rely=0.9, anchor= CENTER)

canvas=Canvas(root, width = 590, height=510, bg= "white", highlightbackground="lightgray")
canvas.pack()

direction = ""
oldx=50
oldy=50
newx=50
newy=50

def right_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newx=newx+5
    direction = "right"
    draw(direction, oldx,oldy, newx ,newy)

def left_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newx=newx-5
    direction = "left"
    draw(direction, oldx,oldy, newx ,newy)
    
def up_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newy=newy-5
    direction = "up"
    draw(direction, oldx,oldy, newx ,newy)
    
def down_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newy=newy+5
    direction = "down"
    draw(direction, oldx,oldy, newx ,newy)


def draw(direction,oldx,oldy,newx,newy):
    fill_color = input_box.get()
    if (direction=="right"):
        right_line=canvas.create_line(oldx,oldy,newx,newy,width = 3,fill=fill_color)
    if (direction=="left"):
        left_line=canvas.create_line(oldx,oldy,newx,newy,width = 3,fill=fill_color)
    if (direction=="up"):
        up_line=canvas.create_line(oldx,oldy,newx,newy,width = 3,fill=fill_color)    
    if (direction=="down"):
        down_line=canvas.create_line(oldx,oldy,newx,newy,width = 3,fill=fill_color)

root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Down>",down_dir)
root.bind("<Up>",up_dir)

root.mainloop()