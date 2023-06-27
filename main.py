import pandas as pd
from fpdf import FPDF

# Create a DataFrame with the chosen Excel file
df = pd.read_excel('invoices/10001-2023.1.18.xlsx')

# Create instance of the FPDF class
pdf = FPDF()

# Create page and set font with a title
pdf.add_page()
pdf.set_font(family='Helvetica', size=15)
# pdf.cell(w=0, txt='Invoice', border='B')

# Create table for the invoice
with pdf.table(width=190, col_widths=(40, 40, 40, 40, 30)) as table:
    table_headings = table.row()
    table_headings.cell('Product ID')
    table_headings.cell('Product Name')
    table_headings.cell('Amount Purchased')
    table_headings.cell('Price Per Unit')
    table_headings.cell('Total Price')

    # add data from the file into the table
    for index, data_row in df.iterrows():
        row = table.row()
        row.cell(str(data_row['product_id']))
        row.cell(str(data_row['product_name']))
        row.cell(str(data_row['amount_purchased']))
        row.cell(str(data_row['price_per_unit']))
        row.cell(str(data_row['total_price']))

pdf.output('test.pdf')
