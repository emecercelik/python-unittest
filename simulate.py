from scipy.integrate import ode
import numpy as np
from matplotlib import pyplot as pp
# =============================================================================
def simulate(t0, t1, dt):
    '''Solve the ODE

        m x'' + c x' + k x = 0

    with initial point and velocity x0, x0p.
    '''

    x0 = -0.1
    x0p = 0.0
    m = 1500.0
    k = 5.0e6
    c = 2*np.sqrt(k*m)

    # Define the RHS of the ODE.
    def f(t, y):
        return [y[1],
                -k/m * y[0] - c/m * y[1]
                ]

    # Use BDF here, but there are many more methods available
    # <http://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.ode.html>.
    r = ode(f).set_integrator('vode',
                              method='bdf'
                              )
    y0 = [x0, x0p]
    r.set_initial_value(y0, t0)

    T = []
    X = []
    while r.successful() and r.t < t1:
        r.integrate(r.t + dt)
        X.append(r.y[0])
        T.append(r.t)

    return T, X
# =============================================================================
if __name__ == '__main__':
    T, X = simulate(t0=0.0, t1=3.0, dt=1.0e-2)
    pp.plot(T, X)
    pp.show()
# =============================================================================
