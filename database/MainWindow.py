import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
import json


def save_json_file(fileName, dataList):
    with open(fileName, "w", encoding="UTF-8") as file:
        json.dump(dataList, file, ensure_ascii=False, indent=4, sort_keys=True)


class MainWindow:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Tools Database")
        self.create_window()
        self.create_text_boxes()
        self.create_combo_box()
        self.data_list = []
        self.data_dict = {}
        self.company_list = []
        self.tool_type_list = []

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def load_json_file_dict(self, fileName):
        with open(fileName, encoding="UTF-8") as file:
            self.data_dict = json.load(file)
            for key in self.data_dict:
                self.data_list.append(key)
                self.combo_data["values"] = self.data_list

    def load_json_company_file(self, fileName):
        with open(fileName, encoding="UTF-8") as file:
            self.company_list = json.load(file)
            self.combo_data2["values"] = self.company_list

    def load_json_tools_file(self, fileName):
        with open(fileName, encoding="UTF-8") as file:
            self.tool_type_list = json.load(file)
            self.combo_data3["values"] = self.tool_type_list

    def add_new_tool(self):
        input_list = []
        elements_list = [self.etb0, self.combo_data2, self.combo_data3, self.etb3]
        for i in range(len(elements_list)):
            input_list.append(elements_list[i].get())

        newList = set(self.data_dict)
        if input_list[0] in newList:
            mBox.showerror("Error!", "Tool already exist!")

        elif input_list[0] and input_list[1] and input_list[2] and input_list[3]:
            self.data_list.append(input_list[0])
            self.data_dict.update({input_list[0]: {"company_name": input_list[1], "tool_type": input_list[2],
                                                   "amount": input_list[3]}})
            self.combo_data["values"] = self.data_list
            for element in range(4):
                elements_list[element].delete(first=0, last=(len(input_list[element])))

            save_json_file("data_dict.json", self.data_dict)

    def add_new_company(self):
        company = self.etb1.get()
        if company:
            self.company_list.append(company)
            print("dodano")
            self.combo_data2["values"] = self.company_list
            self.etb1.delete(first=0, last=len(company))
            save_json_file("company_list.json", self.company_list)

    def add_new_tool_type(self):
        tool_type = self.etb2.get()
        if tool_type:
            self.tool_type_list.append(tool_type)
            self.combo_data3["values"] = self.tool_type_list
            self.etb2.delete(first=0, last=len(tool_type))
            save_json_file("tool_type_list.json", self.tool_type_list)

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

        save_json_file("data_dict.json", self.data_dict)
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

        self.monty2 = ttk.LabelFrame(tab2, text=' Add new Company ')
        self.monty2.grid(column=0, row=1, padx=8, pady=4, sticky="W")

        self.monty3 = ttk.LabelFrame(tab3, text=' Add new Tool type ')
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
        self.etb0.grid(column=0, row=1)

        self.etb1 = ttk.Entry(self.monty, width=12)
        self.etb1.grid(column=0, row=6)

        self.etb2 = ttk.Entry(self.monty, width=12)
        self.etb2.grid(column=2, row=6)

        self.etb3_name = tk.IntVar()
        self.etb3 = ttk.Entry(self.monty, width=12, textvariable=self.etb3_name)
        self.etb3.delete(first=0, last=1)
        self.etb3.grid(column=3, row=1)

        self.etb0.focus()

    def create_labels(self, column, row, text):
        label = ttk.Label(self.monty, text=text)
        label.grid(column=column, row=row)

        self.labelka = ttk.Label(self.monty2, text="")
        self.labelka.grid(column=0, row=6, columnspan=4)

    def create_combo_box(self):
        self.combo_data = ttk.Combobox(self.monty2, width=12)
        self.combo_data.grid(column=1, row=1)

        self.combo_data2 = ttk.Combobox(self.monty, width=12)
        self.combo_data2.grid(column=1, row=1)

        self.combo_data3 = ttk.Combobox(self.monty, width=12)
        self.combo_data3.grid(column=2, row=1)

    def create_buttons(self, buttonText, buttonCommand, column, row):
        bt1 = ttk.Button(self.monty, text=buttonText, command=buttonCommand)
        bt1.grid(column=column, row=row)

        bt2 = ttk.Button(self.monty2, text="Change label!", command=self.change_label)
        bt2.grid(column=2, row=5)

        bt3 = ttk.Button(self.monty2, text="Release!", command=self.release_tool)
        bt3.grid(column=3, row=5)
