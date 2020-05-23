# !/user/bin/env/python3
# -*- coding:utf-8 -*-
# @author heyu<18781085152@163.com>
# @date   2020/5/23

from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import os

# 定义窗口
window = Tk(className="文件搜索工具")
window.geometry('540x400')  # 定义主窗口尺寸


# window.resizable(0, 0) # 限制用户改变窗口大小

# 定义搜索按钮函数 （函数一定要写在定义元素之前）
def search():
    keyWords = entry_key.get()
    type = entry_type.get()
    if not type:
        tkinter.messagebox.showinfo(title='错误提示', message='文件后缀不能为空')
    else:
        type = '.' + type
        listbox.delete(0, END)
        fpath = tkinter.filedialog.askdirectory()  # 选择文件夹
        fileList = os.walk(fpath)  # 所有文件目录
        resList = []
        for path, dir, file in fileList:  # path:路径;dir:文件夹;file:文件
            for fileName in file:
                searchPat = re.compile(r'.*?(%s).*(%s)$' % (keyWords, type), re.I)  # re.I不区分大小写
                searchRes = searchPat.search(fileName)
                if searchRes != None:
                    resList.append(fileName)
                    listbox.insert(END, path + '/' + fileName)
                if len(resList) == 0:
                    tkinter.messagebox.showerror('错误提示', '没有找到相关的文件')
                    return


# 搜索结果：左键双击打开
def click(event):
    index = listbox.curselection()  # 获取文件列表索引
    if index == ():
        tkinter.messagebox.showerror('错误提示', '没有找到相关的文件')
        return
    filePath = listbox.get(index)
    try:
        f = open(filePath, encoding='utf-8')
        fcontent = f.read()
    except:
        tkinter.messagebox.showerror('错误提示', '该文件不能不能读取')
    else:
        showFile = Tk(className='查看')
        showFile.geometry('1000x400')
        fileText = Text(showFile, width=1000)
        fileText.grid(row=0, column=0)
        fileText.insert(END, fcontent)
        f.close()


# 定义listbox 搜索结果 并且设置滚动窗口
listbox = Listbox(window, width=500, height=380)
scroll = Scrollbar(window)
scroll.pack(side=RIGHT, fill=Y, pady=50)
listbox.pack(side=LEFT, fill=NONE, pady=50)
listbox['yscrollcommand'] = scroll.set  # 关键：指定Listbox的yscrollbar的回调函数为Scrollbar的set
listbox.bind('<Double-Button-1>', click)  # 绑定双击事件

# 定义搜索关键字
Label(window, text='搜索关键字：').place(x=5, y=0)
entry_key = Entry(window, relief='flat')  # 文件搜索关键字输入框
entry_key.place(x=80, y=0)

# 定义搜索文件类型关键字
Label(window, text='文件后缀：').place(x=270, y=0)  # 文字标签
entry_type = Entry(window, relief='flat')  # 文件搜索类型输入框
entry_type.place(x=340, y=0)

# 定义搜索按钮
button = Button(window, text='搜索', command=search).place(x=500, y=0)  # command绑定函数

# 循环窗口
window.mainloop()
