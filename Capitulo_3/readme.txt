Neste capítulo foi estudada a recursão. Recursão nada mais é do que uma função que chama a si mesma.

Esta técnica pode ser dividida em duas etapas: caso base e passo iterativo. O passo iterativo é onde a função chama a si mesma, e ele é repetido até que seja satisfeito o critério do caso base. Quando estamos no caso base, a função retorna seu resultado.

Esta técnica pode facilitar o desenvolvimento de software; no entanto, há casos em que ela pode ser mais custosa e difícil do que uma abordagem iterativa. Por exemplo, no caso desenvolvido neste capítulo, usamos a recursão para calcular a sequência de Fibonacci
 (veja a imagem do gráfico). Note que, quanto mais elementos calculamos, mais tempo é necessário para o cálculo. A partir do elemento 30, ocorre a explosão combinatória, ou seja, o tempo para o cálculo começa a crescer vertiginosamente.