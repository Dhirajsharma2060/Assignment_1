import React, { useState, useEffect } from 'react';
import './TaskForm.css';

const TaskForm = ({ addTask, editTask, taskToEdit, totalTasks }) => {
    const [name, setName] = useState('');
    const [status, setStatus] = useState(false);

    useEffect(() => {
        if (taskToEdit) {
            setName(taskToEdit.name);
            setStatus(taskToEdit.status);
        }
    }, [taskToEdit]);

    const handleSubmit = (e) => {
        e.preventDefault();
        const timestamp = new Date().toLocaleString();
        if (name) {
            if (taskToEdit) {
                editTask({ ...taskToEdit, name, status, timestamp });
            } else {
                addTask({ name, status, timestamp });
            }
            setName('');
            setStatus(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="task-form card">
            <div className="form-group">
                <label>Task Name:</label>
                <input
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    placeholder="Enter task name"
                />
            </div>
            <div className="form-group">
                <label>Status:</label>
                <input
                    type="checkbox"
                    checked={status}
                    onChange={(e) => setStatus(e.target.checked)}
                />
            </div>
            <button type="submit" className="btn add-btn">+</button>
            <p className="task-count">You have {totalTasks} tasks remaining</p>
        </form>
    );
};

export default TaskForm;