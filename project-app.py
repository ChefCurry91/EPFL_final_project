from flask import Flask, request
import os
from excel_file_handler import FileHandler
import datetime


# Joining Paths with os.path.join
# https://ioflood.com/blog/python-os-path/#:~:text=In%20this%20example%2C%20we're,to%20a%20user's%20documents%20directory.

# retrieving the user home directory
# https://www.tutorialspoint.com/How-to-find-the-real-user-home-directory-using-Python
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
file = 'expenses_data.txt'

my_file_handler= FileHandler(desktop_path,file)
my_file_handler.create_excel_sheet() 



app = Flask('project-app')


def get_html(page_name):
    path= '/Users/fabio/Documents/TCC/s18-project-app/templates'
    complete_path = os.path.join(path, page_name)
    html_file = open(complete_path + '.html')
    content = html_file.read()
    html_file.close()
    return content


@app.route('/')
def index_page():
    page = get_html('index')
    return page

@app.route('/posting-expenses', methods = ['POST', 'GET'])
def post_expenses():
    page = get_html('posting-expenses')

    # Retrieving HTML Form data using Flask
    # https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/

    amount = request.form.get('amount')
    expense= request.form.get('expense')
    date= request.form.get('date')

    

    
    
    currency_payment = request.form.get('currency-payment')
    #currency_conversion= request.form.get('currency-conversion')
    


    if request.method == 'POST':
        #amount= round(float(amount), 2)

        try:
            amount= round(float(amount), 2)
            converted_amount= my_file_handler.get_payment_converted(currency_payment,amount,date)
        
        except:
            amount=100
            converted_amount= my_file_handler.get_payment_converted(currency_payment,amount,date)
            

        # Parse the date string to datetime object
        # https://www.datacamp.com/tutorial/converting-strings-datetime-objects
        parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d")

        # Format the date in the desired format (DD-MM-YYYY)
        # https://pynative.com/python-datetime-format-strftime/#h-how-to-format-date-and-time-in-python
        formatted_date = parsed_date.strftime("%d-%m-%Y")

        # capitalize only the first letter
        expense= expense.capitalize()


        # populating the dictonnary with input we get from the form.
        dict_expense = {
            'expense':expense,
            'date':formatted_date,
            'currency_payment':currency_payment,
            'amount':amount,
            'amount_CHF':converted_amount
        }

        my_file_handler.add_data_to_excel_sheet(dict_expense)
        #my_file_handler.add_data_in_txt_file(expense,date,currency_payment,amount,converted_amount)
        my_file_handler.add_data_to_txt_file(dict_expense, file)

       
    return page



@app.route('/tracking-expenses')
def track_expenses():
    page= get_html('tracking-expenses')
    return page



