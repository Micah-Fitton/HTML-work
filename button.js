// Function to create a new button
function createNewButton() {
  // Create new button
  let newButton = document.createElement("button")
  newButton.innerHTML= 'new button'
  document.body.appendChild(newButton)
  console.log("createNewButton");
  if (Math.random() < 0.5 ) {
    newButton.innerHTML = "Delete?"
    newButton.addEventListener("click", createNewButton)
  } else {
    newButton.innerHTML = "Create?"
    newButton.addEventListener("click", function () {
      buttons = buttons.filter((button) => button !== this);
      
    this.remove();
    })
    
  }
}

// Initial button
let initialButton = document.createElement("button");
initialButton.innerHTML = "First";
document.body.appendChild(initialButton);

function createDiv(){

  const div = document.createElement('div');
  div.style.backgroundColor = 'red';
  div.style.width = "200px";
  div.style.height= '100px'; 

  text.innerHTML("Hello baby")
  document.body.appendChild(text)
  document.body.appendChild(div);
} 

// Array to store the buttons
let buttons = [initialButton];

initialButton.addEventListener("click", createNewButton);
