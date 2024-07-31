kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

def main():
    for keys, values in kata.items():
        print(f"{keys} was created by {values}")

main()