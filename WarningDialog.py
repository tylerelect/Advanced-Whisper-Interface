import customtkinter

class WarningDialog(customtkinter.CTk):
    def __init__(self, title, label_text, largewindow=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Dynamically adjust window size based on text length or largewindow parameter
        if largewindow:
            self.geometry("300x400")  # Larger window size
        elif len(label_text) > 43:
            self.geometry("300x125")  # Increase height for long text
        else:
            self.geometry("300x100")  # Default height

        self.title(title)

        # Add the main label with word wrapping
        self.label = customtkinter.CTkLabel(
            self, 
            font=customtkinter.CTkFont(size=15), 
            text=label_text, 
            wraplength=280  # Wrap text at 280 pixels
        )
        self.label.pack(padx=20, pady=(10, 5))

        # Add the "Ok" button
        self.ok_button = customtkinter.CTkButton(self, text="Ok", command=self.close_dialog)
        self.ok_button.pack(pady=(5, 15))  # Adjusted padding for spacing

    def close_dialog(self):
        # Destroy the dialog safely
        self.after(100, self.destroy)  # Add a slight delay before destroying

    def update_content(self, title, label_text, largewindow=False):
        # Dynamically adjust window size based on updated text length or largewindow parameter
        if largewindow:
            self.geometry("300x400") 
        elif len(label_text) > 45:
            self.geometry("300x200")
        else:
            self.geometry("300x100")

        self.title(title)  # Update the window title
        self.label.configure(text=label_text)  # Update the label text