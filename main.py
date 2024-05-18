
#сделать цикл по комбобоксу
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
import sqlite3

global height_tf, weight_tf,geight_tf,peight_tf,\
    oeight_tf,ueight_tf,combo,x,d,ii_tf,pi_tf,ui_tf,xi_tf,x2,userid,combo,a52,result1,ww,uu,window1,\
    y,p,b,k,o,yy,h

#сделать запись кнопка добавить
#сделать так чтобы окна сохранялись при закрытии
def save_fail():
    with open("new-file5.txt", "a") as jj:
        ww = str(height_tf.get()) + ':' + str(weight_tf.get()) + ':' + str(geight_tf.get()) + ':' + str(
            peight_tf.get()) + ':' + str(oeight_tf.get()) + ':' + str(ueight_tf.get()) + ':' + str(
            combo.get()) + ':' + str(x.get()) + ':' + str(d.get()) + ':' + str(ii_tf.get()) + ':' + str(
            pi_tf.get()) + ':' + str(ui_tf.get()) + ':' + str(xi_tf.get()) + '\n'
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

        jj.write(ww)
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

    ee = Button(window, text="Выход")
    ee.grid(column=3, row=11)
    #window.protocol(save_fail)#обработка закрытия окна
    window.mainloop()

#окно редактор
def redactor():
    #сделать используемые переменные глобальными
    global combo
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
    userid = combo.get()[0]
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

    ee = Button(window, text="Выход")
    ee.grid(column=3, row=11)
    # window.protocol(save_fail)#обработка закрытия окна
    window.mainloop()

def search():
    global a52,result1,ww,uu,window1,b,o
    window1 = Tk()
    window1.title('База имён')
    window1.geometry('500x300')
    button = Button(window1, text="поиск",command=searchDB)
    button.grid(row=0, column=0)
    y=Label(window1,text='фамилия')
    y.grid(row=1,column=0)
    a52 = Entry(window1)
    a52.grid(row=1, column=1)

def searchDB():
    global uu,window1
    yy = str(b.get())
    h = str(o.get())
    uu = str(a52.get())
    con = sqlite3.connect("phoneboog.db")
    c1 = con.cursor()
    c1.execute("SELECT * FROM phonebook WHERE surname=?", (uu,))
    result = c1.fetchall()
    if result:
        if len(result) == 1:
            editor = Text(window1, height=30, width=50)
            editor.grid(row=4, column=1)
            editor.insert("1.0", result[0])
            #messagebox.showinfo("Результат", f"Найдена запись: {result[0]}")
        else:
            message = "Найдены записи:\n"
            for row in result:
                message += f"{row}\n"
            #messagebox.showinfo("Результат", message)
            editor = Text(window1, height=30, width=50)
            editor.grid(row=4, column=1)
            editor.insert("1.0", message)
    else:
        messagebox.showinfo("Результат", "Записей с такой фамилией не найдено")

    #datetime.date если дата и месяц раны переменным в которых записаны эти данные то вывести инсерт сегодня др у наме и сурнами и отчество вывести

aa = Tk()
aa.title('База имён')
aa.geometry('500x300')
x1=Button(aa,text="добавить",command=click)
x1.grid(row=0, column=0)
x2=Button(aa,text="редактировать",command=redactor)
x2.grid(row=0, column=1)
x3=Button(aa,text="поиск",command=search)
x3.grid(row=0, column=2)
con = sqlite3.connect("phoneboog.db")
cursor = con.cursor()
#получаем данные из базы данных
cursor.execute("SELECT id,surname,name, phone1 FROM phonebook")
rows = cursor.fetchall()
x=(rows)
combo = Combobox(aa,values=x)
combo.grid(column=0, row=1,pady=20,ipadx=50)
print()

aa.mainloop()
#задать каждой команду открывать прошлый код и если добавить то инпут


