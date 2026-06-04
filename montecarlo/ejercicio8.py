import numpy as np

def estimate_exercise_8_expected_value(n_simulations=1000000):
    limit = np.exp(-3)
    # Using a modern generator for better statistical properties [cite: 419]
    
    n_values = []
    
    for _ in range(n_simulations):
        prod = 1.0
        count = 0
        
        while True:
            u = np.random.uniform()
            # Check if the NEXT product would still satisfy the condition
            if prod * u >= limit:
                prod *= u
                count += 1
            else:
                # If the condition fails, we stop. 
                # The current 'count' is the Maximum n.
                break
        
        n_values.append(count)
    
    return np.mean(n_values)

# Execution
expected_n = estimate_exercise_8_expected_value(1000000)
print(f"Estimated E[N]: {expected_n:.6f}")
print(f"Theoretical E[N]: 3.000000") # For this specific distribution, E[N] = -lambda
