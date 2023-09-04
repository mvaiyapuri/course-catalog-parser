grammar Catalog;

// Parser Rules
catalog: (course)+ EOF;

course: COURSELITERAL ': ' WORD WS TITLELITERAL ': '  TITLEDESC WS UNITSLITERAL ': ' NUMBER WS DESCLITERAL ': ' TITLEDESC WS PREREQLITERAL ': ' PREREQ WSPLUS ;

// Lexer Rules
COURSELITERAL: 'Course' ;
TITLELITERAL: 'Title' ;
UNITSLITERAL: 'Units' ;
DESCLITERAL: 'Desc' ;
PREREQLITERAL: 'Prereq' ;

NUMBER: [0-9]+ ;
WORD: [0-9a-zA-Z]+ ;
WS: [ \n\t\r] ;
WSPLUS: WS+ ;
PUNC: (',' | '.' | '?' | '!' | '-') ;

UNITS: (NUMBER) ;
COURSENAME: (WORD) ;
TITLEDESC: '"' (WORD | WS | PUNC)+ '"';
PREREQ: '\'' (WORD | WS)* '\'' ;