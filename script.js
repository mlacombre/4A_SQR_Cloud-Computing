document.getElementById("calculation-form").addEventListener("submit", function(e) {
    e.preventDefault();
    
    const number1 = document.getElementById("number1").value;
    const number2 = document.getElementById("number2").value;
    const operator = document.getElementById("operator").value;
    
    fetch(`https://votre-api.com/calculate/${operator}/${number1}/${number2}`)
      .then(response => response.json())
      .then(data => {
        const calculationId = data.id;
        document.getElementById("result").innerHTML = `Calculation ID : ${calculationId}`;
      });
  });
  