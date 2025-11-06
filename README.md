
# 🚗🤖 Proyecto: Coche Arduino con Inteligencia Artificial  
## ARQUITECTURA DE COMPUTADORAS 
### Integrantes: Acuña Roman, Santillan Ariadna, Marranti Santiago, Moyano Oriana


[![AI Car GIF](https://www.aprendemachinelearning.com/wp-content/uploads/2018/08/coche_evita_02.gif)]

---

## 📘 Descripción del Proyecto  

Este proyecto implementa un **coche inteligente controlado por una red neuronal artificial (RNA)**, desarrollado con **Arduino Uno** y simulado en **Wokwi**.  
El objetivo es que el vehículo aprenda a tomar decisiones automáticamente, reconociendo patrones de entrada (como sensores de distancia) y ajustando sus movimientos (salidas) de acuerdo a los datos aprendidos.

🔗 **Simulación en Wokwi:**  
👉 [Ver Proyecto en Wokwi](https://wokwi.com/projects/446829487827187713)

🔗 **Fuente original del modelo:**  
👉 [Aprende Machine Learning - Coche con IA](https://www.aprendemachinelearning.com/programa-un-coche-arduino-con-inteligencia-artificial/)

---

## 🧠 1. Arquitecturas observadas  

El sistema está basado en una **red neuronal de tres capas**:

- **Capa de entrada:** Recibe los datos de los sensores (distancias o condiciones del entorno).  
- **Capa oculta:** Procesa la información y genera relaciones entre entradas y salidas.  
- **Capa de salida:** Controla las acciones del coche (avanzar, girar, frenar, etc.).  

El modelo se entrena en **Google Colab**, ajustando los pesos sinápticos mediante el método de **retropropagación del error (Backpropagation)**.

---

## 🧩 2. Enfoques de resolución de problemas  

Se aplicaron los siguientes enfoques:

- **Aprendizaje supervisado:** El sistema aprende a partir de ejemplos definidos en una tabla de verdad.  
- **Simulación incremental:** Se ajustan los valores de entrada y salida para mejorar la precisión del modelo.  
- **Optimización de pesos:** Ajuste iterativo de parámetros para minimizar el error cuadrático medio (MSE).  
- **Implementación física virtual:** Integración de la lógica entrenada en un entorno de simulación Arduino (Wokwi).  

---

## 💻 3. Entrenamiento de la red neuronal en Google Colab  

El entrenamiento se realizó en Colab usando Python y librerías como `numpy` y `matplotlib`.  
Se puede ejecutar el entrenamiento base y luego **ajustar el modelo** con nuevas entradas/salidas para cada integrante del equipo.

👉 [Abrir Notebook en Google Colab] (https://colab.research.google.com/drive/1torEMNKfBcbG7NAa9s-TZ-KcYcBykBRv?usp=sharing) 

---

## 🔄 4. Nuevas simulaciones  

Cada miembro del equipo generó su propia tabla de verdad, simulando **2 entradas nuevas y 1 salida adicional**.  
Esto permitió **reentrenar la red neuronal** y observar variaciones en el comportamiento del modelo.

### 🧮 Tabla de verdad (Acuña Roman)
| Entrada 1 | Entrada 2 | Entrada 3 | Entrada 4 | Salida |
|------------|------------|------------|---------|---------|
| 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 |
| 0 | 0 | 0 | 1 | 0 |
| 1 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 1 |

### 1️⃣  Acuña Roman
y_A = np.array([
    [1,0,0,0,0],
    [1,0,0,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [1,0,0,0,0],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,0,1]
])
<img width="585" height="373" alt="image" src="https://github.com/user-attachments/assets/4952cf5e-557f-4fd0-991b-26a9b32de72f" />

### 🧮 Tabla de verdad (Santillan Ariadna)
| Entrada 1 | Entrada 2 | Entrada 3 | Entrada 4 | Salida |
|------------|------------|------------|---------|---------|
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 |
| 0 | 0 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 0 |
| 0 | 0 | 0 | 1 | 0 |

### 2️⃣  Santillan Ariadna
y_B = np.array([
    [1,0,0,1,0],
    [1,0,0,1,0],
    [0,1,0,0,1],
    [0,0,1,0,0],
    [1,0,1,0,0],
    [0,0,0,1,1],
    [1,1,0,0,0],
    [0,1,1,0,0],
    [0,0,0,1,0]
])

<img width="596" height="379" alt="image" src="https://github.com/user-attachments/assets/f483b2ab-7662-4b0b-bd50-b294add5118c" />

### 🧮 Tabla de verdad (Marranti Santiago)
| Entrada 1 | Entrada 2 | Entrada 3 | Entrada 4 | Salida |
|------------|------------|------------|---------|---------|
| 1 | 0 | 0 | 0 | 1 |
| 1 | 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 0 |
| 0 | 0 | 0 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 0 | 0 |
| 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 |

### 3️⃣  Marranti Santiago
y_C = np.array([
    [1,0,0,0,1],
    [1,0,0,0,1],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [1,0,0,0,1],
    [0,1,0,0,0],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,1,0,0]
])

<img width="581" height="373" alt="image" src="https://github.com/user-attachments/assets/9f175671-1d96-4e3e-81e6-55483ccc63e1" />

### 🧮 Tabla de verdad (Moyano Oriana)
| Entrada 1 | Entrada 2 | Entrada 3 | Entrada 4 | Salida |
|------------|------------|------------|---------|---------|
| 0 | 1 | 0 | 0 | 1 |
| 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 |
| 0 | 0 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 0 |
| 0 | 0 | 0 | 1 | 1 |

### 4️⃣ Integrante Moyano Oriana
y_D = np.array([
    [0,1,0,0,1],
    [1,0,0,0,0],
    [1,0,1,0,0],
    [0,0,0,1,0],
    [1,0,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,1],
    [0,0,1,0,0],
    [0,0,0,1,1]
])

<img width="589" height="374" alt="image" src="https://github.com/user-attachments/assets/383cf06b-5c76-48e3-af53-02500baafc83" />



---

## 🚀 5. Conclusiones  

✅ Se logró implementar un sistema de **inteligencia artificial básica en Arduino**.  
✅ La simulación permitió visualizar cómo las redes neuronales pueden aplicarse en sistemas embebidos.  
✅ La red fue **ajustada con nuevas entradas y salidas**, mejorando la capacidad de respuesta del coche.  

---

## 👨‍💻 Equipo de desarrollo  

| Integrante | Nombre  | Apellido |
|-------------|-----|------------------|
|  Integrante 1 | Roman  |Acuña |
|  Integrante 2 |  Ariadna | Santillan |
|  Integrante 3 |  Santiago | Marranti |
|  Integrante 4 | Oriana | Moyano  |

---

## 📷 Galería de la simulación  


![Arduino Simulation](https://media1.tenor.com/m/ujtysPw05X8AAAAd/wall-e-waving.gif)]
---

## 🏁 Tecnologías utilizadas  

- 🧠 Python (entrenamiento en Colab)  
- 🔌 Arduino UNO (implementación del coche)  
- 🌐 Wokwi (simulación virtual)  
- 📊 NumPy / Matplotlib  
- 💾 GitHub (control de versiones y documentación)

---

## ⭐ Cómo clonar y ejecutar  

```bash
git clone https://github.com/Santiago-Marranti/ARDUINO-Redes-Neuronales
```

## 🧠 Códigos
En la carpeta de `Entrenamiento` se encuentra la red neuronal `RedNeuronal.py` en Python y la clase `main.py` que fue modificada para que en una carpeta `output` se guarde el archivo con las matrices a reemplazar, que seria el resultado obtenido del entrenamiento.

En la carpeta de `Arduino` se encuentra el código que va grabado en la placa y que hace funcionar a este coche con una red neuronal incorporada. Aqui una vez se ha entrenado la red neuronal (es opcional, porque ya funciona como está) pueden reemplazarse las matrices con los resultados anteriormente mencionados para lograr una mejor toma de decisiones de la inteligencia artificial.

