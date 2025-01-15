import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const axiosInstance = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

axiosInstance.interceptors.request.use(request => {
    console.log('Starting Request', request);
    return request;
});

axiosInstance.interceptors.response.use(response => {
    console.log('Response:', response);
    return response;
});

export const fetchTasks = async () => {
    try {
        const response = await axiosInstance.get('/tasks');
        return response.data;
    } catch (error) {
        console.error('Error fetching tasks:', error);
        throw error;
    }
};

export const fetchTask = async (taskId) => {
    try {
        const response = await axiosInstance.get(`/tasks/${taskId}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching task:', error);
        throw error;
    }
};

export const createTask = async (task) => {
    try {
        const response = await axiosInstance.post('/tasks', task);
        return response.data;
    } catch (error) {
        console.error('Error creating task:', error);
        throw error;
    }
};

export const updateTask = async (taskId, task) => {
    try {
        const response = await axiosInstance.patch(`/tasks/${taskId}`, task);
        return response.data;
    } catch (error) {
        console.error('Error updating task:', error);
        throw error;
    }
};

export const deleteTask = async (taskId) => {
    try {
        const response = await axiosInstance.delete(`/tasks/${taskId}`);
        return response.data;
    } catch (error) {
        console.error('Error deleting task:', error);
        throw error;
    }
};

export const deleteAllTasks = async () => {
    try {
        const response = await axiosInstance.delete('/tasks');
        return response.data;
    } catch (error) {
        console.error('Error deleting all tasks:', error);
        throw error;
    }
};