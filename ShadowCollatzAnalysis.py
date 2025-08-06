from multiprocessing import Pool, cpu_count
from typing import Tuple
import time  

def shadow_collatz_sequence(n: int, max_steps: int = 1000) -> list[int]:
    if n == 0:
        raise ValueError("n must not be 0")
    sequence = []
    steps = 0
    while n != -1 and steps < max_steps:
        sequence.append(n)
        n = n // -2 if n % 2 == 0 else 3 * n - 1
        steps += 1
    if n == -1:
        sequence.append(-1)
    return sequence

def check_convergence(n: int, max_steps: int = 1000) -> Tuple[int, bool, int]:
    seq = shadow_collatz_sequence(n, max_steps=max_steps)
    converged = seq[-1] == -1
    return (n, converged, len(seq) - 1 if converged else len(seq))

def check_and_report(n: int) -> Tuple[int, bool, int]:
    if n == 0:
        return (0, True, 0)
    return check_convergence(n)

if __name__ == "__main__":
    max_steps = 2000
    N = 50_000_000 
    values = list(range(-N, 0)) + list(range(1, N + 1))

    print(f"🔎 Checking Shadow Collatz convergence from -{N} to +{N} using {cpu_count()} CPU cores...")
    
    start_time = time.time() 
    
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(check_and_report, values)

    elapsed_time = time.time() - start_time 

    # classification
    failed = [(n, steps) for n, ok, steps in results if not ok]
    succeeded = [(n, steps) for n, ok, steps in results if ok]

    if failed:
        print("❌ These values did NOT converge within the step limit:")
        for n, steps in failed:
            print(f"n = {n}, reached {steps} steps")
    else:
        print(f"✅ All values from -{N} to +{N} converged to -1 within {max_steps} steps.")

    # the longest steps and initial number
    if succeeded:
        max_n, max_steps_reached = max(succeeded, key=lambda x: x[1])
        print(f"\n🌟 Maximum steps observed: {max_steps_reached} steps")
        print(f"   Initial value: {max_n}")

    # time
    print(f"\n⏱️ Total execution time: {elapsed_time:.2f} seconds")
