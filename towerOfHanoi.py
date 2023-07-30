def ToH(disk, src, mid, dest):
    if (not disk):
        return

    ToH(disk-1, src, dest, mid)
    print(f'Move disk from {src} to {dest}')
    ToH(disk-1, mid, src, dest)


ToH(3, 'A', 'B', 'C')