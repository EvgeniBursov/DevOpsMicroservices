const express = require('express');
const bodyParser = require('body-parser'); 

const app = express();
const port = 4001;

app.use(express.json());
app.use(bodyParser.urlencoded({ extended: false })); 


app.get('/', (req, res) => {   
    res.send('Hello!');              
    var info = req.body;
    console.log(info)
  });
  
  
  app.post('/', (req, res) => {
      const num1 = req.body.num1;
      const num2 = req.body.num2;
  
      if (num1.includes('-') || num2.includes('-')) {
        const message = "Root can't be negative";
        const data = { error: message };
        return res.json({ result: data });
    }

    if (num2.includes('.')) {
        const message = "Root cannot be float numbers.";
        const data = { result: message };
        return res.json({ result: message });
    } else {
        const num1Float = parseFloat(num1);
        const num2Int = parseInt(num2);
        
        if (num2Int === 0) {
            const message = "Root cannot be 0";
            const data = { error: message };
            return res.json({ result: message });
        }
        
        if (num1Float === 0) {
            const result = 0;
            return res.json({ result: result });
        }
    }

    let guess = num1 / 2;
    for (let i = 0; i < 100; i++) {
        guess = ((num2 - 1) * guess + num1 / Math.pow(guess, (num2 - 1))) / num2;
    }
    result = guess
    console.log(result)

    return res.json({result: result});
});

app.listen(port, host = '0.0.0.0', () => {
    console.log(`Server running at http://localhost:${port}`);
});
