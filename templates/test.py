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
    label_list = list(dict_data_title_column.values())
    

    
   # for key,value in my_dict.items():
    #    my_dict[key]=0
    #    print(my_dict)
    #my_dict['key1'] = '<div class="hello"><h5>colonne1</h5><h5>colone2</h5>'
    

    #for count, inner_array in enumerate(array_expenses_to_be_modified):

     #   if isinstance(inner_array,dict):
      #      for label, value in inner_array.items():
      #          actual_values += f'<div class="div-label-element"><h5>{label}</h5><span>{value}</span></div>'
                

        
      #  else:
            #for element in inner_array:
       #     actual_values += f'<div class="div-label-element">{inner_array}</div>'


            

        




   # for count, inner_array in enumerate(array_expenses):
        
     #   if count == 0:
            
     #       index_label_list= 0
        
     #       for element in inner_array:
      #          current_label =label_list[index_label_list]
#
      #          actual_values += f'<div class="div-label-element"><h5>{current_label}</h5><span>{element}</span></div>'

      #          index_label_list+=1
                #actual_values += '</div>'
        
       # else:

       #     for element in inner_array:
                #current_label =label_list[index_label_list]

        #        actual_values += f'<div class="div"><span>{element}</span></div>'

          #      #index_label_list+=1
           #     #actual_values += '</div>'



                
            


            

    for inner_array in array_expenses:
        
        index_label_list= 0
        
        actual_value='<div class="div">'
        for element in inner_array:

            
            current_label =label_list[index_label_list]

            
            actual_values += f'<div class="hello"><span>{current_label}: {element}</span></div>'
                #actual_values += f'<div class="div-label-value-{index_label_list}"><label class="label-tableau-tracking">{current_label}:</label> <span>{element}</span></div>'
                #actual_values += f'<div id="div-label-value-{index_label_list}"><span>{element}</span></div>'
            
            
            
            index_label_list+=1
        actual_values += '</div>'
            


    
    return page.replace('<p>Track expenses</p>',actual_values)



   # if array_expenses:
    #    for piece_of_data in array_expenses:
    #        array_per_payment= piece_of_data.split()
    

    
   # else:
    #    return page