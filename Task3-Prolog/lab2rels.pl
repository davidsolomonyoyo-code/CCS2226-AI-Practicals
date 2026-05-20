/* ================================================
   MA410 Prolog Practical 2 & CCS 2226 Task 3
   lab2rels.pl - All Relationship Rules
   Name: David Osoro Solomon
   Reg No: CIT-223-089/2023


/* ─────────────────────────────────────────────
   MARRIAGE FACTS
   ───────────────────────────────────────────── */

married(george, mary).
married(mary, george).
married(henry, susan).
married(susan, henry).
married(kate, brian).
married(brian, kate).
married(tom, ann).
married(ann, tom).
married(grace, james).
married(james, grace).
married(john, rose).
married(rose, john).


/* ─────────────────────────────────────────────
   SECTION 1c - MOTHER AND FATHER
   ───────────────────────────────────────────── */

mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).


/* ─────────────────────────────────────────────
   SECTION 1d - DIFF OPERATOR
   ───────────────────────────────────────────── */

diff(X, Y) :- X \== Y.


/* ─────────────────────────────────────────────
   SECTION 1f - ALL RELATIONSHIP RULES
   ───────────────────────────────────────────── */

/* Sibling: share at least one parent */
sibling(X, Y) :- parent(P, X), parent(P, Y), X \== Y.

/* Brother and Sister */
brother(X, Y) :- sibling(X, Y), male(X).
sister(X, Y)  :- sibling(X, Y), female(X).

/* Grandparent, Grandfather, Grandmother */
grandparent(X, Z)  :- parent(X, Y), parent(Y, Z).
grandfather(X, Z)  :- grandparent(X, Z), male(X).
grandmother(X, Z)  :- grandparent(X, Z), female(X).

/* Child and Grandchild */
child(Y, X)      :- parent(X, Y).
grandchild(Z, X) :- grandparent(X, Z).

/* Blood uncle: brother of a parent */
bl_uncle(X, Y) :-
    parent(P, Y),
    brother(X, P),
    X \== Y.

/* Uncle in law: married to a sister of a parent */
uncle_in_law(X, Y) :-
    parent(P, Y),
    sister(S, P),
    married(X, S),
    male(X),
    X \== Y.

/* Uncle: either blood uncle or uncle in law */
uncle(X, Y) :- bl_uncle(X, Y).
uncle(X, Y) :- uncle_in_law(X, Y).

/* Aunt: sister of a parent */
aunt(X, Y) :-
    parent(P, Y),
    sister(X, P),
    X \== Y.

/* Ancestor and Descendant */
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
descendant(X, Y) :- ancestor(Y, X).

/* First cousin: parents are siblings */
firstcousin(X, Y) :-
    parent(PX, X),
    parent(PY, Y),
    sibling(PX, PY),
    X \== Y.


/* ─────────────────────────────────────────────
   SECTION 3 - SETOF LIST QUERIES
   These return results as a clean list
   ───────────────────────────────────────────── */

sister_list(X, L)      :- setof(Y, sister(Y, X), L).
brother_list(X, L)     :- setof(Y, brother(Y, X), L).
sibling_list(X, L)     :- setof(Y, sibling(Y, X), L).
grandparent_list(X, L) :- setof(Y, grandparent(Y, X), L).
cousin_list(X, L)      :- setof(Y, firstcousin(Y, X), L).


