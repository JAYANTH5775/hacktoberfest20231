const firebaseConfig = {
    apiKey: "AIzaSyB6ewIT37A342Y-px1TC87oAfBb9zQ55bQ",
    authDomain: "contactform-929c1.firebaseapp.com",
    databaseURL: "https://contactform-929c1-default-rtdb.firebaseio.com",
    projectId: "contactform-929c1",
    storageBucket: "contactform-929c1.appspot.com",
    messagingSenderId: "316702911872",
    appId: "1:316702911872:web:a9e729377d00701b1ce565",
    measurementId: "G-9G15FR5EYW"
};




firebase.initializeApp(firebaseConfig);

// reference your database
var contactFormDB = firebase.database().ref("contactForm");

document.getElementById("contactForm").addEventListener("submit", submitForm);

function submitForm(e) {
    e.preventDefault();

    var name = getElementVal("name");
    var emailid = getElementVal("email");
    var msgContent = getElementVal("message");

    saveMessages(name, emailid, msgContent);

    //   enable alert
    document.querySelector(".alert").style.display = "block";

    //   remove the alert
    setTimeout(() => {
        document.querySelector(".alert").style.display = "none";
    }, 3000);

    //   reset the form
    document.getElementById("contactForm").reset();
}

const saveMessages = (name, emailid, msgContent) => {
    var newContactForm = contactFormDB.push();

    newContactForm.set({
        name: name,
        emailid: emailid,
        msgContent: msgContent,
    });
};

const getElementVal = (id) => {
    return document.getElementById(id).value;
};


// const contactFormDB = firebase.database().ref("contactForm");
// let name; let email; let message;

// document.getElementById("contactForm").addEventListener("submit", submitForm);


// function submitForm(e) {

//     e.preventDefault();
//     var name = getElementByVal('name');
//     var email = document.getElementByVal('email').value;
//     var message = document.getElementByVal('message').value;

//     console.log(name, email, message);
// }


// const getElementByVal = (id) => {

//     return document.getElementById(id).value;




