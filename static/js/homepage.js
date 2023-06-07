$(document).ready(function () {
    $("a#continue-btn").click(function (e) {
        e.preventDefault();
        $("#selection-div").hide();
        $("#homepage-div").show();
    });
});