# DE LO CLASICO A LO CUANTICO
De lo clasico a lo cuantico es un proyecto en el cual se da a entender al usuario las bases minimas de la computacion cuantica, en el repositorio `complex_number`, se introdugeron varias operaciones para los numeros complejos, en este proyecto usaremos ese repositorio con todas sus librerias, la idea del proyecto presentado es que el usuario tenga la capacidad de usar el programa contenido en este repositorio `Classic_Quantum`, en el cual se encuentran funciones con las cuales el usuario puede generar el experimento d elas canicas, el experimento de multiples rendijas, tanto probabilistico con reales como con numeros complejos.
## Ejecucion
+ Para ejecutar este programa no basta con tener python, es necesario tener librerias adicionales, por este motivo recomiendo la instalacion de [Spyder](https://www.spyder-ide.org/), el cual contiene todo lo necesario para el funcionamiento de la libreria, adicionalmente es recomendable descargar la libreria [complex_numbers](https://github.com/cristian2306/Complex_numbers), para tener un funcionamiento eficaz, cabe recalcar que es necesario que todos los archivos de las dos librerias se encuentren en una misma carpeta.

## Sistema Probabilistico.
+ Por comodidad del usuario, el programa aproxima todos los resultados a dos decimales.
+ La entrada de la funcion `Probabilistic_system()` es una matriz `mat`, donde esta representa la dinamica del sistema, un numero real positivo `click`, y un vector `state`, el cual representa el estado inicial del sistema.
   - La funcion recibe tanto matrices y vectores booleanos.
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
  - Como matrices y vectores reales
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
## Experimento de la multiple rendija probabilistico
+ El experimento de la multiple rendija probabilistico tiene dos funciones, una `exp_real_slit()`, para numeros reales, y `exp_complex_slit`, para numeros complejos.
   - Real
      El experimento de la multiple rendija para numeros reales recibe unicamente,el numero de blancos `targets` y el numero de rendijas ``slits`. La funcion calcula la matriz qe describe la dinamica del sistema, y tomando un `state` como `[1,0,0,...,0]`, calcula la probabilidad de que el blanco de en un blanco.
      ```
      in: exp_real_slit(3,5)
      out: [[0.0],[0.0],[0.0],[0.0],[0.07],[0.07],
            [0.07],[0.13],[0.13],[0.07],[0.13],[0.13],
            [0.07],[0.07],[0.07]]
            
     ```
   - Complejo
      El experimento de la multiple rendija para numeros complejos recibe unicamente la matriz que describe la dinamica del sistema. La salida al igual que en el sistema probabilistico, devuelve un vector columna con la probabilidad de dar en cada blanco, para que esto se cumpla se calcula de la misma manera que en Quantum_system.
      
      ```
        in: mat = [[complex_cart(0,0) for i in range(8)] for j in range(8)]
            mat[1][0]=complex_cart(1/math.sqrt(2),0) 
            mat[2][0]=complex_cart(1/math.sqrt(2),0)
            mat[3][1]=complex_cart(-1/math.sqrt(6),1/math.sqrt(6))
            mat[3][3]=complex_cart(1,0)
            mat[4][1]=complex_cart(-1/math.sqrt(6),-1/math.sqrt(6))      
            mat[4][4]=complex_cart(1,0)
            mat[5][1]=complex_cart(1/math.sqrt(6),-1/math.sqrt(6))
            mat[5][2]=complex_cart(-1/math.sqrt(6),1/math.sqrt(6))
            mat[5][5]=complex_cart(1,0)
            mat[6][2]=complex_cart(-1/math.sqrt(6),-1/math.sqrt(6))
            mat[6][6]=complex_cart(1,0)
            mat[7][2]=complex_cart(1/math.sqrt(6),-1/math.sqrt(6))
            mat[7][7]=complex_cart(1,0)
            exp_commplex_slit(mat)
        out: [[0.0], [0.0], [0.0], [0.17], [0.17], [0.0], [0.17], [0.17]]
      ```
+ De igual manera que en los isteas probabilisticos cada funcion muestra el grafico de probabilidad del sistema
## Autor
__Cristian Andres Castellanos Fino__
  


