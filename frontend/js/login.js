document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value.trim();
  const senha = document.getElementById("senha").value.trim();
  const perfil = document.querySelector('input[name="perfil"]:checked')?.value;

  if (!perfil) {
    alert("Selecione se você é Professor ou Aluno!");
    return;
  }

  try {
    // ⚙️ Simulação (sem backend ainda)
    const usuario = {
      nome: email.split("@")[0],
      tipo: perfil,
      token: "fake_token_123"
    };

    // Salvar login local
    localStorage.setItem("usuario", JSON.stringify(usuario));

    // Redirecionamento com base no tipo
    if (perfil === "aluno") {
      window.location.href = "../aluno/dashboard.html";
    } else {
      window.location.href = "../Professor/dashboard.html";
    }

  } catch (err) {
    console.error("Erro:", err);
    alert("Erro de conexão. Tente novamente.");
  }
});
