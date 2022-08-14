import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
import json


class MainWindow:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Tools Database")
        self.create_window()
        self.create_text_boxes()

        self.create_buttons()
        self.create_combo_box()
        self.load_json_file_dict("data_dict.json")
        self.load_json_company_file("company_list.json")
        self.load_json_tools_file("tool_type_list.json")


    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def save_json_file(self, fileName, dataList):
        with open(fileName, "w", encoding="UTF-8") as file:
            json.dump(dataList, file, ensure_ascii=False, indent=4, sort_keys=True)

    def load_json_file_dict(self, fileName):
        with open(fileName, encoding="UTF-8") as file:
            self.data_dict = json.load(file)
            for key in self.data_dict:
                self.data_list.append(key)
                self.combo_data["values"] = self.data_list

    def load_json_company_file(self, fileName):
        with open(fileName, encoding="UTF-8") as file:
            self.company_list = json.load(file)
            print("loaded")
            print(self.company_list)
            self.combo_data2["values"] = self.company_list

    def load_json_tools_file(self, fileName):
        with open(fileName, encoding="UTF-8") as file:
            self.tool_type_list = json.load(file)
            print("loaded")
            print(self.tool_type_list)
            self.combo_data3["values"] = self.tool_type_list

    def add_new_tool(self):
        cat_nr = self.etb0.get()
        company_name = self.combo_data2.get()
        tool_type = self.combo_data3.get()
        amount = self.etb3.get()
        if cat_nr or company_name or tool_type or amount:
            self.data_list.append(cat_nr)
            self.data_dict.update({cat_nr: {"company_name": company_name, "tool_type": tool_type, "amount": amount}})
            self.combo_data["values"] = self.data_list
            self.etb0.delete(first=0, last=len(cat_nr))
            self.combo_data2.delete(first=0, last=len(company_name))
            self.combo_data3.delete(first=0, last=len(tool_type))
            self.etb3.delete(first=0, last=len(amount))
            self.save_json_file("data_dict.json", self.data_dict)

    def add_new_company(self):
        company = self.etb1.get()
        if company:
            self.company_list.append(company)
            print("dodano")
            self.combo_data2["values"] = self.company_list
            self.etb1.delete(first=0, last=len(company))
            self.save_json_file("company_list.json", self.company_list)

    def add_new_tool_type(self):
        tool_type = self.etb2.get()
        if tool_type:
            self.tool_type_list.append(tool_type)
            print("dodano")
            self.combo_data3["values"] = self.tool_type_list
            self.etb2.delete(first=0, last=len(tool_type))
            self.save_json_file("tool_type_list.json", self.tool_type_list)

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

        self.save_json_file("data_dict.json", self.data_dict)
        mBox.showinfo("Success!", "Tool release done")

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

        self.monty = ttk.LabelFrame(tab1, text=' Add new tools ')
        self.monty.grid(column=0, row=0, padx=8, pady=4)

        self.monty2 = ttk.LabelFrame(tab1, text=' Add new Company ')
        self.monty2.grid(column=0, row=1, padx=8, pady=4, sticky="W")

        self.monty3 = ttk.LabelFrame(tab1, text=' Add new Tool type ')
        self.monty3.grid(column=0, row=2, padx=8, pady=4, sticky="W")

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

        self.etb1 = ttk.Entry(self.monty2, width=12)
        self.etb1.grid(column=0, row=1)

        self.etb2 = ttk.Entry(self.monty3, width=12)
        self.etb2.grid(column=0, row=1)

        self.etb3_name = tk.IntVar()
        self.etb3 = ttk.Entry(self.monty, width=12, textvariable=self.etb3_name)
        self.etb3.delete(first=0, last=1)
        self.etb3.grid(column=3, row=4)


        self.etb0.focus()

    def create_labels(self, column, row, text):
        label = ttk.Label(self.monty, text=text)
        label.grid(column=column, row=row)

        # label1 = ttk.Label(self.monty, text="Cat Nr")
        # label1.grid(column=0, row=3)
        # label2 = ttk.Label(self.monty, text="Company Name")
        # label2.grid(column=1, row=3)
        # label3 = ttk.Label(self.monty, text="Tool Type")
        # label3.grid(column=2, row=3)
        label4 = ttk.Label(self.monty, text="Amount")
        label4.grid(column=3, row=3)

        self.labelka = ttk.Label(self.monty, text="")
        self.labelka.grid(column=0, row=6, columnspan=4)

    def create_combo_box(self):
        self.data_list = []
        self.data_dict = {}
        self.company_list = []
        self.tool_type_list = ["drill", "wkret"]

        self.combo_data = ttk.Combobox(self.monty, width=12)
        self.combo_data.grid(column=1, row=1)

        self.combo_data2 = ttk.Combobox(self.monty, width=12)
        self.combo_data2.grid(column=1, row=4)


        self.combo_data3 = ttk.Combobox(self.monty, width=12)
        self.combo_data3.grid(column=2, row=4)
        self.combo_data3["values"] = self.tool_type_list

    def create_buttons(self):
        self.bt1 = ttk.Button(
            self.monty, text="Add Tool!", command=self.add_new_tool)
        self.bt1.grid(column=2, row=1)

        self.bt2 = ttk.Button(
            self.monty, text="Change label!", command=self.change_label)
        self.bt2.grid(column=2, row=5)

        self.bt3 = ttk.Button(
            self.monty, text="Release!", command=self.release_tool)
        self.bt3.grid(column=3, row=5)

        self.bt4 = ttk.Button(
            self.monty2, text="Add Company", command=self.add_new_company)
        self.bt4.grid(column=1, row=1)

        self.bt5 = ttk.Button(
            self.monty3, text="Add Tool Type", command=self.add_new_tool_type)
        self.bt5.grid(column=2, row=1)