// Get elements
const teacherSearch = document.getElementById("teacherSearch");
const teacherSelect = document.getElementById("teacherSelect");
const courseSelect = document.getElementById("courseSelect");
const viewFeedbackButton = document.getElementById("viewFeedbackButton");

let teachers = {};

// Fetch teachers data from the server
fetch("/get_teachers")
  .then((response) => response.json())
  .then((data) => {
    teachers = data;
    console.log("Fetched teachers data:", teachers);
    // Populate the teacherSelect dropdown
    populateTeacherSelect();
    // Initialize courses if teacher is pre-selected
    initialize();
  })
  .catch((error) => {
    console.error("Error fetching teachers:", error);
  });

function populateTeacherSelect() {
  teacherSelect.innerHTML = "";
  for (let teacher in teachers) {
    const option = document.createElement("option");
    option.value = teacher;
    option.textContent = teacher;
    teacherSelect.appendChild(option);
  }
}

// Event listener for teacher search
teacherSearch.addEventListener("keyup", function () {
  const filter = teacherSearch.value.toLowerCase();
  const options = teacherSelect.options;
  for (let i = 0; i < options.length; i++) {
    const txtValue = options[i].textContent || options[i].innerText;
    if (txtValue.toLowerCase().indexOf(filter) > -1) {
      options[i].style.display = "";
    } else {
      options[i].style.display = "none";
    }
  }
});

// Event listener for teacher selection
teacherSelect.addEventListener("change", function () {
  const selectedTeacher = teacherSelect.value;
  const courses = teachers[selectedTeacher] || [];
  // Clear and populate courses
  courseSelect.innerHTML = "";
  if (courses.length > 0) {
    courses.forEach(function (course) {
      const option = document.createElement("option");
      option.value = course;
      option.textContent = course;
      courseSelect.appendChild(option);
    });
  } else {
    const option = document.createElement("option");
    option.value = "";
    option.textContent = "No courses available";
    courseSelect.appendChild(option);
  }
});

// Initialize courses if teacher is pre-selected
function initialize() {
  if (teacherSelect.value) {
    teacherSelect.dispatchEvent(new Event("change"));
  }
}

// Event listener for view feedback button
viewFeedbackButton.addEventListener("click", function () {
  const selectedTeacher = teacherSelect.value;
  const selectedCourse = courseSelect.value;
  if (selectedTeacher && selectedCourse) {
    window.location.href = `/feedback?teacher=${encodeURIComponent(selectedTeacher)}&course=${encodeURIComponent(selectedCourse)}`;
  }
});
