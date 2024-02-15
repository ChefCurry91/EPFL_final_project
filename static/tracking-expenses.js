{/* variable related to input of type button, "Show Expenses" */}

const showExpensesButton = document.getElementById('submit-button-excel-sheet-tracking');

{/* variable related to input of type button, "Clear All Data" */}

const clearAllData = document.getElementById('submit-button-clear-inputs');

{/* variable related to input of type button, "Clear Sheet" */}

const deleteFileButton = document.getElementById('submit-button-delete-file');

{/* variable related to Form element, */}

const form = document.getElementById('form-for-selecting-sheet');

/* This function is designed to prevent the selection of no sheet, which could potentially lead to an internal error. */

const preventFalseValue = (event) => {
   let clearAllInputs = document.getElementById('dropdown-excel-sheets-tracking-expenses').value;
   
   if (clearAllInputs === "---Select Your Excel Sheet---") {
        event.preventDefault();
        alert('Please Select a Sheet');
    }
      
}
   
form.addEventListener('submit', preventFalseValue);