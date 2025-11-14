// transicoes.js — helpers de transição simples
// Incluir junto com main.js se quiser API separada

const Transitions = (() => {
  const fadeIn = (el, duration = 350) => {
    if (!el) return;
    el.style.transition = `opacity ${duration}ms ease, transform ${duration}ms ease`;
    el.style.opacity = 0;
    el.style.transform = 'translateY(6px)';
    requestAnimationFrame(() => {
      el.style.opacity = 1;
      el.style.transform = 'translateY(0)';
    });
  };

  const fadeOut = (el, duration = 300, cb) => {
    if (!el) { if (cb) cb(); return; }
    el.style.transition = `opacity ${duration}ms ease, transform ${duration}ms ease`;
    el.style.opacity = 1;
    el.style.transform = 'translateY(0)';
    requestAnimationFrame(() => {
      el.style.opacity = 0;
      el.style.transform = 'translateY(6px)';
    });
    setTimeout(() => { if (cb) cb(); }, duration);
  };

  return { fadeIn, fadeOut };
})();
