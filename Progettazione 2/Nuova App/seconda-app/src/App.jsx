import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import UserCrud from './UserCrud'
import Saluto from './Saluto'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <Saluto></Saluto>
    </>
  )
}

export default App
