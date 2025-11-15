
import time
import threading

"""
1. Python Multithreading: Concurrent vs Parallel Processing

In Python, multithreading is primarily CONCURRENT PROCESSING rather than true parallel processing 
due to the Global Interpreter Lock (GIL). The GIL prevents multiple native threads from executing 
Python bytecodes simultaneously, even on multi-core processors.

- Concurrent Processing: Multiple tasks make progress by context switching, but only one thread 
  executes Python code at any given moment
- Parallel Processing: Multiple tasks execute simultaneously on different CPU cores

For CPU-bound tasks (like factorial calculations), Python threads cannot achieve true parallelism 
because of the GIL. However, for I/O-bound tasks (file operations, network requests), multithreading 
can still provide performance benefits as threads can release the GIL while waiting for I/O operations.

This experiment with factorial calculations will demonstrate the GIL's impact on CPU-bound tasks.
"""

def factorial(n):
    """
    2. Factorial Function with Big-O Analysis
    
    Time Complexity: O(n)
    - The function performs exactly n multiplications
    - Each iteration of the loop is a primitive operation
    - Number of operations grows linearly with input size n
    
    Space Complexity: O(log(n!)) ≈ O(n log n)
    - The result requires O(n log n) bits to store
    - We use constant additional space (only one variable 'result')
    
    Primitive Operations Analysis:
    - 1 assignment (result = 1)
    - n comparisons (i <= n)
    - n increments (i += 1)
    - n multiplications (result *= i)
    - Total: 3n + 1 operations → O(n)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


class FactorialThread(threading.Thread):
    """
    3. Multithreading Implementation
    
    This class extends threading.Thread to calculate factorials in separate threads.
    Each thread records its own start and end times for accurate measurement.
    """
    def __init__(self, number, results_dict, times_dict, thread_id):
        threading.Thread.__init__(self)
        self.number = number
        self.results_dict = results_dict
        self.times_dict = times_dict
        self.thread_id = thread_id
        
    def run(self):
        """Thread execution method - calculates factorial and records timing"""
        start_time = time.time_ns()
        
        # Calculate factorial (CPU-bound operation)
        result = factorial(self.number)
        
        end_time = time.time_ns()
        
        # Store results and timing information
        self.results_dict[self.thread_id] = result
        self.times_dict[self.thread_id] = (start_time, end_time)


def run_multithreaded_experiment():
    """
    3. Multithreaded Factorial Calculation
    
    Creates three separate threads for calculating 50!, 100!, and 200!
    Measures time using: Time_Elapsed = End_Time_Last_Thread - Start_Time_First_Thread
    """
    numbers = [50, 100, 200]
    rounds = 10
    multithread_times = []
    
    print("=" * 80)
    print("MULTITHREADED EXECUTION - 10 ROUNDS")
    print("=" * 80)
    
    for round_num in range(rounds):
        # Initialize storage for results and timing
        results = {}
        thread_times = {}
        threads = []
        
        # Create thread objects
        for i, num in enumerate(numbers):
            thread = FactorialThread(num, results, thread_times, f"thread_{i}")
            threads.append(thread)
        
        # Start all threads
        for thread in threads:
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        # Calculate overall timing according to the specified formula
        start_times = [times[0] for times in thread_times.values()]
        end_times = [times[1] for times in thread_times.values()]
        
        first_start = min(start_times)
        last_end = max(end_times)
        elapsed_time = last_end - first_start
        
        multithread_times.append(elapsed_time)
        
        # Display results for this round
        print(f"Round {round_num + 1}:")
        print(f"  Time Elapsed: {elapsed_time:>15,} nanoseconds")
        print(f"  Individual Thread Times:")
        for i, (start, end) in enumerate(thread_times.values()):
            thread_duration = end - start
            print(f"    Thread {i+1} (factorial {numbers[i]}): {thread_duration:>12,} ns")
        
        # Verify calculations (optional - can be removed for cleaner output)
        for i, num in enumerate(numbers):
            result = results[f"thread_{i}"]
            digits = len(str(result))
            print(f"    Factorial {num}! has {digits} digits")
        print()
    
    # Calculate and display average
    avg_time = sum(multithread_times) / len(multithread_times)
    print(f"SUMMARY - MULTITHREADED:")
    print(f"  Average Time: {avg_time:,.2f} nanoseconds")
    print(f"  Min Time: {min(multithread_times):,} nanoseconds")
    print(f"  Max Time: {max(multithread_times):,} nanoseconds")
    print("=" * 80)
    
    return multithread_times, avg_time


def run_single_threaded_experiment():
    """
    4. Single-Threaded Factorial Calculation
    
    Calculates the same factorials (50!, 100!, 200!) sequentially in a single thread
    """
    numbers = [50, 100, 200]
    rounds = 10
    single_thread_times = []
    
    print("SINGLE-THREADED EXECUTION - 10 ROUNDS")
    print("=" * 80)
    
    for round_num in range(rounds):
        results = []
        
        # Record start time
        start_time = time.time_ns()
        
        # Calculate factorials sequentially
        for num in numbers:
            result = factorial(num)
            results.append(result)
        
        # Record end time
        end_time = time.time_ns()
        
        elapsed_time = end_time - start_time
        single_thread_times.append(elapsed_time)
        
        print(f"Round {round_num + 1}:")
        print(f"  Time Elapsed: {elapsed_time:>15,} nanoseconds")
        
        # Display individual calculation info
        for i, (num, result) in enumerate(zip(numbers, results)):
            digits = len(str(result))
            print(f"    Factorial {num}! has {digits} digits")
        print()
    
    # Calculate and display average
    avg_time = sum(single_thread_times) / len(single_thread_times)
    print(f"SUMMARY - SINGLE-THREADED:")
    print(f"  Average Time: {avg_time:,.2f} nanoseconds")
    print(f"  Min Time: {min(single_thread_times):,} nanoseconds")
    print(f"  Max Time: {max(single_thread_times):,} nanoseconds")
    print("=" * 80)
    
    return single_thread_times, avg_time


def main():
    """
    Main function to run both experiments and provide comparative analysis
    """
    print("FACTORIAL CALCULATION PERFORMANCE ANALYSIS")
    print("Comparing Multithreaded vs Single-Threaded Execution")
    print()
    
    # Run multithreaded experiment
    multi_times, multi_avg = run_multithreaded_experiment()
    
    print("\n" + "="*80)
    print()
    
    # Run single-threaded experiment
    single_times, single_avg = run_single_threaded_experiment()
    
    # Comparative Analysis
    print("\n" + "="*80)
    print("COMPARATIVE ANALYSIS")
    print("="*80)
    
    improvement = ((single_avg - multi_avg) / single_avg) * 100
    status = "IMPROVEMENT" if improvement > 0 else "OVERHEAD"
    
    print(f"Multithreaded Average Time:  {multi_avg:>15,.2f} ns")
    print(f"Single-threaded Average Time: {single_avg:>15,.2f} ns")
    print(f"Performance Difference:      {abs(improvement):>15.2f}% {status}")
    print()
    
    print("DETAILED ROUND COMPARISON:")
    print(f"{'Round':<6} {'Multithreaded (ns)':<20} {'Single-threaded (ns)':<20} {'Difference (ns)':<15}")
    print("-" * 65)
    for i in range(10):
        multi_time = multi_times[i]
        single_time = single_times[i]
        diff = single_time - multi_time
        print(f"{i+1:<6} {multi_time:<20,} {single_time:<20,} {diff:>15,}")


if __name__ == "__main__":
    main()