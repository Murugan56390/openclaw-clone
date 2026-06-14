#!/usr/bin/env python3
"""
Prime Number Builder - generates and caches prime numbers.
"""

import sys
import math
import json
import os

CACHE_FILE = os.path.join(os.path.dirname(__file__), ".prime_cache.json")


def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE) as f:
            return json.load(f)
    return []


def save_cache(primes):
    with open(CACHE_FILE, "w") as f:
        json.dump(primes, f)


def sieve_of_eratosthenes(limit):
    """Return list of all primes up to limit using Sieve of Eratosthenes."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [n for n, is_prime in enumerate(sieve) if is_prime]


def is_prime(n):
    """Check if a single number is prime."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def build_prines(limit):
    """Build and cache prime numbers up to the given limit."""
    cached = load_cache()
    if cached and max(cached) >= limit:
        return [p for p in cached if p <= limit]

    primes = sieve_of_eratosthenes(limit)
    save_cache(primes)
    return primes


def main():
    if len(sys.argv) != 2:
        print("Usage: prime_builder.py <limit>")
        sys.exit(1)

    try:
        limit = int(sys.argv[1])
    except ValueError:
        print("Error: limit must be an integer")
        sys.exit(1)

    if limit < 2:
        print("No primes found (limit < 2)")
        sys.exit(0)

    primes = build_prines(limit)
    print(f"Found {len(primes)} prime numbers up to {limit}:")
    print(primes)


if __name__ == "__main__":
    main()
