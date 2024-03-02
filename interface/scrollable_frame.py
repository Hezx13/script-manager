import customtkinter

class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes
    
class ScrollableButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        print(values)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.buttons = []

        for i, value in enumerate(self.values):
            button = customtkinter.CTkButton(self, text=value, command=lambda button=value: self.button_function(button))
            button.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="we")
            self.buttons.append(button)

    def button_function(self, button):
        checked_checkboxes = []
        for button in self.buttons:
            if button.get() == 1:
                checked_checkboxes.append(button.cget("text"))
        return checked_checkboxes