const rootElement= document.querySelector("#root");

const root = ReactDOM.createRoot(rootElement)

const App= (props) => {
    return(
        <main className="main" id="main">
            <h1>Primo Componente</h1>
            {props.children}
        </main>
    )
}
const List=()=>{
    return (
        <ul>
            <li>Php</li>
            <li>JS</li>
            <li>Pyhton</li>
        </ul>
    )
}

root.render(
    <>
    <App>
        <h2>
            Lista competenze
        </h2>
        <List></List>
    </App>
    
    </>
)