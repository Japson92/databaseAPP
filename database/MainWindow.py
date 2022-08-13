import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
import json

class MainWindow():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Tools Database")
        self.create_window()
        self.create_text_boxes()
        self.create_labels()
        self.create_buttons()
        self.create_combo_box()
        self.load_json_file()

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def save_json_file(self, fileName):
        with open(fileName, "w", encoding="UTF-8") as file:
            json.dump(self.data_dict, file, ensure_ascii=False, indent=4, sort_keys=True)

    def load_json_file(self, fileName):
        with open(fileName, encoding="UTF-8") as file:
            self.data_dict = json.load(file)
            for key in self.data_dict:
                self.data_list.append(key)
                self.combo_data["values"] = self.data_list

    def add_data(self):
        cat_nr = self.etb0.get()
        company_name = self.etb1.get()
        tool_type = self.etb2.get()
        amount = self.etb3.get()
        if cat_nr or company_name or tool_type or amount:
            self.data_list.append(cat_nr)
            self.data_dict.update({cat_nr: {"company_name": company_name, "tool_type": tool_type, "amount": amount}})
            self.combo_data["values"] = self.data_list
            self.etb0.delete(first=0, last=len(cat_nr))
            self.etb1.delete(first=0, last=len(company_name))
            self.etb2.delete(first=0, last=len(tool_type))
            self.etb3.delete(first=0, last=len(amount))
            self.save_json_file("data_dict.json")

    def change_label(self):
        picked_tool = self.combo_data.get()
        dictionary = self.data_dict[picked_tool]
        self.labelka.configure(text="Catalog number: " + picked_tool + ", company name: " +
                                    dictionary["company_name"] + ", tool type: " +
                                    dictionary["tool_type"] + ", amount: " + dictionary["amount"])

    def release_tool(self):
        picked_tool = self.combo_data.get()
        dictionary = self.data_dict[picked_tool]

        new_amount = int(dictionary["amount"]) - 1
        if new_amount < 5:
            mBox.showwarning("Warning", "Low amount of tool!")
        dictionary["amount"] = str(new_amount)

        self.labelka.configure(text="Catalog number: " + picked_tool + ", company name: " +
                                    dictionary["company_name"] + ", tool type: " +
                                    dictionary["tool_type"] + ", amount: " + dictionary["amount"])

        self.save_json_file("data_dict.json")

    def create_window(self):
        # Tab Control introduced here --------------------------------------
        tab_control = ttk.Notebook(self.win)     # Create Tab Control

        tab1 = ttk.Frame(tab_control)            # Create a tab
        tab_control.add(tab1, text='Add Tool')      # Add the tab

        tab2 = ttk.Frame(tab_control)            # Add a second tab
        tab_control.add(tab2, text='Tab 2')      # Make second tab visible

        tab3 = ttk.Frame(tab_control)
        tab_control.add(tab3, text='Tab 3')

        tab_control.pack(expand=1, fill="both")  # Pack to make visible

        self.monty = ttk.LabelFrame(tab1, text=' Main 1 ')
        self.monty.grid(column=0, row=0, padx=8, pady=4)

        self.monty2 = ttk.LabelFrame(tab2, text=' Main 1 ')
        self.monty2.grid(column=0, row=0, padx=8, pady=4)

        self.monty3 = ttk.LabelFrame(tab3, text=' Main 1 ')
        self.monty3.grid(column=0, row=0, padx=8, pady=4)

        # Creating a Menu Bar
        menu_bar = tk.Menu(tab1)
        self.win.config(menu=menu_bar)

        # Add menu items
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def create_text_boxes(self):
        self.etb0 = ttk.Entry(self.monty, width=12)
        self.etb0.grid(column=0, row=4)

        self.etb1 = ttk.Entry(self.monty, width=12)
        self.etb1.grid(column=1, row=4)

        self.etb2 = ttk.Entry(self.monty, width=12)
        self.etb2.grid(column=2, row=4)

        self.etb3_name = tk.IntVar()
        self.etb3 = ttk.Entry(self.monty, width=12, textvariable=self.etb3_name)
        self.etb3.delete(first=0, last=1)
        self.etb3.grid(column=3, row=4)

        self.etb2.focus()

    def create_labels(self):
        label = ttk.Label(self.monty2, text="Choose a Tool Type:")
        label.grid(column=1, row=0)
        label1 = ttk.Label(self.monty, text="Cat Nr")
        label1.grid(column=0, row=3)
        label2 = ttk.Label(self.monty, text="Company Name")
        label2.grid(column=1, row=3)
        label3 = ttk.Label(self.monty, text="Tool Type")
        label3.grid(column=2, row=3)
        label4 = ttk.Label(self.monty, text="Amount")
        label4.grid(column=3, row=3)

        self.labelka = ttk.Label(self.monty, text="")
        self.labelka.grid(column=0, row=6, columnspan=4)

    def create_combo_box(self):
        self.data_list = []
        self.data_dict = {}
        self.combo_data = ttk.Combobox(self.monty, width=12)
        self.combo_data.grid(column=1, row=1)

        self.combo_data2 = ttk.Combobox(self.monty2, width=12)
        self.combo_data2.grid(column=1, row=4)

    def create_buttons(self):
        self.bt1 = ttk.Button(
            self.monty, text="Add Tool!", command=self.add_data)
        self.bt1.grid(column=2, row=1)

        self.bt2 = ttk.Button(
            self.monty, text="Change label!", command=self.change_label)
        self.bt2.grid(column=2, row=5)

        self.bt3 = ttk.Button(
            self.monty, text="Release!", command=self.release_tool)
        self.bt3.grid(column=3, row=5)
