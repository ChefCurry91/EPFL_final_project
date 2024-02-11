const showExpensesButton = document.getElementById('submit-button-excel-sheet-tracking');
const clearAllData = document.getElementById('submit-button-clear-inputs')
const deleteFileButton = document.getElementById('submit-button-delete-file');

const form = document.getElementById('form-for-selecting-sheet')

const preventFalseValue = (event) => {
   let clearAllInputs = document.getElementById('dropdown-excel-sheets-tracking-expenses').value;
   
   if (clearAllInputs === "---Select Your Excel Sheet---") {
        event.preventDefault();
        alert('Please Select a Sheet');
    }
      
}
   
form.addEventListener('submit', preventFalseValue);