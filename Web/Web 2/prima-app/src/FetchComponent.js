import React, { useEffect, useState } from 'react'

const FetchComponent = () => {
    const url= "https://jsonplaceholder.typicode.com/users"
    const [users,setUsers]=useState([])
    const getUsers= async ()=> {
        const response= await fetch(url)   
        const result = await response.json()
        setUsers(result)
    }
    useEffect(()=> {
       /* fetch(url)
        .then(response=>response.json())
        .then(ris=>setUsers(ris))
        */
        getUsers()
    },[])

  return (
    <>
    <div>
        <h1> Fetch user form jsonplacheolder</h1>
        {
            users.map((u)=>{
                return <p key={u.id}>{u.name}</p>
            })
        }
    </div>
    </>
  )
}

export default FetchComponent