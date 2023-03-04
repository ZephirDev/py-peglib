import py_peglib

parser = py_peglib.Parser("""
    DUMB_CALC   <- NUMBER (OPERATOR NUMBER)*
    NUMBER      <- < [0-9]+ >
    OPERATOR    <- '+' / '-'
    %whitespace <- [ \n]*
""")

def number(sv):
    return int(sv.toString())

def lambdaOp(sv):
    return sv.toString()

def dumbCalc(sv):
    r = sv.at(0)
    for i in range(1, sv.size(), 2):
        op = sv.at(i)
        if op == "+":
            r += sv.at(i+1)
        else:
            r -= sv.at(i+1)
    return r

parser.on("NUMBER", number)
parser.on("OPERATOR", lambdaOp)
parser.on("DUMB_CALC", dumbCalc)

print(parser.isValid())
print(parser.parse("0 + 1 + 2 - 4"))
