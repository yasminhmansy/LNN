from lnn import Model
from lnn import Predicate
from lnn import Variable
from lnn import Implies, Bidirectional, And, Or, Not, Exists, ForAll
from lnn import TRUE, FALSE, UNKNOWN
from lnn import AXIOM

# define the predicates
Smokes, Asthma, Cough = map(Predicate, ['Smokes', 'Asthma', 'Cough'])
Friends = Predicate('Friends', arity=2)

# define the connectives/quantifiers
x, y = map(Variable, ['x', 'y'])
Smokers_have_friends = And(Smokes(x), Friends(x, y))
Asmatic_smokers_cough = (
    Exists(x,
           Implies(And(Smokes(x), Asthma(x)), Cough(x)), world=AXIOM))
Smokers_befriend_smokers = (
    ForAll(
        x, y,
        Implies(Smokers_have_friends(x, y), Smokes(y)), world=AXIOM))

# add root formulae to model
model = Model()
model.add_formulae(
    Asmatic_smokers_cough,
    Smokers_befriend_smokers)

# add data to the model
model.add_facts({
    Smokes.name: {
        'Person_1': TRUE,
        'Person_2': UNKNOWN,
        'Person_3': UNKNOWN},
    Friends.name: {
        ('Person_1', 'Person_2'): TRUE,
        ('Person_2', 'Person_3'): UNKNOWN}})

# reason over the model
model.infer()

# verify the model outputs
model.print()