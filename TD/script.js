document.getElementById("calculation-form").addEventListener("submit", function(e) {
    e.preventDefault();
    
    const number1 = document.getElementById("number1").value;
    const number2 = document.getElementById("number2").value;
    const operator = document.getElementById("operator").value;
    const option = {
        method: 'POST' 
    };
    
    fetch(`http://127.0.0.1:5000/${operator}/${number1}/${number2}`, option)
      .then(response => response.json())
      .then(data => {
        console.log(response.json());
        const calculationId = data.id;
        document.getElementById("result").innerHTML = 5;
      });
  });
  

