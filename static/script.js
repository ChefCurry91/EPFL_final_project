
{/* variable related to form button "Post It" located in posting-expenses page  */}

const postButton = document.getElementById('post-button');






const checkPreventEmptyValues = (event) => {
    
    var expense = document.getElementById('expense-to-post').value;
    var amount = document.getElementById('amount-to-post').value;
    var currencyPayment = document.getElementById('list-currency').value;
    var date = document.getElementById('date-to-post').value;

    // Check if any field is empty or for currency payment that one the option is selected
    if (!expense.trim() || !amount.trim() || !date.trim() || currencyPayment === "---Choose Currency Payment---" ) {
        // Prevent form submission
        event.preventDefault();
        alert('Please fill in all required fields.');
     }

     else if (isNaN(amount) ) {
        event.preventDefault();
        alert('Please fill in the field with a valid number regarding the amount.');
        
     }
};




postButton.addEventListener('click',checkPreventEmptyValues)

