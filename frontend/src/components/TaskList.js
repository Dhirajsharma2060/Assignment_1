import React, { useState, useEffect } from 'react';
import { fetchTasks, createTask, updateTask, deleteTask, deleteAllTasks } from '../services/api';
import TaskForm from './TaskForm';
import './TaskList.css';
import { FaEdit, FaTrash } from 'react-icons/fa';

const TaskList = () => {
    const [tasks, setTasks] = useState([]);
    const [taskToEdit, setTaskToEdit] = useState(null);

    useEffect(() => {
        const getTasks = async () => {
            try {
                const tasks = await fetchTasks();
                setTasks(tasks);
            } catch (error) {
                console.error('Error fetching tasks:', error);
            }
        };

        getTasks();
    }, []);

    const addTask = async (task) => {
        try {
            const newTask = await createTask(task);
            setTasks([...tasks, newTask]);
        } catch (error) {
            console.error('Error adding task:', error);
        }
    };

    const editTask = async (updatedTask) => {
        try {
            const editedTask = await updateTask(updatedTask.id, updatedTask);
            setTasks(tasks.map(task => (task.id === updatedTask.id ? editedTask : task)));
            setTaskToEdit(null);
        } catch (error) {
            console.error('Error editing task:', error);
        }
    };

    const handleEdit = (task) => {
        setTaskToEdit(task);
    };

    const handleDelete = async (taskId) => {
        try {
            await deleteTask(taskId);
            setTasks(tasks.filter(task => task.id !== taskId));
        } catch (error) {
            console.error('Error deleting task:', error);
        }
    };

    const handleClearAll = async () => {
        try {
            await deleteAllTasks();
            setTasks([]);
        } catch (error) {
            console.error('Error clearing tasks:', error);
        }
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