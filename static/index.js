
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


 // Functionality related to local storage


 // Variable related to the input box where the name is entered"
const userNameToAdd = document.getElementById('username-to-add');
// Variable related to the button used to submit the entered name
const buttonAddUserName = document.getElementById('button-add-username');
// Variable related to the div where the message "Welcome ${userName}" is displayed
const content = document.getElementById('content-to-add');
// Variable related to the div where the input box, button, and title message are displayed.
// This div will be removed once a value is added to local storage.
const contentToEnterUserName = document.getElementById('container-welcome-username');



{/* Function aiming:

      - To add Welcome username on front-end
      - Remove  message, inputbox and button where username is enterred and submitted
      - Storing value of key-value pair username: name in local storage */}
  
const addUserName = () => {

  // First display "Welcome Username" message on front-end
  const userName = document.createElement('p');
  userName.innerText = `Welcome ${userNameToAdd.value}`;
  userName.className = 'username-added';
  content.appendChild(userName);
             
  // Setting up key-value pair in local storage 
  localStorage.setItem('username', userNameToAdd.value);
             
  // Clearing inputbox after submitting username 
  userNameToAdd.value='';

  // Remove  message, inputbox and button where username is enterred and submitted */}
  contentToEnterUserName.remove();
}

{/* Function aiming to:
    
    - Get value from key-value pair stored in local storage
    - Display on Front-end value stored in local storage
    - Remove  message, inputbox and button where username is enterred and submitted */}
   
const getUsernameFromLocalStorage = () => {
    
  // Get value from key-value pair stored in local storage
  const localStorageValue = localStorage.getItem('username');
  
  // if value is equal to True, meaning it is stored in local storage, then
  // Display on front end Message Welcome username
  // Finally remove container with message inputbox and button
      
  
  if (localStorageValue) {
    const userName = document.createElement('p');
    userName.innerText = `Hey ${localStorageValue}, Great To See You ! `;
    userName.className = 'username-added-message';
    content.appendChild(userName);
  
    contentToEnterUserName.remove()

  
    return localStorageValue 
  }

}
  
getUsernameFromLocalStorage();
  
  
  
buttonAddUserName.addEventListener('click', addUserName);
