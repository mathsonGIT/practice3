import sys
def decrypt(s: str) ->str:
    results = []

    for ch in s:
        results.append(ch)
        if len(results)>2 and (results[-1], results[-2]) == ('.', '.'):
            results.pop()
            results.pop()
            if results:
                results.pop()
    return ''.join(ch for ch in results if ch !='.')


if(__name__) == '__main__':
    text = sys.stdin.read()
    print(decrypt(text))