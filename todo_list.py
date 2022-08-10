import tkinter as tk


def main():
    todo_list = []

    def clear():
        for i in todo_list:
            i.destroy()
        todo_list.clear()

    def on_closing():
        with open('data.txt', 'w') as file:
            for i in range(len(todo_list)):
                text = todo_list[i]['text']
                file.write(text)
        window.destroy()

    def create_todo():
        def yes():
            lbl_todo = tk.Label(
                frm_todo,
                text=ent_todo.get(),
                bg='#008000',
                relief=tk.SUNKEN,
                borderwidth=2
            )
            lbl_todo.pack(fill=tk.BOTH)

            todo_list.append(lbl_todo)
            window1.destroy()

        window1 = tk.Tk()
        window1.title('Введите вашу цель')

        window1.rowconfigure(0, minsize=40)
        window1.rowconfigure(1, minsize=35)
        window1.columnconfigure(0, weight=1, minsize=50)

        ent_todo = tk.Entry(
            window1
        )
        ent_todo.grid(row=0, column=0, sticky='nsew')

        btn_create1 = tk.Button(
            window1,
            text='Создать',
            command=yes
        )
        btn_create1.grid(row=1, column=0, sticky='nsew')

        window1.mainloop()

    def delete_todo():
        def yes():
            i = int(ent_todo.get())-1
            todo_list[i].destroy()
            todo_list.pop(i)
            window1.destroy()

        window1 = tk.Tk()
        window1.title('Введите номер для удаления(с 0)')

        window1.rowconfigure(0, minsize=40)
        window1.rowconfigure(1, minsize=35)
        window1.columnconfigure(0, weight=1, minsize=50)

        ent_todo = tk.Entry(
            window1
        )
        ent_todo.grid(row=0, column=0, sticky='nsew')

        btn_create1 = tk.Button(
            window1,
            text='Удалить',
            command=yes
        )
        btn_create1.grid(row=1, column=0, sticky='nsew')

        window1.mainloop()

    window = tk.Tk()
    window.title('ToDo list')

    window.rowconfigure(0, minsize=39)
    window.rowconfigure(1, weight=1, minsize=300)
    window.columnconfigure(0, weight=1, minsize=300)
    frm_btnbar = tk.Frame(
        window,
        bg='#DEB887',
        relief=tk.GROOVE,
        borderwidth=2
    )
    frm_btnbar.grid(row=0, column=0, sticky='nsew')

    btn_create = tk.Button(
        frm_btnbar,
        text='Создать',
        bg='#D2B48C',
        command=create_todo
    )
    btn_create.pack(side=tk.LEFT)

    btn_delete = tk.Button(
        frm_btnbar,
        text='Удалить',
        bg='#D2B48C',
        command=delete_todo
    )
    btn_delete.pack(side=tk.LEFT)

    btn_delete_all = tk.Button(
        frm_btnbar,
        text='Очистить',
        bg='#D2B48C',
        command=clear
    )
    btn_delete_all.pack(side=tk.LEFT)

    frm_todo = tk.Frame(
        window,
        bg='#FFF8DC'
    )
    frm_todo.grid(row=1, column=0, sticky='nsew')

    with open('data.txt', 'r') as file:
        for i in file.readlines():
            lbl_todo = tk.Label(
                frm_todo,
                text=i,
                bg='#008000',
                relief=tk.SUNKEN,
                borderwidth=2
            )
            lbl_todo.pack(fill=tk.BOTH)

            todo_list.append(lbl_todo)

    window.protocol('WM_DELETE_WINDOW', on_closing)
    window.mainloop()

if __name__ == '__main__':
    main()