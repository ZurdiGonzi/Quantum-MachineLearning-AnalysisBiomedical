---
name: biomedical-ml-pipeline
description: >-
  Estándares de preprocesamiento, validación cruzada y métricas clínicas para el análisis
  de datasets biomédicos. Emplear para prevenir fuga de datos (data leakage) y garantizar
  reproducibilidad en clasificación médica.
---

# Biomedical Machine Learning Pipeline Skill

Esta habilidad asegura que todos los experimentos con datos biomédicos cumplan con los más estrictos estándares clínicos y metodológicos.

## 1. Prevención Estricta de Data Leakage
- **Regla de Oro**: Ninguna transformación estadística (imputación por media, escalado estándar, MinMax, reducción PCA) puede ver los datos de validación o test antes de ajustarse.
- **Implementación**: Usar siempre `sklearn.pipeline.Pipeline` integrado con `StratifiedKFold`.
  ```python
  from sklearn.pipeline import Pipeline
  from sklearn.preprocessing import StandardScaler
  from sklearn.model_selection import StratifiedKFold

  cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
  ```

## 2. Rango de Escalado para Cómputo Cuántico
- Para circuitos cuánticos con puertas de rotación ($R_x, R_y, R_z$), los datos continuos deben escalarse explícitamente al rango $[0, 2\pi]$ o $[-\pi, \pi]$:
  ```python
  from sklearn.preprocessing import MinMaxScaler
  scaler = MinMaxScaler(feature_range=(0, 2 * np.pi))
  ```

## 3. Métricas de Evaluación Clínica
- Nunca basar las conclusiones exclusivamente en `accuracy` debido al desbalance habitual de muestras positivas (enfermedad) vs negativas (control).
- Reportar obligatoriamente:
  1. **Sensibilidad (Recall)**: $TP / (TP + FN)$ (minimizar falsos negativos).
  2. **Especificidad**: $TN / (TN + FP)$ (minimizar falsos positivos).
  3. **F1-Score / Macro F1**: Balance entre precisión y recall.
  4. **ROC-AUC**: Capacidad discriminativa global del modelo.
  5. **Matriz de Confusión**.

