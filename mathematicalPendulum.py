import graphics as gr
from math import sin, cos, sqrt, pi
from tkinter import *
#from PIL import ImageTk, Image

g = 3

class MathematicalPendulum:
    def __init__(self, radius, mass, length, color, angle, angle_velocity, k):
        self.r = radius
        self.m = mass
        self.color = color
        self.l = length
        self.angle = angle
        self.angle_velocity = angle_velocity
        self.angle_acceleration = 0
        self.coords = gr.Point(center_point.x + length * sin(angle),
                               center_point.y + length * cos(angle))

        self.circle = None
        self.gamma = k / mass
        self.omega_0 = sqrt(g / length)
        self.line = None


# A function that converts degrees to radians
def degToRad(angle):
    return (angle * pi / 360)


#
def drawBall(coords, radius, color):
    circle = gr.Circle(coords, radius)
    circle.setFill(color)
    circle.draw(window)
    return circle


def drawLine(start, end, color):
    line = gr.Line(gr.Point(start.x, start.y), gr.Point(end.x, end.y))
    line.setFill(color)
    line.draw(window)
    return line


# A function that returns the sum of two vectors
def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)
    return new_point


# A function that returns the difference of two vectors
def sub(point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)
    return new_point


def update_angle(pendulum):
    pendulum.accelaration = -2 * pendulum.gamma * pendulum.angle_velocity - (pendulum.omega_0 ** 2) * sin(pendulum.angle)
    pendulum.angle_velocity = pendulum.angle_velocity + pendulum.angle_acceleration
    pendulum.angle = pendulum.angle + pendulum.angle_velocity
    return pendulum.angle, pendulum.angle_velocity, pendulum.accelaration


def moving(pendulum):
    pendulum.angle, pendulum.angle_velocity, pendulum.angle_acceleration = update_angle(pendulum)
    pendulum.coords = pendulum.circle.getCenter()
    new_coords = gr.Point(center_point.x + pendulum.l * sin(pendulum.angle),
                          center_point.y + pendulum.l * cos(pendulum.angle))
    v = sub(new_coords, pendulum.coords)
    pendulum.circle.move(v.x, v.y)

#Функция, создающая объект с параметрами, введенными в поля
#def object_parameters_entry():
 #   pendulum = MathematicalPendulum(float(entry_radius.get()), float(entry_mass.get()),
  #                                  float(entry_length.get()), variable_color.get(),
   #                                       float(entry_angle.get()), float(entry_velocity.get(), 0)
   # return pendulum



# creating of tkinter window
root = Tk()
root.title('Start settings')
root.geometry('150x300')
root.resizable(0, 0)


#ball's color menu
label_color = Label(root, text="Ball's color", font='bold')
label_color.place(x=20, y=15)

COLORS = [
    "orange",
    "yellow",
    "red",
    "blue",
    "green",
    "gray",
    "black"
]
variable_color = StringVar(root)
variable_color.set(COLORS[0]) #default value
color_menu = OptionMenu(root, variable_color, *COLORS,)
color_menu.place(x=20, y=40)

#Ball's mass input field
label_mass = Label(root, text='m =', font='bold')
label_mass.place(x=20, y=77)
entry_mass = Entry(root, width=4)
entry_mass.place(x=55, y=80)
entry_mass.insert(END, '10')
label_mass_dimension = Label(root, text="units", font='bold')
label_mass_dimension.place(x=83, y=77)

#Ball's radius input field
label_radius = Label(root, text='r   = ', font='bold')
label_radius.place(x=20, y=114)
entry_radius = Entry(root, width=4)
entry_radius.place(x=55, y=117)
entry_radius.insert(END, '30')
label_radius_dimension = Label(root, text="px", font='bold')
label_radius_dimension.place(x=85, y=115)

#Rope length input field
label_length = Label(root, text="l    = ", font='bold')
label_length.place(x=20, y=151)
entry_length = Entry(root, width=4)
entry_length.place(x=55, y=154)
entry_length.insert(END, '300')
label_length_dimension = Label(root, text="px", font='bold')
label_length_dimension.place(x=85, y=152)


#Starting angle input field
label_angle = Label(root, text="α   =", font='bold')
label_angle.place(x=20, y=188)
entry_angle = Entry(root, width=4)
entry_angle.place(x=55, y=191)
entry_angle.insert(END, '120')
label_angle_dimension = Label(root, text="°", font='bold')
label_angle_dimension.place(x=83, y=190)


#Startin angular velocity input field
label_velocity = Label(root, text="ω  = ", font='bold')
label_velocity.place(x=20, y=225)
entry_velocity = Entry(root, width=4)
entry_velocity.place(x=55, y=228)
entry_velocity.insert(END, '0')
label_velocity_dimension = Label(root, text="°/sec", font='bold')
label_velocity_dimension.place(x=83, y=226)


scheme = PhotoImage(file="scheme.png")
scheme_label = Label(root)
scheme_label.image = scheme
scheme_label['image'] = scheme_label.image
scheme_label.place(x=120, y=10)


btn_run = Button(root, text='RUN', font='Bold')
btn_run.bind('<Button-1>', lambda event: (root.quit()))
btn_run.place(x=20, y=255, width=100)




root.mainloop()





# Window drawing
SIZE_X = 800
SIZE_Y = 800
window = gr.GraphWin("Pendulum", SIZE_X, SIZE_Y)


#Window's center:
center_point = gr.Point(SIZE_X / 2, SIZE_Y / 2)

#Creating MathematicalPendulum object with parameters form entry fields
pendulum = MathematicalPendulum(float(entry_radius.get()), float(entry_mass.get()),
                                    float(entry_length.get()), variable_color.get(),
                                ((pi * float(entry_angle.get()))/180),  ((pi * float(entry_velocity.get()))/180), 0.1)
pendulum.circle = drawBall(pendulum.coords, pendulum.r, pendulum.color)
pendulum.circle.setWidth(2)
root.destroy()

while True:
    moving(pendulum)
    #wire drawing
    line_coords = gr.Point(center_point.x + (pendulum.l-pendulum.r) * sin(pendulum.angle),
               center_point.y + (pendulum.l-pendulum.r) * cos(pendulum.angle))

    pendulum.line = drawLine(center_point, line_coords, "black")
    pendulum.line.setWidth(2)
    gr.time.sleep(0.0001)
    pendulum.line.undraw()

