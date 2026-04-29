Генерация тепловой карты
===================================


Пространственная интерполяция методом Inverse Distance Weighting (IDW)
---------------------




.. math::

   weight(x) = \left\{ \begin{array}{cl}
   \frac{\sum_{i=1}^{N} w_{i}(x)weight_{i}}{\sum_{i=1}^{N} w_{i}(x)}  & , \text{if } d(x, x_{i}) \neq  0  \\
   weight_{i} & ,  \text{if }d(x, x_{i}) = 0
   \end{array} \right.