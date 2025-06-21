# McCabe_Thiele_Modeling

Using the Mccabe thiele graphical method to calculate various distllation column parameters like number of plates , position of feed plate etc
McCabe-Thiele Diagram Modeling
This Python script implements the McCabe-Thiele graphical method to determine the number of theoretical stages required for a binary distillation column. It calculates and visualizes the equilibrium curve, operating lines (rectifying, stripping, and feed), and steps off the stages, including the feed tray location. It also calculates the minimum number of theoretical stages.

Features
Equilibrium Curve: Calculates and plots the equilibrium curve based on a constant relative volatility a.
Operating Lines: Generates and plots the rectifying, stripping, and feed operating lines.
Intersection Point: Identifies and plots the intersection of the rectifying and feed lines.
Stage Stepping-Off: Graphically determines the number of theoretical stages required for a given separation, highlighting the feed stage.
Minimum Stages: Calculates and plots the minimum number of theoretical stages (total reflux condition).
Visualization: Utilizes matplotlib to create a clear and informative McCabe-Thiele diagram.


Getting Started
Prerequisites
Before running the script, ensure you have the following Python libraries installed:

numpy
matplotlib
You can install them using pip:

*Bash*
pip install numpy matplotlib


Usage
Save the script: Save the provided Python code as a .py file (e.g., mccabe_thiele_model.py).

Define Parameters: Open the script and adjust the following parameters according to your distillation problem:

a: Relative volatility
R: Reflux ratio
xd: Mole fraction of the more volatile component in the distillate
xf: Mole fraction of the more volatile component in the feed
xb: Mole fraction of the more volatile component in the bottoms
q: Feed condition (q-value, e.g., 1 for saturated liquid, 0 for saturated vapor)

Example Parameter Setup within the script:

*Python*

# Example Parameters (You should adjust these)
a = 2.5   # Relative volatility
R = 1.5   # Reflux ratio
xd = 0.95 # Distillate mole fraction
xf = 0.5  # Feed mole fraction
xb = 0.05 # Bottoms mole fraction
q = 1     # Feed condition (e.g., 1 for saturated liquid)
Run the script: Execute the script from your terminal:

*Bash*

python mccabe_thiele_model.py
The script will output the calculated number of trays (stages), the minimum number of trays, and the position of the feed tray in your console. A matplotlib plot of the McCabe-Thiele diagram will also be displayed.

Code Structure
The script is organized into logical sections:

Parameter Initialization: Defines the key distillation parameters.
Line Equations: Calculates points for the equilibrium curve, 45-degree diagonal, rectifying line, feed line, and stripping line. It handles the q=1 (saturated liquid feed) special case for the feed line.
stepping_off() function: Iteratively calculates and stores the coordinates for each theoretical stage, determining the total number of stages and the feed stage location.
minimum_stages() function: Calculates the minimum number of theoretical stages under total reflux conditions.
Output: Prints the calculated number of stages to the console.
Plotting: Uses matplotlib.pyplot to generate the McCabe-Thiele diagram with all relevant lines and points.
Contributing
Feel free to fork this repository, make improvements, or suggest new features. Pull requests are welcome!

*License*
This project is open-source and available under the MIT License.

