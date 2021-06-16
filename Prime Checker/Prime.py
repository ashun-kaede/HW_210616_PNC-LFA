#coding=utf-8

import tkinter as tk
import math

def CheckPrime_With_ReturnKey(self):
    CheckPrime()

def CheckPrime():
    try:
        num = num_entry.get()
        isPrime = False
        a = 1
        b = 1

        num = int(num)

        if num == 2 or num == 3:
            isPrime = True
        elif num == 1 or num % 2 == 0:
            flag = False
            a = 2
            b = int(num / 2)
        else:
            for i in range(3, int(math.sqrt(num))+2, 2):
                if num % i == 0:
                    isPrime = False
                    a = i
                    b = int(num / i)
                    break
                else:
                    isPrime = True

        if isPrime:
            result_text.configure(text='恭喜你！此為質數')
        else:
            result_text.configure(text='抱歉，這不是質數... {0} = {1} x {2}'.format(num, a, b))
        
    except:
        result_text.configure(text='錯誤！意外狀況可能源自於您輸入的不是正整數')
            
if __name__ == '__main__':
    w = tk.Tk()
    w.title('Prime Check')
    w.geometry('320x70')

    f1 = tk.Frame(w)
    f1.grid(row=0, column=0, sticky='w')
    num_entry = tk.Entry(f1,font=('Arial', 14))
    num_entry.bind('<Return>', CheckPrime_With_ReturnKey)
    num_entry.pack(side='left', pady=5, padx=10)
    start_btn = tk.Button(f1, text='開始判斷', command=CheckPrime)
    start_btn.pack(side='left', pady=5, padx=10)

    f2 = tk.Frame(w)
    f2.grid(row=1, column=0, sticky='w')
    result_text = tk.Label(f2, text='請輸入大於零的正整數')
    result_text.pack(side='left', pady=5, padx=10)

    w.mainloop()

