from flask import Flask, request
from openpyxl import Workbook,load_workbook
from openpyxl.styles import Font 
import os, datetime
import requests


class File():

    # For excel sheet manipulation, I relied on the following source:
    # Automate the Boring Stuff with Python: Practical Programming for Total Beginners by AI Sweighart
    # https://automatetheboringstuff.com/2e/chapter13/

    def create_excel_sheet(self):

        # Joining Paths with os.path.join
        # https://ioflood.com/blog/python-os-path/#:~:text=In%20this%20example%2C%20we're,to%20a%20user's%20documents%20directory.
        
        # retrieving the user home directory
        # https://www.tutorialspoint.com/How-to-find-the-real-user-home-directory-using-Python

        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')


        wb = Workbook()

        # Get the active sheet (or specify a specific sheet if needed)
        sheet = wb.active

        # To customize font styles in cells,
        # import the Font() function from the openpyxl.styles module.
        
        # Create a font.
        bold16Font = Font(size=16, bold=True, italic=True) 

        letters_column_excel = 'ABCDEF'

        # Assign same font to A1:F1 cells
        
        for letter in letters_column_excel:
            sheet[letter +'1'].font=bold16Font
            # Assign same dimension to each column in row 1
            sheet.column_dimensions[letter].width =  35
        
            
        sheet['A1'] = 'Expense'
        sheet['B1'] = 'Date of Payment'
        sheet['C1'] = 'Currency Payment'
        sheet['D1'] = 'Original Amount'
        sheet['E1'] = 'Amount in CHF'
        sheet['F1'] = 'Total Amount in CHF'

        file_name = 'expenses.xlsx'
        file_path = os.path.join(desktop_path, file_name)

        # save operation applied to excell workbook
        wb.save(file_path)
        return file_path
    

    
    def get_payment_converted(self, currency_payment, amount, date_exchange_rate):
        
        # I relied on the documentation from the following web pages to use the Frankfurter API:

        # https://www.frankfurter.app/docs/#conversion
        # https://publicapis.io/frankfurter-api
        

        host = 'api.frankfurter.app'

        #url = f'https://{host}/{date_exchange_rate}?amount={amount}&from={currency_payment}&to={currency_conversion}'
        

        if currency_payment!='CHF':
            url = f'https://{host}/{date_exchange_rate}?amount={amount}&from={currency_payment}&to=CHF'

            # Send GET request to fetch conversion data:
            # https://www.geeksforgeeks.org/response-json-python-requests/
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                # Access elements of a Nested Dictionary:
                # https://www.programiz.com/python-programming/nested-dictionary
                converted_amount = data['rates']['CHF']
                print(f"{amount} {currency_payment} = {converted_amount} CHF at {date_exchange_rate}")
                return converted_amount
        else:
            return amount
    

    def add_data_to_excel(self,data_expense):
        
        # Joining Paths with os.path.join
        # https://ioflood.com/blog/python-os-path/#:~:text=In%20this%20example%2C%20we're,to%20a%20user's%20documents%20directory.
        
        # retrieving the user home directory
        # https://www.tutorialspoint.com/How-to-find-the-real-user-home-directory-using-Python
        
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        file_name = 'expenses.xlsx'
        file_path = os.path.join(desktop_path, file_name)

        # For excel sheet manipulation, I relied on the following source:
        # Automate the Boring Stuff with Python: Practical Programming for Total Beginners by AI Sweighart
        # https://automatetheboringstuff.com/2e/chapter13/

        # Opening Excel Documents with OpenPyXL
        wb = load_workbook(file_path)
        
        # Get the active sheet (or specify a specific sheet if needed)
        sheet = wb.active
        
        # sheet.max_row => get the maximum number of occupied rows 
        target_row = sheet.max_row + 1
        column_index= 1

        # Flag first row 
        skip_first_row = True 

        error_message = 'Please Fill All Fields In'
        
        try:
            # Iterating through the dictionary 'data_expense',
            # which is initially populated upon clicking the "post" button
            # within the @app.route('/posting-expenses') endpoint
            # https://realpython.com/iterate-through-dictionary-python/

            for key,value in data_expense.items():
               
                # Considering that only cells from A1 to F1 are currently occupied,
                # and no cells in row 2 contain assigned values. As a result,
                # sheet.max_row is equal to 1, and the "target_row" variable is set to 2.

                # The variable "column_index" represents columns: 
                # "column_index" = 1 corresponds to the first column,
                # "column_index" = 2 corresponds to the second column on the spreadsheet.
                
                # When traversing dictionnary, we assign for next available row in this case row "2" 
                # and for each column from A to F (because they are 6 key-value pairs) the value stored 
                # in variable "value" to the corresponding cell. 
                # First key-value pair => cell A2, second key-value pair => B2

                # While traversing the dictionary, we assign values to the next available row,
                # in this case, row 2. For each column from A to F (due to 6 key-value pairs),
                # the value stored in the variable "value" is assigned to the corresponding cell.
                # For example, the first key-value pair corresponds to cell A2, the second to B2, and so forth.

                sheet.cell(row=target_row, column=column_index).value = value
                # While the row remains unchanged, the column_index increments,
                # enabling movement to the next column while remaining on the same row
                column_index+=1


               # The subsequent code executes exclusively when the dictionary key corresponds to "amount_CHF".

                # The concept is that upon encountering the key "amount_CHF" in the last column, which is column F,
                # the script sums all the existing amounts present in column "E".
                if key == 'amount_CHF':

                    total_amount= 0

                    # While continuing through the dictionary, we've reached the final key-value pair,
                    # which corresponds to column "F". To aggregate all the amounts from column "E",
                    # we need to navigate or "move back" to column "E".
                   
                    column_E = column_index-1 

                    # Loop through every row in column "E"
                    # https://copyprogramming.com/howto/openpyxl-loop-through-rows-and-columns
                    for cell in sheet.iter_rows(min_col=column_E, max_col=column_E):
                        for row in cell:
                            
                             #Setting the variable "skip_first_row" to "True" ensures that during the initial iteration,
                            # we skip writing data to the first row of column "E", which contains the column title.

                            if skip_first_row:
                                skip_first_row=False


                           # While iterating through column "E" (representing different rows), 
                            # we retrieve the value assigned to each cell. 
                            # The retrieved value is then added to the cumulative total obtained from previous calculations  
                            else:
                                total_amount+=float(row.value)
                                
                                # Subsequently, we assign the total amount to the cell in the next available row of column F.

                                sheet.cell(row=target_row, column=column_index).value = total_amount

                    
            print(total_amount)
            wb.save(file_path)
            return total_amount
        
        except:
            return 