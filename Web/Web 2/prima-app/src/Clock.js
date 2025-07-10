import React, { useState, useEffect } from 'react'

const Clock = (props) => {
  console.log(props.timezone,props.country)
    const t=Date.now() + 3600*props.timezone*1000
    const date=new Date(t);
    const dataIni= new Date(t)
    const [data,setData] = useState(dataIni)

    useEffect(()=>{
      const interval = setTimeout(()=>{
        const t=data.getTime()+1000
         setData(new Date(t));
      },1000)
      return (()=>{clearInterval(interval)})
    },[data])

  return (
    <h3>In {props.country} sono le : {new Date().toLocaleTimeString() + " "} del giorno { date.toLocaleDateString()}</h3>
  )
}

export default Clock