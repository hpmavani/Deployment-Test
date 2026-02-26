from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

app = FastAPI(
    title="Test FastAPI App",
    description="A simple FastAPI application for testing Render deployment",
    version="1.0.0"
)


@app.get("/")
async def root():
    """Root endpoint that returns a welcome message."""
    return {
        "message": "Welcome to the Test FastAPI App!",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {
        "status": "healthy",
        "service": "test-fastapi-app"
    }


@app.get("/api/items/{item_id}")
async def get_item(item_id: int, q: str = None):
    """Get an item by ID with optional query parameter."""
    return {
        "item_id": item_id,
        "query": q,
        "message": f"Retrieved item {item_id}"
    }


@app.post("/api/items")
async def create_item(name: str, description: str = None):
    """Create a new item."""
    return {
        "name": name,
        "description": description,
        "message": "Item created successfully"
    }


@app.get("/config")
async def get_config():
    """Get current configuration."""
    return {
        "environment": os.getenv("ENVIRONMENT", "development"),
        "debug": os.getenv("DEBUG", "False") == "True"
    }


@app.websocket("/ws/chat")
async def chat_ws(websocket: WebSocket):
    """Simple websocket chat endpoint that echoes incoming messages.

    This simulates chatbot-style traffic without calling an actual LLM. The
    client can send text messages and the server replies with a prefixed
    acknowledgment. Useful for exercising WebSocket load handling.
    """
    await websocket.accept()
    try:
        while True:
            text = await websocket.receive_text()
            # pretend to "process" the message then echo it back
            await websocket.send_text(f"You said: {text}")
    except WebSocketDisconnect:
        # client closed connection
        pass


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
