from flask import Flask, request
import os
from excel_file_handler import FileHandler
from data_title_column_excel import dict_data_title_column
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

        # Add input to txt file
        my_file_handler.add_data_to_txt_file(dict_expense, file)
        # Get input from txt file as two dimensional array
        array_expenses = my_file_handler.get_data_added_to_txt_file()
        # Count the number of row for the two dimensional array
        number_of_rows = len(array_expenses)
       
       
        # Only if the two dimensional array "array_expenses" as one single row
        # call function create_excel_sheet() 

        if number_of_rows == 1:
            my_file_handler.create_excel_sheet()
            my_file_handler.add_data_to_excel_sheet(dict_expense)

        # if two dimensional array "array_expenses" has more than one row
        # do not call function create_excel_sheet 
        else:
            my_file_handler.add_data_to_excel_sheet(dict_expense)

       
    return page



@app.route('/tracking-expenses', methods = ['POST', 'GET'])
def track_expenses():
    page= get_html('tracking-expenses')

    if request.method == 'POST':
        my_file_handler.clear_all_data_txt_file()
        my_file_handler.clear_all_data_excel_sheet()

    array_expenses = my_file_handler.get_data_added_to_txt_file()
    
    actual_values=''

    
    label_list = ['Expense', 'Date', 'Currency','Payment', 'Payment CHF' ]
    

    aggregate_expense_in_CHF = 0
    total_amount_in_CHF= 0
    total_amount_in_EUR = 0
    total_amount_in_GBP = 0
    total_amount_in_USD=0
    

    for count, inner_array in enumerate(array_expenses):

        actual_values+='<div class="container-per-expense">'
        
        if count == 0:
            index_label_list=0
            for element in inner_array:

                

                current_label =label_list[index_label_list]

                actual_values += f'<div id="container-label-title"><h4 id="label-{index_label_list}">{current_label}</h4><p id="value-{index_label_list}">{element}</p></div>'
                
                if current_label == 'Payment CHF':
                    aggregate_expense_in_CHF+= round(float(element),2)
                

                elif current_label == 'Currency' and element == 'CHF':
                    total_amount_in_CHF+= round(float(inner_array[3]),2)

                elif current_label == 'Currency' and element == 'EUR':
                    total_amount_in_EUR+= round(float(inner_array[3]),2)

                elif current_label == 'Currency' and element == 'GBP':
                    total_amount_in_GBP+= round(float(inner_array[3]),2)
                
                elif current_label == 'Currency' and element == 'USD':
                    total_amount_in_USD+= round(float(inner_array[3]),2)
                
                
                index_label_list+=1
            
            actual_values+='</div>'
        

        else:
            index = 0
            
            for element in inner_array:
                
                current_label =label_list[index]

                actual_values += f'<div class="values"><span>{element}</span></div>'
                
                if current_label == 'Payment CHF':
                    aggregate_expense_in_CHF+=round(float(element),2)

                elif current_label == 'Currency' and element == 'CHF':
                    total_amount_in_CHF+= round(float(inner_array[3]),2)
                
                elif current_label == 'Currency' and element == 'EUR':
                    total_amount_in_EUR+= round(float(inner_array[3]),2)
                
                elif current_label == 'Currency' and element == 'GBP':
                    total_amount_in_GBP+= round(float(inner_array[3]),2)
                
                elif current_label == 'Currency' and element == 'USD':
                    total_amount_in_USD+= round(float(inner_array[3]),2)
                
                index+= 1
            actual_values+='</div>'
    
    actual_values += '<div id="message-img-we-get-you-cover"><p id="get-you-cover-message">Like a Good Buddy, It Get You Covered</p><img id="img-tracking-expense-page" src ="./static/friendship.svg" alt="people-hanging-out"></div>'
    actual_values += '<div class ="container-aggregate-expenses">'
    actual_values += '<p id="total-payment-owerview">Total Payments Overview</p>'
    actual_values += f'<div class="aggregate-expenses-CHF"><label class="label-agreggate-expenses">Aggregate Expenses in CHF: </label> <p class="total-amount-expenses">{aggregate_expense_in_CHF}</p></div>'
    actual_values += f'<div class="aggregate-expenses"><label class="label-agreggate-expenses">Total Payments CHF: </label> <p class="total-amount-expenses"> {total_amount_in_CHF}</p></div>'
    actual_values += f'<div class="aggregate-expenses"><label class="label-agreggate-expenses">Total Payments €: </label> <p class="total-amount-expenses"> {total_amount_in_EUR}</p></div>'
    actual_values += f'<div class="aggregate-expenses"><label class="label-agreggate-expenses">Total Payments £:</label> <p class="total-amount-expenses"> {total_amount_in_GBP}</p></div>'
    actual_values += f'<div class="aggregate-expenses"><label class="label-agreggate-expenses">Total Payments $: </label> <p class="total-amount-expenses"> {total_amount_in_USD}</p></div>'
    actual_values += '</div>'
    print('Sum total expenses in CHF:', aggregate_expense_in_CHF)

    
    return page.replace('<p>Track expenses</p>',actual_values)





