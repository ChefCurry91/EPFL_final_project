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
    array_expenses = my_file_handler.get_data_added_to_txt_file()
    
    actual_values=''
    #actual_values ='<div class="transaction-item">Item'
    
    expense = array_expenses[0][0]
    payment_date = array_expenses[0][1]
    currency_payment = array_expenses[0][2]
    amount = float(array_expenses[0][3])
    amount_in_chf = float(array_expenses[0][4])

    transformed_dict = {
        'Expense': expense,
        'Date of Payment': payment_date,
        'Currency Payment': currency_payment,
        'Original Amount': amount,
        'Amount in CHF': amount_in_chf
    }

    #array_expenses_to_be_modified = array_expenses
    #removed_element = array_expenses_to_be_modified.pop(0)
    #array_expenses_to_be_modified.insert(0, transformed_dict)
 
    
    # Extract values from imported dictionary "dict_data_title_columnand" and create a list
   # label_list = list(dict_data_title_column.values())
    
    label_list = ['Expense', 'Date', 'Currency','Payment', 'Payment CHF' ]
    

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
                    total_amount_in_CHF+=float(element)

                elif current_label == 'Currency' and element == 'EUR':
                    total_amount_in_EUR+= float(inner_array[3])

                elif current_label == 'Currency' and element == 'GBP':
                    total_amount_in_GBP+= float(inner_array[3])
                
                elif current_label == 'Currency' and element == 'USD':
                    total_amount_in_USD+= float(inner_array[3])
                
                
                index_label_list+=1
            
            actual_values+='</div>'
        

        else:
            index = 0
            
            for element in inner_array:
                
                current_label =label_list[index]

                actual_values += f'<div class="values"><span>{element}</span></div>'
                
                if current_label == 'Payment CHF':
                    total_amount_in_CHF+=float(element)
                
                elif current_label == 'Currency' and element == 'EUR':
                    total_amount_in_EUR+= float(inner_array[3])
                
                elif current_label == 'Currency' and element == 'GBP':
                    total_amount_in_GBP+= float(inner_array[3])
                
                elif current_label == 'Currency' and element == 'USD':
                    total_amount_in_USD+= float(inner_array[3])
                
                index+= 1
            actual_values+='</div>'

    actual_values += f'<div class="aggregate-expenses"><p>Aggregate Expenses in CHF: {total_amount_in_CHF}</p></div>'
    actual_values += f'<div class="aggregate-expenses"><p>Aggregate Expenses in EUR: {total_amount_in_EUR}</p></div>'
    actual_values += f'<div class="aggregate-expenses"><p>Aggregate Expenses in GBP: {total_amount_in_GBP}</p></div>'
    actual_values += f'<div class="aggregate-expenses"><p>Aggregate Expenses in US: {total_amount_in_USD}</p></div>'

    print('Sum total expenses in CHF:', total_amount_in_CHF)

    
    return page.replace('<p>Track expenses</p>',actual_values)




    


    return page



