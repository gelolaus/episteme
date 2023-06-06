const loginLink = document.getElementById('loginLink');
const registerLink1 = document.getElementById('registerLink1');
const registerLink2 = document.getElementById('registerLink2');
const loginDiv = document.getElementById('loginDiv');
const registerDiv = document.getElementById('registerDiv');

// Function to toggle visibility of login and register divs
function toggleDivVisibility(showDiv, hideDiv) {
    showDiv.style.display = 'block';
    hideDiv.style.display = 'none';
}

// Event listener for login link
loginLink.addEventListener('click', function (event) {
    event.preventDefault(); // Prevents following the "#" link
    toggleDivVisibility(loginDiv, registerDiv);
});

// Event listener for register link 1
registerLink1.addEventListener('click', function (event) {
    event.preventDefault(); // Prevents following the "#" link
    toggleDivVisibility(registerDiv, loginDiv);
});

// Event listener for register link 2
registerLink2.addEventListener('click', function (event) {
    event.preventDefault(); // Prevents following the "#" link
    toggleDivVisibility(registerDiv, loginDiv);
});
