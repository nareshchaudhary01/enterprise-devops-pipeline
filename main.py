import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Enterprise Microservice")

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENV_NAME = os.getenv("ENV_NAME", "Local-Dev")

@app.get("/", response_class=HTMLResponse)
def root():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Enterprise DevOps App</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0b0f19; color: #e2e8f0; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
            .card {{ background: #1e293b; border-radius: 12px; padding: 30px; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.5); text-align: center; border: 1px solid #334155; width: 380px; }}
            h1 {{ color: #38bdf8; font-size: 22px; margin-bottom: 5px; }}
            .status {{ background: #10b981; color: #000; font-weight: bold; padding: 4px 12px; border-radius: 9999px; font-size: 12px; display: inline-block; margin-bottom: 15px; }}
            .info {{ background: #0f172a; padding: 12px; border-radius: 8px; text-align: left; font-size: 13px; font-family: monospace; border: 1px solid #334155; margin-top: 15px; }}
            .info p {{ margin: 4px 0; color: #94a3b8; }}
            .info span {{ color: #f43f5e; }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="status">● EKS CLUSTER READY</div>
            <h1>Enterprise DevOps Node</h1>
            <p style="color: #64748b; font-size: 13px;">FastAPI Microservice Running</p>
            <div class="info">
                <p>Environment: <span>{ENV_NAME}</span></p>
                <p>App Version: <span>{APP_VERSION}</span></p>
                <p>Scaling Engine: <span>AWS EKS Pod</span></p>
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "healthy", "version": APP_VERSION, "environment": ENV_NAME}