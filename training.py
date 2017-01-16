import random
import sys
import copy
import test

# datas from test.csv
dataset = []

binary_operators = ['-','+','*','/','^']
unary_operators = ['~', 'abs', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sinh', 'cosh', 'tanh', 'exp', 'sqrt', 'log']
terminals = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x17', 'x18', 'x19', 'x20', 'x21', 'x22', 'x23', 'x24', 'x25', 'x26', 'x27', 'x28', 'x29', 'x30', 'x31', 'x32', 'x33', 'x34', 'x35', 'x36', 'x37', 'x38', 'x39', 'x40', 'x41', 'x42', 'x43', 'x44', 'x45', 'x46', 'x47', 'x48', 'x49', 'x50', 'x51', 'x52', 'x53', 'x54']
operators = binary_operators + unary_operators
all_node = terminals + binary_operators + unary_operators

population = 20
init_max_depth = 3
max_depth = 6
max_random_number = 4


class tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        self.depth = None

    # return True if the tree is complete, else return false
    def tree_complete(self):
        if self.data in binary_operators:
            if self.left == None or self.right == None:
                return False
            else:
                return (self.left.tree_complete() and self.right.tree_complete())
        elif self.data in unary_operators:
            if self.left == None:
                return False
            else:
                return self.left.tree_complete()
        else:
            return True

    # select one random node from the tree excluding terminal
    def random_select(self,selection,count):
        count = count + 1
        if self.data in binary_operators:
            if random.randrange(0,count) == 0:
                selection = self
            if random.randrange(0,2):
                return self.left.random_select(selection,count)
            else:
                return self.right.random_select(selection,count)
        elif self.data in unary_operators:
            if random.randrange(0,count) == 0:
                selection = self
            return self.left.random_select(selection,count)
        else:
            if selection != None:
                return selection
            else:
                print "ERROR"

    # select one random node from the tree including terminal
    def random_select2(self,selection,count):
        count = count + 1
        if self.data in binary_operators:
            if random.randrange(0,count) == 0:
                selection = self
            if random.randrange(0,2):
                return self.left.random_select2(selection,count)
            else:
                return self.right.random_select2(selection,count)
        elif self.data in unary_operators:
            if random.randrange(0,count) == 0:
                selection = self
            return self.left.random_select2(selection,count)
        else:
            if random.randrange(0,count) == 0:
                selection = self
            return selection

     # grow the tree using random grow method
    def random_grow(self, data):
        if self.data in binary_operators:
            if self.left == None:
                new_node = tree()
                new_node.data = data
                new_node.depth = self.depth+1
                self.left = new_node
                return True
            elif self.left.random_grow(data):
                return True 
            elif self.right == None:
                new_node = tree()
                new_node.data = data
                new_node.depth = self.depth+1
                self.right = new_node
                return True
            elif self.right.random_grow(data):
                return True
        elif self.data in unary_operators:
            if self.left == None:
                new_node = tree()
                new_node.data = data
                new_node.depth = self.depth+1
                self.left = new_node
                return True
            else:
                return self.left.random_grow(data)
        else:
            return False

    # grow the tree using full grow method until it reaches the max_depth
    def full_grow(self, max_depth):
        if self.data in binary_operators:
            if self.depth < max_depth - 1:
                if self.left == None:
                    new_node = tree()
                    if random.randrange(0,3) == 0:
                        new_node.data = unary_operators[random.randrange(0,len(unary_operators))]
                    else:
                        new_node.data = binary_operators[random.randrange(0,len(binary_operators))]
                    new_node.depth = self.depth+1
                    self.left = new_node
                    return True
                elif self.left.full_grow(max_depth):
                    return True 
                elif self.right == None:
                    new_node = tree()
                    if random.randrange(0,3) == 0:
                        new_node.data = unary_operators[random.randrange(0,len(unary_operators))]
                    else:
                        new_node.data = binary_operators[random.randrange(0,len(binary_operators))]
                    new_node.depth = self.depth+1
                    self.right = new_node
                    return True
                elif self.right.full_grow(max_depth):
                    return True
            else:
                if self.left == None:
                    new_node = tree()
                    if random.randrange(0,2) == 0:
                        new_node.data = terminals[random.randrange(0,len(terminals))]
                    else:
                        new_node.data = random.uniform(0, 10)
                    new_node.depth = self.depth+1
                    self.left = new_node
                    return True
                elif self.right == None:
                    new_node = tree()
                    if random.randrange(0,2) == 0:
                        new_node.data = terminals[random.randrange(0,len(terminals))]
                    else:
                        new_node.data = random.uniform(0, 10)
                    new_node.depth = self.depth+1
                    self.right = new_node
                    return True
                else:
                    return False

        elif self.data in unary_operators:
            if self.depth < max_depth - 1:
                if self.left == None:
                    new_node = tree()
                    if random.randrange(0,3) == 0:
                        new_node.data = unary_operators[random.randrange(0,len(unary_operators))]
                    else:
                        new_node.data = binary_operators[random.randrange(0,len(binary_operators))]
                    new_node.depth = self.depth+1
                    self.left = new_node
                    return True
                elif self.left.full_grow(max_depth):
                    return True 
            else:
                if self.left == None:
                    new_node = tree()
                    if random.randrange(0,2) == 0:
                        new_node.data = terminals[random.randrange(0,len(terminals))]
                    else:
                        new_node.data = random.uniform(0, 10)
                    new_node.depth = self.depth+1
                    self.left = new_node
                    return True
                else:
                    return False

        else:
            return False

    #print reverse polish notation of the tree
    def rpn_print(self,buffer):
        if self.data in binary_operators:
            self.left.rpn_print(buffer)
            self.right.rpn_print(buffer)
            buffer.append(self.data)
        elif self.data in unary_operators:
            self.left.rpn_print(buffer)
            buffer.append(self.data)
        else:
            buffer.append(str(self.data))

    # measure depth of the tree
    def measure_depth(self,depth):
        depth = depth + 1
        if self.data in binary_operators:
            return max([self.left.measure_depth(depth), self.right.measure_depth(depth)])
        elif self.data in unary_operators:
            return self.left.measure_depth(depth)
        else:
            return depth

    # measure fitness of the tree using test.py
    def measure_fitness(self):
        buffer = []
        self.rpn_print(buffer)
        expression = ' '.join(buffer)

        #evaluate mean square erroor 
        try:
            mean_square_error = test.evaluate_mse(dataset, expression)
        except:
            mean_square_error = float('inf')
        return mean_square_error

# initialize population 
def init_population(trees):

    # if number of populations with non-infinite fitness is more than init_condition, terminate initialization
    init_condition = population/4
    acceptable_population = False 

    #try to initialize polulation until it reaches init condition.
    while not acceptable_population:

        # initialize 10 trees with one node as random operator it's data
        for x in range(0,population):
            init_tree = tree()
            if random.randrange(0,2) == -1:
                init_tree.data = unary_operators[random.randrange(0,len(unary_operators))]
            else:
                init_tree.data = binary_operators[random.randrange(0,len(binary_operators))]
            init_tree.depth = 0
            trees.append(init_tree)

        # grow half of the initial population using Full Initialization
        for x in range(0,population/2):
            while(not trees[x].tree_complete()):
                trees[x].full_grow(init_max_depth)

        # grow half of the initial population using Grow Initialization
        for x in range(population/2,population):
            while(not trees[x].tree_complete()):
                dice = random.randrange(0,4)
                if dice == 0:
                    data = unary_operators[random.randrange(0,len(unary_operators))]
                elif dice == 1:
                    data = binary_operators[random.randrange(0,len(binary_operators))]
                else:
                    if random.randrange(0,2) == 0:
                        data = terminals[random.randrange(0,len(terminals))]
                    else:
                        data = random.uniform(0, 10)
                trees[x].random_grow(data)

        # count number of trees with non-infinite fitness and if it is more that init_condition, terminate the loop
        count = 0
        for x in range(0,population):
            if not trees[x].measure_fitness() == float('inf'):
                count += 1
        if count >= init_condition:
            acceptable_population = True
        else:
            trees = []

# apply crossover on tree_a and tree_b
def crossover(tree_a, tree_b):

    # select random node excluding the terminal node
    crossover_point_a = tree_a.random_select(None,0)
    crossover_point_b = tree_b.random_select(None,0)


    if random.random() < 0.5:
        if crossover_point_a.data in unary_operators:
            crossover_point_a.left = crossover_point_b.left
        else:
            if random.random() < 0.5:
                crossover_point_a.left = crossover_point_b.left
            else:
                crossover_point_a.right = crossover_point_b.left
        new_tree = tree_a
    else:
        if crossover_point_b.data in unary_operators:
            crossover_point_b.left = crossover_point_a.left
        else:
            if random.random() < 0.5:
                crossover_point_b.left = crossover_point_a.left
            else:
                crossover_point_b.right = crossover_point_a.left
        new_tree = tree_b
    return new_tree


# mutate the tree
def mutate(tree):

    # select random node including the terminal node
    mutate_point = tree.random_select2(None,0)

    # with 50%/50% chance, do subtree mutation or point mutaiton
    dice = random.randrange(0,2)
    
    # subtree mutation
    if dice == 0:
        mutate_point.left = None
        mutate_point.right = None
        mutate_point.depth = 0

        # with 25%/25%/50% chance, change mutate_point to unary_operator, or binary_operator, or teminal
        dice = random.randrange(0,2)
        if dice == 0:
            mutate_point.data = unary_operators[random.randrange(0,len(unary_operators))]
        else:
            mutate_point.data = binary_operators[random.randrange(0,len(binary_operators))]
    
        # with 50%/50% chance, generate subtree using random grow or full grow
        if random.randrange(0,2) == 0:
            while(not mutate_point.tree_complete()):
                dice = random.randrange(0,4)
                if dice == 0:
                    data = unary_operators[random.randrange(0,len(unary_operators))]
                elif dice == 1:
                    data = binary_operators[random.randrange(0,len(binary_operators))]
                else:
                    if random.randrange(0,2) == 0:
                        data = terminals[random.randrange(0,len(terminals))]
                    else:
                        data = random.uniform(0, 10)
                mutate_point.random_grow(data) 
        else:
            while(not mutate_point.tree_complete()):
                mutate_point.full_grow(random.randrange(1,max_random_number))

    # point mutation
    else:
        for x in range(0,random.randrange(0,max_random_number)):
            mutate_point = tree.random_select2(None,0)
            if mutate_point.data in binary_operators:
                mutate_point.data = binary_operators[random.randrange(0,len(binary_operators))]
            elif mutate_point.data in unary_operators:
                mutate_point.data = unary_operators[random.randrange(0,len(unary_operators))]
            else:
                if random.randrange(0,2) == 0:
                    mutate_point.data = terminals[random.randrange(0,len(terminals))]
                else:
                    mutate_point.data = random.uniform(0, 10)
    return tree

# apply genetic operations such as crossover and mutation on trees until the termination condition is satisfied
def apply_genetic_operation(trees, termination_cond1, termination_cond2, name):
    while trees[0].measure_fitness() > termination_cond1 or trees[population/2-1].measure_fitness() > termination_cond2:
        #remove trees that does not work
        trees = [k for k in trees if not k.measure_fitness() == float('inf')]
        #sort trees by order of fitness function
        trees.sort(key=lambda x: x.measure_fitness(), reverse=False)
        
        print "\nevolving " + name + "..."
        buffer = []
        trees[0].rpn_print(buffer)
        print  "best expression: " + ' '.join(buffer)
        print "fitness of expression: " + str(trees[0].measure_fitness())

        fitness_list=[]
        for x in range (0,len(trees)):
            fitness_list.append(trees[x].measure_fitness())

        for x in range (0,population):
            fit_tree = False
            while not fit_tree:
                crossover_tree = crossover(copy.deepcopy(trees[random.randrange(0,population/4)]),copy.deepcopy(trees[random.randrange(0,population/4)]))
                mutation_tree = mutate(crossover_tree)
                if mutation_tree.measure_depth(0) < max_depth:
                    fit_tree = True
            if not mutation_tree.measure_fitness() in fitness_list:
                trees.append(mutation_tree)
        trees.sort(key=lambda x: x.measure_fitness(), reverse=False)
        trees = trees[0:population]
    return trees

# print fitness of trees
def print_fitness(trees):
    for x in range (0,len(trees)):
            print trees[x].measure_fitness()


if __name__ == "__main__":
    #open test.csv file that is passed as argument as read only
    f = open(sys.argv[1],'r')
    #ignore first 1 line  
    for x in xrange(1,2):
        f.readline()
    #acquire data from test.csv line by line, and store it in dataset
    for x in xrange(0,747):
        dataset.append(
            map(float,(f.readline().split(","))))
    #close file
    f.close()

    trees1 = []
    trees2 = []

    #create initial population of programs
    init_population(trees1)
    init_population(trees2)

    #sort trees by order of fitness function
    trees1.sort(key=lambda x: x.measure_fitness(), reverse=False)
    trees2.sort(key=lambda x: x.measure_fitness(), reverse=False)

    print "trees1 evolving... "
    print "termination condition: fitness of trees1[0] < 0.15 and trees1[population/2-1] < 0.5"
    trees1 = apply_genetic_operation(trees1,0.15,0.5,"tree1")
    
    print "\ntrees2 evolving... "
    print "termination condition: fitness of trees2[0] < 0.15 and trees2[population/2-1] < 0.5"
    trees2 = apply_genetic_operation(trees2,0.15,0.5,"tree2")

    #merge trees1 and trees2 into tress3
    print "\nmerge trees1 and trees2 into trees3"
    trees3 = trees1[0:population/2] + trees2[0:population/2]

    print "\ntrees3 evolving... "
    print "termination condition: fitness of trees3[0] < 0.08 and trees3[population/2-1] < 0.10"
    trees3 = apply_genetic_operation(trees3,0.08,0.10,"tree3")
    
    print " "

    buffer = []
    trees3[0].rpn_print(buffer)
    print  ' '.join(buffer)






