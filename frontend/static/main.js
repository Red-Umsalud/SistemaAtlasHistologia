window.onload = window.onresize = setWidth;

function setWidth() {
  let ancho = document.documentElement.clientWidth;
  const text = document.querySelector("#navtext");

  if (ancho < 852) text.innerHTML = "FMENT - UMSA";
  else
    text.innerHTML =
      "Facultad de Medicina, Enfermería,<br> Nutrición y Tecnología Médica";
}


