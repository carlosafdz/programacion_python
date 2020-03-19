

def main():
    print(s.union(t))
    
    print(s.intersection(t))

    print(s.difference(t))
    print(t.difference(s))

    print(1 in s)
    print(4 in s)
    print(5 not in t)

    print(3 in t.intersection(s))

    s.add(7)
    s.update([9,8]) #se agregan todos los elementos de la lista
    s.remove(1)
    print(s)

if __name__ == "__main__":
    s = set([1,2,3])
    t = set([3,4,5])
    main()