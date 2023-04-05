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
    var username = document.getElementById("username").value;
    var tweet = document.getElementById("texte").value;

    // Faire quelque chose avec les valeurs récupérées
    // (par exemple, les envoyer à un serveur)

    // Cacher le formulaire et réafficher le bouton "Tweet"
    formTweet.style.display = "none";
    btnTweet.style.display = "block";

  });

  const xhr = new XMLHttpRequest();
  xhr.open('GET', 'https://exemple.com/api/tweets');

  xhr.onload = function() {
    if (xhr.status === 200) {
      const data = JSON.parse(xhr.responseText);
      // faire quelque chose avec les données
    } else {
      console.log('Erreur de requête.');
    }
  };

  xhr.send();
  
  });
  