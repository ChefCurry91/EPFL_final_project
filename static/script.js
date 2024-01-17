
{/* variable related to form button "Post It" located in posting-expenses page  */}

const postButton = document.getElementById('post-button');


const inputTextExpenses = document.getElementById('expense-to-post');
//const selectOptionCurrency = document.getElementById('list-currency');
//const inputTextDate = document.getElementById('date-to-post');
//const inputTextAmount = document.getElementById('amount-to-post');

const content = document.getElementById('tableau-expenses');
const div = document.getElementById('div-label-value');

//const arrayInputUser = [inputTextExpenses]
//const arrayInputUser = [inputTextExpenses,selectOptionCurrency,inputTextDate,inputTextAmount];
//console.log(arrayInputUser)

{/* each variable is related to a div representing a column, each column containing a piece of information */}

const contentExpensesColumn = document.getElementById('column-expenses-name');
//onst contentDateColumn = document.getElementById('column-payment-date');
//const contentPaymentCurrencyColumn = document.getElementById('column-payment-currency');
//const contentOriginalAmountColumn = document.getElementById('column-original-amount');
/* const contentAmountCHFColumn = document.getElementById('column-amount-CHF'); */

const arrayContentToBeAdded = [contentExpensesColumn]
console.log(arrayContentToBeAdded)
//const arrayContentToBeAdded = [contentExpensesColumn, contentDateColumn, contentPaymentCurrencyColumn, contentOriginalAmountColumn];


const addExpensesData = () => {

    for (let index = 0; index <arrayContentToBeAdded.length; index++) {
        const newElement = document.createElement('p');
        console.log(newElement);
        const inputUser = arrayInputUser[index];
        console.log(inputUser);
        console.log(arrayContentToBeAdded)
        newElement.innerText = inputUser.value;
        arrayContentToBeAdded[index].appendChild(newElement)
       // content.appendChild(newElement);
    }
};

