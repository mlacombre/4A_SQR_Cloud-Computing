document.getElementById("calculation-form").addEventListener("submit", function(e) {
    e.preventDefault();
    
    const number1 = document.getElementById("number1").value;
    const number2 = document.getElementById("number2").value;
    const operator = document.getElementById("operator").value;
    firstArgument = '';
    if(operator == '+'){
        firstArgument = 'add';
    }
    else if(operator == '-'){
        firstArgument = 'sub';
    }
    else if(operator == '×'){
        firstArgument == 'mul';
    } 
    else if(operator == '÷'){
        firstArgument == 'div';
    }
    
    fetch(`http://localhost:5000/${firstArgument}/${number1}/${number2}`)
      .then(response => response.json())
      .then(data => {
        const calculationId = data.id;
        document.getElementById("result").innerHTML = 5;
      });
  });
  