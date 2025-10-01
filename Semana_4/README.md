# 📚 Aprendizaje Automático – Clase 4

## 📌 Descripción
En esta clase se trabajaron dos actividades principales:  
1. **Regresión Lineal Múltiple** aplicada a un dataset con variables relacionadas a la **presión arterial**.  
2. **Regresión Logística Multiclase** aplicada a un dataset de **usuarios** para predecir el sistema operativo utilizado (Windows, Macintosh, Linux).  

El objetivo fue comprender la diferencia entre problemas de **regresión** y **clasificación supervisada**, aplicar los modelos en Python con *scikit-learn* y evaluar sus resultados.

---

## 📂 Actividad 1 — Regresión Lineal Múltiple
- **Dataset**: `dataset_regresion_multiple.csv`  
- **Objetivo**: predecir la presión arterial en función de variables como edad, peso, estrés, horas de ejercicio, ingresos y horas de TV.  
- **Trabajo realizado**:
  - Análisis exploratorio (estadísticos, correlaciones, visualizaciones).  
  - Modelo de regresión múltiple con **todas las variables**.  
  - Comparación con un modelo reducido usando solo las más influyentes.  
  - Evaluación con métricas: **R², RMSE, MAE**.  
- **Conclusión**: las variables más influyentes fueron **edad, peso, nivel de estrés y horas de ejercicio**. Ingresos y horas de TV tuvieron menor impacto en la predicción.  

---

## 📂 Actividad 2 — Regresión Logística Multiclase
- **Dataset**: `usuarios_win_mac_lin.csv`  
- **Objetivo**: clasificar usuarios en **Windows, Macintosh o Linux** según variables de uso (duración, páginas vistas, acciones, valor).  
- **Trabajo realizado**:
  - División en entrenamiento (70%) y prueba (30%).  
  - Entrenamiento de un modelo de **Regresión Logística Multiclase**.  
  - Evaluación con métricas: **accuracy, reporte de clasificación y matriz de confusión**.  
- **Resultados**:  
  - Accuracy en test: **0.73**.  
  - Buen desempeño en **Windows y Linux**, más dificultad en **Macintosh** (recall más bajo).  
- **Conclusión**: la regresión logística es un modelo simple pero efectivo para este problema. Podría mejorar con más datos o ajuste de parámetros, sobre todo para la clase Macintosh.  

---

## 🚀 Tecnologías utilizadas
- Python  
- NumPy  
- Pandas  
- Matplotlib  
- Seaborn  
- scikit-learn  

---

## 👤 Autor
Trabajo realizado como parte de la materia **Aprendizaje Automático**.  
