function playsound() {
    let valeur = "";
    let valeur2 = "";
    let elements = document.querySelectorAll(".button");
    Array.from(elements).forEach((element, index) => 
    {
        let label = document.querySelector("div.drum label[for="+ element.id + "]");
        valeur += "ID : " + element.id + ", Class : " + element.className + ", Label Text : " + label.innerText + ", Label Class : " + label.className + "\r";
        if (label.className === "off") {
            label.className = "on";
            label.style.color = "red";
        } else {
            label.className = "off";
            label.style.color = "blue";
        }
        valeur2 += "Label Text : " + label.innerText + ", Label Class : " + label.className  + "\r";
    });
    document.getElementById('output').innerText = valeur;
}