var dropdownBtn = document.querySelector(".dropdown-btn");
var dropdownContent = document.querySelector(".dropdown-content");

dropdownBtn.addEventListener("click", function () {
  dropdownContent.classList.toggle("show");
});

// Close the dropdown when the user clicks outside of it
window.addEventListener("click", function (event) {
  if (!dropdownBtn.contains(event.target)) {
    dropdownContent.classList.remove("show");
  }
});
