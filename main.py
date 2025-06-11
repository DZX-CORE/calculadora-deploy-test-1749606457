from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Calculadora DZX-CORE</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; }
        .calc { max-width: 400px; margin: 0 auto; }
        input, button { padding: 10px; margin: 5px; font-size: 16px; }
        button { background: #4CAF50; color: white; border: none; cursor: pointer; }
    </style>
</head>
<body>
    <div class="calc">
        <h1>Calculadora Web</h1>
        <p>Deploy automático funcionando!</p>
        <input type="number" id="a" placeholder="Número 1">
        <input type="number" id="b" placeholder="Número 2">
        <br>
        <button onclick="calc('+'))">Somar</button>
        <button onclick="calc('-'))">Subtrair</button>
        <button onclick="calc('*'))">Multiplicar</button>
        <button onclick="calc('/'))">Dividir</button>
        <div id="result" style="margin-top: 20px; font-size: 18px;"></div>
    </div>
    <script>
        function calc(op) {
            const a = parseFloat(document.getElementById('a').value);
            const b = parseFloat(document.getElementById('b').value);
            let result;
            
            switch(op) {
                case '+': result = a + b; break;
                case '-': result = a - b; break;
                case '*': result = a * b; break;
                case '/': result = b !== 0 ? a / b : 'Erro: divisão por zero'; break;
            }
            
            document.getElementById('result').innerHTML = 
                'Resultado: ' + a + ' ' + op + ' ' + b + ' = ' + result;
        }
    </script>
</body>
</html>
"""

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
