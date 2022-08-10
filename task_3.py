import tkinter as tk


def main():
    window = tk.Tk()
    window.title('Введите домашний адрес')

    window.columnconfigure(0, weight=1, minsize=500)
    frm_data = tk.Frame(
        master=window,
        height=200,
        width=550,
        bg='silver',
        borderwidth=3,
        relief=tk.SUNKEN
    )
    frm_data.grid(row=0, sticky='nsew')

    frm_btns = tk.Frame(
        master=window,
        height=40,
        width=550,
        bg='silver'
    )
    frm_btns.grid(row=1, sticky='nsew')

    frm_data.columnconfigure(0, weight=1, minsize=20)
    frm_data.columnconfigure(1, weight=1, minsize=20)

    labels=['Имя:', 'Фамилия:', 'Адрес 1:', 'Адрес 2:', 'Город:', 'Регион:', 'Почтовый индекс:', 'Страна:']

    for idx, lbl in enumerate(labels):
        lbl_hint = tk.Label(master=frm_data, text=lbl, bg='silver')
        ent = tk.Entry(master=frm_data, width=50)

        lbl_hint.grid(row=idx, column=0, sticky='e')
        ent.grid(row=idx, column=1)

    btn_send = tk.Button(
        master=frm_btns,
        borderwidth=1,
        relief=tk.RAISED,
        text='Отправить'
    )
    btn_send.pack(side=tk.RIGHT, padx=5, pady=2.5)

    btn_clear = tk.Button(
        master=frm_btns,
        borderwidth=1,
        relief=tk.RAISED,
        text='Очистить'
    )
    btn_clear.pack(side=tk.RIGHT, padx=5, pady=2.5)
    window.mainloop()

if __name__ == '__main__':
    main()