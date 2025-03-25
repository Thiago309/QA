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
    window.location.href = "file:///C:/Users/wagne/Desktop/1000/index.html";
});
