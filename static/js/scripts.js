document.addEventListener("DOMContentLoaded", function () {
  // Toast Notification System
  function showToast(message, type = "error") {
    const toastContainer = document.createElement("div");
    toastContainer.className = `toast ${type}`;
    toastContainer.setAttribute("role", "alert");
    toastContainer.setAttribute("aria-live", "assertive");
    toastContainer.innerHTML = `
            <span>${message}</span>
            <button class="toast-close" aria-label="Close">×</button>
        `;
    document.body.appendChild(toastContainer);

    // Auto-remove after 3 seconds
    setTimeout(() => {
      toastContainer.classList.add("fade-out");
      setTimeout(() => toastContainer.remove(), 300);
    }, 3000);

    // Close on click
    toastContainer
      .querySelector(".toast-close")
      .addEventListener("click", () => {
        toastContainer.classList.add("fade-out");
        setTimeout(() => toastContainer.remove(), 300);
      });
  }

  // Shake Animation for Invalid Inputs
  function shakeElement(element) {
    element.classList.add("shake");
    setTimeout(() => element.classList.remove("shake"), 500);
  }

  // Form Validation for Login
  const loginForm = document.querySelector("#login-form");
  if (loginForm) {
    const emailInput = document.querySelector("#email");
    const passwordInput = document.querySelector("#password");
    const roleInput = document.querySelector("#role");

    loginForm.addEventListener("submit", function (e) {
      const email = emailInput.value;
      const password = passwordInput.value;
      const role = roleInput.value;

      if (!email || !password || !role) {
        e.preventDefault();
        showToast("Please fill in all fields.", "error");
        if (!email) shakeElement(emailInput);
        if (!password) shakeElement(passwordInput);
        if (!role) shakeElement(roleInput);
      } else if (!/\S+@\S+\.\S+/.test(email)) {
        e.preventDefault();
        showToast("Please enter a valid email address.", "error");
        shakeElement(emailInput);
      }
    });
  }

  // Form Validation for Registration
  const registerForm = document.querySelector("#register-form");
  if (registerForm) {
    const nameInput = document.querySelector("#name");
    const emailInput = document.querySelector("#email");
    const passwordInput = document.querySelector("#password");
    const roleInput = document.querySelector("#role");

    registerForm.addEventListener("submit", function (e) {
      const name = nameInput.value;
      const email = emailInput.value;
      const password = passwordInput.value;
      const role = roleInput.value;

      if (!name || !email || !password || !role) {
        e.preventDefault();
        showToast("Please fill in all fields.", "error");
        if (!name) shakeElement(nameInput);
        if (!email) shakeElement(emailInput);
        if (!password) shakeElement(passwordInput);
        if (!role) shakeElement(roleInput);
      } else if (!/\S+@\S+\.\S+/.test(email)) {
        e.preventDefault();
        showToast("Please enter a valid email address.", "error");
        shakeElement(emailInput);
      } else if (password.length < 6) {
        e.preventDefault();
        showToast("Password must be at least 6 characters long.", "error");
        shakeElement(passwordInput);
      }
    });
  }

  // Confirmation for Delete Actions with Animation
  const deleteButtons = document.querySelectorAll(".delete-btn");
  deleteButtons.forEach((button) => {
    button.addEventListener("click", function (e) {
      button.classList.add("pulse");
      setTimeout(() => button.classList.remove("pulse"), 300);
      if (!confirm("Are you sure you want to delete this item?")) {
        e.preventDefault();
      }
    });
  });

  // Dynamic Date Picker Validation for Booking Form
  const bookingForm = document.querySelector("#booking-form");
  if (bookingForm) {
    const bookingDate = document.querySelector("#booking_date");

    bookingDate.addEventListener("change", function () {
      const today = new Date().toISOString().split("T")[0];
      if (bookingDate.value < today) {
        showToast("Booking date cannot be in the past.", "error");
        bookingDate.value = "";
        shakeElement(bookingDate);
      }
    });
  }
});
