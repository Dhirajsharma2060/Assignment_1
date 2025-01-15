import React, { useState } from 'react';
import TaskForm from './TaskForm';
import './TaskList.css';
import { FaEdit, FaTrash } from 'react-icons/fa';

const TaskList = () => {
    const [tasks, setTasks] = useState([]);
    const [taskToEdit, setTaskToEdit] = useState(null);

    const addTask = (task) => {
        setTasks([...tasks, { ...task, id: tasks.length + 1 }]);
    };

    const editTask = (updatedTask) => {
        setTasks(tasks.map(task => (task.id === updatedTask.id ? updatedTask : task)));
        setTaskToEdit(null);
    };

    const handleEdit = (task) => {
        setTaskToEdit(task);
    };

    const handleDelete = (taskId) => {
        setTasks(tasks.filter(task => task.id !== taskId));
    };

    const handleClearAll = () => {
        setTasks([]);
    };

    return (
        <div className="task-list">
            <TaskForm addTask={addTask} editTask={editTask} taskToEdit={taskToEdit} totalTasks={tasks.length} />
            <button onClick={handleClearAll} className="clear-all-btn">Clear All Tasks</button>
            <ul>
                {tasks.map(task => (
                    <li key={task.id} className="task-item card">
                        <div>
                            <h3>{task.name}</h3>
                            <p>Status: {task.status ? 'Completed' : 'Pending'}</p>
                            <p>Added/Updated: {task.timestamp}</p>
                        </div>
                        <div>
                            <button onClick={() => handleEdit(task)} className="edit-btn">
                                <FaEdit />
                            </button>
                            <button onClick={() => handleDelete(task.id)} className="delete-btn">
                                <FaTrash />
                            </button>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TaskList;