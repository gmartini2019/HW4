# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = 'no'
    answers["(b)"] = 'no'
    answers["(c)"] = 'yes'
    answers["(d)"] = 'yes'

    # explain-string: explanation in english prose
    answers["(a) explain"] = """Think of Rule 2 and Rule 3:
    Rule 2: MS=Single --> DB=Yes
    Rule 3: AI=Low --> DB=Yes
    Rule 2 and Rule 3 could be triggered at the same time by the same record, so the set is not mutually exclusive; there are other examples in the dataset as well."""
    answers["(b) explain"] = """There are examples of records that cannot be classified based on our rules. For a set to be exhaustive, t must have at least one rule that applies to every conceivable combination of attribute value, so that no record is left uncovered.
    There might be combinations in the dataset that are not accounted for using the rule set. """
    answers["(c) explain"] = """Because the set of rules is not mutually exclusive; we need ordering to determine which rule applies first when more than one match a specific record, to create no confusion."""
    answers["(d) explain"] = """Because the set of rules is not exhaustive; we need a default class because some records may NOT be covered by all rules, which is something we cannot have, so  a default class assured that for each record there is at LEAST one class."""


    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = 'no'
    answers["(b)"] = 'no'
    answers["(c)"] = 'yes'

    answers["(a) example"] = "Body Temperature = Warm Blooded --> Mammal; all mammals are warm blooded, but also a bird (pigeon) is warm blooded. Rule 3 then overlaps with Rule 1."
    answers["(b) example"] = """To be exhaustive, the set must account for every possible value combination. In our set, only 4 features are accounted for."""
    answers["(c) example"] = """You need ordering if the set is not mutually exclusive, to determine which rule to apply first when an animal could potentially satisfy the criteria for more than one class."""


    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = False
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    answers["(a) explain"] = "The weight update formula is applied in the reverse direction. The weights in a subsequent level are updated before the weights at a preceding level; this means that weights at level k+1 are updated before than weights at level k. With this reasoning, we can use the errors for neurons at the k+1th layer to estimate the errors for neurons at the kth layer."
    answers["(b) explain"] = """This is the reverse process of before; during testing, the weights from the previous iteration are used to compute the output for each neuron in the network and the computation follows  the forward direction. The value of the neurons 
    at level k are elaborated before computing the outputs at level k+1."""
    answers["(c) explain"] = """The vanishing gradient problem is when the gradients of the loss function become too small and training is slowed down or halted, because the weights of the network are no longer significantly updated. Nowhere is there an assurance
    (and the contrary is much more likely)  that the training error becomes 0 and the testing erorr comes out very large. What that is, is overfitting, and vanishing gradient is a different challenge."""
    answers["(d) explain"] = """It will be close to 0, but not perfectly 0. When, during training, a training loss minimum is reached, the gradient of the training loss will be closed to 0.
    The book never explicitly says that it reaches 0, so I cannot assume that it would be so. Using simple mathematically, one could come to the conclusion that the gradient would become 0 and training would
    be halted, but even when one trains NNs and checks the curves, the accuracy will  sometimes hit 100% but WILL keep training, so I assume that the gradient will not be 0."""


    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.4
    answers["(a) P(X_2=1)"] = 0.25
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = 'dependent'

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = 'yes'

    # float
    answers["(c) P(X_1 = 1 | +)"] = 0.8
    answers["(c) P(X_1 = 1 | -)"] = 0.5
    answers["(c) P(X_2 = 1 | +)"] = 0.5
    answers["(c) P(X_2 = 1 | -)"] = 0.32
    answers["(c) P(X_3 = 1 | +)"] = 0.4
    answers["(c) P(X_3 = 1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = "+"
    answers["(d) Row 2"] = "-"
    answers["(d) Row 3"] = "-"
    answers["(d) Row 4"] = "-"

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.38

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 50
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = """The clusters are of sizes way too different. 1 cluster would englobe all of the data, rednering the operation useless. 5 clusters means that the neighborhood for each point would be very large
    and the smaller, denser cluster to the right would be englobed with erraneous data from the right. 50 is best, even if some extra cluster will form to the right, they can be dealt with using postprocessing. This is an approach directly referenced from the slides."""
    answers["(b) explain"] = """5 clusters seems best. Both clusters are of similar sizes and densities. Like before, 1 cluster would invalidate the procedure. 5 clusters is enough to be dealt with afterwards. The neighborhood range is
    just big enough to envelop good sized clusters to deal with efficiently later in post processing. Same principle as the first question, but not as drastic."""

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.6
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = """I got the answer by counting the positive occurences of A and dividing that number by all the positive occurences."""
  
    # type: float
    answers["(b) P(+|R)"] = 0.8571428571428571  # WRONG
    answers["(b) P(R|+)"] = 0.096
    answers["(b) P(R|-)"] = 0.016000000000000004

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # explain_string
    answers["(b) Explain your reasoning"] = """Product of the conditional pobabilities fiven the positive class
    is higher than that given the negative class, indicating a stronger likelihood of the samplebelonging to the positive class"""
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = 'no'
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = 'no'
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = 'no'

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  'A and B are not conditionally independent given the class "+" because the joint probability of A and B given the class "+" does not equal the product of their individual conditional probabilities.'
  
    return answers

def question4():
    return None
def question2():
    return None

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
