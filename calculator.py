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
                    command=self.calculate
                )
                button.grid(row=row, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
            else:
                button = tk.Button(
                    window,
                    text=button_text,
                    font=("Arial", 16),
                    height=2,
                    command=lambda value=button_text: self.on_button_click(value)
                )
                button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
                col += 1
                if col > 3:
                    col = 0
                    row += 1
        # Configure grid resizing behavior
        for i in range(6): self.window.grid_rowconfigure(i, weight=1)
        for i in range(4): self.window.grid_columnconfigure(i, weight=1)
        
    def on_button_click(self, value):
        """Handle button press events."""
        if value == "C":
            self.clear()
            return
        if value in "+-*/":
            # Prevent starting with an operator or repeating them
            if not self.expression or self.expression[-1] in "+-*/":
                if self.expression and self.expression[-1] in "+-*/":
                    self.expression = self.expression[:-1] + value
                return
            self.expression += value
        elif value == ".":
            # Handle decimal point logic
            last_number = self.get_last_number()
            if "." not in last_number:
                if not self.expression or self.expression[-1] in "+-*/":
                    self.expression += "0."
                else:
                    self.expression += "."
        else:
            # Handle number input
            if self.expression == "0":
                self.expression = value
            else:
                self.expression += value

        self.update_display()
        
    def get_last_number(self):
        """Extract the last number from the current expression."""
        operators = "+-*/"
        last_number = ""
        for char in reversed(self.expression):
         if char in operators:
            break
        last_number = char + last_number
        return last_number
    
    def calculate(self):
        """Evaluate the current expression."""
        if not self.expression or self.expression[-1] in "+-*/":
            return

        try:
            # Use eval to compute the expression
            result = eval(self.expression)
            self.expression = str(result)
            self.update_display()
        except ZeroDivisionError:
            self.display.config(text="Error: Div by Zero")
            self.expression = ""
        except Exception:
            self.display.config(text="Error")
            self.expression = ""
    
    def clear(self):
        """Reset the calculator."""
        self.expression = ""
        self.update_display()
    
    def update_display(self):
        """Update the calculator screen."""
        self.display.config(text=self.expression if self.expression else "0")


if __name__ == "__main__":
    window = tk.Tk()
    app = CalculatorApp(window)
    window.mainloop()
        
        
        

