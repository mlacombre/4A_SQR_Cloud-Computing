const axios = require('axios');

const input = document.getElementById("calculation-form")
input.addEventListener("click", () => {
    const number1 = document.getElementById("number1").value;
    const number2 = document.getElementById("number2").value;
    const operator = document.getElementById("operator").value;
    const option = {
        method: 'POST' 
    };

    axios.post('https://localhost:5000/${operator}/${number1}/${number2}')
        .then((response) => {
        console.log(response.data);
    })
    .catch((error) => {
        console.log(error);
    });

})


document.getElementById("calculation-form").addEventListener("submit", function(e) {
    e.preventDefault();
    
    const number1 = document.getElementById("number1").value;
    const number2 = document.getElementById("number2").value;
    const operator = document.getElementById("operator").value;
    const option = {
        method: 'POST' 
    };
    
    axios.post('https://localhost:5000/${operator}/${number1}/${number2}')
        .then((response) => {
        console.log(response.data);
    })
    .catch((error) => {
        console.log(error);
    });
});
