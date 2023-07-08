const otpInputs = document.querySelectorAll(".otp-input");
const combinedOTPInput = document.getElementById("combinedOTP");

for (let i = 0; i < otpInputs.length; i++) {
  otpInputs[i].addEventListener("input", function () {
    this.value = this.value.replace(/[^0-9]/g, "");
    if (this.value.length === this.maxLength) {
      if (i < otpInputs.length - 1) {
        otpInputs[i + 1].focus();
      }
    }
  });

  otpInputs[i].addEventListener("keydown", function (event) {
    if (event.key === "Backspace" && this.value.length === 0) {
      if (i > 0) {
        otpInputs[i - 1].focus();
      }
    }
  });

  // Add event listeners to each OTP input field
  otpInputs.forEach(function (input) {
    input.addEventListener("input", updateCombinedOTP);
  });

  // Function to update the combined OTP value
  function updateCombinedOTP() {
    let otpValue = "";
    otpInputs.forEach(function (input) {
      otpValue += input.value;
    });
    combinedOTPInput.value = otpValue;
  }
}
