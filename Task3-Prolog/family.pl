/* ================================================
   CCS 2226 - Foundations of Artificial Intelligence
   Task Three - Prolog Family Tree
   Name: David Osoro Solomon
   Reg No: CIT-223-089/2023
   ================================================

   FAMILY STRUCTURE:

   Generation 1 (Grandparents of peter and david):
     george + mary  (henry and kate's parents)
     john   + rose  (ann's parents)

   Generation 2 (Parents):
     henry + susan  (children of george and mary)
     kate  + brian  (children of george and mary)
     ann           (child of john and rose)
     grace + james

   Generation 3 (Children):
     tom   + ann    (children of henry and susan)
     grace          (child of henry and susan)
     helen          (child of kate and brian)

   Generation 4 (Grandchildren):
     peter          (child of tom and ann)
     david          (child of tom and ann)
     kevin          (child of grace and james)

   ================================================ */


/* ─────────────────────────────────────────────
   FACTS - GENDER
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
   FACTS - PARENT RELATIONSHIPS
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


/* ─────────────────────────────────────────────
   RULES
   ───────────────────────────────────────────── */

/* Father: parent who is male */
father(X, Y) :- parent(X, Y), male(X).

/* Mother: parent who is female */
mother(X, Y) :- parent(X, Y), female(X).

/* Grandparent: parent of a parent */
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

/* Grandfather: grandparent who is male */
grandfather(X, Z) :- grandparent(X, Z), male(X).

/* Grandmother: grandparent who is female */
grandmother(X, Z) :- grandparent(X, Z), female(X).

/* Child: Y is child of X */
child(Y, X) :- parent(X, Y).

/* Grandchild: Z is grandchild of X */
grandchild(Z, X) :- grandparent(X, Z).

/* Sibling: share at least one parent */
sibling(X, Y) :- parent(P, X), parent(P, Y), X \== Y.

/* Brother: sibling who is male */
brother(X, Y) :- sibling(X, Y), male(X).

/* Sister: sibling who is female */
sister(X, Y) :- sibling(X, Y), female(X).

/* Uncle: brother of a parent */
uncle(X, Y) :- parent(P, Y), brother(X, P), X \== Y.

/* Aunt: sister of a parent */
aunt(X, Y) :- parent(P, Y), sister(X, P), X \== Y.

/* Cousin: parents are siblings - use setof to remove duplicates */
cousins_of(X, Cousins) :-
    setof(C, P1^P2^(parent(P1,X), parent(P2,C), sibling(P1,P2), C \== X), Cousins).

/* Ancestor */
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

/* Descendant */
descendant(X, Y) :- ancestor(Y, X).


