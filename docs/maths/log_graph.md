# Formulas for calculating points along a straight line if axes are logarithmic

Reading from graphs manually with logarithmic scales is vey error prone. 

If you have a graph with a straight line on it where both the x and y axes are in a logarithmic scale the formula of the straight line is found by.  

$$
\begin{aligned}
&X=log(x);Y=log(y);B=log(b)\\
&Y=mX+B\\
&m=\frac{Y_1-Y_0}{X_1-X_0}\\
&m=\frac{log\left(\frac{y_1}{y_0}\right)}{log\left(\frac{x_1}{x_0}\right)}\\
&B=Y-mX\\
&B=log(y_0)-mlog(x_0)\\
&log(x)=\frac{Y-B}{m}\\
&x=10^{\frac{log(y)-B}{m}}\\
&y=10^{mlog(x)+B}
\end{aligned}
$$

Where $(x_0,y_0)$ and $(x_1,y_1)$ are two coordinates along the straight line on the graph.

A similar approach can be taken to derive formulas for a graph where only one of the axes are logarithmic.