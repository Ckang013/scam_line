"""
    圖形化GUI介面操作
"""
import tkinter
import scam_line

## 視窗設定
window = tkinter.Tk()   # 建立一個視窗物件
window.title("GUI")     # 設定視窗標題
window.geometry('380x400')      # 設定長寬
window.resizable(False, False)  # 設定x, y 方向都不能縮放
window.configure(background='#eee')   # 設定背景色灰色

## 文字
txt = '---' # 建立一個字串變數 給查詢id存放
a = tkinter.StringVar()
a.set(txt)
def show():
    a.set(entry_txt.get())
    lines = scam_line.get_LineID()  #qaq124b
    for line in lines:
        if a.get() == line:
            b.set("此帳號為詐騙id")
            result.config(fg='red')
            return
    b.set("此帳號為一般id")
    result.config(fg='green')

query_txt = '---'
b = tkinter.StringVar()
b.set(query_txt)
mylabel = tkinter.Label(window, text='詐騙Line ID 查詢', font=('Arial',20,'bold')).pack()  # 建立 label 標籤，加入文字，並用pack加入視窗中
lineid = tkinter.Label(window, textvariable=a, font=('Arial',15)).pack()
result = tkinter.Label(window, textvariable=b, font=('Arial',15))   # 這裡如果一起執行pack，進到show時呼叫result會出現Nonetype error
result.pack()

## 輸入框
entry_txt = tkinter.StringVar()
def clear():
    entry_txt.set('')   # 設定變數為空字串
    entry.delete(0, 'end')  # 清空欄位內容

entry = tkinter.Entry(window, textvariable=entry_txt).pack()   # 單行輸入框

## 按鈕
btn = tkinter.Button(window, text='查詢', font=('Arial', 15), padx=3, pady=3, activeforeground='#f00', command=show)   # 建立一個 Button
btn.pack()  # 加入視窗中
clr_btn = tkinter.Button(window, text='清除', font=('Arial', 15), padx=3, pady=3, activeforeground='#f00', command=clear)
clr_btn.pack()

window.mainloop()
