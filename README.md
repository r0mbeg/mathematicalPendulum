A model of a mathematical pendulum.

To run the code you need install the `graphics` and `tkinter` libraries.

To calculate the deflection angle we use the following differential equation:

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulas/equation.png)

Where γ is an attenuation coefficient, omega_0 is a self-resonant frequency and k - is resistance coefficient:

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulas/gammaAndOmega0.png)

Knowing the initial conditions, we can calculate the acceleration:

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulas/acceleration.png)

Next, we numerically calculate the speed and angle:

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulas/angleAndVelocity.png)

When we know the angle on the new iteration, we calculate the new coordinates:

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulas/newCoords.png)

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulas/nextIteration1.png)

To move the ball to a new position, we calculate the vector v and use the `move` function:

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulas/move.png)

Repeat the iteration from the acceleration calculation.
