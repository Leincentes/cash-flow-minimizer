import tkinter as tk
from gui import CashFlowMinimizerGUI

def main():
    root = tk.Tk()
    app = CashFlowMinimizerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
