# PROVENANCE.md — Origen y trazabilidad

- **Fuente original**: archivo SAS NHAMCS ED 2022 (`ed2022_sas.sas7bdat`).  
- **Conversión**: SAS → CSV realizada en Jupyter con `pyreadstat` + `pandas`.  
- **Archivo actual**: `ed2022_clean_min.csv` | **Tamaño**: 24.82 MB | **SHA256**: `7d6fbba43814945bb624b00799a69caddd4d015979942b37165d0c7d9ea9fffc`  
- **Fecha de conversión**: 2025-10-20  
- **Licencia/uso**: Uso académico – NHAMCS/CDC 2022 (ver condiciones de NCHS/CDC).

## Pasos reproducibles
1. `df, meta = pyreadstat.read_sas7bdat('ed2022_sas.sas7bdat')`
2. Limpieza mínima: códigos -7/-8/-9 → NaN; `ARRTIME` → `ARRTIME_ts`/`ARR_HOUR`; `WAITTIME<0` → NaN.
3. Depuración: eliminación de columnas 100% NaN y constantes; remoción de `ARRTIME` (redundante).
4. `df.to_csv('ed2022_clean_min.csv', index=False, encoding='utf-8')`
