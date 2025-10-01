import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import UserCrud from './UserCrud'
import Saluto from './Saluto'
import TodoApp from './todo/TodoApp'
import MainComponent from './UseContext/MainComponent'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    {/* <MainComponent></MainComponent>  per mettere i commenti spingere cntrl ù */}
     <TodoApp></TodoApp>
    </>
  )
}

export default App
