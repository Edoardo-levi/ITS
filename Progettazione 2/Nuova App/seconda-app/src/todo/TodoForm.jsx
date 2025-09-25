import React, { useState } from "react";

const TodoForm = ({onAddTask}) => {
  const [todo, setTodo] = useState("");

  const handleSubmit=(e)=>{
    e.preventDefault();
    if(!todo.trim()) return
onAddTask(todo);
   setTodo("");
  }
  return (
    <form className="d-flex mb-3" onSubmit={handleSubmit}>
      <input
        type="text"
        className="form-control me-2"
        value={todo}
        onChange={(e) => {
          setTodo(e.target.value);
        }}
      ></input>
      <button type="submit" className="btn btn-primary">
        Aggiungi
      </button>
    </form>
  );
};

export default TodoForm;