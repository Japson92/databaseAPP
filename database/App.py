import MainWindow

startApp = MainWindow.MainWindow()
text = ["Cat Nr", "Company Name", "Tool Type"]
for labels in range(3):
    startApp.create_labels(labels, 3, text[labels])


startApp.win.mainloop()
