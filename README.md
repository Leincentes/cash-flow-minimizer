# Cash Flow Minimizer

A comprehensive Python application for managing and minimizing cash flow by tracking income and expenses. This application features a full-screen graphical user interface (GUI) built with Tkinter and supports saving reports in multiple formats including CSV, Excel, and PDF.

## Features

- Add and track income and expenses with descriptions.
- Set and track a budget limit.
- Generate detailed cash flow reports.
- Save reports in CSV, Excel, or PDF formats.
- Display and manage income and expense lists.
- Full-screen, non-resizable, and responsive GUI that adapts to various screen sizes.
- Plot graphs to visualize income and expenses.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- pandas (install with `pip install pandas`)
- openpyxl (for Excel support; install with `pip install openpyxl`)
- matplotlib (for plotting graphs; install with `pip install matplotlib`)
- fpdf2 (for PDF support; install with `pip install fpdf2`)

## Installation

1. Clone the repository or download the source code.
2. Make sure you have Python 3 installed on your system.
3. Install the required packages using pip:

    ```sh
    pip install pandas openpyxl matplotlib fpdf2
    ```

## Usage

1. Run the application:

    ```sh
    python main.py
    ```

2. The GUI will open in full-screen mode. Use the sections to add income, expenses, and set a budget limit.
3. Click "Generate Report" to view a summary of your cash flow.
4. Click "Save Report" to save the report in CSV, Excel, or PDF format. You will be prompted to enter a filename and select the format.
5. Use the "Show All Income and Expenses" button to view all records in a separate window.
6. Click "Plot Graphs" to visualize your income and expenses.

## GUI Layout

- **Income Section:** Allows you to add income with an amount and description.
- **Expenses Section:** Allows you to add expenses with an amount and description.
- **Budget Section:** Set and track a budget limit.
- **Report and Save Section:** Provides buttons to generate and save the cash flow report.
- **Income List:** Displays a list of all recorded incomes.
- **Expense List:** Displays a list of all recorded expenses.
- **Report Area:** Shows the generated cash flow report.
- **Plot Section:** Button to plot graphs visualizing income and expenses.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
