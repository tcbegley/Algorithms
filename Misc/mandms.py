"""
This code is a solution of the following problem:

You have a cake which has been decorated with a ring of M&Ms around the edge.
What's the largest number of (equal) pieces the cake can be cut into, such that
each piece of cake has the same sequence of M&Ms on it.

Stated another (equivalent) way, given a string, determine the largest number
of equal substrings that the starting string can be split into.

Concrete examples: 'abab' -> 2 * 'ab', 'abc' -> 1 * 'abc', 'aaa' -> 3 * 'a' etc

The solution here is based on the observation that the length of the solution
substring must be a factor of the length of the original string s. Hence we
find a prime factor p of len(s), split s into p equal pieces, check if they are
all the same, and if so, recursively apply the search to one of the pieces.

This approach has the advantage that string comparisons rapidly become less
expensive, because the length of the chunks decreases very rapidly.
"""


def smallest_prime_factor(n):
    """Return smallest prime factor of a natural number. Returns 1 if n = 1"""
    if n % 2 == 0:
        return 2
    i = 3
    while i * i < n:
        if n % i == 0:
            return i
        i += 2
    return n


def chunk(s, p):
    """
    Split s into pieces of length p. Note, it doesn't actually check whether
    p divides len(s)
    """
    return [s[(i - p):i] for i in range(p, len(s) + 1, p)]


def period(s):
    """Find shortest substring t for which s is period with period t"""
    len_s = len(s)
    if len(set(s)) == 1:
        return len_s, s[0]
    n = len_s
    while n > 1:
        p = smallest_prime_factor(n)
        if len(set(chunk(s, len_s // p))) == 1:
            res = period(s[: len_s // p])
            return res[0] * p, res[1]
        n //= p
    return 1, s
