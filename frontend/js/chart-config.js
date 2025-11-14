// chart-config.js — configuração base para Chart.js
// Incluir APÓS importar Chart.js (cdn ou local)

const ChartConfig = (() => {
  const defaultOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: true, labels: { color: '#d1d5db' } },
      tooltip: { enabled: true }
    },
    scales: {
      x: { ticks: { color: '#9ca3af' }, grid: { color: 'rgba(255,255,255,0.02)' } },
      y: { ticks: { color: '#9ca3af' }, grid: { color: 'rgba(255,255,255,0.02)' } }
    }
  };

  const createLine = (ctx, labels = [], data = [], label = 'Série') => {
    return new Chart(ctx, {
      type: 'line',
      data: { labels, datasets: [{ label, data, fill: true, tension: 0.3, backgroundColor: 'rgba(59,130,246,0.12)', borderColor: 'rgba(59,130,246,0.9)' }] },
      options: defaultOptions
    });
  };

  const createBar = (ctx, labels = [], data = [], label = 'Valores') => {
    return new Chart(ctx, {
      type: 'bar',
      data: { labels, datasets: [{ label, data, backgroundColor: 'rgba(37,99,235,0.8)' }] },
      options: defaultOptions
    });
  };

  return { createLine, createBar };
})();
