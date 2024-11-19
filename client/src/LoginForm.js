import React from "react";

function LoginForm() {
  return (
    <form action="entrada1" method="post">
      <div>
        <label htmlFor="email">Email:</label>
        <input type="text" id="email" name="email" />
      </div>
      <div>
        <label htmlFor="senha">Senha:</label>
        <input type="text" id="senha" name="senha" />
      </div>
      <button type="submit">Enviar</button>
    </form>
  );
}

export default LoginForm;
