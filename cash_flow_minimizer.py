import pandas as pd
import matplotlib.pyplot as plt

class CashFlowMinimizer:
    def __init__(self):
        self.income = []
        self.expenses = []
        self.budget_limit = None

    def add_income(self, amount, description):
        self.income.append({'Amount': amount, 'Description': description})

    def add_expense(self, amount, description):
        self.expenses.append({'Amount': amount, 'Description': description})

    def set_budget_limit(self, limit):
        self.budget_limit = limit

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
        
        if self.budget_limit is not None:
            report += f"Budget Limit: ${self.budget_limit:.2f}\n"
            if net_cash_flow < 0:
                report += "You are over budget.\n"
            elif net_cash_flow < self.budget_limit:
                report += "You are within budget.\n"
            else:
                report += "You have exceeded your budget.\n"
        
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

    def save_report(self, filename, format='csv'):
        total_income, total_expenses, net_cash_flow = self.calculate_cash_flow()
        
        data = {
            'Income': [item['Description'] + ": $" + str(item['Amount']) for item in self.income],
            'Expenses': [item['Description'] + ": $" + str(item['Amount']) for item in self.expenses]
        }
        df = pd.DataFrame(data)
        df.loc['Total'] = ['', f"Total Income: ${total_income:.2f}"]
        df.loc['Total'] = ['', f"Total Expenses: ${total_expenses:.2f}"]
        df.loc['Total'] = ['', f"Net Cash Flow: ${net_cash_flow:.2f}"]
        
        if format == 'csv':
            df.to_csv(filename, index=False)
        elif format == 'excel':
            df.to_excel(filename, index=False)
        elif format == 'pdf':
            from fpdf import FPDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for line in df.to_string(index=False).split('\n'):
                pdf.cell(200, 10, txt=line, ln=True)
            pdf.output(filename)

    def plot_graphs(self):
        # Plot Income
        income_amounts = [item['Amount'] for item in self.income]
        income_descriptions = [item['Description'] for item in self.income]

        plt.figure(figsize=(10, 6))
        plt.barh(income_descriptions, income_amounts, color='green')
        plt.xlabel('Amount ($)')
        plt.title('Income Breakdown')
        plt.show()

        # Plot Expenses
        expense_amounts = [item['Amount'] for item in self.expenses]
        expense_descriptions = [item['Description'] for item in self.expenses]

        plt.figure(figsize=(10, 6))
        plt.barh(expense_descriptions, expense_amounts, color='red')
        plt.xlabel('Amount ($)')
        plt.title('Expense Breakdown')
        plt.show()
