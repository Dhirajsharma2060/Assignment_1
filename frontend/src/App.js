// filepath: /home/dhiraj2060/Documents/assignments/Dimentionless/frontend/src/App.js
import React from 'react';
import TaskList from './components/TaskList';
import './App.css';

function App() {
    return (
        <div className="App">
            <div className="container">
                <h1 className="app-title">Todo App</h1>
                <TaskList />
            </div>
        </div>
    );
}

export default App;