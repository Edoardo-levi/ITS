import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import UserCrud from './UserCrud'
import Saluto from './Saluto'
import TodoApp from './todo/TodoApp'
import MainComponent from './UseContext/MainComponent'
import ProvaRoutes from './routes/ProvaRoutes'
import Esercizio1 from './Esercizi base useState/Esercizio1'
import Esercizio2 from './Esercizi base useState/Esercizio2'
import Esercizio3 from './Esercizi base useState/Esercizio3'
import Esercizio4 from './Esercizi base useState/Esercizio4'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    {/* <MainComponent></MainComponent>  per mettere i commenti spingere cntrl ù */}
     {/* <TodoApp></TodoApp> */}
     {/* <ProvaRoutes></ProvaRoutes> */}
     {/* <Esercizio1></Esercizio1> */}
      {/* <Esercizio2></Esercizio2>  */}
     {/* <Esercizio3></Esercizio3> */}
     <Esercizio4></Esercizio4>
    </>
  )
}

export default App
