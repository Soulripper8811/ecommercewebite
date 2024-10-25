def toh(n,soruce,destination,extra):
    if n==1:
        print(f"move 1 disk form {soruce} to {destination}")
        return
    toh(n-1,soruce,extra,destination)
    print(f"move  {n} disk from {soruce} to {destination}")
    toh(n-1,extra,destination,soruce)

toh(3,'A','B','C')