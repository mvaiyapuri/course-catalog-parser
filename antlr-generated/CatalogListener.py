# Generated from Catalog.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CatalogParser import CatalogParser
else:
    from CatalogParser import CatalogParser

# This class defines a complete listener for a parse tree produced by CatalogParser.
class CatalogListener(ParseTreeListener):

    # Enter a parse tree produced by CatalogParser#catalog.
    def enterCatalog(self, ctx:CatalogParser.CatalogContext):
        pass

    # Exit a parse tree produced by CatalogParser#catalog.
    def exitCatalog(self, ctx:CatalogParser.CatalogContext):
        pass


    # Enter a parse tree produced by CatalogParser#course.
    def enterCourse(self, ctx:CatalogParser.CourseContext):
        pass

    # Exit a parse tree produced by CatalogParser#course.
    def exitCourse(self, ctx:CatalogParser.CourseContext):
        pass



del CatalogParser