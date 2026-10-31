---
name: qiskit-quantum-computing
description: >-
  Guía y mejores prácticas para el diseño de circuitos cuánticos, simulación, transpilación
  y ejecución utilizando Qiskit 1.0+. Emplear para implementar algoritmos cuánticos fundamentales
  (Deutsch-Jozsa, Grover, Bernstein-Vazirani, Simon) y primitivas de cómputo cuántico.
---

# Qiskit Quantum Computing Skill

Esta habilidad proporciona patrones, convenciones y directrices para desarrollar circuitos cuánticos con **Qiskit 1.0+**.

## 1. Reglas de Compatibilidad (Qiskit 1.0+)
- **NUNCA** importar paquetes discontinuados como `qiskit.aqua` o `qiskit-ibmq-provider`.
- Usar las primitivas modernas de ejecución:
  - `qiskit.primitives.StatevectorSampler` o `SamplerV2` para muestreo de cuentas.
  - `qiskit.primitives.StatevectorEstimator` o `EstimatorV2` para valores esperados de observables $\langle \psi | O | \psi \rangle$.
- Usar el transpilador de Qiskit explícitamente:
  ```python
  from qiskit import transpile
  from qiskit_aer import AerSimulator

  backend = AerSimulator()
  transpiled_circuit = transpile(circuit, backend, optimization_level=2)
  ```

## 2. Convenciones de Circuitos
- Nombrar registros cuánticos y clásicos claramente:
  ```python
  from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

  qr = QuantumRegister(n_qubits, name="q")
  cr = ClassicalRegister(n_qubits, name="c")
  qc = QuantumCircuit(qr, cr)
  ```
- Modularizar subcircuitos mediante `to_gate()` o composición de `QuantumCircuit`.

## 3. Algoritmos Fundamentales
- **Deutsch-Jozsa**: Oráculos balanceados vs constantes con fase kickback (puerta $X$ y $H$ en el qubit ancilla).
- **Bernstein-Vazirani**: Determinación de cadena binaria oculta en una sola consulta.
- **Simon**: Búsqueda de período $s$ mediante muestreo de ecuaciones lineales módulo 2.
- **Grover**: Difusor de inversión sobre la media y amplificación de amplitud.

