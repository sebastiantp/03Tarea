# Tarea nro. 3
## FI3104B - Metodos Numericos Para la Ciencia y la Ingenieria
#### Prof. Valentino González

## P1
El oscilador de van der Pool fue propuesto para describir la dinámica de algunos circuitos eléctricos. La ecuación es la siguiente:

<img src='eqs/van_der_pool_1.png' alt='van de Pool eqn.' height='40'>

> Latex:
    `\dfrac{d^2x}{dt^2} = - k x - \mu (x^2 - a^2) \dfrac{dx}{dt}`

donde k es la constante elástica y &mu; es un coeficiente de roce. Si |x| > a el roce amortigua el movimiento, pero si |x| < a el roce inyecta energía. Se puede hacer un cambio de variable para convertir la ecuación a:

<img src='eqs/van_der_pool_2.png' alt='van de Pool eqn. transformada' height='40'>

> Latex:
    `\dfrac{d^2y}{ds^2} = - y - \mu^* (y^2 - 1) \dfrac{dy}{ds}`

con lo cual ahora la ecuación sólo depende de un parámetro, &mu;<sup>\*</sup>. Indique cuál es el cambio de variable realizado.

Integre la ecuación de movimiento usando el método de Runge-Kutta de orden 2 visto en clase. Se pide que Ud. implemente su propia versión del algoritmo y descriva la discretización yusada y el paso de tiempo. Use &mu;<sup>\*</sup>=1.RRR, donde RRR son los 3 últimos dígitos de su RUT antes del guión.

