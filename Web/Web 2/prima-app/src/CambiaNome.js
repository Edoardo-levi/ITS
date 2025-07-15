import React, { useState } from 'react'

const CambiaNome = () => {
    const [nome,SetNome]= useState("Edoardo")
    const cambiaNome= () => {
        if (nome === "Edoardo"){
            SetNome ("Andrea")
        }
        else {
            SetNome("Edoardo");
        }
    }
  return (
    <div>
        <h3>
            {nome}
        </h3>
        <button 
        className="btn btn-dark" onClick={cambiaNome}>
            CambiaNome
        </button>
        
    </div>
  )
}

export default CambiaNome