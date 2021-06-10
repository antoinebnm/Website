function playsound(self) {
    let element = document.getElementsByClassName(self);
    let button = element.item(self).className;
    document.getElementById('output').innerText = button;
    
}