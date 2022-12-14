def main():
    for _ in range(int(input())):
        n = int(input())
        candies = sorted(map(int,input().split()),reverse=True)
        alice, bob = 0, 0
        for c in candies:
            if alice < bob:
                alice += c
            else:
                bob += c
        print('YES' if alice == bob else 'NO')

main() 
