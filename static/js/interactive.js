function locationWarn() {
  if (confirm("Changing this setting will affect long-term tracking of outside AQI. Continue?"))
    return true;
  else
    return false;
}