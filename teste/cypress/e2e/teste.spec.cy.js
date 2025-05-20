/// <reference types="cypress" />

const testes = [
  { email: "", senha: "1@Bc", descricao: "E-mail vazio" },
  { email: "1usuario@email.com", senha: "1@Bc", descricao: "E-mail iniciando com número" },
  { email: ".user@email.com", senha: "1@Bc", descricao: "E-mail iniciando com ponto" },
  { email: "usuario@dominio", senha: "1@Bc", descricao: "E-mail sem extensão de domínio" },
  { email: "usuario@@email.com", senha: "1@Bc", descricao: "E-mail com dois @ (inválido)" },
  { email: "usuario@teste.com", senha: "1@Bc", descricao: "E-mail com domínio bloqueado" },
  { email: "", senha: "", descricao: "Campos vazios" },
  { email: "usuarioemail.com", senha: "1@Bc", descricao: "E-mail sem @" },
  { email: "usuario@", senha: "1@Bc", descricao: "E-mail sem domínio" },
  { email: "teste@email.com", senha: "", descricao: "Senha vazia" },
  { email: "teste@email.com", senha: "1@", descricao: "Senha muito curta" },
  { email: "teste@email.com", senha: "Abc123!@", descricao: "Senha muito longa" },
  { email: "teste@email.com", senha: "@Abc!", descricao: "Senha sem número" },
  { email: "teste@email.com", senha: "Abc123", descricao: "Senha sem caractere especial" },
  { email: "teste@email.com", senha: "abc123@", descricao: "Senha sem letra maiúscula" },
  { email: "teste@email.com", senha: "ABC123@", descricao: "Senha sem letra minúscula" },
  { email: "errado@email.com", senha: "1@Bc", descricao: "Credenciais inválidas" },
  { email: "teste@email.com", senha: "1@Bc", descricao: "Login válido" },
];

describe('Teste de Login - Validações avançadas de e-mail e senha', () => {

  beforeEach(() => {
    cy.visit('http://localhost:5500/login.html');
  });

  testes.forEach((teste) => {
    it(`Cenário: ${teste.descricao}`, () => {

      cy.get('#email').clear().type(teste.email, { delay: 150 });
      cy.get('#password').clear().type(teste.senha, { delay: 150 });

      cy.contains('Entrar').click();

      cy.get('#emailAlert').invoke('text').then(alerta_email => {
        cy.get('#passwordAlert').invoke('text').then(alerta_senha => {
          cy.log(`${teste.descricao}`);
          cy.log(`Email: ${teste.email} | Alerta: ${alerta_email}`);
          cy.log(`Senha: ${teste.senha} | Alerta: ${alerta_senha}`);
        });
      });
    });
  });

});
