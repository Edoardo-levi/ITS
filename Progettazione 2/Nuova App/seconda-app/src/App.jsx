import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import UserCrud from './UserCrud'
import Saluto from './Saluto'
import TodoApp from './todo/TodoApp'
import MainComponent from './UseContext/MainComponent'
import ProvaRoutes from './routes/ProvaRoutes'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    {/* <MainComponent></MainComponent>  per mettere i commenti spingere cntrl ù */}
     {/* <TodoApp></TodoApp> */}
     <ProvaRoutes></ProvaRoutes>
    </>
  )
}

export default App
