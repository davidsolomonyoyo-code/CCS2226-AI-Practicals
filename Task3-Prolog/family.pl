/* ================================================
   MA410 Prolog Practical 2 & CCS 2226 Task 3
   family.pl - Family Tree Facts
   Name: David Osoro Solomon
   Reg No: CIT-223-089/2023

   FAMILY STRUCTURE:
   Generation 1: george + mary
   Generation 2: henry + susan, kate + brian, ann (john + rose)
   Generation 3: tom + ann, grace + james, helen
   Generation 4: peter, david, kevin
   ================================================ */


/* ─────────────────────────────────────────────
   GENDER FACTS
   ───────────────────────────────────────────── */

male(george).
male(henry).
male(brian).
male(tom).
male(james).
male(peter).
male(david).
male(kevin).
male(john).

female(mary).
female(susan).
female(kate).
female(grace).
female(ann).
female(helen).
female(rose).


/* ─────────────────────────────────────────────
   PARENT FACTS
   ───────────────────────────────────────────── */

/* Generation 1 to 2 */
parent(george, henry).
parent(george, kate).
parent(mary, henry).
parent(mary, kate).

/* Ann's parents */
parent(john, ann).
parent(rose, ann).

/* Generation 2 to 3 */
parent(henry, tom).
parent(henry, grace).
parent(susan, tom).
parent(susan, grace).
parent(kate, helen).
parent(brian, helen).

/* Generation 3 to 4 */
parent(tom, peter).
parent(tom, david).
parent(ann, peter).
parent(ann, david).
parent(grace, kevin).
parent(james, kevin).
