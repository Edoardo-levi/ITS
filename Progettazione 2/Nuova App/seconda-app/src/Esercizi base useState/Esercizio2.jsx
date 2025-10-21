import { useState } from "react";

const Esercizio2 =() => {
  const [colore, setColore] = useState("black"); 

  return (
    <div className="flex flex-col items-center justify-center min-h-screen gap-6 bg-gray-100">
      
      <h1 style={{ color: colore }} className="text-4xl font-bold">
        Ciao Mondo!
      </h1>

      <div className="flex gap-4">
        <button style={{backgroundColor:"black", color:"red"}}
          onClick={() => setColore("red")}
        >
          Rosso
        </button>
        <button  style={{backgroundColor:"black", color: "green" }}
          onClick={() => setColore("green")}
        >
          Verde
        </button>
        <button style={{ backgroundColor:"black", color: "blue" }}
          onClick={() => setColore("blue")}
        >
          Blu
        </button>
      </div>
    </div>
  );
}

export default Esercizio2;
