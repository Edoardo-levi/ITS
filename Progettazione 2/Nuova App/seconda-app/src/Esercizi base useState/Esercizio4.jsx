import React, { useState } from "react";

function SelettorePizza() {
  const [pizza, setPizza] = useState("");

  const handleChange = (event) => {
    setPizza(event.target.value);
  };

  return (
    <div style={{ fontFamily: "Arial", padding: "20px" }}>
      <h2>Scegli la tua pizza preferita</h2>

      <select value={pizza} onChange={handleChange}>
        <option value="">-- Seleziona una pizza --</option>
        <option value="Margherita">Margherita</option>
        <option value="Diavola">Diavola</option>
        <option value="Capricciosa">Capricciosa</option>
        <option value="Quattro Formaggi">Quattro Formaggi</option>
        <option value="Boscaiola">Boscaiola</option>
      </select>

      {pizza && (
        <p>
          Hai scelto la pizza: <h4>{pizza}</h4>
        </p>
      )}
    </div>
  );
}

export default SelettorePizza;
