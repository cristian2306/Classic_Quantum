# DE LO CLASICO A LO CUANTICO
De lo clasico a lo cuantico es un proyecto en el cual se da a entender al usuario las bases minimas de la computacion cuantica, en el repositorio `complex_number`, se introdugeron varias operaciones para los numeros complejos, en este proyecto usaremos ese repositorio con todas sus librerias, la idea del proyecto presentado es que el usuario tenga la capacidad de usar el programa contenido en este repositorio `Classic_Quantum`, en el cual se encuentran funciones con las cuales el usuario puede generar el experimento d elas canicas, el experimento de multiples rendijas, tanto probabilistico con reales como con numeros complejos.

## Sistema Probabilistico.
++ Por comodidad del usuario, el programa aproxima todos los resultados a dos decimales.
+ La entrada de la funcion `Probabilistic_system()` es una matriz `mat`, donde esta representa la dinamica del sistema, un numero real positivo `click`, y un vector `state`, el cual representa el estado inicial del sistema.
   La funcion recibe tanto matrices y vectores booleanos.
   ```
   in: mat =[[False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, True, False, False, False, True],
            [False, False, False, True, False, False],
            [False, False, True, False, False, False],
            [True, False, False, False, True, False]] 
       state = [False, False, True, False, False, False]
       Probabilistic_system(mat,5,state)
  
  out: [[False], [False], [False], [False], [False], [True]]
   ```
  Como matrices y vectores reales
  ```
  in: mat = [[0,1/6,5/6],[1/3,1/2,1/6],[2/3,1/3,0]]
      state = [1/6,1/6,2/3]
      Probabilistic_system(mat,1,state)
      
  out: [[0.3],[ 0.3], [0.4]]
  
  ```
  La funcion adicionalmente presenta un grafico de barras en donde se ve la probabilidad del sistema.
  
## Sistema Cuantico
+ Le entrada de la funcion `Quantum_system()` recibe una matriz `mat` de complejos, un numero real entero `click`, y un vector `state`, donde cada una de estas variables representan la dinamica del sistema, los click de tiempo y el estado inicial del sitema, respectivamente.
La funcion `Probabilistic_system` retornaba un vector columna de numeros reales o booleanos, puesto que hablamos de probabilidad, para este caso que hablamos de matrices y vectores complejos, para que se de una salida de reales, a cada componente del vector columna, se calcula su modulo cuadrado, esto genera que el vector columna sea probabilistico, es decir la suma de sus componentes es 1.
   ```
    in: mat = [[complex_cart(0,0) for i in range(3)]for j in range(3)]
        mat[0][0]= complex_cart(1/math.sqrt(2),0)
        mat[1][0]=complex_cart(0,-1/math.sqrt(2))
        mat[0][1]=complex_cart(1/math.sqrt(2),0)
        mat[1][1]=complex_cart(0,1/math.sqrt(2))
        mat[2][2]=complex_cart(0,-1)
        state = [complex_cart(1/math.sqrt(3),0),complex_cart(0,2/math.sqrt(15)),complex_cart(math.sqrt(2/5),0)]
        Quantum_system(mat,1,state)
        
    out: [[0.0],[0.0],[0.0],[0.0],[0.07],[0.07],
          [0.07],[0.13],[0.13],[0.07],[0.13],[0.13],
          [0.07],[0.07],[0.07]]
          
        
        
   ```
  


