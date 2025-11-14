// aluno.js — scripts do módulo aluno
// Incluir nas páginas do aluno (cards/dashboard/notas/etc)

document.addEventListener('DOMContentLoaded', () => {
  const user = App.session.get();
  // Se não autenticado, redireciona ao login
  if (!user) {
    Feedback.toast('Você precisa estar logado.', 'error');
    setTimeout(() => App.navigateWithFade('/index.html'), 500);
    return;
  }

  // Exibe nome em header (se existir)
  const headerName = document.querySelector('[data-user-name]');
  if (headerName) headerName.textContent = user.name || user.email;

  // Voltar para cards (padronizado)
  document.querySelectorAll('.btn-voltar, [data-back-to-cards]').forEach(el => {
    el.addEventListener('click', e => {
      e.preventDefault();
      App.navigateWithFade('/aluno/cards.html');
    });
  });

  // Perfil edit (somente nome e avatar local)
  const formProfile = document.querySelector('#profile-form');
  if (formProfile) {
    const nameInput = formProfile.querySelector('input[name="name"]');
    const emailSpan = formProfile.querySelector('[data-profile-email]');
    if (nameInput) nameInput.value = user.name || '';
    if (emailSpan) emailSpan.textContent = user.email || '';

    formProfile.addEventListener('submit', e => {
      e.preventDefault();
      const newName = nameInput.value.trim();
      if (!newName) {
        Feedback.toast('Nome não pode ficar vazio', 'error');
        return;
      }
      // Atualiza sessão (mock)
      const updated = Object.assign({}, user, { name: newName });
      App.session.set(updated);
      Feedback.toast('Perfil atualizado', 'success');
      // Atualiza header
      document.querySelectorAll('[data-user-name]').forEach(n => n.textContent = newName);
    });
  }

  // Placeholder: carregar últimas notas (empty state)
  const notasContainer = document.querySelector('#notas-list');
  if (notasContainer) {
    notasContainer.innerHTML = '<div class="empty">Sem dados — pronto para conectar ao backend.</div>';
  }

  // Placeholder: atividades list
  const atividadesContainer = document.querySelector('#atividades-list');
  if (atividadesContainer) {
    atividadesContainer.innerHTML = '<div class="empty">Nenhuma atividade carregada.</div>';
  }
});
