import argparse
import sqlite3
from tabulate import tabulate


def list_course(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT coursename, title from course WHERE coursename LIKE ?", ('%'+name.upper()+'%',))
    rows = cur.fetchall()
    if len(rows) == 0:
        print("no courses matched name: ", name)
        return
    print(tabulate(rows, headers=['Course name', 'Title']))

def show_course(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT coursename, title, units, descr from course WHERE coursename = ?", (name.upper(), ))
    row = cur.fetchone()
    if row == None:
        print("error: course ", name, "not found.")
        return
    print("Coursename:   ", row[0])
    print("Title:        ", row[1])
    print("Units:        ", row[2])
    print("Desc:         ", row[3])

    cur.execute("SELECT prereq from prereq WHERE coursename = ?", (name.upper(), ))
    rows = cur.fetchall()
    prereqs = ""
    if len(rows) == 0:
        prereqs = 'None'
    for r in rows:
        prereqs += " " + r[0]
    print("Prerequisites:", prereqs)

def list_prereq(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT coursename, title from course WHERE coursename IN (SELECT coursename FROM prereq WHERE prereq = ?)", (name.upper(),))
    rows = cur.fetchall()
    if len(rows) == 0:
        print("no prereqs matched name: ", name)
        return
    print("List of courses which have ", name.upper(), "as a prerequisite:")
    print(tabulate(rows, headers=['Course name', 'Title']))

def print_output(args, conn):
    if args.objecttype == 'course':
        if args.commandtype == 'list':
            list_course(conn, args.name)
        else:
            show_course(conn, args.name)
    else:
        list_prereq(conn, args.name)


if __name__ == '__main__':
    # Set up the argument parser with subcommands and options
    parser = argparse.ArgumentParser(description='Catalog command-line tool.')
    subparsers = parser.add_subparsers(dest='objecttype', help='Specify one of "course" or "prereq"')
    parser_course = subparsers.add_parser('course')
    parser_course_subparsers = parser_course.add_subparsers(dest='commandtype', help='Specify one of "list" or "show"' )
    parser_course_list = parser_course_subparsers.add_parser('list')
    parser_course_list.add_argument('name', help='Name of the course.')
    parser_course_show = parser_course_subparsers.add_parser('show')
    parser_course_show.add_argument('name', help='Name of the course.')

    parser_prereq = subparsers.add_parser('prereq')
    parser_prereq_subparsers = parser_prereq.add_subparsers(dest='commandtype', help='Specify "list"')
    parser_prereq_list = parser_prereq_subparsers.add_parser('list')
    parser_prereq_list.add_argument('name', help='Prereq name (should match exactly).')
    args = parser.parse_args()

    # Connect to DB
    conn = sqlite3.connect("catalog.db")

    # Process and print output
    print_output(args, conn)

    conn.close()
