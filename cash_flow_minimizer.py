import tkinter as tk
from tkinter import messagebox, simpledialog
import pandas as pd

class CashFlowMinimizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cash Flow Minimizer")
        self.root.geometry("600x500")  # Initial window size

        # Initialize CashFlowMinimizer
        self.cash_flow_minimizer = CashFlowMinimizer()

        # Income Section
        tk.Label(root, text="Income", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=(10, 5), sticky='w')
        tk.Label(root, text="Amount:", anchor='w').grid(row=1, column=0, padx=10, sticky='w')
        tk.Label(root, text="Description:", anchor='w').grid(row=1, column=1, padx=10, sticky='w')
        
        self.income_amount_entry = tk.Entry(root)
        self.income_amount_entry.grid(row=2, column=0, padx=10, pady=5, sticky='ew')
        self.income_description_entry = tk.Entry(root)
        self.income_description_entry.grid(row=2, column=1, padx=10, pady=5, sticky='ew')
        
        tk.Button(root, text="Add Income", command=self.add_income).grid(row=3, column=0, columnspan=2, pady=10)

        # Expense Section
        tk.Label(root, text="Expenses", font=("Arial", 14)).grid(row=4, column=0, columnspan=2, pady=(10, 5), sticky='w')
        tk.Label(root, text="Amount:", anchor='w').grid(row=5, column=0, padx=10, sticky='w')
        tk.Label(root, text="Description:", anchor='w').grid(row=5, column=1, padx=10, sticky='w')
        
        self.expense_amount_entry = tk.Entry(root)
        self.expense_amount_entry.grid(row=6, column=0, padx=10, pady=5, sticky='ew')
        self.expense_description_entry = tk.Entry(root)
        self.expense_description_entry.grid(row=6, column=1, padx=10, pady=5, sticky='ew')
        
        tk.Button(root, text="Add Expense", command=self.add_expense).grid(row=7, column=0, columnspan=2, pady=10)

        # Report and Save Section
        tk.Button(root, text="Generate Report", command=self.generate_report).grid(row=8, column=0, pady=10, sticky='ew')
        tk.Button(root, text="Save Report", command=self.save_report).grid(row=8, column=1, pady=10, sticky='ew')

        # Income List Section
        tk.Label(root, text="Income List", font=("Arial", 12)).grid(row=9, column=0, pady=(10, 5), sticky='w')
        self.income_listbox = tk.Listbox(root, width=50, height=6)
        self.income_listbox.grid(row=10, column=0, pady=5, sticky='nsew')

        # Expense List Section
        tk.Label(root, text="Expense List", font=("Arial", 12)).grid(row=9, column=1, pady=(10, 5), sticky='w')
        self.expense_listbox = tk.Listbox(root, width=50, height=6)
        self.expense_listbox.grid(row=10, column=1, pady=5, sticky='nsew')

        # Results Section
        tk.Label(root, text="Report", font=("Arial", 12)).grid(row=11, column=0, columnspan=2, pady=(10, 5), sticky='w')
        self.results_text = tk.Text(root, height=10, wrap='word')
        self.results_text.grid(row=12, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Configure column and row weights for responsiveness
        root.grid_rowconfigure(10, weight=1)
        root.grid_rowconfigure(11, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def add_income(self):
        try:
            amount = float(self.income_amount_entry.get())
            description = self.income_description_entry.get().strip()
            if not description:
                raise ValueError("Description cannot be empty.")
            self.cash_flow_minimizer.add_income(amount, description)
            self.update_income_list()
            self.income_amount_entry.delete(0, tk.END)
            self.income_description_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def add_expense(self):
        try:
            amount = float(self.expense_amount_entry.get())
            description = self.expense_description_entry.get().strip()
            if not description:
                raise ValueError("Description cannot be empty.")
            self.cash_flow_minimizer.add_expense(amount, description)
            self.update_expense_list()
            self.expense_amount_entry.delete(0, tk.END)
            self.expense_description_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def update_income_list(self):
        self.income_listbox.delete(0, tk.END)
        for item in self.cash_flow_minimizer.income:
            self.income_listbox.insert(tk.END, f"${item['Amount']:.2f} - {item['Description']}")

    def update_expense_list(self):
        self.expense_listbox.delete(0, tk.END)
        for item in self.cash_flow_minimizer.expenses:
            self.expense_listbox.insert(tk.END, f"${item['Amount']:.2f} - {item['Description']}")

    def generate_report(self):
        report = self.cash_flow_minimizer.generate_report()
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, report)

    def save_report(self):
        filename = simpledialog.askstring("Save Report", "Enter the filename (e.g., 'cash_flow_report.csv'):")
        if filename:
            self.cash_flow_minimizer.save_report(filename)
            messagebox.showinfo("Save Report", f"Report saved to {filename}")
        else:
            messagebox.showwarning("Save Report", "Filename cannot be empty.")

class CashFlowMinimizer:
    def __init__(self):
        self.income = []
        self.expenses = []

    def add_income(self, amount, description):
        self.income.append({'Amount': amount, 'Description': description})

    def add_expense(self, amount, description):
        self.expenses.append({'Amount': amount, 'Description': description})

    def calculate_cash_flow(self):
        total_income = sum(item['Amount'] for item in self.income)
        total_expenses = sum(item['Amount'] for item in self.expenses)
        net_cash_flow = total_income - total_expenses
        return total_income, total_expenses, net_cash_flow

    def generate_report(self):
        total_income, total_expenses, net_cash_flow = self.calculate_cash_flow()
        report = f"Cash Flow Report\n"
        report += f"===================\n"
        report += f"Total Income: ${total_income:.2f}\n"
        report += f"Total Expenses: ${total_expenses:.2f}\n"
        report += f"Net Cash Flow: ${net_cash_flow:.2f}\n"
        
        if net_cash_flow < 0:
            report += "\nRecommendations:\n"
            report += "- Review and reduce discretionary expenses.\n"
            report += "- Look for ways to increase income, such as additional revenue streams.\n"
            report += "- Consider creating a budget plan to track and control spending.\n"
        elif net_cash_flow > 0:
            report += "\nYou have a positive cash flow!\n"
            report += "Consider investing the surplus or saving for future needs.\n"
        else:
            report += "\nYour cash flow is balanced.\n"
        
        return report

    def save_report(self, filename):
        total_income, total_expenses, net_cash_flow = self.calculate_cash_flow()
        
        data = {
            'Income': [item['Description'] + ": $" + str(item['Amount']) for item in self.income],
            'Expenses': [item['Description'] + ": $" + str(item['Amount']) for item in self.expenses]
        }
        df = pd.DataFrame(data)
        df.loc['Total'] = ['', f"Total Income: ${total_income:.2f}"]
        df.loc['Total'] = ['', f"Total Expenses: ${total_expenses:.2f}"]
        df.loc['Total'] = ['', f"Net Cash Flow: ${net_cash_flow:.2f}"]
        
        df.to_csv(filename, index=False)

if __name__ == "__main__":
    root = tk.Tk()
    app = CashFlowMinimizerGUI(root)
    root.mainloop()
