import React, { useEffect, useState } from 'react'

const CleanUp = () => {

    const [size, setSize]= useState(window.innerWidth);

    const dimensione= () => {
        setSize(window.innerWidth)
    }

    useEffect (()=> {
        window.addEventListener("resize", dimensione)
        return (()=>{
            window.removeEventListener("resize", dimensione)
        })
    })

  return (
    <h2>dimensione schermo:{size}</h2>
  )
}

export default CleanUp