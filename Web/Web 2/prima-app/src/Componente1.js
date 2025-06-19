import React from 'react'

const Componente1 = (props) => {
  const anni = 20
  const divStyle={
        color: "red",
        fontWeight: "600",
        margin: "5px",
        border: "1px #000 solid",
        padding: "15px",
      
        
    }
  return (

    <div 
      style={divStyle}>
       {props.nome} {props.cognome} di anni {anni}
      
      <Anagrafica />
      <Messaggio />
    </div>
  )
}
const Anagrafica = () => {
  return (
    <div>Anagrafica</div>
  )
}
const Messaggio = () => {
  return (
    <div>Messaggio</div>
  )
}

export default Componente1