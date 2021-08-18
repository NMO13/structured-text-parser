from src.parser import parser
text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR
END_PROGRAM"""

parser.parseString(text)
################

text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR
END_PROGRAM"""

parser.parseString(text)

###############


text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR
i := 0;
j := 3;
END_PROGRAM"""

parser.parseString(text)

##############

text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR
x.y := 0;
u.v := 3;
END_PROGRAM"""

parser.parseString(text)

##############

text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR
i := 4;
REPEAT
i := i + 1;
UNTIL i < j+4;
END_REPEAT;
END_PROGRAM"""

parser.parseString(text)

##############

text = """
PROGRAM main
FOR(i := 0 TO 10) DO
avg := avg + 4;
END_FOR;
END_PROGRAM
"""
parser.parseString(text)

##############

text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR
avg := 0;
i := 0;
WHILE (i < 5) DO
avg := avg + f[i];
i := i + 1;
END_WHILE;
avg := avg / 5;
END_PROGRAM"""

parser.parseString(text)

##############

text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR
i := 3 + f[5];
END_PROGRAM"""

parser.parseString(text)

##############

text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR
IF (a = 1) THEN
i := 3;
END_IF;
END_PROGRAM"""

parser.parseString(text)

##############

text = """
PROGRAM main
VAR_INPUT
i : INT;
a : INT;
b : BOOL;
END_VAR
IF (a) THEN
i := 3;
END_IF;
END_PROGRAM"""

parser.parseString(text)

##############

text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR
IF (a = 1 AND b = 3 OR c = 5) THEN
i := 3;
END_IF;
END_PROGRAM"""

parser.parseString(text)

##############

text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR
IF (a = 1) THEN
   i := 3;
ELSE
   x := 0;
END_IF;
END_PROGRAM"""

parser.parseString(text)

##############

text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR
IF (a = 1) THEN
    x := 1;
ELSIF (b = 1) THEN
    y := 1;
ELSE
    x := 0;
    y := 0;
    z := 0;
END_IF;
END_PROGRAM"""

parser.parseString(text)

##############

text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR
IF (a = 1) THEN
    x := 1;
ELSIF (b = 1 AND t = 1) THEN
    y := 1;
    IF (000/02 = 0) THEN
        z := 1;
    END_IF;
ELSE
    x := 0;
    y := 0;
    z := 0;
END_IF;
END_PROGRAM"""

##############
text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR

CASE state OF
0: IF (green_EW)THEN
     state :=1;
   END_IF;
1: IF (yellow_EW) THEN
     state :=2;
   END_IF;
2: IF (green_NS) THEN
     state :=3;
   END_IF;
END_CASE;
END_PROGRAM"""

parser.parseString(text)

##############
text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR

CASE state OF
0: IF (green_EW)THEN
     state :=1;
   END_IF;
1: IF (yellow_EW) THEN
     state :=2;
   END_IF;
2: IF (green_NS) THEN
     state :=3;
   END_IF;
END_CASE;
END_PROGRAM"""

parser.parseString(text)

##############

text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR
x := foo();
END_PROGRAM"""

parser.parseString(text)

##############

text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR
x := foo(3);
x := foo(3, i);
END_PROGRAM"""

parser.parseString(text)

##############

text = """
PROGRAM main
VAR_INPUT
i : INT;
END_VAR
ramp(OUT :=);
END_PROGRAM"""

parser.parseString(text)