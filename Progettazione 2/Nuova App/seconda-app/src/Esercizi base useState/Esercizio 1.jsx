import React, { useState } from "react";

function MostraNascondiTesto() {
  const [mostra, setMostra] = useState(false);

  return (
    <div>
      <button onClick={() => setMostra(!mostra)}>
        {mostra ? "Nascondi" : "Mostra"}
      </button>

      {mostra && <p>mostra e nascondi il testo</p>}
    </div>
  );
}

export default MostraNascondiTesto;
