import tkinter as tk
from PIL import Image, ImageTk
import hashlib
import pandas as pd
from csv import writer
import traceback
import random


def logmain():
    global log
    log = tk.Toplevel(root)
    log.geometry("350x160")
    log.title('Login')

    global mail_entry
    global passw_entry
    global mail_var
    global passw_var
    global logt_entry
    global logt_var

    mail_var = tk.StringVar()
    passw_var = tk.StringVar()

    mail_label = tk.Label(log, text='Email Id', font=('calibre', 10, 'bold'))
    mail_entry = tk.Entry(log, textvariable=mail_var, font=('calibre', 10, 'normal'))

    passw_label = tk.Label(log, text='Password', font=('calibre', 10, 'bold'))
    passw_entry = tk.Entry(log, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')

    global var
    var = tk.StringVar()
    var.set(None)
    R1 = tk.Radiobutton(log, text="Customer", variable=var, value='customer')
    R2 = tk.Radiobutton(log, text="Driver", variable=var, value='driver')

    sub_btn = tk.Button(log, text='Submit', command=submitlogin)

    exit_btn = tk.Button(log, text='Exit', command=destroyall)

    mail_label.grid(row=0, column=1)
    mail_entry.grid(row=0, column=2)
    passw_label.grid(row=1, column=1)
    passw_entry.grid(row=1, column=2)
    R1.grid(row=2, column=1)
    R2.grid(row=2, column=2)
    sub_btn.grid(row=3, column=2)
    exit_btn.grid(row=5, column=2)
    log.mainloop()


def destroyall():
    exit(0)


def deletelog():
    global loggedin
    loggedin = True
    log.destroy()
    root.destroy()


def submitlogin():
    global mail
    mail = mail_entry.get()
    password = passw_entry.get()
    mail_entry.delete(0, tk.END)
    passw_entry.delete(0, tk.END)
    global logtype
    logtype = str(var.get())

    if len(mail) == 0 or len(password) == 0:
        inv = tk.Label(log, text='Invalid details !', fg='red')
        inv.grid(row=8, column=2)
        return
    pwd_hash = hashlib.sha256(password.encode()).hexdigest()
    global successful

    if logtype == 'driver':
        try:
            df = pd.read_csv('driver.csv')
            if mail not in df.name.tolist():
                raise FileNotFoundError

            if pwd_hash in df[df['name'] == mail].password.values:
                successful = tk.Toplevel(log)
                successful.title('Successful')
                successful.geometry('200x80')
                suc = tk.Label(successful, text='Login Successful', fg='green')
                suc.grid(row=1, column=3)
                okb = tk.Button(successful, text='ok', command=deletelog)
                okb.grid(row=2, column=3)
                return True
            else:
                suc = tk.Label(log, text='Login Unsuccessful', fg='red')
                suc.grid(row=8, column=2)
                return False

        except FileNotFoundError:
            suc = tk.Label(log, text='User not found !', fg='red')
            suc.grid(row=7, column=2)
            return False
    else:
        try:
            df = pd.read_csv('credentials.csv')
            if mail in df.email.tolist():
                if pwd_hash in df[df['email'] == mail].pwd.values:
                    mail_var.set("")
                    passw_var.set("")
                    successful = tk.Toplevel(log)
                    successful.title('Successful')
                    successful.geometry('200x80')
                    tk.Label(successful, text='Login Successful', fg='green').pack()
                    tk.Button(successful, text='ok', command=deletelog).pack()
                    return True
                else:
                    mail_var.set("")
                    passw_var.set("")
                    suc = tk.Label(log, text='Login Unsuccessful', fg='red')
                    suc.grid(row=8, column=2)
                    return False
            mail_var.set("")
            passw_var.set("")
            suc = tk.Label(log, text='User not found !', fg='red')
            suc.grid(row=7, column=2)
            return False

        except FileNotFoundError:
            mail_var.set("")
            passw_var.set("")
            suc = tk.Label(log, text='User not found !', fg='red')
            suc.grid(row=7, column=2)
            return False


def signup():
    global sg
    sg = tk.Toplevel(root)
    sg.geometry("400x200")
    sg.title('Register')

    global name_entry
    global passw_entry
    global name_var
    global passw_var
    global mail_entry
    global num_entry
    global mail_var
    global num_var
    global add_entry
    global add_var

    name_var = tk.StringVar()
    passw_var = tk.StringVar()
    num_var = tk.StringVar()
    mail_var = tk.StringVar()
    add_var = tk.StringVar()

    name_label = tk.Label(sg, text='Username', font=('calibre', 10, 'bold'))
    name_entry = tk.Entry(sg, textvariable=name_var, font=('calibre', 10, 'normal'))

    passw_label = tk.Label(sg, text='Password', font=('calibre', 10, 'bold'))
    passw_entry = tk.Entry(sg, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')

    mail_label = tk.Label(sg, text='Email Id', font=('calibre', 10, 'bold'))
    mail_entry = tk.Entry(sg, textvariable=mail_var, font=('calibre', 10, 'normal'))

    num_label = tk.Label(sg, text='Mobile Number', font=('calibre', 10, 'bold'))
    num_entry = tk.Entry(sg, textvariable=num_var, font=('calibre', 10, 'normal'))

    add_label = tk.Label(sg, text='Address', font=('calibre', 10, 'bold'))
    add_entry = tk.Entry(sg, textvariable=add_var, font=('calibre', 10, 'normal'))

    sub_btn = tk.Button(sg, text='Submit', command=submitsignup)

    exit_btn = tk.Button(sg, text='Exit', command=destroyall)

    name_label.grid(row=0, column=1)
    name_entry.grid(row=0, column=2)
    mail_label.grid(row=1, column=1)
    mail_entry.grid(row=1, column=2)
    passw_label.grid(row=2, column=1)
    passw_entry.grid(row=2, column=2)
    num_label.grid(row=3, column=1)
    num_entry.grid(row=3, column=2)
    add_label.grid(row=4, column=1)
    add_entry.grid(row=4, column=2)
    sub_btn.grid(row=5, column=2)
    exit_btn.grid(row=7, column=2)
    sg.mainloop()


def submitsignup():
    name = name_entry.get()
    password = passw_entry.get()
    address = add_entry.get()
    mailid = mail_entry.get()
    number = num_entry.get()
    if len(name) == 0 or len(password) == 0 or len(address) == 0 or len(mailid) == 0 or len(number) == 0:
        inv = tk.Label(sg, text='Invalid details !', fg='red')
        inv.grid(row=9, column=2)
        return
    name_entry.delete(0, tk.END)
    passw_entry.delete(0, tk.END)
    add_entry.delete(0, tk.END)
    mail_entry.delete(0, tk.END)
    num_entry.delete(0, tk.END)
    pwd_hash = hashlib.sha256(password.encode()).hexdigest()
    flag = 1
    global logtype
    while True:
        global successfulsg
        try:
            li = []
            df = pd.read_csv('credentials.csv')
            if not mailid in df.email.tolist():
                f = open('credentials.csv', 'a+', newline='')
                cwrite = writer(f)
                cwrite.writerow([name, mailid, pwd_hash, address, number])
                successfulsg = tk.Toplevel(sg)
                successfulsg.title('Successful')
                successfulsg.geometry('200x80')
                suc = tk.Label(successfulsg, text='Registration Successful', fg='green')
                suc.grid(row=1, column=3)
                okb = tk.Button(successfulsg, text='ok', command=deletesg)
                okb.grid(row=2, column=3)
                logtype = 'student'
                return True
            else:
                suc = tk.Label(sg, text='This mail_id is already registered !', fg='red')
                suc.grid(row=8, column=2)
                return False

        except FileNotFoundError:
            df = pd.DataFrame(columns=['name', 'email', 'pwd', 'add', 'mobile'])
            df.to_csv('credentials.csv', index=False)
            f = open('credentials.csv', 'a+', newline='')
            cwrite = writer(f)
            cwrite.writerow([name, mailid, pwd_hash, address, number])
            successfulsg = tk.Toplevel(sg)
            successfulsg.title('Successful')
            successfulsg.geometry('200x80')
            suc = tk.Label(successfulsg, text='Registration Successful', fg='green')
            suc.grid(row=1, column=3)
            okb = tk.Button(successfulsg, text='ok', command=deletesg)
            okb.grid(row=2, column=3)
            return True

        except:
            suc = tk.Label(sg, text='Registration Unsuccessfull', fg='red')
            suc.grid(row=5, column=2)
            return False


def deletesg():
    global loggedin
    loggedin = True
    sg.destroy()


def deletevi():
    vi.destroy()


def view():
    global vi
    vi = tk.Toplevel(st)
    vi.geometry("1400x400")
    vi.title('View Rides')
    df = pd.read_csv('rides.csv')
    df = df[df['cmail'] == mail]
    source = df.csource.tolist()
    destination = df.cdestination.tolist()
    time = df.ctime.tolist()
    date = df.cdate.tolist()
    driver = df.dname.tolist()
    plate = df.dplate.tolist()
    if len(source) == 0:
        non = tk.Label(vi, text='No rides booked yet !', font=(15), fg='red')
        non.grid(row=5, column=2)
        exit_btn = tk.Button(vi, text='Exit', command=destroyall)
        back_btn = tk.Button(vi, text='Back', command=deletevi)
        back_btn.grid(row=7, column=2)
        exit_btn.grid(row=8, column=2)
        return
    else:

        li = list(zip(date, time, source, destination, driver, plate))
        li.sort()
        li.insert(0, ('Date', 'Time', 'Source', 'Destination', 'Driver', 'License Plate'))

        class Table:

            def __init__(self, root):

                for i in range(total_rows):
                    for j in range(total_columns):
                        if i == 0:
                            col = 'black'
                            font = ('Helvetica', 16, 'bold')
                        else:
                            col = 'blue'
                            font = ('Helvetica', 13, 'bold')
                        self.e = tk.Entry(root, width=20, fg=col,
                                          font=font)

                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, li[i][j])

        total_rows = len(li)
        total_columns = len(li[0])

        t = Table(vi)
        exit_btn = tk.Button(vi, text='Exit', command=destroyall)
        back_btn = tk.Button(vi, text='Back', command=deletevi)
        back_btn.grid(row=11, column=2)
        exit_btn.grid(row=12, column=2)
        return


def book():
    global bk
    bk = tk.Toplevel(st)
    bk.geometry("600x400")
    bk.title('Book A Taxi')

    global pic_entry
    global dest_entry
    global time_entry
    global pic_var
    global dest_var
    global time_var
    global date_var
    global date_entry

    pic_var = tk.StringVar()
    dest_var = tk.StringVar()
    time_var = tk.StringVar()
    date_var = tk.StringVar()

    lab = tk.Label(bk, text='Enter the Details to Book a Taxi', font=('Calibre', 15, 'bold'))

    pic_label = tk.Label(bk, text='Pickup Address', font=('calibre', 10, 'bold'))
    pic_entry = tk.Entry(bk, textvariable=pic_var, font=('calibre', 10, 'normal'))

    dest_label = tk.Label(bk, text='Destination Address', font=('calibre', 10, 'bold'))
    dest_entry = tk.Entry(bk, textvariable=dest_var, font=('calibre', 10, 'normal'))

    time_label = tk.Label(bk, text='Pickup Time (HH:MM)', font=('calibre', 10, 'bold'))
    time_entry = tk.Entry(bk, textvariable=time_var, font=('calibre', 10, 'normal'))

    date_label = tk.Label(bk, text='Pickup Date(DD/MM/YYYY)', font=('calibre', 10, 'bold'))
    date_entry = tk.Entry(bk, textvariable=date_var, font=('calibre', 10, 'normal'))

    sub_btn = tk.Button(bk, text='Submit', command=sbbook)

    exit_btn = tk.Button(bk, text='Exit', command=destroyall)

    back_btn = tk.Button(bk, text='Back', command=deletebk)

    lab.grid(row=0, column=2)
    pic_label.grid(row=2, column=1)
    pic_entry.grid(row=2, column=2)
    dest_label.grid(row=3, column=1)
    dest_entry.grid(row=3, column=2)
    date_label.grid(row=4, column=1)
    date_entry.grid(row=4, column=2)
    time_label.grid(row=5, column=1)
    time_entry.grid(row=5, column=2)
    sub_btn.grid(row=6, column=2)
    back_btn.grid(row=9, column=2)
    exit_btn.grid(row=10, column=2)


def deletebk():
    bk.destroy()


def sbbook():
    csource = pic_entry.get()
    cdestination = dest_entry.get()
    ctime = time_entry.get()
    cdate = date_entry.get()
    df = pd.read_csv('credentials.csv')
    cname = df[df['email'] == mail].name.values[0]
    if len(csource) == 0 or len(cdestination) == 0 or len(ctime) == 0 or len(cdate) == 0 or len(ctime) == 0:
        inv = tk.Label(bk, text='Invalid details !', fg='red')
        inv.grid(row=8, column=2)
        return
    try:
        if int(ctime.split(':')[0]) > 23 or int(ctime.split(':')[1]) > 59 or len(cdate.split('/')) != 3:

            inv = tk.Label(bk, text='Invalid details !', fg='red')
            inv.grid(row=10, column=2)
            return
        else:
            d = ['Hardik', 'Het', 'Jeet', 'Nikhil']
            random.shuffle(d)
            random.shuffle(d)
            for i in d:
                df = pd.read_csv('rides.csv')
                df = df[(df['dname'] == i) & (df['cdate'] == cdate)].ctime.tolist()
                flag = 0
                for j in df:
                    if int(j.split(':')[0]) == int(ctime.split(':')[0]):
                        flag = 1
                        break
                if flag == 0:
                    df = pd.read_csv('driver.csv')
                    df = df[df['name'] == i].plate.values[0]
                    f = open('rides.csv', 'a+', newline='')
                    cwrite = writer(f)
                    cwrite.writerow([cname, mail, csource, cdestination, ctime, cdate, i, df])
                    successful = tk.Toplevel(bk)
                    successful.title('Successful')
                    successful.geometry('200x80')
                    suc = tk.Label(successful, text='Ride is Booked', fg='green')
                    suc.grid(row=1, column=3)
                    okb = tk.Button(successful, text='ok', command=deletebk)
                    okb.grid(row=2, column=3)
                    return
            unsuccessful = tk.Toplevel(bk)
            unsuccessful.title('Successful')
            unsuccessful.geometry('200x80')
            suc = tk.Label(unsuccessful, text='Driver not available. Try Later.', fg='red')
            suc.grid(row=1, column=3)
            okb = tk.Button(unsuccessful, text='ok', command=deletebk)
            okb.grid(row=2, column=3)
            return
    except:
        inv = tk.Label(bk, text='Invalid details !', fg='red')
        inv.grid(row=12, column=2)
        return


def deletecc():
    cc.destroy()


def cancel():
    global cc
    cc = tk.Toplevel(st)
    cc.geometry("1400x400")
    cc.title('Cancel Rides')
    df = pd.read_csv('rides.csv')
    global index
    index = df[df['cmail']==mail].index
    df = df[df['cmail'] == mail]
    source = df.csource.tolist()
    destination = df.cdestination.tolist()
    time = df.ctime.tolist()
    date = df.cdate.tolist()
    driver = df.dname.tolist()
    plate = df.dplate.tolist()
    if len(source) == 0:
        non = tk.Label(cc, text='No rides booked yet !', font=(15), fg='red')
        non.grid(row=5, column=2)
        exit_btn = tk.Button(cc, text='Exit', command=destroyall)
        back_btn = tk.Button(cc, text='Back', command=deletecc)
        back_btn.grid(row=7, column=2)
        exit_btn.grid(row=8, column=2)
        return
    else:

        li = list(zip([i for i in range(1, len(index)+1)], date, time, source, destination, driver, plate))
        li.insert(0, ('RideId', 'Date', 'Time', 'Source', 'Destination', 'Driver', 'License Plate'))

        class Table:

            def __init__(self, root):

                for i in range(total_rows):
                    for j in range(total_columns):
                        if i == 0:
                            col = 'black'
                            font = ('Helvetica', 16, 'bold')
                        else:
                            col = 'blue'
                            font = ('Helvetica', 13, 'bold')
                        self.e = tk.Entry(root, width=20, fg=col,
                                          font=font)

                        self.e.grid(row=i, column=j)
                        self.e.insert(tk.END, li[i][j])

        total_rows = len(li)
        total_columns = len(li[0])

        t = Table(cc)

        global id_entry
        global id_var
        id_var = tk.StringVar()

        cclabel = tk.Label(cc, text='Enter Ride-Id to cancel a ride', font=('calibre', 11, 'normal'))
        id_entry = tk.Entry(cc, textvariable=id_var, font=('calibre', 10, 'normal'))
        ccbutton = tk.Button(cc, text='Cancel Ride', font=('calibre', 10, 'normal'), command=ccride)
        exit_btn = tk.Button(cc, text='Exit', command=destroyall)
        back_btn = tk.Button(cc, text='Back', command=deletecc)

        cclabel.grid(row=12,column=1)
        id_entry.grid(row=12,column=2)
        ccbutton.grid(row=12, column=3)
        back_btn.grid(row=14, column=2)
        exit_btn.grid(row=15, column=2)
        return


def ccride():
    rideid = id_entry.get()
    df = pd.read_csv('rides.csv')
    try:
        if rideid in [str(i) for i in range(1, len(index)+1)]:
            df=df.drop(index[int(rideid)-1])
            df.to_csv('rides.csv', index=False)
            successful = tk.Toplevel(cc)
            successful.title('Successful')
            successful.geometry('200x80')
            suc = tk.Label(successful, text='Your Ride is cancelled.', fg='green')
            suc.grid(row=1, column=3)
            okb = tk.Button(successful, text='ok', command=deletecc)
            okb.grid(row=2, column=3)
            return
        else:
            inv = tk.Label(cc, text='Invalid !', fg='red')
            inv.grid(row=16, column=2)
            return
    except:
        inv = tk.Label(cc, text='Invalid !', fg='red')
        inv.grid(row=16, column=2)
        return

loggedin = False
while not loggedin:
    global root
    root = tk.Tk()
    root.title('Taxi Booking System')
    root.geometry('500x400')
    img = Image.open('taxi.png')
    img = img.resize((150, 80), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    w = tk.Label(root, image=photo)
    w.photo = photo
    w.pack()
    tk.Label(root, text="Welcome, please Login / Register to continue", font=("Helvetica", 16), pady=20).pack()
    frame = tk.Frame(root)
    frame.pack()

    button1 = tk.Button(frame, text="Login", fg="blue", padx=9, pady=4, font=("Helvetica", 10), command=logmain)
    button1.pack(side=tk.TOP)
    tk.Label(frame, text="").pack()
    button2 = tk.Button(frame, text="Register", fg='blue', pady=4, font=("Helvetica", 10), command=signup)
    button2.pack(side=tk.TOP)

    tk.Label(frame, text="\n\n").pack()
    exit_btn = tk.Button(frame, text='Exit', command=destroyall)
    exit_btn.pack(side=tk.BOTTOM)

    root.mainloop()

while loggedin:
    if logtype == 'driver':
        driver = tk.Tk()
        driver.title('Driver Page')
        driver.geometry('1400x500')
        lab = tk.Label(driver, text='Welcome driver {}\n'.format(mail), font=('Helvetica', 25))
        lab.grid(row=1, column=2)
        try:
            df = pd.read_csv('rides.csv')
            if len(df[df['dname'] == mail].cname.tolist()) > 0:
                df = df[df['dname'] == mail]
                source = df.csource.tolist()
                destination = df.cdestination.tolist()
                time = df.ctime.tolist()
                date = df.cdate.tolist()
                passenger = df.cname.tolist()
                li = list(zip(date, time, passenger, source, destination))
                li.sort()
                li.insert(0, ('Date', 'Time', 'Passenger', 'Source', 'Destination'))


                class Table:

                    def __init__(self, root):

                        for i in range(total_rows):
                            for j in range(total_columns):
                                if i == 0:
                                    col = 'black'
                                    font = ('Helvetica', 16, 'bold')
                                else:
                                    col = 'blue'
                                    font = ('Helvetica', 13, 'bold')
                                self.e = tk.Entry(root, width=20, fg=col,
                                                  font=font)

                                self.e.grid(row=i + 3, column=j)
                                self.e.insert(tk.END, li[i][j])


                total_rows = len(li)
                total_columns = len(li[0])

                t = Table(driver)
                exit_btn = tk.Button(driver, text='Exit', command=destroyall)
                exit_btn.grid(row=10, column=2)

            else:
                tk.Label(driver, text='Sorry, you have no assigned rides right now.', font=('Helvetica', 20),
                         fg='red').grid(row=3, column=2)
                exit_btn = tk.Button(driver, text='Exit', command=destroyall)
                exit_btn.grid(row=5, column=2)
        except:
            traceback.print_exc()
            tk.Label(driver, text='No rides available !', font=('Helvetica', 10)).grid(row=1, column=2)
            exit_btn = tk.Button(driver, text='Exit', command=destroyall)
            exit_btn.grid(row=5, column=2)

        driver.mainloop()

    elif logtype == 'customer':
        global st
        st = tk.Tk()
        st.title('Customer Page')
        st.geometry('500x400')
        df = pd.read_csv('credentials.csv')
        tk.Label(st, text='Welcome {}\n'.format(df[df['email'] == mail].name.values[0]), font=('Helvetica', 25)).pack()
        tk.Button(st, text='Book A Ride', font=('Helvetica', 10), command=book).pack()
        tk.Button(st, text='View Rides', font=('Helvetica', 10), command=view).pack()
        tk.Button(st, text='Cancel A Ride', font=('Helvetica', 10), command=cancel).pack()
        tk.Label(st, text='\n').pack()
        tk.Button(st, text='Exit', command=destroyall).pack()
        st.mainloop()

    else:
        exit(0)
