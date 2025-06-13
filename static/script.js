
document.getElementById("formulario").addEventListener("submit", function (e) {
  e.preventDefault();
  const formData = new FormData(e.target);
  fetch("/calcular", {
    method: "POST",
    body: formData,
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.erro) return alert(data.erro);
      const ctx = document.getElementById("grafico").getContext("2d");
      new Chart(ctx, {
        type: "line",
        data: {
          labels: data.meses,
          datasets: [{
            label: "Montante (R$)",
            data: data.montantes,
            borderColor: "#00acc1",
            backgroundColor: "rgba(0,172,193,0.2)",
            fill: true,
            tension: 0.3,
          }],
        },
        options: {
          responsive: true,
          scales: {
            x: { title: { display: true, text: "Período (meses)" } },
            y: { title: { display: true, text: "Montante acumulado (R$)" } }
          }
        }
      });
    });
});
        