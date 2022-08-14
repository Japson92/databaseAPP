import MainWindow

startApp = MainWindow.MainWindow()
text = ["Cat Nr", "Company Name", "Tool Type", "Amount"]
text2 = ["New Company", "", "New Tool Type"]
button_column = [2, 1, 3]
button_text = ["Add Tool", "Add Company", "Add Tool Type"]
button_row = [2, 6, 6]
button_methods = [startApp.add_new_tool, startApp.add_new_company, startApp.add_new_tool_type]
for labels in range(4):
    startApp.create_labels(labels, 0, text[labels])

for labels in range(0,4,2):
    startApp.create_labels(labels, 3, text2[labels])
for button in range(3):
    startApp.create_buttons(button_text[button], button_methods[button], button_column[button], button_row[button])

startApp.load_json_file_dict("data_dict.json")
startApp.load_json_company_file("company_list.json")
startApp.load_json_tools_file("tool_type_list.json")

startApp.win.mainloop()
