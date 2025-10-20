# DATASET.md — Descripción técnica del dataset

**Nombre**: NHAMCS — Emergency Department 2022 (CSV depurado).  
**Archivo**: `ed2022_clean_min.csv`  
**Filas**: **16025**  
**Columnas**: **771**  
**Tamaño en disco (CSV)**: **24.82 MB**  
**Uso de memoria aprox. (pandas)**: **114.49 MB**  
**SHA256**: 7d6fbba43814945bb624b00799a69caddd4d015979942b37165d0c7d9ea9fffc

## Tipos de datos (inferidos por pandas)
- Numéricas: 728
- Fechas/horas: 1
- Categóricas/Textuales: 42

## Calidad inicial (resumen)
- **Depuración aplicada:** 72 columnas 100% NaN y 72 constantes fueron removidas; ver `dropped_columns.csv`.
- Columnas con faltantes (>0%): 613 / 771
- Columnas sin faltantes: 158
- Columnas con alta cardinalidad (unique > 500): 20

> Nota: Los **labels/definiciones** originales de SAS no vienen en el CSV. Deben completarse con el **diccionario oficial NHAMCS 2022**.

Para el detalle por columna, ver **DATADICT.md**.
