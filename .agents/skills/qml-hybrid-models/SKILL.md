---
name: qml-hybrid-models
description: >-
  Guía para el diseño y entrenamiento de modelos cuánticos variacionales (VQC), Quantum Support
  Vector Machines (QSVM), Quantum Kernels y arquitecturas híbridas clásico-cuánticas con PyTorch y Qiskit.
---

# Quantum Machine Learning Hybrid Models Skill

Esta habilidad cubre el desarrollo de clasificadores cuánticos y modelos híbridos aplicados a problemas biomédicos.

## 1. Arquitecturas Principales

### A. Variational Quantum Classifier (VQC)
- **Feature Map**: Codificación del dato clásico en el espacio de Hilbert (ej. `ZZFeatureMap`, `ZFeatureMap` o ángulo simple).
- **Ansatz Variacional**: Capas parametrizadas (ej. `RealAmplitudes`, `TwoLocal`, `EfficientSU2`) con entrelazamiento controlado (`linear` o `full`).
- **Medición**: Estimación del valor esperado de un observable observable (ej. $\langle Z_0 \rangle$ o $\sum_i Z_i$).

### B. Quantum Kernel Methods (QSVM)
- Cálculo de la matriz de Gram cuántica: $K_{ij} = |\langle \phi(x_i) | \phi(x_j) \rangle|^2$.
- Entrenamiento mediante un clasificador SVM clásico (`sklearn.svm.SVC(kernel='precomputed')`).
- Excelente para datasets pequeños y medianos por su convexidad (no sufre de mínimos locales ni barren plateaus).

## 2. Mitigación de Barren Plateaus
- Evitar circuitos excesivamente profundos con inicialización completamente aleatoria en espacios de Hilbert grandes ($n > 10$ qubits).
- Utilizar capas ansatz con topología local y parametrización inicial cercana a la identidad cuando sea viable.
- Optimización con optimizadores robustos a ruido: `SPSA` para simulaciones con shots y `COBYLA` o `L-BFGS-B` para simulaciones de vector de estado ideal.

## 3. Integración Híbrida PyTorch
- Conectar capas cuánticas mediante estimadores parametrizados o interfaces de gradiente cuántico (Parameter Shift Rule).

