# API mínima para servir el modelo calibrado con política.
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd, numpy as np, joblib, json
from pathlib import Path
from typing import List, Dict

MODELS = Path("models")
pipe = joblib.load(MODELS / "pipe.joblib")
cal  = joblib.load(MODELS / "calibrated.joblib")
META = json.loads((MODELS / "meta.json").read_text(encoding="utf-8"))
POLICY = json.loads((MODELS / "policy.json").read_text(encoding="utf-8"))

IDX2 = int(np.where(np.array(META["classes"]) == POLICY["positive_class"])[0][0])
COLS = META["columns_expected"]
TH, DELTA = POLICY["threshold"], POLICY["gray_delta"]

app = FastAPI(title="NHAMCS Triage API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class Record(BaseModel):
    data: Dict  # un paciente (columna -> valor)

class Batch(BaseModel):
    data: List[Dict]  # varios pacientes

def predict_df(df: pd.DataFrame):
    df = df.astype(object).reindex(columns=COLS)
    p2 = cal.predict_proba(df)[:, IDX2]
    y = np.where(p2 >= TH, 2, 1)
    zone = np.where((p2 >= TH - DELTA) & (p2 <= TH + DELTA), "gray", "decided")
    return y.tolist(), p2.tolist(), zone.tolist()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict_one(item: Record):
    y, p, z = predict_df(pd.DataFrame([item.data]))
    return {"pred": y[0], "proba": p[0], "zone": z[0]}

@app.post("/predict_batch")
def predict_batch(batch: Batch):
    y, p, z = predict_df(pd.DataFrame(batch.data))
    return {"pred": y, "proba": p, "zone": z}
