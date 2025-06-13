document.getElementById('form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('/calcular', {
        method: 'POST',
        body: formData
    });
    const data = await response.json();
    if (data.erro) {
        document.getElementById('resultado').innerText = data.erro;
    } else {
        document.getElementById('resultado').innerText = "Resultado: " + data.montantes.pop().toFixed(2);
    }
});