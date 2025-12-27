document.getElementById("contactForm").addEventListener("submit", function(e) {
    let valid = true;

    // Fields
    const name = document.getElementById("name");
    const email = document.getElementById("email");
    const message = document.getElementById("message");

    // Error elements
    document.getElementById("nameError").textContent = "";
    document.getElementById("emailError").textContent = "";
    document.getElementById("messageError").textContent = "";

    if (name.value.trim() === "") {
        document.getElementById("nameError").textContent = "Name is required";
        valid = false;
    }

    if (email.value.trim() === "") {
        document.getElementById("emailError").textContent = "Email is required";
        valid = false;
    }

    if (message.value.trim() === "") {
        document.getElementById("messageError").textContent = "Message is required";
        valid = false;
    }

    if (!valid) {
        e.preventDefault(); // Stop form submission
    }
});