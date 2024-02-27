let insideVal = parseInt(document.getElementById("inside-aqi-number").innerText);
let insideCircle = document.getElementById("inside-circle");

function insideColor() {
  let insideCircleText = document.getElementById("inside-aqi-number");
  let insideCircleLocation = document.getElementById("inside-aqi-location");
  
  if (insideVal <= 50) { 
    insideCircle.style.borderColor = 'var(--q1-good)';
    insideCircleText.style.color = 'var(--q1-good)';
    insideCircleLocation.style.color = 'var(--q1-good)';
  } else if (50 < insideVal && insideVal < 101) {
    insideCircle.style.borderColor = 'var(--q2-moderate)';
    insideCircleText.style.color = 'var(--q2-moderate)';
    insideCircleLocation.style.color = 'var(--q2-moderate)';
  } else if (100 < insideVal && insideVal < 151) {
    insideCircle.style.borderColor = 'var(--q3-low-unhealthy)';
    insideCircleText.style.color = 'var(--q3-low-unhealthy)';
    insideCircleLocation.style.color = 'var(--q3-low-unhealthy)';
  } else if (150 < insideVal && insideVal < 201) {
    insideCircle.style.borderColor = 'var(--q4-unhealthy)';
    insideCircleText.style.color = 'var(--q4-unhealthy)';
    insideCircleLocation.style.color = 'var(--q4-unhealthy)';
  } else if (200 < insideVal && insideVal < 301) {
    insideCircle.style.borderColor = 'var(--q5-very-unhealthy)';
    insideCircle.style.backgroundColor = 'var(--off-white)';
    insideCircleText.style.color = 'var(--q5-very-unhealthy)';
    insideCircleLocation.style.color = 'var(--q5-very-unhealthy)';
    
  } else {
    insideCircle.style.borderColor = 'var(--q6-hazardous)';
    insideCircle.style.backgroundColor = 'var(--off-white)';
    insideCircleText.style.color = 'var(--q6-hazardous)';
    insideCircleLocation.style.color = 'var(--q6-hazardous)';
  }
}


function outsideColor() {
  let outsideVal = parseInt(document.getElementById("outside-aqi-number").innerText);
  let outsideCircle = document.getElementById("outside-circle");
  let outsideCircleText = document.getElementById("outside-aqi-number");
  let outsideCircleLocation = document.getElementById("outside-aqi-location");
  
  if (outsideVal <= 50) { 
    outsideCircle.style.borderColor = 'var(--q1-good)';
    outsideCircleText.style.color = 'var(--q1-good)';
    outsideCircleLocation.style.color = 'var(--q1-good)';
  } else if (50 < outsideVal && outsideVal < 101) {
    outsideCircle.style.borderColor = 'var(--q2-moderate)';
    outsideCircleText.style.color = 'var(--q2-moderate)';
    outsideCircleLocation.style.color = 'var(--q2-moderate)';
  } else if (100 < outsideVal && outsideVal < 151) {
    outsideCircle.style.borderColor = 'var(--q3-low-unhealthy)';
    outsideCircleText.style.color = 'var(--q3-low-unhealthy)';
    outsideCircleLocation.style.color = 'var(--q3-low-unhealthy)';
  } else if (150 < outsideVal && outsideVal < 201) {
    outsideCircle.style.borderColor = 'var(--q4-unhealthy)';
    outsideCircleText.style.color = 'var(--q4-unhealthy)';
    outsideCircleLocation.style.color = 'var(--q4-unhealthy)';
  } else if (200 < outsideVal && outsideVal < 301) {
    outsideCircle.style.borderColor = 'var(--q5-very-unhealthy)';
    outsideCircle.style.backgroundColor = 'var(--off-white)';
    outsideCircleText.style.color = 'var(--q5-very-unhealthy)';
    outsideCircleLocation.style.color = 'var(--q5-very-unhealthy)';
    
  } else {
    outsideCircle.style.borderColor = 'var(--q6-hazardous)';
    outsideCircle.style.backgroundColor = 'var(--off-white)';
    outsideCircleText.style.color = 'var(--q6-hazardous)';
    outsideCircleLocation.style.color = 'var(--q6-hazardous)';
  }
}


function aqiColors() {
  insideColor();
  outsideColor();
}