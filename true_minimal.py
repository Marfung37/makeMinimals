import re
from py_fumen_py import decode, encode, Page

def makefumen(fumens, percents):
    out = []
    for fumen, percent in zip(fumens, percents):
        out.append(Page(field=decode(fumen)[0].field, comment = percent))
    return f"https://fumen.zui.jp/?{encode(out)}"

def make_tiny(url):
    import contextlib

    try:
        from urllib.parse import urlencode

    except ImportError:
        from urllib import urlencode
    from urllib.request import urlopen

    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8 ')

with open("path_minimal_strict.md", "r") as trueMinFile:
    trueMinLines = trueMinFile.readlines()

totalCases = int(re.search(r"/ (\d+)\)", trueMinLines[2]).group(1))
percents = []
for line in trueMinLines[13::9]:
    numCoverCases = int(re.match(r"(\d+)", line).group(1))
    percent = numCoverCases / totalCases * 100
    percent = f'{percent:.2f}% ({numCoverCases}/{totalCases})'
    percents.append(percent)


fumenLst = re.findall("(v115@[a-zA-Z0-9?/+]*)", trueMinLines[6])
line = makefumen(fumenLst, percents)

try:
    line = make_tiny(line)
except:
    pass

print("True minimal:")
print(line)
