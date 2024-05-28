#/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import time
from tkinter import IntVar
import xlrd
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import os

# In[2]:
# 创建数据库和表
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')

# 向数据库中插入一些用户
users = [
    ('admin', 'password'),
    ('1', '1'),
    ('user2', 'password2')
]

for user in users:
    c.execute("INSERT INTO users VALUES (?, ?)", user)

conn.commit()
conn.close()

# 用户认证
def authenticate(username, password):
    # 查询数据库以验证用户名和密码
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None
# 在登录函数中添加忘记密码和注册的按钮
def login():
    username = name_tap.get()
    password = code_tap.get()

    if authenticate(username, password):
        root = get_in()
    else:
        result = messagebox.askokcancel('登录失败，用户名或密码错误', '是否重新设置密码，否的话将会为您注册新用户')
        if result:
            # 用户选择了忘记密码
            reset_password()
        else:
            # 用户选择了注册新用户
            register_new_user()

# 忘记密码函数
# 忘记密码函数
# 忘记密码函数
def reset_password():
    # 创建一个新的窗口，用于重设密码

    reset_password_window = tk.Toplevel(root)
    reset_password_window.title("重设密码")
    reset_password_window.geometry("300x200")

    # 在重设密码的窗口中添加一个标签和输入框，用于输入新的用户名
    username_label = tk.Label(reset_password_window, text="请输入用户名：")
    username_label.pack()
    username_entry = tk.Entry(reset_password_window)
    username_entry.pack()

    # 在重设密码的窗口中添加一个标签和输入框，用于输入新的密码
    new_password_label = tk.Label(reset_password_window, text="请输入新的密码：")
    new_password_label.pack()
    new_password_entry = tk.Entry(reset_password_window, show="*")
    new_password_entry.pack()

    # 在重设密码的窗口中添加一个确认按钮，用于确认重设密码
    confirm_button = tk.Button(reset_password_window, text="确认重设", command=lambda: reset_password_confirm(username_entry.get(), new_password_entry.get(), reset_password_window))
    confirm_button.pack()

def reset_password_confirm(username, new_password, reset_password_window):
    # 连接到数据库文件 'users.db'
    conn = sqlite3.connect('users.db')

    # 创建一个游标对象，用于执行SQL命令
    c = conn.cursor()

    # 执行SQL查询命令，查询用户名是否存在
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    result = c.fetchone()
    if result is None:
        # 用户名不存在，显示错误消息
        messagebox.showerror("重设密码失败", "用户名不存在")
        reset_password_window.destroy()
    else:
        # 执行SQL更新命令，更新用户的密码
        # 使用参数化更新来避免SQL注入攻击
        c.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))

        # 提交更改
        conn.commit()

        # 关闭数据库连接
        conn.close()

        # 重设密码成功后，关闭重设密码的窗口，并提示用户
        messagebox.showinfo("重设密码成功", "您的密码已重设为：{}".format(new_password))
        reset_password_window.destroy()

def register_new_user():
    # 创建一个新的窗口，用于注册新用户
    register_window = tk.Toplevel(root)
    register_window.title("注册新用户")
    register_window.geometry("300x200")

    # 在注册窗口中添加一个标签和输入框，用于输入新的用户名和密码
    new_username_label = tk.Label(register_window, text="请输入新的用户名：")
    new_username_label.pack()
    new_username_entry = tk.Entry(register_window)
    new_username_entry.pack()

    new_password_label = tk.Label(register_window, text="请输入新的密码：")
    new_password_label.pack()
    new_password_entry = tk.Entry(register_window, show="*")
    new_password_entry.pack()

    # 在注册窗口中添加一个确认按钮，用于确认注册新用户
    confirm_button = tk.Button(register_window, text="确认注册", command=lambda: register_confirm(new_username_entry.get(), new_password_entry.get()))
    confirm_button.pack()

def register_confirm(new_username, new_password, register_window=None):
    # 在这里可以调用数据库函数，将新的用户名和密码保存到数据库中
    # 例如：
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (new_username, new_password))
    conn.commit()
    conn.close()

    # 注册成功后，关闭注册窗口，并提示用户
    messagebox.showinfo("注册成功", "您已成功注册为新用户：{}".format(new_username))
    register_window.destroy()

