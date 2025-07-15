import React, { useState } from 'react'

const LoginForm = () => {
    const [nome, setNome] = useState ("")
    const [cognome, setCognome] = useState("")
  return (
    <div className="container">
      <form className="row g-3">
        <div className="col-md-6">
          <label htmlFor="nome">Nome</label>
          <input
            type="text"
            id="nome"
            className="form-control"
            required
            value={nome}
            onChange={(event) => setNome(event.target.value)}
          ></input>
        </div>
        <div className="col-md-6">
          <label htmlFor="cognome">Cognome</label>
          <input
            type="text"
            id="cognome"
            required
            value={cognome}
            onChange={(event) => setCognome(event.target.value)}
          ></input>
        </div>

        <button className="btn btn-success">Login</button>
      </form>
      
    </div>
    
  )
}

export default LoginForm