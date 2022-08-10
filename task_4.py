import tkinter as tk
from random import randint

def main():
    def cast():
        lbl_val['text'] = f'{randint(1, 6)}'

    window = tk.Tk()
    window.title('Гральны кости')

    window.rowconfigure([0, 1], weight=1, minsize=50)
    window.columnconfigure(0, weight=1, minsize=150)

    btn_throw = tk.Button(
        master=window,
        text='Бросить',
        command=cast
    )
    btn_throw.grid(row=0, column=0, sticky='nsew')

    lbl_val = tk.Label(
        master=window,
        text='0',
    )
    lbl_val.grid(row=1, column=0, sticky='nsew')

    window.mainloop()


if __name__ == '__main__':
    main()