import pandas as pd
from fpdf import FPDF
from glob import glob

# Bundle all Excel files in invoices directory
filenames = glob('invoices/*.xlsx')

# Create PDF from each Excel file
for filename in filenames:

    # Create a DataFrame with the chosen Excel file
    df = pd.read_excel(filename)

    # Create instance of the FPDF class
    pdf = FPDF()

    # Create page and set font with a title
    pdf.add_page()
    pdf.set_font(family='Helvetica', size=15)
    pdf.cell(w=0, txt='Customer Invoice', align='C')
    pdf.ln(15)

    # Create table for the invoice
    with pdf.table(width=190, col_widths=(40, 50, 50, 45, 30), text_align='CENTER') as table:
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

        total_row = table.row()
        total_row.cell('', colspan=3)
        total_row.cell('')
        total_row.cell('')
        total_row.cell('Total Due:')
        total_price = df['total_price'].sum()
        total_row.cell(str(total_price))

    pdf.output(f'PDFs/{filename[9:].strip(".xlsx")}.pdf')
