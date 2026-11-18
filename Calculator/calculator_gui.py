
import tkinter as tk
import ast
import operator

# Safe mathematical operations
operations = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def safe_calculate(expression):
    def calculate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in operations:
            return operations[type(node.op)](
                calculate(node.left),
                calculate(node.right)
            )

        if isinstance(node, ast.UnaryOp) and type(node.op) in operations:
            return operations[type(node.op)](calculate(node.operand))

        raise ValueError("Invalid expression")

    tree = ast.parse(expression, mode="eval")
    return calculate(tree.body)


# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("360x570")
root.resizable(False, False)
root.configure(bg="#F7F7F7")

expression = tk.StringVar()
result = tk.StringVar()

# Display
display = tk.Entry(
    root,
    textvariable=expression,
    font=("Arial", 28),
    justify="right",
    bd=0,
    bg="#F7F7F7"
)
display.pack(fill="x", padx=20, pady=(55, 15), ipady=10)

result_label = tk.Label(
    root,
    textvariable=result,
    font=("Arial", 18),
    fg="gray",
    bg="#F7F7F7",
    anchor="e"
)
result_label.pack(fill="x", padx=20, pady=(0, 35))


def update_result():
    exp = expression.get()

    try:
        if exp and exp[-1] not in "+-*/.":
            answer = safe_calculate(exp)
            result.set(str(answer))
        else:
            result.set("")
    except Exception:
        result.set("")


def press(value):
    expression.set(expression.get() + value)
    update_result()


def clear():
    expression.set("")
    result.set("")


def backspace():
    expression.set(expression.get()[:-1])
    update_result()


def percentage():
    if expression.get():
        expression.set(expression.get() + "/100")
        update_result()


def parentheses():
    exp = expression.get()
    if exp.count("(") > exp.count(")"):
        press(")")
    else:
        press("(")


def calculate():
    try:
        answer = safe_calculate(expression.get())
        expression.set(str(answer))
        result.set("")
    except Exception:
        result.set("Error")


# Button layout
buttons = [
    ["C", "⌫", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["()", "0", ".", "="]
]

button_frame = tk.Frame(root, bg="#F7F7F7")
button_frame.pack(expand=True, fill="both", padx=12, pady=5)

for r, row in enumerate(buttons):
    for c, value in enumerate(row):

        if value == "=":
            command = calculate
            bg = "#20B477"
            fg = "white"
        elif value == "C":
            command = clear
            bg = "white"
            fg = "#D65A5A"
        elif value == "⌫":
            command = backspace
            bg = "white"
            fg = "#D65A5A"
        elif value == "%":
            command = percentage
            bg = "white"
            fg = "#333333"
        elif value == "()":
            command = parentheses
            bg = "white"
            fg = "#333333"
        elif value in ["÷", "×", "−", "+"]:
            symbol = {"÷": "/", "×": "*", "−": "-"}
            command = lambda v=value: press(symbol.get(v, v))
            bg = "#E5E5E5"
            fg = "#333333"
        else:
            command = lambda v=value: press(v)
            bg = "white"
            fg = "#222222"

        button = tk.Button(
            button_frame,
            text=value,
            command=command,
            font=("Arial", 20),
            bg=bg,
            fg=fg,
            bd=0,
            activebackground="#D8D8D8",
            relief="flat"
        )

        button.grid(
            row=r,
            column=c,
            sticky="nsew",
            padx=5,
            pady=5
        )

for r in range(5):
    button_frame.rowconfigure(r, weight=1)

for c in range(4):
    button_frame.columnconfigure(c, weight=1)

root.mainloop()
