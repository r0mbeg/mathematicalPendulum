# How to launch

To run the code you need install the `graphics` and `tkinter` libraries.

After you have run the file `mathematicalPendulum.py` you will see a window:

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulasAndImages/interface.png)

In this window, you can configure the parameters of the pendulum - the color of the ball, the mass of the ball, the radius of the ball, the length of the thread, the initial angle and the initial angular velocity.

When all the parameters are configured, click "RUN":

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulasAndImages/RUN.png)

# Mathematical description

To calculate the deflection angle we use the following differential equation:

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulasAndImages/equation.png)

Where γ is an attenuation coefficient, omega_0 is a self-resonant frequency and k - is resistance coefficient:

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulasAndImages/gammaAndOmega0.png)

Knowing the initial conditions, we can calculate the acceleration:

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulasAndImages/acceleration.png)

Next, we numerically calculate the speed and angle:

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulasAndImages/angleAndVelocity.png)

When we know the angle on the new iteration, we calculate the new coordinates:

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulasAndImages/newCoords.png)

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulasAndImages/nextIteration1.png)

To move the ball to a new position, we calculate the vector v and use the `move` function:

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulasAndImages/move.png)

Repeat the iteration from the acceleration calculation.

![hippo](https://media3.giphy.com/media/aUovxH8Vf9qDu/giphy.gif)


