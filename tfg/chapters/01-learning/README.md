# Capítulo 1: Fundamentos de Aprendizaje (Quantum Computing & Deep Learning)

Este capítulo agrupa el material formativo, cuadernos interactivos y scripts experimentales desarrollados para establecer los fundamentos teóricos y prácticos del Trabajo de Fin de Grado (**Quantum Machine Learning aplicado al Análisis Biomédico**).

---

## 1. Estructura de Contenidos

```text
01-learning/
├── notebooks/
│   ├── Algoritmos_del_libro.ipynb   # Cuaderno de algoritmos cuánticos fundamentales en Qiskit
│   └── PyTorch.ipynb                # Cuaderno de fundamentos de Deep Learning con PyTorch
│
├── code/
│   ├── basics/                      # Conceptos básicos y circuitos iniciales
│   │   ├── Base.py                  # Estructura básica de circuito y medidas
│   │   ├── Inicializar.py           # Inicialización de estados cuánticos personalizados
│   │   └── EjercicioGPT1.py         # Ejercicio práctico de simulación
│   │
│   └── algorithms/                  # Implementación de algoritmos cuánticos de referencia
│       ├── COn-Kickback/            # Algoritmos basados en Phase Kickback
│       │   ├── KickBack.py          # Demostración del fenómeno Phase Kickback
│       │   ├── Deustch.py           # Algoritmo de Deutsch (1 qubit)
│       │   ├── Deustch-Jozsa.py     # Algoritmo de Deutsch-Jozsa (n qubits)
│       │   ├── Bernstein-Vazinari.py# Algoritmo de Bernstein-Vazirani (oráculo de producto interno)
│       │   └── Simon.py             # Algoritmo de Simon (búsqueda de período módulo 2)
│       │
│       └── Sin-Kickback/            # Búsqueda no estructurada
│           └── Grover.py            # Algoritmo de Grover (amplificación de amplitud y difusor)
```

---

## 2. Descripción de Cuadernos Jupyter

### 2.1. [`Algoritmos_del_libro.ipynb`](./notebooks/Algoritmos_del_libro.ipynb)
- **Objetivo**: Implementación paso a paso de los circuitos de superposición, entrelazamiento (estados de Bell) y oráculos cuánticos.
- **Técnicas**:
  - Manipulación de puertas unitarias: $H$, $X$, $Z$, $CX$ (CNOT).
  - Medición y análisis de distribuciones de probabilidad con simulador de vector de estado y cuentas.
  - Comprensión intuitiva de la interferencia cuántica destructiva y constructiva.

### 2.2. [`PyTorch.ipynb`](./notebooks/PyTorch.ipynb)
- **Objetivo**: Fundamentos de aprendizaje profundo clásico para servir como base comparativa e híbrida.
- **Técnicas**:
  - Tensores, autograd y propagación hacia atrás (backpropagation).
  - Definición de arquitecturas de redes neuronales (`nn.Module`).
  - Bucles de entrenamiento con optimizadores (`Adam`, `SGD`) y funciones de pérdida (`CrossEntropyLoss`, `BCEWithLogitsLoss`).
  - Preparación de datos mediante `Dataset` y `DataLoader`.

---

## 3. Síntesis Teórica de Algoritmos Cuánticos

| Algoritmo | Propósito | Complejidad Clásica | Complejidad Cuántica | Rol en QML |
| :--- | :--- | :--- | :--- | :--- |
| **Deutsch-Jozsa** | Determinar si una función booleana es constante o balanceada | $O(2^{n-1} + 1)$ | $O(1)$ | Introducción a superposición y oráculos globales |
| **Bernstein-Vazirani** | Encontrar una cadena oculta $s \in \{0,1\}^n$ tal que $f(x) = s \cdot x$ | $O(n)$ | $O(1)$ | Extracción eficiente de características vectoriales |
| **Simon** | Hallar el período $s$ de una función 2-a-1 tal que $f(x) = f(x \oplus s)$ | $O(2^{n/2})$ | $O(n)$ | Inspiración directa del algoritmo de Shor y simetrías |
| **Grover** | Búsqueda en una base de datos no estructurada de $N = 2^n$ elementos | $O(N)$ | $O(\sqrt{N})$ | Aceleración cuadrática aplicable a optimización y búsqueda de estados |

---

## 4. Conexión con el Proyecto de TFG
Este capítulo sienta las bases para avanzar hacia los capítulos posteriores:
- **Capítulo 2: Preprocesamiento de Datos Biomédicos** (normalización para circuitos y reducción dimensional PCA).
- **Capítulo 3: Circuitos Cuánticos Parametrizados (PQC) y Feature Maps** (extensión de los conceptos de superposición y rotaciones).
- **Capítulo 4: Modelos Híbridos VQC y Quantum Kernels** (fusión del loop de optimización de PyTorch con primitivas de Qiskit).
- **Capítulo 5: Resultados, Benchmarking Clínico y Conclusiones**.

