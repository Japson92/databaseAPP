import tkinter as tk
from tkinter import ttk
import json


class MainWindow():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Tools Database")
        self.createWindow()
        self.createTextBoxes()
        self.createLabels()
        self.createButtons()
        self.createComboBox()

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def save_json_file(self):
        with open("data_dict.json", "w", encoding="UTF-8") as file:
            json.dump(self.data_dict, file, ensure_ascii=False)

    def load_json_file(self):
        with open("data_dict.json", encoding="UTF-8") as file:
            self.data_dict = json.load(file)
            for key in self.data_dict:
                self.data_list.append(key)
                print(self.data_list)
                self.combo_data["values"] = self.data_list
        self.enabled_widgets()

    def enabled_widgets(self):
        self.bt1.configure(state=tk.NORMAL)
        self.bt2.configure(state=tk.NORMAL)
        self.etb0.configure(state=tk.NORMAL)
        self.etb1.configure(state=tk.NORMAL)
        self.etb2.configure(state=tk.NORMAL)
        self.combo_data.configure(state=tk.NORMAL)

    def add_data(self):
        data = self.etb0.get()
        data2 = self.etb1.get()
        data3 = self.etb2.get()
        if data or data2 or data3:
            self.data_list.append(data)
            self.data_dict.update({data: {"company_name": data2, "cat_nr": data3}})
            print(self.data_dict)
            self.combo_data["values"] = self.data_list
            self.etb0.delete(first=0, last=len(data))
            self.etb1.delete(first=0, last=len(data2))
            self.etb2.delete(first=0, last=len(data3))
            self.save_json_file()

    def change_label(self):
        nowa = self.combo_data.get()
        dict = self.data_dict[nowa]
        self.labelka.configure(text="Tool type: " + nowa + ", company name: " +
                                    dict["company_name"] + ", catalog number: " +
                                    dict["cat_nr"])




    def createWindow(self):
        # Tab Control introduced here --------------------------------------
        tab_control = ttk.Notebook(self.win)     # Create Tab Control

        tab1 = ttk.Frame(tab_control)            # Create a tab
        tab_control.add(tab1, text='Tab 1')      # Add the tab

        tab2 = ttk.Frame(tab_control)            # Add a second tab
        tab_control.add(tab2, text='Tab 2')      # Make second tab visible

        tab3 = ttk.Frame(tab_control)
        tab_control.add(tab3, text='Tab 3')

        tab_control.pack(expand=1, fill="both")  # Pack to make visible

        self.monty = ttk.LabelFrame(tab1, text=' Main 1 ')
        self.monty.grid(column=0, row=0, padx=8, pady=4)

        bt3 = ttk.Button(
            self.monty, text="Load Data!", command=self.load_json_file)
        bt3.grid(column=1, row=5)

        # Creating a Menu Bar
        menu_bar = tk.Menu(tab1)
        self.win.config(menu=menu_bar)

        # Add menu items
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def createTextBoxes(self):
        #textbox
        self.etb0 = ttk.Entry(self.monty, width=12, state=tk.DISABLED)
        self.etb0.grid(column=0, row=4)

        self.etb1 = ttk.Entry(self.monty, width=12, state=tk.DISABLED)
        self.etb1.grid(column=1, row=4,)

        self.etb2 = ttk.Entry(self.monty, width=12, state=tk.DISABLED)
        self.etb2.grid(column=2, row=4)
        # self.etb.bind('<KeyPress-Enter>', self.add_data()) nie działa
        self.etb0.focus()

    def createLabels(self):
        label1 = ttk.Label(self.monty, text="Tool Type")
        label1.grid(column=0, row=3)
        label2 = ttk.Label(self.monty, text="Company Name")
        label2.grid(column=1, row=3)
        label3 = ttk.Label(self.monty, text="Cat Nr")
        label3.grid(column=2, row=3)

        self.labelka = ttk.Label(self.monty, text="Choose a Tool Type:")
        self.labelka.grid(column=1, row=0)

    def createComboBox(self):
        self.data_list = []
        self.data_dict = {}
        self.combo_data = ttk.Combobox(self.monty, width=30, state=tk.DISABLED)
        self.combo_data.grid(column=1, row=1)

    def createButtons(self):
        #button
        self.bt1 = ttk.Button(
            self.monty, text="Click Me!", command=self.add_data, state=tk.DISABLED)
        self.bt1.grid(column=2, row=1)
        self.bt2 = ttk.Button(
            self.monty, text="Change label!", command=self.change_label, state=tk.DISABLED)
        self.bt2.grid(column=2, row=5)
