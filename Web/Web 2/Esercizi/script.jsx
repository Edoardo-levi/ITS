const rootElement= document.querySelector("#root");

const root = ReactDOM.createRoot(rootElement)

const App= () => {
    return(
        <main className="main" id="main">
            <h1>Primo Componente</h1>
        </main>
    )
}

root.render(
    <App></App>
)