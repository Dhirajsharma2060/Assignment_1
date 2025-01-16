# Assignment_1

## Overview

This project is a full-stack web application that allows users to manage tasks. It includes a frontend built with React and a backend built with FastAPI. The application is deployed on Render, with the frontend served as a static site and the backend running as a web service. The database used is PostgreSQL, also hosted on Render.

## Tech Stack

### Frontend
- **React**: A JavaScript library for building user interfaces.
- **Axios**: A promise-based HTTP client for making API requests.
- **React Icons**: A library for including popular icons in React projects.

### Backend
- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **SQLAlchemy**: The Python SQL toolkit and Object-Relational Mapping (ORM) library.
- **Pydantic**: Data validation and settings management using Python type annotations.

### Database
- **PostgreSQL**: A powerful, open-source object-relational database system.

### Deployment
- **Render**: A unified cloud to build and run all your apps and websites with free SSL, a global CDN, private networks, and auto deploys from Git.

## Why FastAPI?

FastAPI was chosen for the backend because of its:
- **Automatic interactive API documentation**: FastAPI provides interactive API documentation with Swagger UI, making it easier to test and debug APIs.
- **High performance**: FastAPI is one of the fastest Python web frameworks available.
- **Ease of use**: FastAPI allows for rapid development and easy maintenance.

## Live Links

- **Frontend**: [https://frontend-5w9c.onrender.com](https://frontend-5w9c.onrender.com)
- **Backend API Docs**: [https://todo-app-myh1.onrender.com/docs](https://todo-app-myh1.onrender.com/docs)

## Local Development

### Prerequisites

- **Node.js**: Ensure you have Node.js installed. You can download it from [nodejs.org](https://nodejs.org/).
- **Python**: Ensure you have Python 3.6+ installed. You can download it from [python.org](https://www.python.org/).
- **PostgreSQL**: Ensure you have PostgreSQL installed. You can download it from [postgresql.org](https://www.postgresql.org/).

### Frontend Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo/frontend
   ```
2. Install dependencies:
    ```sh
    npm install
    ```
3.  Create a .env file in the frontend directory and add the following:
    ```sh
    REACT_APP_API_URL=http://localhost:8000
    ```
4.  Start the development server:
    ```sh
    npm start
    ```
### Backend Setup
1. Navigate to the backend directory:
   ```sh
   cd ../backend
   ```
2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate` similar for the linux as well
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Create a .env file in the backend directory and add your PostgreSQL connection URL:
    ```sh
    DATABASE_URL=postgresql://username:password@localhost:5432/yourdatabase
    ```
5.  Start the backend server:
    ```sh
    uvicorn main:app --reload
    ```
## Secure Steps
- **Environment Variables**: Ensure that sensitive information such as database credentials and API keys are stored in environment variables and not hard-coded in the source code.
- **HTTPS**: Use HTTPS to encrypt data transmitted between the client and server.
- **CORS**: Configure CORS to allow only trusted origins to access your API.
### Testing
- **Frontend**: Access the frontend at http://localhost:3000.
- **Backend**: Access the backend API documentation at http://localhost:8000/docs.  

## Deployment
### Frontend
1. Build the frontend:
   ```sh
   npm run build
   ```
2. Deploy the build directory to your static site hosting provider (e.g., Render).

## Backend
1. Push your backend code to your GitHub repository.
2. Create a new web service on Render and connect it to your GitHub repository.
3. Configure the environment variables and deploy the backend.
## License
This project is licensed under the MIT License. See the LICENSE file for details.

### Summary:
- **Overview**: Provides a brief description of the project.
- **Tech Stack**: Lists the technologies used in the project.
- **Why FastAPI**: Explains why FastAPI was chosen for the backend.
- **Live Links**: Provides links to the live frontend and backend API documentation.
- **Local Development**: Provides steps to set up the project locally.
- **Secure Steps**: Lists steps to ensure the project is secure.
- **Testing**: Provides information on how to test the project locally.
- **Deployment**: Provides steps to deploy the frontend and backend.
- **License**: Provides information about the project's license.

This `README.md` file should provide a comprehensive guide to your project, including setup, deployment, and testing instructions.
### Summary:
- **Overview**: Provides a brief description of the project.
- **Tech Stack**: Lists the technologies used in the project.
- **Why FastAPI**: Explains why FastAPI was chosen for the backend.
- **Live Links**: Provides links to the live frontend and backend API documentation.
- **Local Development**: Provides steps to set up the project locally.
- **Secure Steps**: Lists steps to ensure the project is secure.
- **Testing**: Provides information on how to test the project locally.
- **Deployment**: Provides steps to deploy the frontend and backend.
- **License**: Provides information about the project's license.

This `README.md` file should provide a comprehensive guide to your project, including setup, deployment, and testing instructions.

   

