const containers = document.querySelectorAll(".ls-container");
containers.forEach((container) => {
  container.addEventListener("click", () => {
    containers.forEach((container) => {
      container.classList.remove("active");
    });
    container.classList.add("active");
  });
});

let originalFormValues = {};

function toggleInput(inputId) {
  const input = document.getElementById(inputId);
  const icon = input.parentElement.querySelector(".fa-pen");

  input.disabled = !input.disabled;

  if (!input.disabled) {
    input.focus();
    input.select();
  }

  icon.classList.toggle("active");
  checkFormChanges();
}

function checkFormChanges() {
  const form = document.querySelector("form");
  const saveButton = document.getElementById("save-button");

  const formInputs = Array.from(form.querySelectorAll("input"));
  const hasChanges = formInputs.some((input) => {
    const originalValue = originalFormValues[input.id];
    return input.value !== originalValue;
  });

  saveButton.style.display = hasChanges ? "block" : "none";
}

window.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const formInputs = form.querySelectorAll("input");

  formInputs.forEach((input) => {
    originalFormValues[input.id] = input.value;
  });
});
