import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import UserCrud from './UserCrud'
import Saluto from './Saluto'
import TodoApp from './todo/TodoApp'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <TodoApp></TodoApp>
    </>
  )
}

export default App
