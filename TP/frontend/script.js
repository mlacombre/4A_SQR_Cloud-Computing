// Attendre que le document soit chargé
document.addEventListener("DOMContentLoaded", function(event) {
  

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

    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:5000/flip/' + username +'/' + tweet);
    xhr.send();
 
  });


    // Faire quelque chose avec les valeurs récupérées
    // (par exemple, les envoyer à un serveur)

    // Cacher le formulaire et réafficher le bouton "Tweet"
    

  });

  
  