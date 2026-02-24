# Test FastAPI Application

A simple FastAPI application for testing deployment on Render.

## Features

- REST API endpoints
- Health check endpoint
- CRUD operations example
- Automatic API documentation (Swagger UI)

## Local Development

### Prerequisites
- Python 3.11 or higher
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/hpmavani/Deployment-Test.git
cd Deployment-Test
```

2. Create a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Locally

Start the development server:
```bash
python main.py
```

The application will be available at `http://localhost:8000`

### API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Available Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /api/items/{item_id}` - Get item by ID
- `POST /api/items` - Create a new item
- `GET /config` - Get current configuration

## Deployment on Render

### Steps to Deploy

1. Push the code to GitHub (if not already done)

2. Go to [Render](https://render.com) and sign up/log in

3. Click "New +" and select "Web Service"

4. Connect your GitHub repository

5. Configure the service:
   - **Name**: `test-fastapi-app` (or your preferred name)
   - **Runtime**: Python 3.11
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

6. Click "Create Web Service"

The application will be deployed and accessible at a URL like `https://test-fastapi-app.onrender.com`

### Environment Variables

You can add environment variables in the Render dashboard:
- `ENVIRONMENT` - Set to `production`
- `DEBUG` - Set to `False` in production

## Project Structure

```
Deployment-Test/
├── main.py           # FastAPI application
├── requirements.txt  # Python dependencies
├── render.yaml       # Render deployment configuration
├── .gitignore        # Git ignore rules
├── README.md         # This file
└── LICENSE           # License file
```

## Testing the Deployment

After deployment, you can test the endpoints:

```bash
# Test root endpoint
curl https://your-app-name.onrender.com/

# Test health check
curl https://your-app-name.onrender.com/health

# Test item endpoint
curl "https://your-app-name.onrender.com/api/items/1?q=test"
```

## License

This project is licensed under the terms in the LICENSE file.