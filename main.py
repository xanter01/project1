
#сделать цикл по комбобоксу
import os
from datetime import datetime
import webbrowser
#import datetime
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
import sqlite3

global height_tf, weight_tf,geight_tf,peight_tf,\
    oeight_tf,ueight_tf,combo,x,d,ii_tf,pi_tf,ui_tf,xi_tf,x2,userid,a52,result1,ww,uu,window1,\
    y,p,b,k,o,yy,h,ddq,current_month,a53,label,aa

#сделать запись кнопка добавить
#сделать так чтобы окна сохранялись при закрытии
def save_fail():
    f = str(height_tf.get())  # фамилия
    l = str(weight_tf.get())  # имя
    q = str(geight_tf.get())  # очество
    k = str(peight_tf.get())  # телефон 1
    t = str(oeight_tf.get())  # телефон 2
    u = str(ueight_tf.get())  # почта
    s = int(combo.get())  # дата
    v = int(x.get())  # месяц
    m = int(d.get())  # год
    y = str(ii_tf.get())  # город
    r = str(pi_tf.get())  # улица
    p = str(ui_tf.get())  # дом
    o = str(xi_tf.get())  # квартира

    #jj.write(ww)
    #window.destroy()  # Закрыть окно
    conn = sqlite3.connect('phoneboog.db')
    c = conn.cursor()  # вставить м или ж
    c.execute(
        '''CREATE TABLE IF NOT EXISTS phonebook (id integer primary key,
        surname text, 
        name text,
        patronymic text, 
        phone1 text,
        phone2 text DEFAULT ' ',
        Email text,
        date integer,
        month integer,
        year integer,
        city text,
        street text,
        home text,
        apartment text DEFAULT ' '
        )
        ''')
    conn.commit()

    c.execute(
        '''INSERT INTO phonebook (surname, name, patronymic, phone1, phone2, Email, date, month, year, city, street, home, apartment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ''',
        (f, l, q, k, t, u, s, v, m, y, r, p, o))
    conn.commit()

            # Создание базы данных
        #print(ww)

