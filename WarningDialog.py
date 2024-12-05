import customtkinter

class WarningDialog(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = customtkinter.CTkLabel(self, text="Warning: You cannot ")
        self.label.pack(padx=20, pady=20)

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = WarningDialog(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

app = WarningDialog()
app.mainloop()