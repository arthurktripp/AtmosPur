function locationWarn() {
  if (confirm("Changing this setting will affect long-term tracking of outside AQI. Continue?")) {
    return true;
  } else {
    return false;
  }
}



function showLocUpdate() {
  locForm = document.getElementById("location-update");
  locForm.style.visibility = "visible";
}

function hideLocUpdate() {
  locForm = document.getElementById("location-update");
  locForm.style.visibility = "hidden";
}

cancelButton = document.getElementById("cancel-location-update")
cancelButton.addEventListener('click', function(event) {
  event.preventDefault()
})