def click():
    global height_tf, weight_tf, geight_tf, peight_tf, \
        oeight_tf, ueight_tf, combo, x, d, ii_tf, pi_tf, ui_tf, xi_tf, x2
    window =Tk()
    window.title("Новое окно")
    window.geometry("1920x1080")
    window.wm_attributes("-topmost",1)
    # ФАМИЛИЯ
    height_lb = Label(window,
        # frame,
        text="фамилия  "
    )
    height_lb.grid(row=0, column=0)

    height_tf =Entry(window,
        # frame,
    )
    height_tf.grid(row=0, column=1, pady=3)

    ####ИМЯ
    weight_lb = Label(window,
        # frame,
        text=" имя "
    )
    weight_lb.grid(row=1, column=0)

    weight_tf = Entry(window
        # frame,
    )
    weight_tf.grid(row=1, column=1, pady=3)

    # ОТЧЕСТВО
    geight_lb = Label(window,
        # frame,
        text=" отчество ",
    )
    geight_lb.grid(row=2, column=0)

    geight_tf = Entry(window,
        # frame,
    )
    geight_tf.grid(row=2, column=1, pady=3)

    ###ТЕЛЕФОН
    peight_lb = Label(window,
        # frame,
        text=" телефон 1",
    )
    peight_lb.grid(row=3, column=0)

    peight_tf = Entry(window
        # frame,
    )
    peight_tf.grid(row=3, column=1, pady=3)
    ###ТЕЛЕФОН 2
    oeight_lb = Label(window,
        # frame,
        text=" телефон 2 ",
    )
    oeight_lb.grid(row=4, column=0)

    oeight_tf = Entry(window
        # frame,
    )
    oeight_tf.grid(row=4, column=1, pady=3)

    ####EMAIL
    ueight_lb = Label(window,
        # frame,
        text=" Email",
    )
    ueight_lb.grid(row=5, column=0)

    ueight_tf = Entry(window
        # frame,
    )
    ueight_tf.grid(row=5, column=1, pady=3)
    # 2 столб дата
    yeight_lb = Label(window,
        # frame,
        text=" Дата рождения", font=("Arial Bold", 19)
    )
    yeight_lb.grid(row=0, column=3)

    teight_lb = Label(window,
        # frame,
        text=" дата"
    )
    teight_lb.grid(row=1, column=2)

    combo = Combobox(window)
    combo['values'] = (
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31)
    combo.current()  # установите вариант по умолчанию
    combo.grid(column=2, row=2)

    zeight_lb = Label(window,
        # frame,
        text="месяц"
    )
    zeight_lb.grid(row=1, column=3)

    x = Combobox(window)
    x['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    x.current()  # установите вариант по умолчанию
    x.grid(column=3, row=2)

    beight_lb = Label(window,
        # frame,
        text="год"
    )

    beight_lb.grid(row=1, column=4)

    k = []
    for i in range(1950, 2025):
        k.append(i)
    d = Combobox(window)
    d['values'] = (k)
    # d.current(1)  # установите вариант по умолчанию
    d.grid(column=4, row=2)

    pight_lb = Label(window,
        # frame,
        text="пол:"
    )

    pight_lb.grid(row=3, column=3)

    chk_state = IntVar()
    chk_state.set(0)  # False
    # chk_state.set(True)  # задайте проверку состояния чекбокса
    chk = Checkbutton(window, text='мужской', var=chk_state)
    chk.grid(column=2, row=4)

    q = IntVar()
    q.set(0)  # False
    # q.set(True)  # задайте проверку состояния чекбокса
    q = Checkbutton(window, text='женский', var=q)
    q.grid(column=4, row=4)

    tt_lb = Label(window,
        # frame,
        text="Адрес", font=("Arial Bold", 19)
    )

    tt_lb.grid(row=5, column=3)

    ii_lb = Label(window,
        # frame,
        text="Город:"
    )

    ii_lb.grid(row=6, column=2)

    ii_tf = Entry(window
        # frame,
    )
    ii_tf.grid(row=6, column=3, pady=3)

    pi_lb = Label(window,
        # frame,
        text="Улица:"
    )

    pi_lb.grid(row=7, column=2)

    pi_tf = Entry(window
        # frame,
    )
    pi_tf.grid(row=7, column=3, pady=3)

    ui_lb = Label(window,
        # frame,
        text="Дом:"
    )

    ui_lb.grid(row=8, column=2)

    ui_tf = Entry(window
        # frame,
    )
    ui_tf.grid(row=8, column=3, pady=3)

    xi_lb = Label(window,
        # frame,
        text="Квартира:"
    )

    xi_lb.grid(row=9, column=2)

    xi_tf = Entry(window
        # frame,
    )
    xi_tf.grid(row=9, column=3, pady=3)

    xi_lb = Label(window,
        text=" "
    )

    xi_lb.grid(row=10, column=2)

    btn = Button(window, text="Сохранить",command=save_fail)
    btn.grid(column=2, row=11)

    def on_closing():
        window.destroy()  # Закрыть окно

    ee = Button(window, text="Выход",command=on_closing)
    ee.grid(column=3, row=11)
    #window.protocol(save_fail)#обработка закрытия окна
    window.mainloop()

#окно редактор
def redactor():
    #сделать используемые переменные глобальными
    global ddq
    window = Tk()
    window.title("Новое окно")
    window.geometry("1920x1080")
    window.wm_attributes("-topmost", 1)
    # ФАМИЛИЯ
    height_lb = Label(window,
                      # frame,
                      text="фамилия  "
                      )
    height_lb.grid(row=0, column=0)

    height_lb_tf = Text(window, height=2, width=26)
    height_lb_tf.grid(row=0, column=1)
    con = sqlite3.connect("phoneboog.db")
    #получаем данные из базы данных
    userid = ddq.get()[0]
    id = userid
    c = con.cursor()
    c.execute("SELECT surname FROM phonebook WHERE id = ?", (id,))
    result = c.fetchone()
    qqq=result[0]
    #cursor.execute("SELECT * FROM phonebook")
    #rows = cursor.fetchall()[1][1]
    height_lb_tf.insert("1.0", qqq)

    ####ИМЯ
    weight_lb = Label(window,
                      # frame,
                      text=" имя "
                      )
    weight_lb.grid(row=1, column=0)

    weight_tf = Text(window, height=2, width=26)
    weight_tf.grid(row=1, column=1)
    c.execute("SELECT name FROM phonebook WHERE id = ?", (id,))
    result = c.fetchone()
    ppp = result[0]
    #cursor.execute("SELECT * FROM phonebook")
    #gg = cursor.fetchmany(2)[1][2]
    weight_tf.insert("1.0", ppp)

    # ОТЧЕСТВО
    geight_lb = Label(window,
                      # frame,
                      text=" отчество ",
                      )
    geight_lb.grid(row=2, column=0)

    geight_tf = Text(window, height=2, width=26)
    geight_tf.grid(row=2, column=1)
    c.execute("SELECT patronymic FROM phonebook WHERE id = ?", (id,))
    result = c.fetchone()
    ff = result[0]
    #cursor.execute("SELECT * FROM phonebook")
    #ff = cursor.fetchall()[1][3]
    geight_tf.insert("1.0", ff)

    ###ТЕЛЕФОН
    peight_lb = Label(window,
                      # frame,
                      text=" телефон 1",
                      )
    peight_lb.grid(row=3, column=0)

    peight_tf = Text(window, height=2, width=26)
    peight_tf.grid(row=3, column=1)
    c.execute("SELECT phone1 FROM phonebook WHERE id = ?", (id,))
    result = c.fetchone()
    qq = result[0]
    #cursor.execute("SELECT * FROM phonebook")
    #qq = cursor.fetchall()[1][4]
    peight_tf.insert("1.0", qq)
    ###ТЕЛЕФОН 2
    oeight_lb = Label(window,
                      # frame,
                      text=" телефон 2 ",
                      )
    oeight_lb.grid(row=4, column=0)

    oeight_tf = Text(window, height=2, width=26)
    oeight_tf.grid(row=4, column=1)
    c.execute("SELECT phone2 FROM phonebook WHERE id = ?", (id,))
    result = c.fetchone()
    pp = result[0]
    #cursor.execute("SELECT * FROM phonebook")
    #pp = cursor.fetchall()[1][5]
    oeight_tf.insert("1.0", pp)

    ####EMAIL
    ueight_lb = Label(window,
                      # frame,
                      text=" Email",
                      )
    ueight_lb.grid(row=5, column=0)

    ueight_tf = Text(window, height=2, width=26)
    ueight_tf.grid(row=5, column=1)
    c.execute("SELECT Email FROM phonebook WHERE id = ?", (id,))
    result = c.fetchone()
    ss = result[0]
    #cursor.execute("SELECT * FROM phonebook")
    #ss = cursor.fetchall()[1][6]
    ueight_tf.insert("1.0", ss)

    # 2 столб дата
    yeight_lb = Label(window,
                      # frame,
                      text=" Дата рождения", font=("Arial Bold", 19)
                      )
    yeight_lb.grid(row=0, column=3)

    teight_lb = Label(window,
                      # frame,
                      text=" дата"
                      )
    teight_lb.grid(row=1, column=2)
    c.execute("SELECT date FROM phonebook WHERE id = ?", (id,))
    result = c.fetchone()
    xx = result[0]
    #cursor.execute("SELECT * FROM phonebook")
    #xx = cursor.fetchall()[1][7]
    combo=Combobox(window)
    combo['values'] = (
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31)
    combo.current(xx-1)  # установите вариант по умолчанию
    combo.grid(column=2, row=2)

    zeight_lb = Label(window,
                      # frame,
                      text="месяц"
                      )
    zeight_lb.grid(row=1, column=3)
    c.execute("SELECT month FROM phonebook WHERE id = ?", (id,))
    result = c.fetchone()
    ll = result[0]
    #cursor.execute("SELECT * FROM phonebook")
    #ll = cursor.fetchall()[1][8]
    x = Combobox(window)
    x['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    x.current(ll-1)  # установите вариант по умолчанию
    x.grid(column=3, row=2)

    beight_lb = Label(window,
                      # frame,
                      text="год"
                      )

    beight_lb.grid(row=1, column=4)

    k = []
    for i in range(1950, 2025):
        k.append(i)
    c.execute("SELECT year FROM phonebook WHERE id = ?", (id,))
    result = c.fetchone()
    mm = result[0]
    mm=int(mm)
    #cursor.execute("SELECT * FROM phonebook")
    #mm = cursor.fetchall()[1][9]
    d = Combobox(window)
    d['values'] = (k)
    d.current(mm-1950)  # установите вариант по умолчанию
    d.grid(column=4, row=2)

    pight_lb = Label(window,
                     # frame,
                     text="пол:"
                     )

    pight_lb.grid(row=3, column=3)

    chk_state = IntVar()
    chk_state.set(0)  # False
    # chk_state.set(True)  # задайте проверку состояния чекбокса
    chk = Checkbutton(window, text='мужской', var=chk_state)
    chk.grid(column=2, row=4)

    q = IntVar()
    q.set(0)  # False
    # q.set(True)  # задайте проверку состояния чекбокса
    q = Checkbutton(window, text='женский', var=q)
    q.grid(column=4, row=4)

    tt_lb = Label(window,
                  # frame,
                  text="Адрес", font=("Arial Bold", 19)
                  )

    tt_lb.grid(row=5, column=3)

    ii_lb = Label(window,
                  # frame,
                  text="Город:"
                  )

    ii_lb.grid(row=6, column=2)

    ii_tf = Text(window, height=2, width=26)
    ii_tf.grid(row=6, column=3)
    c.execute("SELECT city FROM phonebook WHERE id = ?", (id,))
    result = c.fetchone()
    dd = result[0]
    #cursor.execute("SELECT * FROM phonebook")
    #dd = cursor.fetchall()[1][10]
    ii_tf.insert("1.0", dd)

    pi_lb = Label(window,
                  # frame,
                  text="Улица:"
                  )

    pi_lb.grid(row=7, column=2)

    pi_tf = Text(window, height=2, width=26)
    pi_tf.grid(row=7, column=3)
    c.execute("SELECT street FROM phonebook WHERE id = ?", (id,))
    result = c.fetchone()
    e = result[0]
    #cursor.execute("SELECT * FROM phonebook")
    #e = cursor.fetchall()[1][11]
    pi_tf.insert("1.0", e)

    ui_lb = Label(window,
                  # frame,
                  text="Дом:"
                  )

    ui_lb.grid(row=8, column=2)

    ui_tf = Text(window, height=2, width=26)
    ui_tf.grid(row=8, column=3)
    c.execute("SELECT home FROM phonebook WHERE id = ?", (id,))
    result = c.fetchone()
    oo = result[0]
    #cursor.execute("SELECT * FROM phonebook")
    #oo = cursor.fetchall()[1][12]
    ui_tf.insert("1.0", oo)

    xi_lb = Label(window,
                  # frame,
                  text="Квартира:"
                  )

    xi_lb.grid(row=9, column=2)

    xi_tf = Text(window, height=2, width=26)
    xi_tf.grid(row=9, column=3)
    c.execute("SELECT apartment FROM phonebook WHERE id = ?", (id,))
    result = c.fetchone()
    rr = result[0]
    #cursor.execute("SELECT * FROM phonebook")
    #rr = cursor.fetchall()[1][13]
    xi_tf.insert("1.0", rr)

    xi_lb = Label(window,
                  text=" "
                  )

    xi_lb.grid(row=10, column=2)

    btn = Button(window, text="Сохранить", command=save_fail)
    btn.grid(column=2, row=11)

    def on_closing():
        window.destroy()

    ee = Button(window, text="Выход",command=on_closing)
    ee.grid(column=3, row=11)
    # window.protocol(save_fail)#обработка закрытия окна
    window.mainloop()

def search():
    global a52,result1,ww,uu,window1,b,o,a53
    window1 = Tk()
    window1.title('База имён')
    window1.geometry('500x300')
    button = Button(window1, text="поиск",command=searchDB)
    button.grid(row=0, column=0)
    def vuxod():
        window1.destroy()
    button1 = Button(window1, text="выход", command=vuxod)
    button1.grid(row=0, column=1)
    y=Label(window1,text='фамилия')
    y.grid(row=1,column=0)
    a52 = Entry(window1)
    a52.grid(row=1, column=1)
    y1 = Label(window1, text='имя')
    y1.grid(row=2, column=0)
    a53 = Entry(window1)
    a53.grid(row=2, column=1)



def searchDB():
    global uu, window1
    surname = str(a52.get())
    name = str(a53.get())  # Предположим, что a53 - это поле для ввода имени
    con = sqlite3.connect("phoneboog.db")
    c1 = con.cursor()

    if surname and name:  # Если введены и фамилия, и имя
        c1.execute("SELECT * FROM phonebook WHERE surname=? AND name=?", (surname, name))
    elif surname:  # Если введена только фамилия
        c1.execute("SELECT * FROM phonebook WHERE surname=?", (surname,))
    elif name:  # Если введено только имя
        c1.execute("SELECT * FROM phonebook WHERE name=?", (name,))
    else:  # Если ничего не введено
        messagebox.showinfo("Предупреждение", "Введите фамилию и/или имя для поиска")
        return

    result = c1.fetchall()
    if result:
        if len(result) == 1:
            editor = Text(window1, height=30, width=50)
            editor.grid(row=4, column=1)
            editor.insert("1.0", result[0])
        else:
            message = "Найдены записи:\n"
            for row in result:
                message += f"{row}\n"
            editor = Text(window1, height=30, width=50)
            editor.grid(row=4, column=1)
            editor.insert("1.0", message)
    else:
        messagebox.showinfo("Результат", "Записей с такой фамилией и/или именем не найдено")


def DR():
    global current_month
    con = sqlite3.connect("phoneboog.db")
    c1 = con.cursor()
    c1.execute("SELECT name,surname,patronymic,date,month,year FROM phonebook WHERE month=?", (current_month,))
    result = c1.fetchall()
    if result:
        if len(result) == 1:
            messagebox.showinfo("Результат", f"Найдена запись: {result[0]}")
        else:
            message = "Найдены записи:\n"
            for row in result:
                message += f"{row}\n"
            messagebox.showinfo("Результат", message)
    else:
        messagebox.showinfo("Результат", "в этом месяце др не найдено")

def update_time():
    global label,aa
    label.config(text=f"{datetime.now():%D   %H:%M:%S}")
    aa.after(100, update_time)  # Запланировать выполнение этой же функции через 100 миллисекунд

def rt():
    global ddq,current_month,aa,label
    aa = Tk()
    #aa["bg"] = "#DCDCDC"
    aa.title('информационное окно')
    aa.geometry('600x400')
    label =Label(aa, font=("helvetica", 15),foreground='#9ACD32')
    label.grid(row=0,column=0)

    update_time()

    x1=Button(aa,text="добавить",command=click)
    x1.grid(row=1, column=0)
    x2=Button(aa,text="редактировать",command=redactor)
    x2.grid(row=0, column=1)

    def hhh():
        import csv

        # Подключение к базе данных
        conn = sqlite3.connect('phoneboog.db')
        cursor = conn.cursor()

        # Выполнение запроса к базе данных
        cursor.execute("SELECT * FROM phonebook")

        # Получение результатов запроса и названий столбцов
        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Запись результатов в CSV файл с названиями столбцов
        with open('human.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(column_names)  # записываем названия столбцов
            writer.writerows(rows)  # записываем данные

        # Закрытие соединения с базой данных
        conn.close()

    pechat=Button(aa,text="записать в файл",command=hhh)
    pechat.grid(row=0, column=2)
    x3=Button(aa,text="поиск",command=search)
    x3.grid(row=1, column=1)

    def yuy():
        if os.name=='nt':
            import win32com.client

            # Создание экземпляра приложения Excel
            excel = win32com.client.Dispatch("Excel.Application")

            # Открытие файла
            workbook = excel.Workbooks.Open(r'путь_к_вашему_файлу.xlsx')

            # Печать файла
            workbook.PrintOut()

            # Закрытие файла и приложения Excel
            workbook.Close(SaveChanges=False)
            excel.Quit()

        import subprocess

        def print_csv_on_mac(file_path):
            applescript = f'''
            tell application "Finder"
                set theFile to POSIX file "{file_path}" as alias
                print theFile
            end tell
            '''

            process = subprocess.Popen(['osascript', '-e', applescript], stdout=subprocess.PIPE)
            output, _ = process.communicate()
            if output:
                print(output.decode('utf-8'))

        # Укажите путь к вашему CSV файлу
        csv_file_path = "/Users/artemabasov/PycharmProjects/всплывыющее окно/human.csv"

        print_csv_on_mac(csv_file_path)

    ll = Button(aa, text="печать", command=yuy)
    ll.grid(row=1, column=2)
    x4=Button(aa,text="день рождения",command=DR)
    x4.grid(row=2,column=1)


    def web():
        webbrowser.open_new('https://www.youtube.com/?app=desktop&hl=ru')

    x5=Button(aa,text="ютуб",command=web,foreground='red')
    x5.grid(row=2,column=2)

    con = sqlite3.connect("phoneboog.db")
    cursor = con.cursor()
    #получаем данные из базы данных
    cursor.execute("SELECT id,surname,name, phone1 FROM phonebook")
    rows = cursor.fetchall()
    x=rows

    ddq= Combobox(aa,values=x)
    ddq.grid(column=0, row=2,pady=20,ipadx=50)

    current_datetime = datetime.now()
    current_month = current_datetime.month

    aa.mainloop()



global entry_login4 , entry_password3,registrator

def login():
    global entry_login4 , entry_password3,registrator
    qq = str(entry_login4.get())
    gg = str(entry_password3.get())
    if qq=='' or gg=='':
        messagebox.showinfo("Результат", "вы ничего не ввели")
    elif gg!='' and gg!='':
        rek = sqlite3.connect('phoneboog.db')

        hh = rek.cursor()
        hh.execute('''CREATE TABLE IF NOT EXISTS users
                        (id INTEGER PRIMARY KEY, login TEXT, password TEXT)''')
        rek.commit()
        hh.execute(
            '''INSERT INTO users (login,password) VALUES (?, ?) ''',
            (qq,gg))
        rek.commit()
        rt()

def registr():
    global entry_login4, entry_password3
    def showpass():
        if entry_password3['show'] == '*':
            entry_password3['show'] = ''
        else:
            entry_password3['show'] = '*'

    vxod.destroy()
    global registrator
    registrator = Tk()
    registrator.title('регистрация')
    registrator.geometry('270x260')

    login2 = Label(registrator, text='Login:', foreground='#8370D8')
    login2.grid(row=0, column=1)

    entry_login2 = Entry(registrator)
    entry_login2.grid(row=1, column=1)

    login3 = Label(registrator, text='повторить Login:', foreground='#8370D8')
    login3.grid(row=2, column=1)

    entry_login4 = Entry(registrator)
    entry_login4.grid(row=3, column=1)

    password2 = Label(registrator, text='Password:', foreground='#8370D8')
    password2.grid(row=4, column=1)

    entry_password2 = Entry(registrator, show='*')
    entry_password2.grid(row=5, column=1)

    password3 = Label(registrator, text='повторить Password:', foreground='#8370D8')
    password3.grid(row=6, column=1)

    entry_password3 = Entry(registrator, show='*')
    entry_password3.grid(row=7, column=1)

    show2 = Button(registrator, text='show', foreground='#8370D8', command=showpass)
    show2.grid(row=7, column=2)

    signin2 = Button(registrator, text='Sign in', foreground='#8370D8', command=login)
    signin2.grid(row=9, column=1)



def showpass():
    if entry_password1['show'] == '*':
        entry_password1['show'] = ''
    else:
        entry_password1['show'] = '*'
def vvod():
    global entry_login1,entry_password1
    s = str(entry_login1.get())
    q=str(entry_password1.get())
    con = sqlite3.connect("phoneboog.db")
    c1 = con.cursor()
    c1.execute("SELECT * FROM users WHERE login=?", (s,))
    result = c1.fetchall()
    if s=='' or q=='':
        messagebox.showinfo("Результат", "вы ничего не ввели")
    elif len(result)==0:
        messagebox.showinfo("Результат", "неверные данные для входа")
    else:
        f=result[0][2]
        if q==f:
            rt()
        elif q!=f:
            messagebox.showinfo("Результат", "неверные данные для входа")



vxod = Tk()
vxod.title('Авторазиция')
vxod.geometry('260x160')

login1=Label(vxod, text='Login:', foreground='#8370D8')
login1.grid(row=0,column=1)

entry_login1 = Entry(vxod)
entry_login1.grid(row=1,column=1)


password1=Label(vxod, text='Password:', foreground='#8370D8')
password1.grid(row=2,column=1)

entry_password1 = Entry(vxod, show='*')
entry_password1.grid(row=3,column=1)


show1=Button(vxod, text='show',foreground='#8370D8', command=showpass)
show1.grid(row=3,column=2)

signin1=Button(vxod, text='Sign in',foreground='#8370D8' , command=vvod)#rt)
signin1.grid(row=4,column=1)

req1=Button(vxod, text='зарегестрироваться',foreground='#8370D8' , command=registr)
req1.grid(row=5,column=1)

vxod.mainloop()



#update в редактироать


