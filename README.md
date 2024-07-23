# Cash Flow Minimizer

A simple Python application to help manage and minimize cash flow by tracking income and expenses. This application uses a graphical user interface (GUI) built with Tkinter, and it saves reports in CSV format for easy analysis.

## Features

- Add and track income and expenses
- Generate a detailed cash flow report
- Save the report to a CSV file
- Display income and expense lists within the application
- Responsive GUI that adjusts to different window sizes

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- pandas (install with `pip install pandas`)

## Installation

1. Clone the repository or download the source code.
2. Make sure you have Python 3 installed on your system.
3. Install the required packages using pip:

   ```sh
   pip install pandas

## Usage

1. Run the application:
```sh
python cash_flow_minimizer.py
```
2. The GUI will open with sections to add income and expenses. Enter the amount and description for each and click the respective button to add them.
3. Click Generate Report to view a summary of your cash flow.
4. Click Save Report to save the report as a CSV file. You will be prompted to enter a filename.

## GUI Layout

- Income Section: Allows you to add income with an amount and description.
- Expenses Section: Allows you to add expenses with an amount and description.
- Report and Save Section: Provides buttons to generate and save the cash flow report.
- Income List: Displays a list of all recorded incomes.
- Expense List: Displays a list of all recorded expenses.
- Report Area: Shows the generated cash flow report.

## Code Overview

`CashFlowMinimizer`
This class handles the core logic of tracking income and expenses, calculating cash flow, generating reports, and saving them to CSV.

`CashFlowMinimizerGUI`
This class creates the Tkinter GUI, handles user input, and displays results.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
You can save this content into a file named `README.md` in your project's root directory.
