// view.js

// Function to handle the radio button change event
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


function editSubmission() {
    // Get the form element
    const form = document.querySelector('.box.view-box-ni-luis');

    // Check if the form is already in edit mode
    if (form.dataset.editable !== 'true') {
        // Enable editing of form fields
        const formFields = form.querySelectorAll('input, textarea, select');
        formFields.forEach(field => {
            field.disabled = false;
        });

        // Hide the Edit Submission button and show the Cancel Changes button
        const editButton = document.getElementById('editButton');
        const cancelButton = document.createElement('a');
        cancelButton.classList.add('button', 'is-danger');
        cancelButton.innerText = 'Cancel Changes';
        cancelButton.onclick = cancelChanges;
        editButton.parentNode.replaceChild(cancelButton, editButton);

        // Show the Submit button
        const submitButton = document.querySelector('button[type="submit"]');
        submitButton.style.display = 'block';

        // Set the form's data-editable attribute to true
        form.dataset.editable = 'true';
    }
}

function cancelChanges() {
    // Reload the page to cancel any changes made
    location.reload();
}

// Hide the Submit button on page load
document.addEventListener('DOMContentLoaded', () => {
    const submitButton = document.querySelector('button[type="submit"]');
    submitButton.style.display = 'none';
});

// Call the handleRadioChange() function on page load
document.addEventListener('DOMContentLoaded', handleRadioChange);
