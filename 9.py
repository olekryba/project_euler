# Function to find the Pythagorean triplet
def find_pythagorean_triplet(sum_total):
    for a in range(1, sum_total // 3):
        for b in range(a + 1, sum_total // 2):
            c = sum_total - a - b
            if a**2 + b**2 == c**2:
                return a, b, c
    return None

# Find the triplet where a + b + c = 1000
triplet = find_pythagorean_triplet(1000)

if triplet:
    a, b, c = triplet
    print(f"The Pythagorean triplet is: a={a}, b={b}, c={c}")
    print(f"The product abc is: {a * b * c}")
else:
    print("No Pythagorean triplet found.")