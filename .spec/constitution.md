# Constitution: Quantum Machine Learning for Biomedical Analysis (TFG)

## 1. Propósito y Alcance
Este proyecto investiga la aplicación de **Quantum Machine Learning (QML)** en el análisis y clasificación de datos biomédicos, evaluando su rendimiento, complejidad y viabilidad frente a modelos clásicos de referencia (SVM, Random Forest, Redes Neuronales).

## 2. Principios Fundamentales

### 2.1. Rigor Metodológico y Clínico
- **Prevención estricta de fuga de datos (Data Leakage)**: Todas las transformaciones de preprocesamiento (escalado, codificación, PCA, imputación) deben ajustarse exclusivamente sobre el conjunto de entrenamiento (`fit_transform`) y aplicarse al conjunto de test (`transform`) dentro de esquemas de validación cruzada estratificada (`StratifiedKFold`).
- **Métricas médicas relevantes**: Más allá del Accuracy (que suele ser engañoso en datasets biomédicos desbalanceados), se deben reportar siempre: **Sensibilidad / Recall**, **Especificidad**, **F1-Score**, **ROC-AUC** y **PR-AUC**.

### 2.2. Estándares Cuánticos (Qiskit 1.0+)
- **Sintaxis moderna**: Usar exclusivamente la API moderna de Qiskit (>=1.0). Quedan prohibidos módulos obsoletos como `qiskit.aqua`, `qiskit-ibmq-provider` o constructores discontinuados.
- **Primitivas**: Emplear primitivas estándar (`StatevectorEstimator`, `StatevectorSampler` o `SamplerV2`/`EstimatorV2`).
- **Limitación de profundidad y decoherencia**: Limitar la profundidad de circuito y número de qubits basándose en técnicas de reducción dimensional previa (PCA, Autoencoders o selección de características).

### 2.3. Reproducibilidad
- Fijar semillas aleatorias (`seed`) tanto a nivel clásico (`numpy`, `torch`, `scikit-learn`) como a nivel de simulación cuántica (`AerSimulator(seed_simulator=...)`).
- Todo experimento debe generar métricas reproducibles y guardarse en `qml-biomedico/results/` con su correspondiente configuración en `qml-biomedico/config/`.

### 2.4. Flujo Spec-Kit
- Todo desarrollo de modelo o pipeline experimental debe originarse a partir de una especificación en `.spec/specs/<id>-<nombre>/spec.md` con su correspondiente desglose en `tasks.md`.
- El código se implementará de forma modular en `qml-biomedico/src/` con sus respectivos tests en `qml-biomedico/tests/`.

