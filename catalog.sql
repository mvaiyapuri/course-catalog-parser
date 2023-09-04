-- drop tables first
DROP TABLE prereq;
DROP TABLE course;

-- creating class table
CREATE TABLE course (
    coursename TEXT PRIMARY KEY,
    title      TEXT,
    units      INTEGER,
    descr      TEXT
);

-- creating pre-req table
CREATE TABLE prereq (
    coursename TEXT,
    prereq     TEXT,
    FOREIGN KEY(coursename) REFERENCES course(coursename) ON DELETE CASCADE,
    FOREIGN KEY(prereq)     REFERENCES course(coursename) ON DELETE CASCADE
);