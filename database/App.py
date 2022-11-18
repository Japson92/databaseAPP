import MainWindow


startApp = MainWindow.MainWindow()
text = ["Cat Nr", "Company Name", "Tool Type", "Amount", "Rack Nr", "Drawer NR"]
text2 = ["New Company", "", "New Tool Type"]
button_column = [3, 1, 3]
button_text = ["Add Tool", "Add Company", "Add Tool Type"]
button_row = [3, 6, 6]
button_methods = [startApp.add_new_tool, startApp.add_new_company, startApp.add_new_tool_type]

for labels in range(4):
    startApp.create_labels(labels, 0, text[labels])

for labels in range(0, 4, 2):
    startApp.create_labels(labels, 4, text2[labels])

for labels in range(2):
    startApp.create_labels(labels, 2, text[4 + labels])

for button in range(3):
    startApp.create_buttons(button_text[button], button_methods[button], button_column[button], button_row[button])

startApp.create_text_boxes()
startApp.create_combo_box()
startApp.load_json_file_dict("data_dict.json")
startApp.load_json_company_file("company_list.json")
startApp.load_json_tools_file("tool_type_list.json")
startApp.load_json_tree_list("tree_list.json")
startApp.create_tree()

startApp.win.mainloop()
