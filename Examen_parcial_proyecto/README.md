# NHAMCS ED 2022 — Transformación y Documentación del Dataset

Este repositorio contiene el flujo reproducible para **convertir**, **limpiar** y **documentar** el dataset público **NHAMCS — Emergency Department 2022**.

---

<h2>Estructura</h2>
<pre>
.
├── 1. Transformacion_dataset/
│ └── Transformacion_Dataset.ipynb # Convierte ed2022_sas.sas7bdat → CSV mínimo y limpio
├── 2. Documentacion_dataset/
│ ├── Documentacion_Dataset.ipynb
│ └── dataset_docs/
│ ├── DATASET.md
│ ├── DATADICT.md
│ ├── DATADICT_full.csv
│ ├── DATADICT_part1.md
│ ├── … / DATADICT_partN.md
│ ├── PROVENANCE.md
│ ├── SHA256SUMS.txt
│ └── DATADICT_bundle.zip
├── 3. Modelo de aprendizaje automatico/
│ ├── 01_modelo_logistico.ipynb # Notebook principal del modelo
│ ├── api/
│ │ └── main.py # FastAPI (/health, /predict, /predict_batch)
│ ├── data/
│ │ └── ed2022_clean_min.csv # Dataset mínimo (16.025 × 771)
│ ├── models/
│ │ ├── pipe.joblib
│ │ ├── calibrated.joblib
│ │ ├── policy.json # {"threshold":0.59,"gray_delta":0.05,"positive_class":2}
│ │ └── meta.json # versión de columnas, SHA256, random_state, etc.
│ └── requirements.txt
└── data/
├── ed2022_clean.csv
└── ed2022_clean_min.csv
</pre>


## Qué se realizó

1. **Transformación (SAS → CSV)**
   - Origen: `ed2022_sas.sas7bdat`.
   - Conversión con `pyreadstat` + `pandas`.
   - Limpieza mínima:
     - Códigos de no-respuesta SAS `-7/-8/-9` → `NaN`.
     - `ARRTIME` (HHMM) → `ARRTIME_ts` (timestamp) y `ARR_HOUR`.
     - `WAITTIME < 0` → `NaN`.
   - Salidas: `data/ed2022_clean.csv` y `data/ed2022_clean_min.csv`.

2. **Documentación automática**
   - **DATASET.md**: ficha técnica (filas, columnas, memoria, SHA256, tipos).
   - **DATADICT.md** + **DATADICT_full.csv**: diccionario por columna (faltantes, cardinalidad, ejemplos).
   - **PROVENANCE.md**: fuente, fecha y pasos reproducibles.
   - **SHA256SUMS.txt**: verificación de integridad del CSV.
   - **DATADICT_part*.md**: el diccionario segmentado (para facilitar carga/visualización).
   - **DATADICT_bundle.zip**: paquete comprimido para revisión externa.


3. **Modelo de aprendizaje automático** 

   * **Notebook principal**: `01_modelo_logistico.ipynb` (pipeline: imputación → one-hot → escalado → Regresión Logística).
   * **Particiones**: `train/valid/test = 60/20/20` estratificadas (`random_state=42`). **Fugas bloqueadas** (sin tiempos/outcomes posteriores).
   * **Calibración**: Platt (sigmoid). **Política**: `threshold=0.59`, `gray_delta=0.05` (zona gris ≈ 9%).
   * **Métricas clave**: VALID (acc ~0.777, macro-F1 ~0.775, AUC ~0.844) · TEST (acc ~0.769, macro-F1 ~0.769, AUC ~0.849).
   * **Artefactos** (`models/`): `pipe.joblib`, `calibrated.joblib`, `policy.json`, `meta.json`.
   * **API** (`api/`): `main.py` con `GET /health`, `POST /predict`, `POST /predict_batch`.
   * **Datos usados**: `data/ed2022_clean_min.csv` (16.025 × 771).
