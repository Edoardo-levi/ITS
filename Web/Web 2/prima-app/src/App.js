
import './App.css';
import CambiaNome from './CambiaNome';
import CleanUp from './CleanUp';
import Clock from './Clock';
import Componente1 from './Componente1';
import StampaNumeri from './Esercizi/Stampanumeri';
import Tabellina from './Esercizi/Tabellina';
import LoginForm from './LoginForm';
/*function getDate(date){
   return date.toLocaleDateString() + " " + new Date().toLocaleTimeString()
      }*/


function App() {
  const persona={
    id:"1",
    nome:"Edoardo",
    cognome:"Levi"
  }
  let nome="Edoardo";
   
  return (

    <div className="App">
      <LoginForm></LoginForm>
        <CambiaNome></CambiaNome>

        <Clock timezone="0" country="Italia"></Clock>
        <CleanUp></CleanUp>

        <StampaNumeri></StampaNumeri>
        <Tabellina numero="5"></Tabellina>
        <h1>Primo Elemento{nome}</h1>
        <Componente1 {...persona}></Componente1>
        
        <Componente1/>
        
        <br></br>
        
        <h2>
            {
              new Date().toLocaleDateString() + " " + new Date().toLocaleTimeString()
            }
            <br></br>
            <br></br>
            Importo il componente clock <Clock timezone="0" country="Italia"></Clock>
            <br></br> 
            {/*
            getDate(new Date())
            */}
        </h2>
    </div>
  )
}

export default App;
