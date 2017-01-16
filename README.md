# Simple Genetic Programming for Symbolic Regression

# 1. Symbolic Regression
The goal of this program is to find a expression that fits the given dataset with as small error as possible. For example, suppose your training data set includes tuples (x, y), from which you want to learn the best model f such that y = f(x) explains the given data set, as well as unseen test data set, as precisely as possible. If the training data consist of X = {1.2, 2, 3} and Y = {3.1, 4.6, 6.8}, and the test data set consist of X0 = {6, 5} and Y 0 = {13, 10.5}, one possible symbolic regression model would be y = 2x + 1. Figure 1 shows the result of symbolic regression.

![Alt text](Figures/Figure1.jpg?raw=true "Title")

With Genetic Programming, you can build candidate expressions for f , and evaluate them using Mean Square Error, which is calculated as follows:

![Alt text](Figures/Figure2.jpg?raw=true "Title")

# 2. Dataset
The symbolic regression dataset we are using contains 57 input variables (x1,...,x57), 1 output variables, y and contains 747 rows. Using this dataset, this program evolves a symbolic regression model.

# 3. How to get started

The first program, "train.py" is an implementation of GP that takes a .csv file containing the training data as input, and prints out the evolved expression using Reverse Polish Notation. 

The second program, "test.py" takes two inputs: the evolved RPN expression in one string, and a .csv file containing the test data. Subsequently, it evaluatse the given RPN expression on the test data and print out the MSE.

Following ternimal and non-terminal nodes for GP, and corresponding symbols when printing out the evolved expression in RPN are used:
-  Terminals: x1,. . ., x57, as well as any floating point constant numbers
-  Unary Operators: ⇠ (unary minus), abs, sin, cos, tan, asin, acos, atan, sinh, cosh,
tanh, exp, sqrt, log
-  Binary Operators: +, -, *, /,ˆ(power)
-  
```sh
# For example, x24   sin( 2x3) would be represented by x24 2 ^ 2 ~ x3 * sin -.
# in directory "Simple_Genetic_Programming/"
$ python training.py test.csv
...
x24 2 ^ 2 ~ x3 * sin - # this RPN equation can be different everytime the program is run
$ python test.py "x24 2 ^ 2 ~ x3 * sin -" test.csv

```

# 4. Best Result
The program was run on azure server with 5 different instances. After 3 days of testing, the best expression was “x49 x35 - x15 / x20 x38 / x29 x35 / + * sqrt”. Its fitness is 0.70533828692. 

# 5. Common problems and solutions
1. Even though merging mechanism (merging of trees1 and trees2 into trees3) was implmeneted to increase diversity of each individual, it failed to improve the result at all, compared to the one with no merging mechanism.

# 6. Detailed Explanation of the CODE

test.py takes two inputs: the evolved RPN expression in one string, and a .csv file containing the test data. Subsequently, it evaluates the given RPN expression on the test data and print out the MSE. 
Stack was used to evaluate the expression in reverse polish notation.

train.py 
“train.py” takes a .csv file containing the training data as input, and prints out the evolved expression using Reverse Polish Notation. 

“tree” class represents each expression. “tree” has 4 elements. “left”, “right”, “data” and “depth”. “left” and “right” can point to another tree and data contains operator or terminal data. “depth” refers to how deep the current node is located at.

First, 2 initial population of programs are created, “trees1” and “trees2”. Half of the trees in each population (“trees1” and “trees2”) are created using full grow method, and the other half using random grow method.

Next, genetic operations are repeatedly applied to “trees1” and “trees2” until the termination condition is met. These two populations will later be merged into one population “trees3”. I believe this approach can increase the diversity of population.

1 iteration of genetic operation does the following. First, it sorts the “trees” regarding to its fitness function in increasing manner. Then, 2 trees that are in the first quarter of the “trees” are randomly selected. Next, Mutation and Crossover are applied to these two trees (Detailed explanation of Mutation and Crossover is in the following paragraphs). If the result tree exceeds the “max_depth”, it repeats the Mutation and Crossover process until it doesn’t exceed. This is to restrict the depth of each trees, since deep trees increases computation time exponentially. Iteration of genetic operations are terminated when the termination condition is met. 

Crossover of “tree_a” and “tree_b” does the following. First it selects a random node in each trees excluding the terminal nodes. Then it swaps the one of the selected node’s child with the other selected node’s child. 

Mutation of “tree” does the following. First it selects a random node in the “tree” including the terminal nodes. Next, with 50%/50% chance, subtree mutation or point mutation is applied. Point mutation changes the selected node’s randomly to another data in the same group. Subtree mutation replaces the selected node with completely new tree. This is done by random grow initialization method or full grow initialization method with 50%/50% chance (Ramped Half and Half initialization method).

When genetic operation for “trees1” and “trees2” are finished, these two populations are merged into “trees3”. Then, final while-loop of genetic operation is applied to the “trees3”. Then, the program prints the final expression.

