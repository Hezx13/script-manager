import customtkinter
from utils.fetch_files import fetchFiles 
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
scripts = fetchFiles()
def button_function(text):
    print(text)

# Use CTkButton instead of tkinter Button
for i in range(len(scripts)):
    button = customtkinter.CTkButton(master=app, text=scripts[i], 
                                     command=lambda script=scripts[i]: button_function(script))
    button.place(relx=0.5, rely=0.5+i/7, anchor=customtkinter.CENTER)


app.mainloop()