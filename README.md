# course-catalog-parser
Used ANTLR &amp; Python to parse a ‘Course Catalog’ text file and store the parsed information in a SQLite database. Created a command line tool that displays course information based on user input.

Catalog.g4: ANTLR grammar that defines a ‘Course Catalog’.

DBListener.py: Extends the ANTLR-generated CatalogListener, deletes any pre-existing data in the database on ‘enterCatalog’, and inserts data into the course and prereq tables on ‘enterCourse’. 

catalog.db: The SQLite database created after reading catalog.sql.

catalog.sql: Defines a ‘course’ table and ‘prereq’ table.

catalog.txt: The input catalog text file.

cb.py: A command line tool that defines subcommands, uses argparse to parse & utilize user input, and queries database & prints results.

main.py: Specifies the database that is connected to, reads & parses the input catalog text file, and loads parsed info into the database as it invokes methods from DBListener.

New line of content.
