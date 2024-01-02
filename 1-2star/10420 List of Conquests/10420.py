n = int(input())  # Read the number of lines
country_counts = {}  # Dictionary to store country counts

for _ in range(n):
    line = input().split()  # Split the input line into words
    country = line[0]  # The first word is the country name
    country_counts[country] = country_counts.get(country, 0) + 1

for country in sorted(country_counts):
    print(country, country_counts[country])
