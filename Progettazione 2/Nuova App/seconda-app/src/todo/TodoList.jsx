import React from 'react'
import Todoitem from './Todoitem'

const TodoList = (props) => {

    return (
        <ul className='list-group'>
            {
                props.tasks.map((task) => {
                    return (<Todoitem 
                    key={task.id} 
                    task={task}
                    onDeleteTask={props.onDeleteTask}
                    onToggleTask={props.onToggleTask}>

                    </Todoitem>)
                })
            }


        </ul>
    )
}

export default TodoList