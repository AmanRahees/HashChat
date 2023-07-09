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

var fileUploadBtn = document.getElementById("fileUploadBtn");
var fileInput = document.getElementById("fileInput");

fileUploadBtn.addEventListener("click", function () {
  fileInput.click();
});

fileInput.addEventListener("change", function () {
  var selectedFiles = fileInput.files;
  // Perform further actions with the selected files
});

const containers = document.querySelectorAll(".ls-container");

// Add click event listener to each container
containers.forEach((container) => {
  container.addEventListener("click", () => {
    // Remove active class from all containers
    containers.forEach((container) => {
      container.classList.remove("active");
    });

    // Add active class to the clicked container
    container.classList.add("active");
  });
});
