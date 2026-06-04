import numpy as np

def estimate_expected_n(n_simulations=100000):
    """
    Estimates E[N], the number of U(0,1) variables needed to exceed a sum of 1.
    """
    
    n_values = []
    
    for _ in range(n_simulations):
        current_sum = 0.0
        count = 0
        
        # We continue adding numbers until the sum exceeds 1 [cite: 5]
        while current_sum <= 1.0:
            # Generate a pseudo-random number in [0, 1) [cite: 14, 101]
            current_sum += np.random.uniform()
            count += 1
            
        n_values.append(count)
    
    # Calculate the average (estimated expectation) [cite: 38]
    return np.mean(n_values)

# Execution
n_trials = 1_000_000
estimated_e = estimate_expected_n(n_trials)

print(f"Total Simulations: {n_trials}")
print(f"Estimated E[N]: {estimated_e:.6f}")
print(f"Theoretical E[N] (e): {np.exp(1):.6f}")
print(f"Difference: {abs(estimated_e - np.exp(1)):.6e}")
