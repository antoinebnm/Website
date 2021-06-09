function playsound(button) {
    element = document.getElementById(button)
    if(element.class == "on") {
        element.class = "off"
    }else{
        element.class = "on"
    }
}