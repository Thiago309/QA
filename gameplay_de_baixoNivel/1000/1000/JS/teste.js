const inputName = document.querySelector("#name");
const form = document.querySelector(".form");  // Seleciona o formulário
const cadastrarBtn = document.querySelector("#cadastrarBtn");

// Impede a digitação de números no campo de nome
inputName.addEventListener("keypress", function(e){
    const keyCode = (e.keyCode ? e.keyCode : e.which);

    if(keyCode > 47 && keyCode < 58){
        e.preventDefault();
    }
});

// Adiciona um evento de clique no botão de cadastrar
cadastrarBtn.addEventListener("click", function(e){
    // Impede o envio padrão para simular a limpeza antes do envio
    e.preventDefault();

    // Limpa todos os campos do formulário
    form.reset(); 

    // Opcional: Caso queira redirecionar o usuário após o envio
    window.location.href = "file:///C:/Users/thiago.vsantos/Documents/GitHub/QA/gameplay_de_baixoNivel/1000/1000/index.html";
});

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const senha = document.getElementById('password');
    const confirmarSenha = document.getElementById('password_2');
    const errorMessage = document.getElementById('error-message');
    const matchStatus = document.getElementById('match-status');
    const toggleButtons = document.querySelectorAll('.toggle-visibility');

    // Mostrar/ocultar senha
    toggleButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const input = document.getElementById(btn.dataset.target);
        input.type = input.type === 'password' ? 'text' : 'password';
        btn.textContent = input.type === 'password' ? '👁️' : '🙈';
      });
    });

    // Verificação visual em tempo real
    confirmarSenha.addEventListener('input', () => {
      if (confirmarSenha.value === senha.value) {
        matchStatus.textContent = '✔ As senhas coincidem';
        matchStatus.className = 'password-match match';
      } else {
        matchStatus.textContent = '✖ As senhas não coincidem';
        matchStatus.className = 'password-match mismatch';
      }
    });

    // Validação antes de enviar
    form.addEventListener('submit', function (e) {
      if (senha.value !== confirmarSenha.value) {
        e.preventDefault();
        errorMessage.style.display = 'block';
        confirmarSenha.focus();
      } else {
        errorMessage.style.display = 'none';
      }
    });
  });