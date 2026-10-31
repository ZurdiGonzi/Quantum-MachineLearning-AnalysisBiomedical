# Spec: 001 - Fundamentos de Aprendizaje (Qiskit & Deep Learning)

## 1. Contexto y Objetivos
- **Problema**: Establecer y documentar los fundamentos computacionales y matemáticos necesarios para abordar el TFG sobre Aprendizaje Automático Cuántico aplicado a Biomedicina.
- **Objetivo**: Estructurar los cuadernos formativos y algoritmos cuánticos base como el **Capítulo 1** del TFG, asegurando compatibilidad con los estándares modernos de Qiskit 1.0+ y PyTorch.
- **Hipótesis**: La comprensión de oráculos cuánticos (Phase Kickback) y amplificación de amplitudes (Grover), unida a los bucles de optimización clásicos de PyTorch, proporciona el puente metodológico directo hacia los clasificadores cuánticos variacionales (VQC) y métodos kernel cuánticos (QSVM).

## 2. Artefactos y Entregables
- **Cuadernos**:
  - `tfg/chapters/01-learning/notebooks/Algoritmos_del_libro.ipynb` (Algoritmos cuánticos y visualización de circuitos)
  - `tfg/chapters/01-learning/notebooks/PyTorch.ipynb` (Fundamentos de redes neuronales y backpropagation)
- **Código Cuántico**:
  - Scripts en `tfg/chapters/01-learning/code/` organizados en `basics/` y `algorithms/` (`COn-Kickback/` y `Sin-Kickback/`).
- **Memoria**:
  - `tfg/chapters/01-learning/README.md` estructurado como primer capítulo de la memoria.

## 3. Criterios de Aceptación
- [x] Cuadernos de Jupyter ubicados en el Capítulo 1 del TFG.
- [x] Algoritmos cuánticos organizados y comentados.
- [x] Skills de Antigravity configuradas para asistir en el desarrollo posterior de Qiskit y ML Biomédico.
- [x] Constitución de Spec-Kit activa para regir futuros experimentos.

