// Attendre que le document soit chargé
document.addEventListener("DOMContentLoaded", function(event) {
  const optionsPOST = {
    method: 'POST',
    mode: 'cors',
  };
  

  const optionsGET = {
    method: 'GET',
    mode: 'cors',
  };

  // Récupérer le bouton "Tweet" et le formulaire
  var btnTweet = document.querySelector("button");
  var formTweet = document.getElementById("formulaire");

  // Ajouter un écouteur d'événement sur le bouton "Tweet"
  btnTweet.addEventListener("click", function(event) {

    // Cacher le bouton "Tweet" et afficher le formulaire
    btnTweet.style.display = "none";
    formTweet.style.display = "block";

  });

  // Ajouter un écouteur d'événement sur le formulaire
  formTweet.addEventListener("submit", function(event) {

    // Empêcher le formulaire de se soumettre
    event.preventDefault();

    // Récupérer les valeurs saisies dans les champs de saisie
    var username = document.getElementById("nomUtilisateur").value;
    var tweet = document.getElementById("texte").value;
    formTweet.style.display = "none";
    btnTweet.style.display = "block";

    let xhr = new XMLHttpRequest();

    xhr.open('POST', `http://localhost:5000/flip/${username}/${tweet}`, true);
    xhr.onload = function() {
      if (xhr.status === 200) {
        let donnees = JSON.parse(xhr.responseText);
        console.log(donnees);
      }
    };
    xhr.onerror = function() {
      console.log("Une erreur est survenue lors de la requête");
    };
    
    xhr.send();

  });

});
  