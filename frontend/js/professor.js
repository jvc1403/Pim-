// professor.js — scripts do módulo professor
// Incluir nas páginas do professor

document.addEventListener('DOMContentLoaded', () => {
  const user = App.session.get();
  if (!user || user.role !== 'professor') {
    Feedback.toast('Acesso reservado a professores.', 'error');
    setTimeout(() => App.navigateWithFade('/index.html'), 700);
    return;
  }

  // Show name in header
  document.querySelectorAll('[data-user-name]').forEach(n => n.textContent = user.name || user.email);

  // Back to cards
  document.querySelectorAll('.btn-voltar, [data-back-to-cards]').forEach(el => {
    el.addEventListener('click', e => {
      e.preventDefault();
      App.navigateWithFade('/professor/cards.html');
    });
  });

  // Placeholders for professor pages
  const stats = document.querySelector('#prof-stats');
  if (stats) {
    stats.innerHTML = `
      <div class="stat">Total de turmas: <strong>--</strong></div>
      <div class="stat">Alunos cadastrados: <strong>--</strong></div>
      <div class="stat">Atividades pendentes: <strong>--</strong></div>
    `;
  }

  // Hook para abrir página de correção/envio
  document.querySelectorAll('[data-open-correct]').forEach(btn => {
    btn.addEventListener('click', e => {
      e.preventDefault();
      App.navigateWithFade('/professor/correcao.html');
    });
  });
});
