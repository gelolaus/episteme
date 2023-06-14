function updateStatus(submissionId, button) {
    var selectElement = button.parentNode.previousElementSibling.querySelector('select');
    var status = selectElement.value;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/update_status', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Status updated successfully, you can perform additional actions if needed
        }
    };
    var data = JSON.stringify({ submissionId: submissionId, status: status });
    xhr.send(data);
}
