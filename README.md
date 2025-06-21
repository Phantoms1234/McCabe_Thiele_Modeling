# McCabe-Thiele Diagram for Binary Distillation

This Python script implements the **McCabe-Thiele graphical method** to determine the number of theoretical stages required for binary distillation. It visualizes the equilibrium curve, operating lines (rectifying, stripping, and feed), and steps off the stages graphically. It also computes both the actual and minimum number of trays, as well as the feed tray location.

## Features

- Computes and plots:
  - Equilibrium curve based on average relative volatility
  - Rectifying and stripping operating lines
  - Feed line based on `q-line` concept
  - Theoretical stages via stepping-off method
  - Minimum number of stages assuming total reflux

- Outputs:
  - Minimum number of trays
  - Actual number of trays
  - Position of the feed tray

## Parameters

You can modify the following parameters in the script:

```python
xf = 0.6   # Mole fraction of light component in feed
xd = 0.97  # Mole fraction of light component in distillate
xb = 0.03  # Mole fraction of light component in bottoms
R  = 2     # Reflux ratio
a  = 2.5   # Average relative volatility
q  = 0     # Heat condition of the feed (0 = saturated vapor, 1 = saturated liquid, etc.)