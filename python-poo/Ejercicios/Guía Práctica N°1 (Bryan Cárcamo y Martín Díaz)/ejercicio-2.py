import numpy as np
import matplotlib.pyplot as plt

"""
2. Implementar una clase FuncionTrigonometrica, que permita representar, graficar y evaluar
funciones trigonométricas como seno, coseno y tangente. Se solicita realizar lo siguiente:
Clase FuncionTrigonometrica:
   ● Atributos:
      ○ Tipo de función (seno, coseno, tangente)
      ○ Amplitud y periodo de la función.
   ● Métodos:
      ○ Crear un método que evalúe la función trigonométrica en un valor x (en radianes)
      ○ Crear un método que grafique la función en un intervalo de valores.
      ○ Crear un método mágico que devuelva una representación de texto de la función trigonométrica.
      ○ Crear un método que devuelva un valor crítico de la función (por ejemplo, los máximos o mínimos para seno y coseno).
Además de implementar las funciones trigonométricas, se debe demostrar gráficamente la
periodicidad de la función y cómo se afecta por cambios en la amplitud y el periodo.
"""

# Creando una clase FunciónTrigonométrica y añadiendo sus atributos
class FunciónTrigonométrica:
   def __init__(self, tipo_función, amplitud=1, periodo=2*np.pi):
      self.tipo_función = tipo_función
      self.amplitud = amplitud
      self.periodo = periodo
   
   # Método que evalua la función trigonométrica en un valor x (en radianes)
   def evaluar_función(self, x):
      if self.tipo_función == 'seno':
            return self.amplitud * np.sin(x * (2 * np.pi / self.periodo))
      elif self.tipo_función == 'coseno':
            return self.amplitud * np.cos(x * (2 * np.pi / self.periodo))
      elif self.tipo_función == 'tangente':
            return self.amplitud * np.tan(x * (2 * np.pi / self.periodo))
      else:
            raise ValueError("Tipo de función inválido") # ValueError ocurre cuando una función recibe un argumento del tipo de datos correcto pero un valor inadecuado
        
   # Método que grafica la función en un intervalo de valores
   def graficar_función(self, x_min, x_max, num_puntos=1000):
      x = np.linspace(x_min, x_max, num_puntos)
      y = np.array([self.evaluar_función(xi) for xi in x])

      plt.figure(figsize=(10, 6))
      plt.plot(x, y, label=f"{self.tipo_función.capitalize()}(x)")
      plt.title(f"Gráfica de {self.tipo_función.capitalize()}(x)")
      plt.xlabel(f"x (radianes)")
      plt.ylabel(f"(x)")
      plt.axhline(0, color="black", linewidth=0.5)
      plt.axvline(0, color="black", linewidth=0.5)
      plt.grid(color="red", linestyle="--", linewidth=0.5)
      plt.legend()
      plt.show()
   
   # Método mágico que devuelve una representación de texto de la función trigonométrica
   def __str__(self):
        return f'FunciónTrigonométrica(tipo_función="{self.tipo_función}", amplitud="{self.amplitud}", periodo="{self.periodo})'
   
   # Método que devuelve un valor crítico de la función (en este caso, los máximos o mínimos para seno y coseno)
   def valor_crítico(self):
        if self.tipo_función in ['seno', 'coseno']:
             if self.tipo_función == 'seno':
                  return [self.amplitud, -self.amplitud] # Máximos o mínimos para seno
             elif self.tipo_función == 'coseno':
                  return [self.amplitud, -self.amplitud] # Máximos o mínimos para coseno
             elif self.tipo_función == 'tangente':
                  return 'Debido a sus asínotas vericales, la tangente carece de finitos máximos o mínimos'
             else:
                  raise ValueError("Tipo de función inválido")
             
if __name__ == "__main__":
     seno = FunciónTrigonométrica(tipo_función='seno', amplitud=2, periodo=2*np.pi)
     coseno = FunciónTrigonométrica(tipo_función='coseno', amplitud=1, periodo=np.pi)
     tangente = FunciónTrigonométrica(tipo_función='tangente', amplitud=1, periodo=np.pi)

     print(seno)
     seno.graficar_función(-4*np.pi, 4*np.pi)
     print(f"Valores críticos del seno:", seno.valor_crítico())

     print(coseno)
     coseno.graficar_función(-2*np.pi, 2*np.pi)
     print(f"Valores críticos del coseno:", coseno.valor_crítico())

     print(tangente)
     tangente.graficar_función(-2*np.pi, 2*np.pi)
     print(f"Valores críticos del tangente:", tangente.valor_crítico())