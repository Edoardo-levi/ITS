import React from 'react'

const Tabellina = (props) => {
    const num= [0,1,2,3,4,5,6,7,8,9,10]
  return (
     
    <div>Tabellina
        
        {
           num.map((i)=>{
            return <p>{i*props.numero}</p>
           }) 
        }
    </div>
     
      
      
  )
  
}

export default Tabellina