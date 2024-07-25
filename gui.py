import tkinter as tk
from tkinter import messagebox, simpledialog
from cash_flow_minimizer import CashFlowMinimizer

class CashFlowMinimizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cash Flow Minimizer")
        self.root.attributes("-fullscreen", True)
        self.root.resizable(False, False)

        self.cash_flow_minimizer = CashFlowMinimizer()

        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Income Section Frame
        income_frame = tk.LabelFrame(main_frame, text="Income", font=("Arial", 14), padx=10, pady=10)
        income_frame.grid(row=0, column=0, sticky='ew')
        
        tk.Label(income_frame, text="Amount:", anchor='w').grid(row=0, column=0, padx=10, sticky='w')
        tk.Label(income_frame, text="Description:", anchor='w').grid(row=0, column=1, padx=10, sticky='w')
        
        self.income_amount_entry = tk.Entry(income_frame)
        self.income_amount_entry.grid(row=1, column=0, padx=10, pady=5, sticky='ew')
        self.income_description_entry = tk.Entry(income_frame)
        self.income_description_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')
        
        tk.Button(income_frame, text="Add Income", command=self.add_income).grid(row=2, column=0, columnspan=2, pady=10, sticky='ew')

        # Expense Section Frame
        expense_frame = tk.LabelFrame(main_frame, text="Expenses", font=("Arial", 14), padx=10, pady=10)
        expense_frame.grid(row=1, column=0, sticky='ew')
        
        tk.Label(expense_frame, text="Amount:", anchor='w').grid(row=0, column=0, padx=10, sticky='w')
        tk.Label(expense_frame, text="Description:", anchor='w').grid(row=0, column=1, padx=10, sticky='w')
        
        self.expense_amount_entry = tk.Entry(expense_frame)
        self.expense_amount_entry.grid(row=1, column=0, padx=10, pady=5, sticky='ew')
        self.expense_description_entry = tk.Entry(expense_frame)
        self.expense_description_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')
        
        tk.Button(expense_frame, text="Add Expense", command=self.add_expense).grid(row=2, column=0, columnspan=2, pady=10, sticky='ew')

        # Budget Section Frame
        budget_frame = tk.LabelFrame(main_frame, text="Set Budget Limit", font=("Arial", 12), padx=10, pady=10)
        budget_frame.grid(row=2, column=0, sticky='ew')
        
        self.budget_limit_entry = tk.Entry(budget_frame)
        self.budget_limit_entry.grid(row=0, column=0, padx=10, pady=5, sticky='ew')
        tk.Button(budget_frame, text="Set Budget", command=self.set_budget_limit).grid(row=1, column=0, pady=10, sticky='ew')

        # Report and Save Section
        report_frame = tk.Frame(main_frame)
        report_frame.grid(row=3, column=0, pady=10, sticky='ew')

        tk.Button(report_frame, text="Generate Report", command=self.generate_report).pack(side='left', padx=5)
        tk.Button(report_frame, text="Save Report", command=self.save_report).pack(side='left', padx=5)
        tk.Button(report_frame, text="Show All Income and Expenses", command=self.show_all).pack(side='left', padx=5)
        tk.Button(report_frame, text="Plot Graphs", command=self.plot_graphs).pack(side='left', padx=5)

        # Results Section
        results_frame = tk.LabelFrame(main_frame, text="Report", font=("Arial", 12), padx=10, pady=10)
        results_frame.grid(row=4, column=0, pady=10, sticky='nsew')

        self.results_text = tk.Text(results_frame, wrap='word')
        self.results_text.pack(fill='both', expand=True)
        self.results_text.config(height=12)  # Set height to adjust to space

        # Income and Expense Listboxes
        listbox_frame = tk.Frame(main_frame)
        listbox_frame.grid(row=0, column=1, rowspan=5, padx=10, pady=10, sticky='ns')

        tk.Label(listbox_frame, text="Income List", font=("Arial", 12)).pack(pady=(10, 5), anchor='w')
        self.income_listbox = tk.Listbox(listbox_frame, width=40, height=15)
        self.income_listbox.pack(fill='both', expand=True)

        tk.Label(listbox_frame, text="Expense List", font=("Arial", 12)).pack(pady=(10, 5), anchor='w')
        self.expense_listbox = tk.Listbox(listbox_frame, width=40, height=15)
        self.expense_listbox.pack(fill='both', expand=True)

        # Configure row and column weights
        for i in range(5):
            main_frame.grid_rowconfigure(i, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

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

    def set_budget_limit(self):
        try:
            limit = float(self.budget_limit_entry.get())
            self.cash_flow_minimizer.set_budget_limit(limit)
            self.budget_limit_entry.delete(0, tk.END)
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
            file_format = simpledialog.askstring("Save Report", "Enter format (csv, excel, pdf):")
            if file_format in ['csv', 'excel', 'pdf']:
                self.cash_flow_minimizer.save_report(filename, format=file_format)
                messagebox.showinfo("Save Report", f"Report saved to {filename}")
            else:
                messagebox.showwarning("Save Report", "Invalid format selected.")
        else:
            messagebox.showwarning("Save Report", "Filename cannot be empty.")

    def plot_graphs(self):
        self.cash_flow_minimizer.plot_graphs()

    def show_all(self):
        # Create a new window to show all income and expenses
        all_window = tk.Toplevel(self.root)
        all_window.title("All Income and Expenses")
        all_window.attributes("-fullscreen", True)  # Set full-screen mode
        all_window.resizable(False, False)  # Disable resizing

        # Create text widgets to display all income and expenses
        all_frame = tk.Frame(all_window)
        all_frame.pack(fill='both', expand=True, padx=10, pady=10)

        tk.Label(all_frame, text="All Income", font=("Arial", 12)).pack(pady=(10, 5), anchor='w')
        income_text = tk.Text(all_frame, wrap='word')
        income_text.pack(fill='both', expand=True)
        
        tk.Label(all_frame, text="All Expenses", font=("Arial", 12)).pack(pady=(10, 5), anchor='w')
        expense_text = tk.Text(all_frame, wrap='word')
        expense_text.pack(fill='both', expand=True)
        
        # Populate the text widgets with all income and expenses
        income_text.insert(tk.END, "Income:\n")
        for item in self.cash_flow_minimizer.income:
            income_text.insert(tk.END, f"${item['Amount']:.2f} - {item['Description']}\n")
        
        expense_text.insert(tk.END, "Expenses:\n")
        for item in self.cash_flow_minimizer.expenses:
            expense_text.insert(tk.END, f"${item['Amount']:.2f} - {item['Description']}\n")

