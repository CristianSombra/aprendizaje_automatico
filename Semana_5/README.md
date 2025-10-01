# 🧠 Comparación de Algoritmos de Clasificación: KNN vs Árbol de Decisión

## 📌 Descripción
En este ejercicio se trabajó con el dataset **Breast Cancer Wisconsin**, incluido en la librería *scikit-learn*.  
El objetivo fue aplicar y comparar dos algoritmos de clasificación supervisada:  

- **K-Nearest Neighbors (KNN)**  
- **Árbol de Decisión**  

La idea fue evaluar el rendimiento de cada modelo en la predicción de tumores **benignos** o **malignos**, y analizar sus fortalezas y debilidades.  

---

## 📂 Dataset
- **Fuente**: `sklearn.datasets.load_breast_cancer`  
- **Características**: 30 variables que describen medidas de células tumorales.  
- **Clases objetivo**:  
  - `0 = malignant` (maligno)  
  - `1 = benign` (benigno)  

---

## 🔎 Análisis de resultados

- **KNN**: anda bien, pero depende mucho del valor de *k* y de que las variables estén escaladas.  
  Es fácil de usar pero puede volverse lento si el dataset crece.  

- **Árbol de Decisión**: es más fácil de interpretar porque muestra claramente qué variables pesan más.  
  El problema es que si lo hago muy simple pierde precisión, y si lo dejo crecer demasiado se sobreajusta.  

👉 En este caso los dos modelos funcionan bien, pero el árbol me da más claridad para explicar cómo toma las decisiones.  

---

## 📊 Conclusión

En este trabajo probé dos algoritmos de clasificación sobre el dataset **Breast Cancer**: **KNN** y **Árbol de Decisión**.  
Ambos modelos lograron buenos resultados en términos de precisión.  

- El **KNN** funcionó bien, aunque depende de elegir un buen valor de *k* y de escalar las variables.  
- El **Árbol de Decisión** resultó más fácil de interpretar, mostrando de forma clara qué características tienen mayor peso en la clasificación.  

👉 En resumen, los dos modelos cumplen, pero el Árbol de Decisión aporta mayor interpretabilidad, mientras que el KNN puede ajustarse más si se optimizan bien sus parámetros.  

---

## 🚀 Tecnologías utilizadas
- Python  
- NumPy  
- Pandas  
- scikit-learn  
- Matplotlib  

---

## 👤 Autor
Trabajo realizado como parte de la materia **Aprendizaje Automático**.  
