# AI Orchestration System

A simple AI orchestration system that simulates a small software company workflow:

```text
User Goal -> CEO Agent -> CTO Agent -> Dev Agent -> QA Agent -> Final Output
```

The orchestrator controls the execution order. Agents receive shared state, update it, and return it.

## Run Phase 1

```powershell
python -m backend.run_phase1 "Create a hello world Python script"
```

## Run API

```powershell
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
```

Then open:

```text
http://127.0.0.1:8000/run?goal=Create%20a%20hello%20world%20Python%20script
```

## Optional OpenRouter Setup

```powershell
$env:OPENROUTER_API_KEY="your_key_here"
$env:OPENROUTER_MODEL="deepseek/deepseek-chat-v3-0324:free"
```
