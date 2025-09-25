import React, { useEffect, useState } from 'react'
import TodoForm from './TodoForm'
import TodoList from './TodoList'

const API_URL = "http://localhost:3000/tasks"
const TodoApp = () => {
    const [tasks, setTasks] = useState([])
    const getTask = async () => {
        try {
            const response = await fetch(API_URL)
            if (!response.ok) throw new Error("Errore Fetch")

            const data = await response.json();
            console.log(data)
            setTasks(data)
        } catch (err) {
            console.log(err)
        }
    }

   const addTask=async (text) =>{
    await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body:JSON.stringify({text,completed:false})
    });
    getTask();
  }
    const deleteTask=async (id)=>{
        await fetch(API_URL +"/"+id,{method:"DELETE"});
            getTask();
        
    }
    const toggleTask=async(id,completed)=>{
        await fetch(API_URL +"/"+id,
            {
                method:"PATCH",
                headers:{"Content-Type":"application/json"},
                body:JSON.stringify({completed:!completed})
            });
            getTask();
    }
    useEffect(()=>{
        getTask()
    },[])

    return (
        <div>
            TodoApp
            <TodoForm onAddTask={addTask}></TodoForm>
            <TodoList tasks={tasks} onDeleteTask={deleteTask} onToggleTask={toggleTask}></TodoList>

        </div>
    )
}

export default TodoApp