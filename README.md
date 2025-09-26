# How to launch

To run the code you need install the `graphics` and `tkinter` libraries.

After you have run the file `mathematicalPendulum.py` you will see a window:

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulasAndImages/interface.png)

In this window, you can configure the parameters of the pendulum - the color of the ball, the mass of the ball, the radius of the ball, the length of the thread, the initial angle and the initial angular velocity.

When all the parameters are configured, click "RUN":

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulasAndImages/Pendulum%20(1).gif)

# Mathematical description

To calculate the deflection angle we use the following differential equation:

$$\ddot{\alpha}+2\gamma\dot{\alpha}+\omega_0^2\sin\alpha=0$$

Where γ is an attenuation coefficient, omega_0 is a self-resonant frequency and k - is resistance coefficient:

$$\gamma=\frac{k}{m} \quad \omega_0=\sqrt{\frac{g}{l}}$$

Knowing the initial conditions, we can calculate the acceleration:

$$\ddot{\alpha}=-2\gamma\dot{\alpha}-\omega_0^2\sin\alpha$$

Next, we numerically calculate the speed and angle:

$$\dot{\alpha}_{new}=\dot{\alpha}_{old}+0.99\cdot\ddot{\alpha}\quad\alpha_{new}=\alpha_{old}+0.99\cdot\dot{\alpha}$$

When we know the angle on the new iteration, we calculate the new coordinates:

$$(x_{new}, y_{new})=(x_c+l\cdot\alpha, y_c+l\cdot\alpha)$$

![Image alt](https://github.com/r0mbeg/mathematicalPendulum/blob/main/pendulumFormulasAndImages/nextIteration1.png)

To move the ball to a new position, we calculate the vector v and use the `move` function:

$$(v_x,v_y)=(x_{new},y_{new})-(x_{old},y_{old})$$

Repeat the iteration from the acceleration calculation.


