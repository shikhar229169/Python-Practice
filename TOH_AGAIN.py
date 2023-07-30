def towerOfHanoi(n, src, mid, dest):
    if (n == 0):
        return
    
    towerOfHanoi(n - 1, src, dest, mid)
    print(f'Move {src} to {dest}')
    towerOfHanoi(n-1, mid, src, dest)

towerOfHanoi(3, 'A', 'B', 'C')