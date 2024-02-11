
{/* variable related to form button "Post It" located in posting-expenses page  */}

const postButton = document.getElementById('post-button');



// https://www.freecodecamp.org/news/javascript-date-now-how-to-get-the-current-date-in-javascript/
// Get current date in milliseconds
const today = Date.now(); 

const convertDateStringIntoMS = (dateString) => {
   //https://www.w3schools.com/jsref/jsref_gettime.asp

   // Create a new Date object using the date string
   const dateObject = new Date(dateString);
   // Get the date in milliseconds
   const milliseconds = dateObject.getTime();

   return milliseconds

}


{/* This function aims to prevent empty or non-numerical values in input boxes within a form, 
    and also ensures that a date earlier than the current day is selected. */}

const checkValues = (event) => {
    
   const expense = document.getElementById('expense-to-post').value;
   const amount = document.getElementById('amount-to-post').value;
   const currencyPayment = document.getElementById('list-currency').value;
   const date = document.getElementById('date-to-post').value;
   const excel_sheet_selected = document.getElementById('list-excel-sheet').value;

   const datePosted = convertDateStringIntoMS(date)
   

   // Verify if any field is empty, if a currency payment option is selected, or if an Excel sheet is selected
   if (!expense.trim() || !amount.trim() || !date.trim() || currencyPayment === "---Choose Currency Payment---" || excel_sheet_selected === "---Choose Excel Sheet---") {
         // Prevent form submission
      event.preventDefault();
      alert('Please fill in all required fields.');
   } else if (isNaN(amount) ) {
        event.preventDefault();
        alert('Please enter a valid number for the amount field.');
   } else if (datePosted > today) {
      event.preventDefault();
      alert('Please enter a date earlier than today.')
   }

};


 postButton.addEventListener('click',checkValues);


