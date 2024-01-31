
{/* variable related to form button "Post It" located in posting-expenses page  */}

const postButton = document.getElementById('post-button');

{/* Function aiming to prevent empty values and non-numerical values for input box in Form */}

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

// Get the modal
var modal = document.getElementById("modal-index-page");

// Get the button that opens the modal
var btn = document.getElementById("create-new-excel-sheet");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close-modal")[0];


// When the user clicks on the button, open the modal
btn.onclick = () => {
   modal.style.display = "block";
 }

 // When the user clicks on <span> (x), close the modal
span.onclick = () => {
   modal.style.display = "none";
 }

 // When the user clicks anywhere outside of the modal, close it
window.onclick = (event) => {
   if (event.target == modal) {
     modal.style.display = "none";
   }
 }



postButton.addEventListener('click',checkPreventEmptyValues);



// variable related to select tag located in tracking-expenses page 

const selectSheetTrackingExpenses = document.getElementById('dropdown-excel-sheets-tracking-expenses');

// Variable related to form tag located in tracking-expenses page to select the sheet
const formSelectSheetTrackingExpenses = document.getElementById('form-for-selecting-sheet');

selectSheetTrackingExpenses.addEventListener('change', () => {
   formSelectSheetTrackingExpenses.submit();
});
