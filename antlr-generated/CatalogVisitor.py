# Generated from Catalog.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CatalogParser import CatalogParser
else:
    from CatalogParser import CatalogParser

# This class defines a complete generic visitor for a parse tree produced by CatalogParser.

class CatalogVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CatalogParser#catalog.
    def visitCatalog(self, ctx:CatalogParser.CatalogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CatalogParser#course.
    def visitCourse(self, ctx:CatalogParser.CourseContext):
        return self.visitChildren(ctx)



del CatalogParser