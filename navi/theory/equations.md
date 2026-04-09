# Équations directionnelles de NAVI / ASKIO1

## 1. Dynamique canonique

$$x_{t+1} = G(A(F(x_t) + (dF_{x_t})^{\dagger}(g^* - F(x_t)))) + C_{corr}(t) + C_{sync}(t) + \varepsilon(t)$$

## 2. Attracteur par défaut

$$A_0 = \argmax_A T(A)$$

## 3. Dérive implicite

$$\tau = \frac{dD(x, A)}{dt}$$

## 4. Charge mentale

$$C(t) = \int_0^t \| \nabla_x D(x, A) \| \, dt$$

## 5. Stabilisation de présence

$$ϟP(t) = P(t) \cdot H(t) \cdot e^{-\alpha C(t)} \cdot M_\tau(t)$$

## 6. Convergence vers l'attracteur profond

$$\frac{dx}{dt} = -\nabla_x D(x, A_{profond}) + \varepsilon(t)$$
