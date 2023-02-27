import py_peglib

parser = py_peglib.Parser("""
    DUMB_CALC   <- NUMBER (OPERATOR NUMBER)*
    NUMBER      <- < [0-9]+ >
    OPERATOR    <- '+' / '-'
    %whitespace <- [ \n]*
""")

def lambdaOp(sv):
    print(sv.toString())

parser.on("OPERATOR", lambdaOp)
parser.parse("0 + 1 + 2 - 3")