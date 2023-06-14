// Function to handle file input change event
const fileInput = document.querySelector('#file-js-example input[type=file]');
fileInput.onchange = () => {
    if (fileInput.files.length > 0) {
        const fileName = document.querySelector('#file-js-example .file-name');
        fileName.textContent = fileInput.files[0].name;
    }
};

// Function to handle radio button change event
function handleRadioChange() {
    const individualNameField = document.getElementById('individualNameField');
    const groupNameField = document.getElementById('groupNameField');
    const memberFields = document.getElementById('memberFields');

    const individualRadio = document.querySelector('input[value="individual"]');
    const groupRadio = document.querySelector('input[value="group"]');

    if (individualRadio.checked) {
        individualNameField.style.display = 'block';
        groupNameField.style.display = 'none';
        memberFields.style.display = 'none';
    } else if (groupRadio.checked) {
        individualNameField.style.display = 'none';
        groupNameField.style.display = 'block';
        memberFields.style.display = 'block';
    }
}

// Get the keywords input element
const keywordsInput = document.getElementById('keywords-input');

// Get the tag container element
const tagContainer = document.getElementById('tag-container');

// Function to handle adding a tag
function addTag() {
    // Get the keywords text from the input
    const keywordsText = keywordsInput.value.trim();

    // Check if the input is not empty
    if (keywordsText !== '') {
        // Create a new tag element
        const tagElement = document.createElement('span');
        tagElement.classList.add('tag');
        tagElement.textContent = keywordsText;

        // Append the tag element to the tag container
        tagContainer.appendChild(tagElement);

        // Clear the input
        keywordsInput.value = '';
    }
}

// Function to handle form submission
function submitForm(event) {
    event.preventDefault();

    // Get the form element
    const form = document.querySelector('form');

    // Create a new FormData object
    const formData = new FormData(form);

    // Get the keywords tags from the tag container
    const tags = Array.from(tagContainer.querySelectorAll('.tag')).map(tag => tag.textContent);

    // Append the tags as an array to the formData object
    formData.append('keywords', JSON.stringify(tags));

    // Get the file input element
    const fileInput = document.querySelector('#file-js-example input[type=file]');

    // Check if a file is selected
    if (fileInput.files.length > 0) {
        // Append the file to the formData object
        formData.append('file', fileInput.files[0]);
    }

    // Make an AJAX request to submit the form data to the server
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/submit');

    // Set the appropriate headers
    xhr.setRequestHeader('Content-Type', 'multipart/form-data');

    xhr.onload = function () {
        if (xhr.status === 200) {
            // Handle the response from the server
            console.log(xhr.responseText);
        } else {
            // Handle the error
            console.error('Error:', xhr.statusText);
        }
    };

    xhr.send(formData);
}



// Add an event listener for the Enter key press on the keywords input
keywordsInput.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        addTag();
    }
});

// Add an event listener for the click event on the tag container
tagContainer.addEventListener('click', function (event) {
    if (event.target.classList.contains('tag')) {
        // Remove the tag element
        event.target.remove();
    }
});

// Function to prevent form submission on Enter key press
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            event.preventDefault();
        }
    });
});

// Function to handle form reset button click event
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const clearFormButton = document.querySelector('#clearFormButton');

    clearFormButton.addEventListener('click', function (event) {
        event.preventDefault();
        form.reset();

        // Clear the keywords
        tagContainer.innerHTML = '';

        // Reset radio buttons to "Individual"
        const individualRadio = document.querySelector('input[value="individual"]');
        individualRadio.checked = true;
        handleRadioChange();
    });
});
