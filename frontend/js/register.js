// register.js — formulário de cadastro mock
// Incluir em login/register.html

document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('#register-form');
  if (!form) return;

  const loadUsers = () => JSON.parse(localStorage.getItem('sa_users') || '[]');
  const saveUsers = (arr) => localStorage.setItem('sa_users', JSON.stringify(arr));

  form.addEventListener('submit', e => {
    e.preventDefault();
    const name = (form.querySelector('input[name="name"]') || {}).value?.trim() || '';
    const email = (form.querySelector('input[name="email"]') || {}).value?.trim() || '';
    const password = (form.querySelector('input[name="password"]') || {}).value?.trim() || '';

    if (!name || !email || !password) {
      Feedback.toast('Preencha todos os campos.', 'error');
      return;
    }

    const users = loadUsers();
    if (users.some(u => u.email === email)) {
      Feedback.toast('E-mail já cadastrado.', 'error');
      return;
    }

    users.push({ name, email, password, role: 'aluno' });
    saveUsers(users);
    Feedback.toast('Conta criada com sucesso!', 'success');

    setTimeout(() => App.navigateWithFade('/index.html'), 700);
  });
});
