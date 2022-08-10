import tkinter as tk

def main():
    def convert():
        lbl_celcius['text'] = f'{round((int(ent_fahrenheit.get()) - 32) * (5/9), 2)} \u00B0C'

    window = tk.Tk()
    window.title('Конвертер \u00B0F в \u00B0C')

    window.rowconfigure(0, weight=1, minsize=30)
    window.columnconfigure(0, weight=1, minsize=50)
    window.columnconfigure(1, weight=1, minsize=20)
    window.columnconfigure(2, weight=1, minsize=20)
    window.columnconfigure(3, weight=1, minsize=50)

    ent_fahrenheit = tk.Entry(
        master=window
    )
    ent_fahrenheit.grid(row=0, column=0, sticky='nsew')

    lbl_fahrenheit = tk.Label(
        master=window,
        text='\u00B0F'
    )
    lbl_fahrenheit.grid(row=0, column=1, sticky='nsew')

    btn_convert = tk.Button(
        master=window,
        text='\N{RIGHTWARDS BLACK ARROW}',
        command=convert
    )
    btn_convert.grid(row=0, column=2, sticky='nsew')

    lbl_celcius = tk.Label(
        master=window,
        text='? \u00B0C'
    )
    lbl_celcius.grid(row=0, column=3, sticky='nsew')

    window.mainloop()


if __name__ == '__main__':
    main()