import React from 'react'

const StampaNumeri = () => {
    const num= [0,1,2,3,4,5,6,7,8,9,10]
  return (
     
    <div>StampaNumeri
        
        {
           num.map((i)=>{
            return <p>{i}</p>
           }) 
        }
    </div>
     
      
      
  )
  
}

export default StampaNumeri