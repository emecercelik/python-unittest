import unittest
import simulate
# =============================================================================
class TestDesign(unittest.TestCase):

    def test_damping(self):
        '''Test if X is damped below 1.0e-3 after t=2.0.
        '''
        T, X = simulate.simulate(t0=0.0, t1=2.0, dt=1.0e-2)
        self.assertLess(abs(X[-1]), 1.0e-3)
        return

    def test_overshoot(self):
        '''Test if the overshoot is less than 1.0e-2.
        '''
        T, X = simulate.simulate(t0=0.0, t1=2.0, dt=1.0e-2)
        # Make sure that X is damped below 1.0e-3 at the last iteration.
        self.assertLess(max(X), 1.0e-2)
        return
# =============================================================================
if __name__ == '__main__':
    unittest.main()
# =============================================================================
