import { useState, useEffect } from "react";


const API_URL = "/api/users";
const UserCrud = () => {
  const [users, setUsers] = useState([]);
  const [formData,setFormData]=useState({
    id: null,
      nome: "",
      cognome: "",
      email: "",
      telefono: ""
  })


  const [isEditing,setIsEditing]=useState(false)


  const getUsers = async () => {
    const response = await fetch(API_URL);
    const result = await response.json();
    setUsers(result);
  };
  useEffect(() => {
    getUsers();
  }, []);


  const handleDelete = async(id)=>{
    if(window.confirm("Sei sicuro di voler coancellare questo utente?")){
       try{
            const response= await fetch(API_URL+"/"+id,{
                method:"DELETE"
            });
        if(!response.ok) throw new Error("La chiamata non è andata a buon fine");
        getUsers();
       }catch(err){
        console.log(err)
       }
    }
  }


  const handlerInput=(e)=>{
    const {name,value}=e.target
    setFormData(prev=>({
      ...prev,
      [name]:value
    }))
  }


  const handlerEdit=(user)=>{
      setFormData(user)
      setIsEditing(true)
  }


  const onSubmit= async()=>{
      const method= isEditing ? "PUT" :"POST";
      const url= isEditing ? API_URL+"/"+formData.id :API_URL;
      try{
        const response= await fetch(url,{
          method,
          headers:{"Content-type":"application/json"},
          body:JSON.stringify({
            ...formData,
            id: isEditing ? formData.id: undefined
          })
        })
          if(!response.ok) throw new Error("Errore su inserimento o modifica")
      }catch(err){
        console.log(err)
      }
  }


  const resetForm=()=>{
     setFormData({ id: null, nome: "", cognome: "", telefono: "", email: "" });
    setIsEditing(false);
  }


  const handlerSubmit=(e)=>{
    e.preventDefault()
    onSubmit()
    getUsers()
    resetForm()
  }
  return (
    <div className="container my-5">
      <h1 className="mb-4">USER CRUD</h1>
<div className="card shado-sm mb-4">
          <div className="card-body">
             <h2 className="card-title mb-4">Gestione utente</h2>
             <form onSubmit={handlerSubmit}>
         
          <div className="row g-3 mb-3">
            <div className="col-md-6">
              <label htmlFor="nome" className="form-label fw-bold">Nome *</label>
              <input
                type="text"
                id="nome"
                name="nome"
                className="form-control"
                value={formData.nome}
                onChange={handlerInput}
                required
              />
            </div>
            <div className="col-md-6">
              <label htmlFor="cognome" className="form-label fw-bold">Cognome *</label>
              <input
                type="text"
                id="cognome"
                name="cognome"
                className="form-control"
                  value={formData.cognome}
                   onChange={handlerInput}
                required
              />
            </div>
          </div>
          <div className="row g-3 mb-4">
            <div className="col-md-6">
              <label htmlFor="telefono" className="form-label fw-bold">Telefono</label>
              <input
                type="tel"
                id="telefono"
                name="telefono"
                className="form-control"
                  value={formData.telefono}
                   onChange={handlerInput}
              />
            </div>
            <div className="col-md-6">
              <label htmlFor="email" className="form-label fw-bold">Email *</label>
              <input
                type="email"
                id="email"
                name="email"
                className="form-control"
                 value={formData.email}
                  onChange={handlerInput}
                required
              />
            </div>
          </div>
          <div className="d-flex gap-2">
            <button type="submit" className="btn btn-primary">
            {isEditing ? "Modifica" : "Inserisci"}
            </button>
                  
          </div>
        </form>
          </div>
        </div>
      <div className="table-responsive">
        <table className="table table-hover table-bordered align-middle">
          <thead className="table-light">
            <tr>
              <th>Nome</th>
              <th>Cognome</th>
              <th>Telefono</th>
              <th>Email</th>
              <th>Azioni</th>
            </tr>
          </thead>
          <tbody>
            {users.map((u) => {
              return (
                <tr key={u.id}>
                  <td>{u.nome}</td>
                  <td>{u.cognome}</td>
                  <td>{u.telefono}</td>
                  <td>{u.email}</td>
                  <td><button className="btn btn-primary" onClick={()=>handlerEdit(u)}>Modifica</button> <button className="btn btn-danger" onClick={()=>handleDelete(u.id)}>Elimina</button></td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};


export default UserCrud;
