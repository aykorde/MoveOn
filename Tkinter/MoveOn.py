from tkinter import *
from tkinter import messagebox
from Test import *
import webbrowser


class MyWindow:
    def __init__(self, win):

        self.x = Label(win, text='X', width=5)
        self.x.place(x=210, y=10)
        self.y = Label(win, text='Y', width=5)
        self.y.place(x=280, y=10)
        self.z = Label(win, text='Z', width=5)
        self.z.place(x=350, y=10)

        self.acc = Label(win, text='Acceleration', width=11)
        self.acc.place(x=100, y=50)
        self.ax = Entry(width=10)
        self.ax.place(x=200, y=50)
        self.ay = Entry(width=10)
        self.ay.place(x=270, y=50)
        self.az = Entry(width=10)
        self.az.place(x=340, y=50)

        self.gyro = Label(win, text='Gyro', width=11)
        self.gyro.place(x=100, y=100)
        self.gx = Entry(width=10)
        self.gx.place(x=200, y=100)
        self.gy = Entry(width=10)
        self.gy.place(x=270, y=100)
        self.gz = Entry(width=10)
        self.gz.place(x=340, y=100)

        self.wristL = Label(win, text='Wrist', width=11)
        self.wristL.place(x=100, y=150)

        self.wrist = IntVar()
        self.radio = Radiobutton(win, variable=self.wrist, value=0, text="Left", width=5)
        self.radio.place(x=200, y=150)
        self.radio2 = Radiobutton(win, variable=self.wrist, value=1, text="Right", width=5)
        self.radio2.place(x=270, y=150)

        self.checkB = Button(win, text='Check', command=self.submit, width=11)
        self.checkB.place(x=100, y=250)
        self.checkL = Label(win, text='', width=20)
        self.checkL.place(x=230, y=250)

        self.myreport = Button(win, text="PowerBI Dashboard", command=self.showReport)
        self.myreport.place(x=160, y=350)

    @staticmethod
    def alert(title, message, kind='error', hidemain=True):
        show_method = getattr(messagebox, 'show{}'.format(kind))
        show_method(title, message)

    def submit(self):

        try:

            ax = float(self.ax.get())
            ay = float(self.ay.get())
            az = float(self.az.get())

            gx = float(self.gx.get())
            gy = float(self.gy.get())
            gz = float(self.gz.get())

            wrist = self.wrist.get()

            astatus = ax <= 16 and ax >= -16 and ay <= 16 and ay >= -16 and az <= 16 and az >= -16
            gstatus = gx <= 2000 and gx >= -2000 and gy <= 2000 and gy >= -2000 and gz <= 2000 and gz >= -2000

            if (gstatus and astatus):

                print("Acceleration", ax, ay, az)
                print("Gyro", gx, gy, gz)
                if wrist == 0:
                    print("Left was selected")
                elif wrist == 1:
                    print("Right was selected")

                df = createDF(ax, ay, az, gx, gy, gz, wrist)
                print("df created")
                out = mergeFeatures(df)
                print("fea merged")
                predval = prediction(out)
                print(predval)
                if (predval == 0.0):
                    self.checkL.config(text="WALKING")
                elif (predval == 1.0):
                    self.checkL.config(text="RUNNING")

            elif ((not gstatus) and astatus):
                MyWindow.alert('Error', 'Enter valid  Gyroscope values for x, y and z \n(Range = -2000 to +2000)')

            elif (gstatus and (not astatus)):
                MyWindow.alert('Error', 'Enter valid  Acceleration values for x, y and z \n(Range = -16 to +16)')

            else:
                MyWindow.alert('Error',
                               'Enter valid Acceleration (Range = -16 to +16) & \nGyroscope (Range = -2000 to +2000) values for x, y and z')
        except ValueError:
            MyWindow.alert('Error', 'Enter valid numerical values')

    def showReport(self):

        webbrowser.open("https://app.powerbi.com/links/EPSy77Nad3?ctid=e85f2c00-2730-4ca5-b8d8-609b15bd4746&pbi_source=linkShare")
window = Tk()

img = PhotoImage(file="images/run.png")
label = Label(window, image=img)
label.place(x=0, y=0)

mywin = MyWindow(window)
window.title('Move On')
window.geometry("800x450+10+10")
window.mainloop()
