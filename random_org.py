from requests import get

def randint(min, max):
    a = get(f"https://www.random.org/integers/?num=1&min={min}&max={max}&col=1&base=10&format=plain&rnd=new")
    if a:
        return int(a.text)
    else:
        raise ValueError(a.text[7:])

def randSequence(min, max):
    a = get(f"https://www.random.org/sequences/?min={min}&max={max}&format=plain&rnd=new&col=1")
    if a:
        text = a.text
        lst = text.split()
        ans = []
        for num in lst:
            ans.append(int(num))
        return ans
    else:
        raise ValueError(a.text[7:])

def choice(sequence):
    num = randint(0, len(sequence)-1)
    return sequence[num]

def random():
    num = randint(0, m := 1_000_000_000)
    return num / m
