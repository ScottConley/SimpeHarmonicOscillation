# Simple Harmonic Oscillation

## Derivation
Starting from F = −kx
1. apply Newton's second law: F = ma = -kx; m(dv/dt) = −kx
2. Convert using chain rule: dv/dt = v(dv/dx)
3. Substitute and separate: ∫[v₀→v] m·v' dv' = ∫[x₀→x] −k·x' dx'

Result: ½mv² + ½kx² = E (constant)

For simulation, we will use Velocity Verlet integration:
1. x(t+dt) = x(t) + v(t)·dt + ½a(t)·dt²
2. a(t+dt) = −k·x(t+dt)/m
3. v(t+dt) = v(t) + ½[a(t) + a(t+dt)]·dt

However, at this time it is simpler to model using Euler's method
1. a = -(k/m) * x
2. v_new = v_old + a*dt
3. x_new = x_old + v_new*dt

Energy conservation (flat E plot) validates the integrator.