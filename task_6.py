import tkinter as tk
import tkinter.filedialog


def main():
    def open_file():
        filepath = tk.filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        txt_entry.delete('1.0', tk.END)
        with open(filepath) as input_file:
            txt_entry.insert(tk.END, input_file.read())
        window.title(f"Text Editor - {filepath}")

    def save_file():
        filepath = tk.filedialog.asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        with open(filepath, 'w') as output_file:
            output_file.write(txt_entry.get('1.0', tk.END))
        window.title(f"Text Editor - {filepath}")

    window = tk.Tk()
    window.title('Text Editor')

    window.rowconfigure(0, weight=1, minsize=800)
    window.columnconfigure(1, weight=1, minsize=800)

    frm_forbtns = tk.Frame(
        window,
        bg='#F5DEB3'
    )
    frm_forbtns.grid(column=0, sticky='nsew')

    btn_open = tk.Button(
        frm_forbtns,
        text='Open...',
        command=open_file,
        bg='BurlyWood'
    )
    btn_open.pack(pady=10, padx=5)

    btn_save = tk.Button(
        frm_forbtns,
        text='Save as',
        command=save_file,
        bg='BurlyWood'
    )
    btn_save.pack(pady=10, padx=5)

    txt_entry = tk.Text(
        window
    )
    txt_entry.grid(row=0, column=1, sticky='nsew')

    window.mainloop()


if __name__ == '__main__':
    main()