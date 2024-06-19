def obtener_calificacion(prompt):
  while True:
      try:
          nota = float(input(prompt))
          if nota < 0:
              raise ValueError("La calificación no puede ser negativa.")
          return nota
      except ValueError as e:
          print(e)

def main():
  estudiantes = []
  while True:
      nombre = input("Ingrese el nombre del estudiante: ")
      matricula = input("Ingrese la matrícula del estudiante: ")
      notas = [obtener_calificacion(f"Ingrese la nota {i+1}: ") for i in range(4)]
      promedio = sum(notas) / len(notas)
      estudiantes.append((nombre, matricula, promedio))

      continuar = input("¿Desea incluir otro estudiante? (si/no): ")
      if continuar.lower() != 's':
          break

  print("\nPromedios de los estudiantes:")
  for nombre, matricula, promedio in estudiantes:
      print(f"Estudiante: {nombre}, Matrícula: {matricula}, Promedio: {promedio:.2f}")

if __name__ == "__main__":
  main()

