<script>
    // Function to show the alert popup
    function showAlert(message) {
        var alertPopup = document.getElementById("alert-popup");
        alertPopup.textContent = message;
        alertPopup.style.display = "block";

        // Hide the popup after 5 seconds (adjust as needed)
        setTimeout(function () {
            alertPopup.style.display = "none";
        }, 5000); // 5000 milliseconds = 5 seconds
    }

    // Check if there are flashed messages
    var messages = document.querySelectorAll(".feedback-messages li");
    if (messages.length > 0) {
        // Display each flashed message as an alert
        messages.forEach(function (messageElement) {
            showAlert(messageElement.textContent);
        });
    }
</script>
