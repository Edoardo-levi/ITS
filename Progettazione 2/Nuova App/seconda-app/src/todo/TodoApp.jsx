import React, { useEffect, useState } from 'react'
import TodoForm from './TodoForm'
import TodoList from './TodoList'
import { createTasks, fetchTasks,cancellaTask, ToggleTasks } from '../services/api'


const API_URL = "http://localhost:3000/tasks"
const TodoApp = () => {
    const [tasks, setTasks] = useState([])
    const getTask = async () => {
        try {
            const data = await fetchTasks()
            console.log(data)
            setTasks(data)
        } catch (err) {
            console.log(err)
        }
    }

    const addTask = async (text) => {
        await createTasks(text)
        getTask();
    }
    const deleteTask = async (id) => {
        await cancellaTask(id);
        getTask();

    }
    const toggleTask = async (id, completed) => {
        await ToggleTasks(id,completed)
        
        getTask();
    }
    useEffect(() => {
        getTask()
    }, [])

    return (
        <div>
            TodoApp
            <TodoForm onAddTask={addTask}></TodoForm>
            <TodoList tasks={tasks} onDeleteTask={deleteTask} onToggleTask={toggleTask}></TodoList>

        </div>
    )
}

export default TodoApp