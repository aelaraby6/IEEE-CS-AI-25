def probability_distribution(data):
    if not isinstance(data, list) or not data:
        raise ValueError("Input must be a non-empty list of discrete values.")
    
    total_count = len(data)
    unique_values = set(data)
    return {value: data.count(value) / total_count for value in unique_values}


data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1]
print(probability_distribution(data)) 




def conditional_probability(event_a, event_b):
    if not (isinstance(event_a, list) and isinstance(event_b, list)):
        raise ValueError("Both inputs must be lists.")
    if len(event_a) != len(event_b):
        raise ValueError("Both lists must have the same length.")
    if not all(isinstance(x, int) for x in event_a + event_b):
        raise ValueError("All elements in the input lists must be integers.")
    
    count_a = sum(event_a)
    if count_a == 0:
        return 0
    
    count_a_and_b = sum(1 for a, b in zip(event_a, event_b) if a == 1 and b == 1)
    return count_a_and_b / count_a


event_a = [1, 0, 1, 0, 1]
event_b = [1, 1, 0, 0, 1]
print(conditional_probability(event_a, event_b)) 



def bayes_theorem(prior_a, prior_b, conditional_b_given_a):
    if not all(isinstance(x, (int, float)) for x in [prior_a, prior_b, conditional_b_given_a]):
        raise ValueError("All inputs must be numbers.")
    if not (0 <= prior_a <= 1 and 0 <= prior_b <= 1 and 0 <= conditional_b_given_a <= 1):
        raise ValueError("Probabilities must be between 0 and 1.")
    if prior_b == 0:
        raise ZeroDivisionError("The prior probability of B cannot be zero.")
    
    return (conditional_b_given_a * prior_a) / prior_b

prior_a = 0.3
prior_b = 0.6
conditional_b_given_a = 0.8
print(bayes_theorem(prior_a, prior_b, conditional_b_given_a))  
