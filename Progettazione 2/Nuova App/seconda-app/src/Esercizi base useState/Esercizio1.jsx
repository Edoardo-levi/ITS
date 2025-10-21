import React, { useState } from "react";

function Esercizio1() {
  const [mostra, setMostra] = useState(false);

  return (
    <div>
      <h4>Click per mostrare e nascondere il testo</h4>
      <button onClick={() => setMostra(!mostra)}>
        {mostra ? "Nascondi" : "Mostra"}
      </button> 

      {mostra && <p>Il testo viene mostrato e nascosto correttamnte</p>}
    </div>
  );
}

export default Esercizio1;
