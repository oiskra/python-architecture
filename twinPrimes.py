import multiprocessing

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def find_twin_in_primes(start, end): 
    twins = []
    prev_prime = None
    
    for num in range(start, end):
        if is_prime(num):
            if prev_prime is not None and num - prev_prime == 2:
                twins.append((prev_prime, num))
            prev_prime = num
    
    return twins
               

if __name__ == "__main__":
    start_range = 1
    end_range = 1000000
    num_processes = 4
    
    with multiprocessing.Pool(num_processes) as p:
        chunk_size = (end_range - start_range) // num_processes
        ranges = [(i, min(i + chunk_size, end_range)) for i in range(start_range, end_range, chunk_size)]
        
        results = p.starmap(find_twin_in_primes, ranges)
        p.close()
        p.join()
    
    prime_numbers = []
    for result in results:
        prime_numbers.extend(result)
        
    print(prime_numbers)
    