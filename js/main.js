function playsound(button) {
    element = document.getElementById(button)
    if(element.style.class == "on") {
        element.style.class = "off"
    }else{
        element.style.class = "on"
    }
}