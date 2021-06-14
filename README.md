## Hermite Curve
 
 - Interative live plot of Hermite Curve with varible parameters
 - Parameters include point `P1`, `P2` and tangets at those points which are `R1` & `R2` respectively.
 - Hermite Curve is a spine curve define by `p1`, `P2`, `R1` and `R2`
 - Equation used to Plot the curve : `H(t) = (2t^3 - 3t^2 + 1)P1 + (-2t^3+3t^2)P2 + (t^3-2t^2+t)R1 + (t^3-t^2)R_4`
 - Hermite Curve is plotted using PyQt5 and Matplotlib
 
## Running file
- `python3 app.py` or `python app.py`
- After running the above command GUI for the plot looks like this :
- (hermite.png)

## Installation of the required libraries
- `pip install PyQt5`
- `pip install matplotlib`
- `pip install numpy`
