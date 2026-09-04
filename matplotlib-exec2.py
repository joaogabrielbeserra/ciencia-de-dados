import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 10000000)   # 100 pontos de 0 até 2π (uma volta completa)

plt.plot(x, np.sin(x), color="blue", label="seno")
plt.plot(x, np.cos(x), color="red", label="cosseno")

plt.title("Seno e Cosseno")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()      # mostra a caixinha explicando cada cor
plt.grid(True)
plt.show()