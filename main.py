from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import run_analysis
import os

app = FastAPI(title="Financial Agent API")

class RequestPayload(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
async def analyze_text(payload: RequestPayload):
    try:
        result = await run_analysis(payload.text)
        return {"status": "success", "analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)