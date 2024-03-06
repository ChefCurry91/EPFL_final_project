
// In order to create the modal, I relied on the following source:

// https://www.w3schools.com/howto/howto_css_modals.asp


// Get the modal
const modal = document.getElementById("modal-index-page");

// Get the button that opens the modal
const btn = document.getElementById("create-new-excel-sheet");

// Get the <span> element that closes the modal
const span = document.getElementsByClassName("close-modal")[0];


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

 
// Get the button responsible for submitting the name of the new Excel sheet to be created

const btnSubmitNewExcelSheet = document.getElementById("submit-new-name-sheet");

// This function aims to prevent the submission of names containing whitespace; 
// only a single string of characters is allowed

const checkNameExcelSheetToCreate = (event) => {
  
  const inputExcelSheetName = document.getElementById('input-sheet-name').value

  // Verify that only a single string of characters is allowed
  if (inputExcelSheetName.includes(' ')) {
    event.preventDefault();
    alert('Please provide a string of characters without spaces.');
  }

 }

 btnSubmitNewExcelSheet.addEventListener('click',checkNameExcelSheetToCreate)


 // Local storage


// Get the the inputbox the username is entered
const userNameToAdd = document.getElementById('username-to-add');

// Get the button used to submit username
const buttonAddUserName = document.getElementById('button-add-username');

// Get the div where where message is displayed
const content = document.getElementById('content-to-add');

// Get the div, where the input box, button, and title message are displayed.
// This div will be removed once a value is added to local storage.
const contentToEnterUserName = document.getElementById('container-welcome-username');



    // Function aiming at:
 
    //  - Adding a welcome message with the username on the front-end
    //  - Removing the message, input box, and button where the username is entered and submitted
    //  - Storing the value of the key-value pair 'username: name' in local storage 

const addUserName = () => {

  // First display "Welcome Username" message on front-end
  const userName = document.createElement('p');
  userName.innerText = `Welcome ${userNameToAdd.value} !`;
  userName.className = 'username-added-message';
  content.appendChild(userName);
             
  // Setting up key-value pair in local storage 
  localStorage.setItem('username', userNameToAdd.value);
             
  // Clearing inputbox after submitting username 
  userNameToAdd.value='';

  // Remove message, inputbox and button where username is enterred and submitted 
  contentToEnterUserName.remove();
}

{/* Function aiming to:
    
    - Get value from key-value pair stored in local storage
    - Display on Front-end value stored in local storage
    - Remove  message, inputbox and button where username is enterred and submitted */}
   
const getUsernameFromLocalStorage = () => {
    
  // Get value from key-value pair stored in local storage
  const localStorageValue = localStorage.getItem('username');
  


{/* If the value is equal to True, indicating it is stored in local storage, then
    Display on the front end message "Hey ${localStorageValue}, Great To See You!"
    Finally, remove the container with the message, input box, and button */}
      
  
  if (localStorageValue) {
    const userName = document.createElement('p');
    userName.innerText = `Hey ${localStorageValue}, Great To See You ! `;
    userName.className = 'username-added-message';
    content.appendChild(userName);
  
    contentToEnterUserName.remove();

    return localStorageValue; 
  }

 else {
    return;
  }
}


  
getUsernameFromLocalStorage();
  

buttonAddUserName.addEventListener('click', addUserName)
