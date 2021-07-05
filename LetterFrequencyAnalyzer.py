#coding=UTF-8

import matplotlib.pyplot as plt # 圖表繪製套件
import tkinter as tk # GUI套件
from tkinter import filedialog #檔案總管API呼叫套件

# 按鈕點擊事件
def btn_click():

    # 呼叫出檔案選擇器
    filePath = filedialog.askopenfilename(title = '選擇明文文本',filetypes = [('text','*.txt')])

    # 開啟選擇檔案
    f = open(filePath, 'r') 

    wordNumLsit = [0 for i in range(26)] # 字母頻率列表
    sumnum = 0 # 計數加總(用於計算百分比)

    #統計字數
    w = 'x'
    while w:
        try:
            w = f.read(1) # 一次讀一個字
            if ord(w) in range(97, 123):
                wordNumLsit[ord(w)-97] += 1
                sumnum += 1 
        except:
            pass

    # 印出結果於結果列表
    for i in range(len(wordNumLsit)):
        key = chr(i+97).upper()
        percent = str('{:.1%}'.format(wordNumLsit[i]/sumnum))
        frq_text.insert(i, '  {0} :  {1}   ( {2} )'.format(key, str(wordNumLsit[i]), percent))

    chart_show([chr(i) for i in range(97,123)], wordNumLsit)

#展示圖表
def chart_show(x, y):
    plt.ylabel('Count')
    plt.bar(x, y)
    plt.show()

if __name__ == '__main__':

    # GUI部分
    w = tk.Tk()
    w.resizable(width=0, height=0)
    w.title('LFA')
    w.geometry('250x550')

    f1 = tk.Frame(w)
    f1.grid(row=0, column=0, sticky='w')
    t = tk.Label(f1, text='請選擇要分析的檔案 ->', font=('Arial', 10)) # 建立提示標籤元件
    t.pack(side='left', pady=5, padx=10)
    start_btn = tk.Button(f1, text='選擇檔案', command=btn_click) # 建立選擇檔案按鈕元件
    start_btn.pack(side='left', pady=5, padx=10)

    f2 = tk.Frame(w)
    f2.grid(row=1, column=0, sticky='w')
    frq_text = tk.Listbox(f2, height=26, width=25, highlightbackground='black', font=('Arial', 12)) # 建立列表元件
    frq_text.pack(padx=10)

    w.mainloop()
