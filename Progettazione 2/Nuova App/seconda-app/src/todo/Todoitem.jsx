
import React from "react";


const Todoitem = ({task,onDeleteTask,onToggleTask}) => {
  return (
    <li className="list-group-item d-flex justify-content-between">
      <div>
        <input
          className="form-check-input me-2"
          type="checkbox"
          checked={task.completed}
          onChange={()=>{onToggleTask(task.id,task.completed)}}
        ></input>
        <span
          style={{
            textDecoration: task.completed ? "line-through" : "none",
          }}
        >
          {task.text}
        </span>
      </div>
      <button
        className="btn btn-danger"
        onClick={() => {
          onDeleteTask(task.id);
        }}
      >
        Delete
      </button>
    </li>
  );
};

export default Todoitem;