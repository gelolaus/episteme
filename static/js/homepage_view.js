// Function to handle radio button change event
function handleRadioChange() {
    const individualNameField = document.getElementById('individualNameField');
    const groupNameField = document.getElementById('groupNameField');
    const memberFields = document.getElementById('memberFields');
    const fullNameInput = document.querySelector('input[name="full_name"]');
    const groupNameInput = document.querySelector('input[name="group_name"]');
    const memberNameInputs = document.querySelectorAll('input[name^="member_name"]');
    const submissionTypeInput = document.querySelector('input[name="submission_type"]');

    const individualRadio = document.querySelector('input[value="individual"]');
    const groupRadio = document.querySelector('input[value="group"]');

    if (individualRadio.checked) {
        individualNameField.style.display = 'block';
        groupNameField.style.display = 'none';
        memberFields.style.display = 'none';
        groupNameInput.value = ''; // Clear Group Name input
        for (const memberInput of memberNameInputs) {
            memberInput.value = ''; // Clear Group Members input
        }
        submissionTypeInput.value = 'Individual'; // Set submission_type to Individual
    } else if (groupRadio.checked) {
        individualNameField.style.display = 'none';
        groupNameField.style.display = 'block';
        memberFields.style.display = 'block';
        fullNameInput.value = ''; // Clear Full Name input
        submissionTypeInput.value = 'Group'; // Set submission_type to Group
    }
}

document.getElementById("backButton").addEventListener("click", () => {
    history.back();
});


// Call the handleRadioChange() function on page load
document.addEventListener('DOMContentLoaded', handleRadioChange);
