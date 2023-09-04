from antlr4 import *
from CatalogListener import CatalogListener
from CatalogParser import CatalogParser

# This class defines a complete listener for a parse tree produced by CatalogParser.
class DBListener(CatalogListener):

    # Initializes the connection, number of courses, and number of prerequisites.
    def __init__(self, conn):
        self.conn = conn
        self.numCourses = 0
        self.numPrereqs = 0

    # Enter a parse tree produced by CatalogParser#catalog.
    def enterCatalog(self, ctx:CatalogParser.CatalogContext):
        # Delete all rows from Course and Prereq tables.
        print ("Clearing Catalog DB")
        cur = self.conn.cursor()
        cur.execute("DELETE FROM course")
        cur.execute("DELETE FROM prereq")
        self.conn.commit()
        

    # Enter a parse tree produced by CatalogParser#course.
    def enterCourse(self, ctx:CatalogParser.CourseContext):
        # Insert into Course and Prereq tables.
        print("Inserting Course and Prerequisites for course: ", ctx.WORD())
        # Getting course name
        name = str(ctx.WORD())
        # Removing double quotes around title and getting title
        title = str(ctx.TITLEDESC()[0]).replace('"', '')
        # Removing double quotes around description and getting description
        desc = str(ctx.TITLEDESC()[1]).replace('"', '')
        # Getting number of units
        units = int(str(ctx.NUMBER()))
        # Getting prereq(s) as a list of strings
        prereq = str(ctx.PREREQ()).split(" ")

        # Inserting course data into course table
        cur = self.conn.cursor()
        cur.execute('''INSERT INTO course (coursename, title, units, descr)
                    VALUES (?, ?, ?, ?)
                    ''', (name, title, units, desc))
        
        # Inserting prereq data into prereq table and removing single quotes around prereq
        for p in prereq:
            if p == "'NONE'":
                continue
            cur.execute('''INSERT INTO prereq (coursename, prereq)
                        VALUES (?, ?)
                        ''', (name, p.replace("'","")))
            # Increment numPrereqs after inserting a prereq
            self.numPrereqs += 1
        self.conn.commit()
        # Increment numCourses after inserting a course
        self.numCourses += 1

    # Enter a parse tree produced by CatalogParser#catalog.
    def exitCatalog(self, ctx:CatalogParser.CatalogContext):
        # Print number of courses and number of prereqs
        print("Parsed and inserted ", self.numCourses, "courses.")
        print("Parsed and inserted ", self.numPrereqs, "prerequisites.")
    