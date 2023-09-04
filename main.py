import sys
from antlr4 import *
import sqlite3
from CatalogLexer import CatalogLexer
from CatalogParser import CatalogParser
from CatalogVisitor import CatalogVisitor
from DBListener import DBListener
 
 
def main(argv):

    # Connect to DB
    conn = sqlite3.connect("catalog.db")

    # Read input file
    with open(sys.argv[1]) as f:
      lines = f.readlines()
    
    print("Loading file ", sys.argv[1], "into database catalog.db")
 
    input = InputStream("".join(lines))
 
    lexer = CatalogLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CatalogParser(stream)
    tree = parser.catalog()

    dbListener = DBListener(conn)
    walker = ParseTreeWalker()
    walker.walk(dbListener, tree)

    conn.close()

 
if __name__ == '__main__':
    main(sys.argv)
