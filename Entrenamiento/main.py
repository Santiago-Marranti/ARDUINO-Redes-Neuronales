import matplotlib.pyplot as plt
import RedNeuronal as NeuralRed
import numpy as np
import os

# Red Coche para Evitar obstáculos
nn = NeuralRed.NeuralNetwork([2,3,4],activation ='tanh')
X = np.array([[-1, 0],   # sin obstaculos
              [-1, 1],   # sin obstaculos
              [-1, -1],  # sin obstaculos
              [0, -1],   # obstaculo detectado a derecha
              [0,1],     # obstaculo a izq
              [0,0],     # obstaculo centro
              [1,1],     # demasiado cerca a derecha
              [1,-1],    # demasiado cerca a izq
              [1,0]      # demasiado cerca centro
             ])
# las salidas 'y' se corresponden con encender (o no) los motores
y = np.array([[1,0,0,1], # avanzar
              [1,0,0,1], # avanzar
              [1,0,0,1], # avanzar
              [0,1,0,1], # giro derecha
              [1,0,1,0], # giro izquierda (cambie izq y derecha)
              [1,0,0,1], # avanzar
              [0,1,1,0], # retroceder
              [0,1,1,0], # retroceder
              [0,1,1,0]  # retroceder
             ])
nn.fit(X, y, learning_rate=0.03,epochs=40001)

def valNN(x):
    return (int)(abs(round(x)))

index=0
for e in X:
    prediccion = nn.predict(e)
    print("X:",e,"esperado:",y[index],"obtenido:", valNN(prediccion[0]),valNN(prediccion[1]),valNN(prediccion[2]),valNN(prediccion[3]))
    #print("X:",e,"y:",y[index],"Network:",prediccion)
    index=index+1

def to_str(name, W):
    s = str(W.tolist()).replace('[', '{').replace(']', '}')
    return 'float '+name+'['+str(W.shape[0])+']['+str(W.shape[1])+'] = ' + s + ';'

#######################

deltas = nn.get_deltas()
valores=[]
index=0
for arreglo in deltas:
    valores.append(arreglo[1][0] + arreglo[1][1])
    index=index+1

plt.plot(range(len(valores)), valores, color='b')
plt.ylim([0, 0.4])
plt.ylabel('Cost')
plt.xlabel('Epochs')
plt.tight_layout()
plt.show()

# Obtenermos los pesos entrenados para poder usarlos en el codigo de arduino
pesos = nn.get_weights();

# Obtiene la ruta actual de main.py
path = os.path.dirname(os.path.abspath(__file__));

# Crea la subcarpeta "output" dentro de la carpeta actual
path = os.path.join(path, "output")
os.makedirs(path, exist_ok=True);

path = os.path.join(path, "replace_arduino.txt");

# Escribe el archivo (sobrescribe el contenido cada vez)
with open(path, "w", encoding="utf-8") as f:
    f.write("// Reemplazar estas lineas en tu codigo arduino:\n" +
            "// float HiddenWeights ...\n" +
            "// float OutputWeights ...\n" +
            "// Con lo pesos entrenados.\n\n" +
            to_str('HiddenWeights', pesos[0]) + "\n\n" +
            to_str('OutputWeights', pesos[1]));

print("Se ha guardado en la carpeta Output un archivo con los resultados del entrenamiento." \
      " Aquellas variables que estan en el código de arduino deben ser reemplazadas por estas.");

##########################################