##登录界面
from PIL import Image, ImageTk
import tkinter as tk
root = tk.Tk()
root.title('欢迎进入北邮抬头率检测系统！')
root.geometry('600x420')
#增加背景图片
img = Image.open(r"C:\TaiTouLv_Jiance\TaiTouLv_Jiance\bupt.jpg")
img2 = img.resize((600, 420), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(img2)
# 创建标签并使用调整后的图片
theLabel = tk.Label(root,
                 text="",#内容
                 justify=tk.LEFT,#对齐方式
                 image=photo,#加入图片
                compound = tk.CENTER,#关键:设置为背景图片
                font=("华文行楷",20),#字体和字号
                fg = "white")#前景色
theLabel.place(x=0,y=0)


# In[3]:


##主窗口
def get_in():
    # GUI代码
    root.destroy()
    window = tk.Tk()  # 这是一个窗口object
    window.title('抬头率监测系统')
    window.geometry('600x400')  # 窗口大小

    def read_data():
        path = r'C:\TaiTouLv_Jiance\TaiTouLv_Jiance\py_excel.xls'

        # 打开文件
        data = xlrd.open_workbook(path)
        # path + '/' +file 是文件的完整路径
        # 获取表格数目
        # nums = len(data.sheets())
        # for i in range(nums):
        #     # 根据sheet顺序打开sheet
        #     sheet1 = data.sheets()[i]

        # 根据sheet名称获取
        sheet1 = data.sheet_by_name('Sheet1')
        sheet2 = data.sheet_by_name('Sheet2')
        # 获取sheet（工作表）行（row）、列（col）数
        nrows = sheet1.nrows  # 行
        ncols = sheet1.ncols  # 列
        # print(nrows, ncols)

        # 获取教室名称列表
        global room_name, time_name
        room_name = sheet2.col_values(0)
        time_name = sheet2.col_values(1)
        print(room_name)
        print(time_name)
        # 获取单元格数据
        # 1.cell（单元格）获取
        # cell_A1 = sheet2.cell(0, 0).value
        # print(cell_A1)
        # 2.使用行列索引
        # cell_A2 = sheet2.row(0)[1].value

    read_data()

    def gettime():  # 当前时间显示
        timestr = time.strftime('%Y.%m.%d %H:%M', time.localtime(time.time()))
        lb.configure(text=timestr)
        window.after(1000, gettime)

    lb = tk.Label(window, text='', font=("黑体", 20))
    lb.grid(column=0, row=0)
    gettime()

    # 选择教室标签加下拉菜单
    choose_classroom = tk.Label(window, text="选择教室", width=15, height=2, font=("黑体", 12)).grid(column=0, row=1,
                                                                                               sticky='w')
    class_room = tk.StringVar()
    class_room_chosen = ttk.Combobox(window, width=20, height=10, textvariable=class_room, state='readonly')
    class_room_chosen['values'] = room_name
    class_room_chosen.grid(column=0, row=1, sticky='e')

    # 选择课时标签加下拉菜单
    choose_time = tk.Label(window, text="选择课时", width=15, height=2, font=("黑体", 12)).grid(column=0, row=2, sticky='w')
    course_time = tk.StringVar()
    course_time_chosen = ttk.Combobox(window, width=20, height=10, textvariable=course_time, state='readonly')
    course_time_chosen['values'] = time_name
    course_time_chosen.grid(column=0, row=2, sticky='e')

    pic_tip = tk.Label(window, text="所选教室时实图像", width=16, height=2, font=("黑体", 12)).grid(column=1, row=2, sticky='s')

    img = r'C:\TaiTouLv_Jiance\TaiTouLv_Jiance\bupt.jpg'##初始化图片界面
    img_open = Image.open(img)
    # 显示图片的代码
    (x, y) = img_open.size  # read image size
    x_s = 200  # define standard width
    y_s = y * x_s // x  # calc height based on standard width
    img_adj = img_open.resize((x_s, y_s), Image.Resampling.LANCZOS)
    img_png = ImageTk.PhotoImage(img_adj)

    Image2 = tk.Label(window, bg='white', bd=20, height=y_s * 0.83, width=x_s * 0.83,
                      image=img_png)  ##0.83用来消除白框
    Image2.grid(column=1, row=4, sticky='w')

    flag = IntVar()
    flag.set(0)

    '''
        if(flag.get()!=0):
        pic_path = str(flag.get())+'.jpg'

        img_open = Image.open(img)
        # 显示图片的代码
        (x, y) = img_open.size  # read image size
        x_s = 200  # define standard width
        y_s = y * x_s // x  # calc height based on standard width
        img_adj = img_open.resize((x_s, y_s), Image.ANTIALIAS)
        img_png = ImageTk.PhotoImage(img_adj)
        Image2 = tk.Label(window, bg='black', bd=20, height=y_s * 0.83, width=x_s * 0.83, imagevariable=img_png)  ##0.83用来消除白框
        Image2.grid(column=1, row=4, sticky='w')
    '''

    def rate_cal():
        face = 0

        def inspect():  ##将人脸检测函数内嵌
            nonlocal face
            str1 = "教室"
            str2 = "课上的抬头率为："
            path = r'C:\TaiTouLv_Jiance\TaiTouLv_Jiance\faces'
            pic_path = str(class_room_chosen.get()) + str(course_time_chosen.get()) + '.jpg'
            p = path + '/' + pic_path
            img = cv2.imread(p)
            print(p)
            # img = cv2.imread('image_path')
            color = (0, 255, 0)
            print(img)
            grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            classfier = cv2.CascadeClassifier(r"C:\TaiTouLv_Jiance\TaiTouLv_Jiance\haarcascade_frontalface_alt2.xml")
            faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
            a = len(faceRects)
            face = a
            str3 = str(a)
        inspect()
        path = r'C:\TaiTouLv_Jiance\TaiTouLv_Jiance\py_excel.xls'
        data = xlrd.open_workbook(path)
        sheet1 = data.sheet_by_name('Sheet1')
        nrows = sheet1.nrows  # 行
        ncols = sheet1.ncols  # 列
        total = 0
        for i in range(nrows):
            if (sheet1.cell(i, 0).value == class_room_chosen.get() and sheet1.cell(i,
                                                                                   1).value == course_time_chosen.get()):
                total = sheet1.cell(i, 2).value
        print(total)
        global rate
        print(face)
        rate = face /total
        print(rate)
        str1 = "教室"
        str2 = "课上的抬头率为："
        str3 = str(rate)
        var.set(f"{class_room_chosen.get()} {str1} {course_time.get()} 应到人数: {total}, 实到人数: {face}, {str2} {str3}")

    '''新加的'''
    def rate_cal2():

        if rate < 0.4:
            suggestion = "抬头率低，需要督促"
        elif rate > 0.9:
            suggestion = "抬头率较高，值得表扬"
        else:
            suggestion = "抬头率处于正常范围，学习状态良好"
        var.set(f"抬头率：{rate:.2f}，{suggestion}")
    '''新加的'''


    def pic_re():
        if (flag.get() == 0):
            pic_path = str(class_room_chosen.get()) + str(course_time_chosen.get()) + '.jpg'
            img = os.path.join(r'C:\TaiTouLv_Jiance\TaiTouLv_Jiance\faces', pic_path) #图片的命名需按规则来命名，具体规则可参考示例图片名称
            img_open = Image.open(img)
            # 显示图片的代码
            (x, y) = img_open.size  # read image size
            global x_s
            global y_s
            x_s = 200  # define standard width
            y_s = y * x_s // x  # calc height based on standard width
            img_adj = img_open.resize((x_s, y_s), Image.Resampling.LANCZOS)
            global img_png  ##这里一定要设置为全局变量，不然图片无法正常显示！！！！！！！！！！！
            img_png = ImageTk.PhotoImage(img_adj)
            Image2.configure(image=img_png)
        window.update_idletasks()

    var = tk.StringVar()  # tkinter中的字符串
    display = tk.Label(window, textvariable=var, font=('Arial', 12), width=38, height=10)
    display.grid(column=0, row=4, sticky='n')

    # 在GUI中添加按钮以调用rate_cal函数
    rate_button = ttk.Button(window, text="Get_rate", command=rate_cal)
    rate_button.grid(column=0, row=4, sticky='s')
    '''xinjiade'''
    suggestion = tk.StringVar()
    suggest_label = tk.Label(window, textvariable=suggestion, font=('Arial', 12), width=38, height=2)
    suggest_label.grid(column=0, row=5, sticky='n')

    suggest_button = ttk.Button(window, text="获取建议", command=rate_cal2)
    suggest_button.grid(column=0, row=6)
    '''xinjiade'''

    pic_button = ttk.Button(window, text="Updata picture", command=pic_re).grid(column=0, row=5)
    window.mainloop()

# In[4]:


name = tk.Label(root, text="请输入用户名:", width=16, height=1)
name.place(x=50, y=220)
name_tap = tk.Entry(root, width=16)
name_tap.place(x=250, y=220)

code = tk.Label(root, text="请输入密码:", width=16, height=1)
code.place(x=50, y=250)
code_tap = tk.Entry(root, show='*', width=16)  # 密码输入框显示为星号
code_tap.place(x=250, y=250)

get_into = ttk.Button(root, text='登录', command=lambda: login())
get_into.place(x=250, y=300)

root.mainloop()


#In[ ]:

