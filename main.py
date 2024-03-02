import customtkinter
import tkinter as tk
import os
from utils.fetch_files import fetchFiles
from interface.scrollable_frame import ScrollableButtonFrame
import json
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()  # create CTk window like you do with the Tk window
        self.geometry("800x600")
        self.resizable(False, False)
        self.scripts = self.fetchScripts()
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure((1, 2), weight=3)
            
        #SIDEBAR FRAME
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        #BUTTON FRAME
        self.scrollable_checkbox_frame = ScrollableButtonFrame(self, title="Scripts", values=self.scripts)
        self.scrollable_checkbox_frame.grid(row=0, column=0, rowspan=3, padx=10, pady=(10, 0), sticky="nsew")
        
        
    def fetchScripts(self):
        try:
            scripts = fetchFiles()
            return scripts
        except KeyError:
            dialog = customtkinter.CTkInputDialog(text="Please specify name of the scripts directory", title="Scripts directory not")
            with open('options.json','w') as options:
                data = {}
                data['ScriptDirectory'] = dialog.get_input()
                json.dump(data, options, indent=4)
            scripts = self.fetchScripts()
            return scripts
    
if __name__ == "__main__":
    app = App()
    app.mainloop()