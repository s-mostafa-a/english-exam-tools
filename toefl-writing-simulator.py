from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askokcancel


class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(expand=YES, fill=BOTH, side=LEFT)

    def quit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans:
            Frame.quit(self)


class ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.text = None
        self.make_widgets()
        self.set_text(text, file)

    def make_widgets(self):
        sc_bar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        sc_bar.config(command=text.yview)
        text.config(yscrollcommand=sc_bar.set)
        sc_bar.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT, expand=YES, fill=BOTH)
        self.text = text

    def set_text(self, text='', file=None):
        if file:
            text = open(file, 'r').read()
        self.text.delete('1.0', END)
        self.text.insert('1.0', text)
        self.text.mark_set(INSERT, '1.0')
        self.text.focus()

    def get_text(self):
        return self.text.get('1.0', END + '-1c')


class SimpleEditor(ScrolledText):
    def __init__(self, parent=None, file=None):
        frm = Frame(parent)
        frm.pack(fill=X)
        Button(frm, text='Save', command=self.on_save).pack(side=LEFT)
        Button(frm, text='Cut', command=self.on_cut).pack(side=LEFT)
        Button(frm, text='Paste', command=self.on_paste).pack(side=LEFT)
        self.lbl = Label(frm, text='0 words')
        self.lbl.pack(side=RIGHT)
        Quitter(frm).pack(side=LEFT)
        ScrolledText.__init__(self, parent, file=file)
        self.text.config(font=('courier', 20, 'normal'))
        self.text.bind("<KeyRelease>", self.keydown)

    def on_save(self):
        filename = asksaveasfilename()
        if filename:
            all_text = self.get_text()
            open(filename, 'w').write(all_text)

    def keydown(self, char):
        all_text = self.get_text()
        all_text = re.sub(r'[^A-Za-z0-9 ]+', ' ', all_text)
        self.lbl.config(text=f"{len(all_text.split())} words")

    def on_cut(self):
        text = self.text.get(SEL_FIRST, SEL_LAST)
        self.text.delete(SEL_FIRST, SEL_LAST)
        self.clipboard_clear()
        self.clipboard_append(text)

    def on_paste(self):
        try:
            text = self.selection_get(selection='CLIPBOARD')
            self.text.insert(INSERT, text)
        except TclError:
            pass


if __name__ == '__main__':
    app = Tk()
    app.title('Toefl writing simulator')
    try:
        SimpleEditor(file=sys.argv[1], parent=app)
    except IndexError:
        SimpleEditor(parent=app)
    app.mainloop()
