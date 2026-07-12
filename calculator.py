import tkinter as tk 
class CalculatorApp:
    """A simple GUI calculator application using tkinter."""
    def __init__(self, window):
        self.window = window
        self.window.title ("Python Calculator")
        self.window.geometry("320x420")
        self.window.resizable(False, False)
        # Stores the current mathematical expression
        self.expression = ""
        # Display label for showing numbers and results
        self.display = tk.Label(
            window,
            text="0",
            anchor="e",
            bg="white",
            fg="black",
            font=("Arial", 20),
            relief="sunken",
            bd=2,
            padx=10,
            height=2
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
        # Button layout definition
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            ".", "0", "C", "+",
            "="
        ]
        # Initialize buttons in the grid
        row , col = 1 , 0
        for button_text in buttons:
            if button_text == "=":
                button = tk.Button(
                    window,
                    text=button_text,
                    font=("Arial", 16),
                    height=2,
                    #command=self.calculate
                )
                button.grid(row=row, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
            else:
                button = tk.Button(
                    window,
                    text=button_text,
                    font=("Arial", 16),
                    height=2,
                    #command=lambda value=button_text: self.on_button_click(value)
                )
                button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
                col += 1
                if col > 3:
                    col = 0
                    row += 1
        # Configure grid resizing behavior
        for i in range(6): self.window.grid_rowconfigure(i, weight=1)
        for i in range(4): self.window.grid_columnconfigure(i, weight=1)


if __name__ == "__main__":
    window = tk.Tk()
    app = CalculatorApp(window)
    window.mainloop()
        
        
        

