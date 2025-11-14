// suporte.js — mock de chat/suporte simples
// Incluir em aluno/suporte.html ou professor/suporte.html

document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('#suporte-form');
  const convo = document.querySelector('#suporte-conversation');
  if (!form || !convo) return;

  form.addEventListener('submit', e => {
    e.preventDefault();
    const input = form.querySelector('input[name="q"]');
    const text = input.value.trim();
    if (!text) return;
    appendMessage('Você', text, true);
    input.value = '';
    // resposta simulada
    setTimeout(() => {
      appendMessage('Assistente', `Recebi: "${text}". Em breve integração com backend retornará resposta real.`, false);
    }, 600);
  });

  function appendMessage(who, text, isUser) {
    const el = document.createElement('div');
    el.className = `msg ${isUser ? 'user' : 'bot'}`;
    el.textContent = `${who}: ${text}`;
    el.style.padding = '8px 10px';
    el.style.marginBottom = '8px';
    el.style.borderRadius = '8px';
    el.style.background = isUser ? '#0f172a' : '#111827';
    el.style.color = '#fff';
    convo.appendChild(el);
    convo.scrollTop = convo.scrollHeight;
  }
});
