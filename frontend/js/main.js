// main.js — inicialização global e helpers
// Usar em todas as páginas: <script src="../js/main.js"></script>

const App = (() => {
  const SELECTORS = {
    body: document.body,
    fadeClass: 'fade-out',
  };

  // Faz fade-out e navega
  const navigateWithFade = (href, duration = 500) => {
    if (!href) return;
    SELECTORS.body.classList.add(SELECTORS.fadeClass);
    setTimeout(() => (window.location.href = href), duration);
  };

  // Simple session helpers (mock)
  const session = {
    set(user) { localStorage.setItem('sa_user', JSON.stringify(user)); },
    get() { return JSON.parse(localStorage.getItem('sa_user') || 'null'); },
    clear() { localStorage.removeItem('sa_user'); },
    isLogged() { return !!session.get(); }
  };

  // Attach logout button behaviour (any element with data-logout)
  const bindLogoutButtons = () => {
    document.querySelectorAll('[data-logout]').forEach(btn => {
      btn.addEventListener('click', e => {
        e.preventDefault();
        session.clear();
        Feedback.toast('Sessão encerrada', 'info');
        setTimeout(() => navigateWithFade('/index.html'), 400);
      });
    });
  };

  // On DOM ready
  const init = () => {
    // Remove fade-out class after load for fade-in effect
    requestAnimationFrame(() => {
      SELECTORS.body.classList.remove(SELECTORS.fadeClass);
    });
    bindLogoutButtons();
  };

  return { init, navigateWithFade, session };
})();

// Auto init on load
window.addEventListener('DOMContentLoaded', () => App.init());
