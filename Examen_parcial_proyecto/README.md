# NHAMCS ED 2022 — Transformación y Documentación del Dataset

Este repositorio contiene el flujo reproducible para **convertir**, **limpiar** y **documentar** el dataset público **NHAMCS — Emergency Department 2022**.

---

## Estructura

.
├── 1. Transformacion_dataset/
│   └── Transformacion_Dataset.ipynb        # Transforma ed2022_sas.sas7bdat → CSV (limpio y mínimo)
├── 2. Documentacion_dataset/
│   ├── Documentacion_Dataset.ipynb
│   └── dataset_docs/
│       ├── DATASET.md
│       ├── DATADICT.md
│       ├── DATADICT_full.csv
│       ├── DATADICT_part1.md
│       ├── … 
│       ├── DATADICT_partN.md
│       ├── PROVENANCE.md
│       ├── SHA256SUMS.txt
│       └── DATADICT_bundle.zip
└── data/
    ├── ed2022_clean.csv
    └── ed2022_clean_min.csv



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

