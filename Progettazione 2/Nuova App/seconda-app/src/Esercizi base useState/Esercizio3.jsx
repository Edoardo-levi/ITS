import { useState } from "react";

const Esercizio3=()=> {
  const [testo, setTesto] = useState("");

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <input
        type="text"
        placeholder="Scrivi qualcosa..."
        value={testo}
        onChange={(e) => setTesto(e.target.value)}
        style={{ padding: "8px", fontSize: "16px" }}
      />
      <p style={{ marginTop: "20px", fontSize: "18px", fontWeight: "bold" }}>
        Hai scritto: <p></p>{testo}
      </p>
    </div>
  );
}
export default  Esercizio3