document.getElementById("registerForm").addEventListener("submit", function(e) {
    let valid = true;

    // Fields
    const username = document.getElementById("username");
    const email = document.getElementById("email");
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirmPassword");

    // Errors
    document.getElementById("usernameError").textContent = "";
    document.getElementById("emailError").textContent = "";
    document.getElementById("passwordError").textContent = "";
    document.getElementById("confirmError").textContent = "";

    if (username.value.trim() === "") {
        document.getElementById("usernameError").textContent = "Username is required";
        valid = false;
    }

    if (email.value.trim() === "") {
        document.getElementById("emailError").textContent = "Email is required";
        valid = false;
    }

    if (password.value.length < 6) {
        document.getElementById("passwordError").textContent = "Password must be at least 6 characters";
        valid = false;
    }

    if (password.value !== confirmPassword.value) {
        document.getElementById("confirmError").textContent = "Passwords do not match";
        valid = false;
    }

    if (!valid) {
        e.preventDefault(); // Stop form submission
    }
});