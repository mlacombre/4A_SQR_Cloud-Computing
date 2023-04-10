// Attendre que le document soit chargé
document.addEventListener("DOMContentLoaded", function(event) {
  

  let xhr = new XMLHttpRequest();
    
    xhr.open('GET', `http://127.0.0.1:5000/getAllFlip`, true);
    xhr.onload = function() {
      if (xhr.status === 200) {
        let donnees = JSON.parse(xhr.responseText);
        console.log(donnees);
        for (let i = 0; i < donnees.length; i++) {
          let flip = donnees[i].flip;
          let author = donnees[i].author;
          let flipDiv = document.createElement("div");
          flipDiv.classList.add("flip");
          let flipPseudo = document.createElement("p");
          flipPseudo.classList.add("flip-pseudo");
          flipPseudo.textContent = "auteur : " + author;
          let flipText = document.createElement("p");
          flipText.classList.add("flip-text");
          flipText.textContent = flip;
          flipDiv.appendChild(flipPseudo);
          flipDiv.appendChild(flipText);
          document.getElementById("flip-container").appendChild(flipDiv);
        }
      }
    };
    xhr.onerror = function() {
      console.log("Une erreur est survenue lors de la requête");
    };
    
    xhr.send();  


    let xhr2 = new XMLHttpRequest();
    
    xhr2.open('GET', `http://127.0.0.1:5000/getAllSubject`, true);
    xhr2.onload = function() {
      if (xhr2.status === 200) {
        let donnees = JSON.parse(xhr.responseText);
        for (let i = 0; i < donnees.length; i++) {
          let subject = donnees[i].subject;
          let subjectDiv = document.createElement("div");
          subjectDiv.classList.add("subject");
          let subjectText = document.createElement("p");
          subjectText.classList.add("subject-text");
          subjectText.textContent = subject;
          subjectDiv.appendChild(subjectText);
          document.getElementById("subject-container").appendChild(subjectDiv);
        }
      }
    };
    xhr2.onerror = function() {
      console.log("Une erreur est survenue lors de la requête");
    };

    xhr2.send();


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
    var tweet =  document.getElementById("texte").value;
    
    formTweet.style.display = "none";
    btnTweet.style.display = "block";

    let xhr3 = new XMLHttpRequest();
    
    xhr3.open('POST', `http://127.0.0.1:5000/flip/${encodeURIComponent(encodeURI(username))}/${encodeURIComponent(encodeURI(tweet))}`, true);
    xhr3.onload = function() {
      if (xhr3.status === 200) {
        let donnees = JSON.parse(xhr.responseText);
        console.log(donnees);
      }
    };
    xhr3.onerror = function() {
      console.log("Une erreur est survenue lors de la requête");
    };
    
    xhr3.send();  

  });

});
  