const express = require('express'); 
const bodyParser = require('body-parser'); 
  
const app = express(); 
  
app.use(bodyParser.json()); 
app.use(bodyParser.urlencoded({ extended: false })); 

const port = 4000;


app.get('/', (req, res) => {   
  res.send('Hello!');              
  var info = req.body;
  console.log(info)
});


app.post('/', (req, res) => {
    const num1 = req.body.num1;
    const num2 = req.body.num2;

    if (!num1 || !num2) {
      const message = "Both num1 and num2 must be provided.";
      return res.status(400).json({ error: message });
  }

  if (num1.includes('.') || num2.includes('.')) {
      const message = "GCD is not defined for float numbers.";
      const data = { error: message };
      return res.json({ reult : message });
  } else {
      const num1Int = Math.abs(parseInt(num1));
      const num2Int = Math.abs(parseInt(num2));

      if (num1Int === 0) {
          return res.json({ result: num2Int });
      }
      if (num2Int === 0) {
          return res.json({ result: num1Int });
      }

      let a = num1Int;
      let b = num2Int;

      while (b !== 0) {
          let temp = b;
          b = a % b;
          a = temp;
      }

      const result = a;
      return res.json({ result: result });
  }
});



app.listen(port, host = '0.0.0.0', () => {
    console.log(`Server running at http://localhost:${port}`);
});
