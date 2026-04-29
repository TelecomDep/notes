Генерация тепловой карты
===================================



Пространственная интерполяция методом Inverse Distance Weighting (IDW)
---------------------

.. figure:: ./image/heatmap/IDW-3Points-425x213.png

   Как найти значение в точках, где нет экспериментальных данных?


.. figure:: ./image/heatmap/IDW-Buffer-425x213.png

   Пример с ограничением радиуса. Источник: https://gisgeography.com/inverse-distance-weighting-idw-interpolation/



.. math::
   :label: (1)

   weight(x) = \left\{ \begin{array}{cl}
   \frac{\sum_{i=1}^{N} w_{i}(x)weight_{i}}{\sum_{i=1}^{N} w_{i}(x)}  & , \text{if } d(x, x_{i}) \neq  0  \\
   weight_{i} & ,  \text{if }d(x, x_{i}) = 0
   \end{array} \right.

, где:

.. math::

   w_{i}(x) = \frac{1}{d(x, x_{i})^{p}}



.. figure:: ./image/heatmap/IDW-Power1-Surface-425x135.png

   Результат интерполяции. Источник: https://gisgeography.com/inverse-distance-weighting-idw-interpolation/