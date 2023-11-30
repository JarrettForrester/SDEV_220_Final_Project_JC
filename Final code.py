import tkinter as tk

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("80/20 Material List")
        self.master.geometry("700x700")
        self.button = tk.Button(self.master, text="View Metric Material", command=self.open_window2)
        self.button.pack()

    def open_window2(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window2(self.new_window)

class Window2:
    def __init__(self, master,):
        self.master = master
        self.master.title("Metric Material")
        self.master.geometry("700x700")
        self.button = tk.Button(self.master, text="View Standard Material", command=self.open_window3)
        self.button.pack()
        self.listbox = tk.Listbox(self.master)
        self.listbox.pack()
        self.listbox.insert(tk.END, "40 Series")
        self.listbox.insert(tk.END, "30 Series")
        self.listbox.insert(tk.END, "25 Series")
        self.listbox.insert(tk.END, "45 Series")
        self.listbox.insert(tk.END, "20 Series")
        

    def open_window3(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window3(self.new_window)

class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title("Standard Material")
        self.master.geometry("700x700")
        self.label = tk.Label(self.master, text="80/20 Standard Material")
        self.label.pack()
        self.listbox = tk.Listbox(self.master)
        self.listbox.pack()
        self.listbox.insert(tk.END, "10 Series")
        self.listbox.insert(tk.END, "15 Series")

def main():
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()