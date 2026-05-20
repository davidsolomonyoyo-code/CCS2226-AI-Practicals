/* ================================================
   MA410 Prolog Practical 2
   lab2rels.pl - Relationship Definitions
   Name: David Osoro Solomon
   Reg No: CIT-223-089/2023
   ================================================ */


/* ─────────────────────────────────────────────
   SECTION 1c - MOTHER AND FATHER DEFINITIONS
   ───────────────────────────────────────────── */

mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).


/* ─────────────────────────────────────────────
   SECTION 1d - EXPERIMENTING WITH OPERATORS
   = means unification (can they be made equal)
   == means strict equality (already equal)
   \== means not equal
   \= means cannot be unified
   ───────────────────────────────────────────── */

/* Examples:
   ?- a = a.        true  (same atom)
   ?- X = a.        true  (X unifies with a)
   ?- a == a.       true  (strictly equal)
   ?- X == a.       false (X not yet bound)
   ?- a \== b.      true  (a and b are different)
   ?- X \= a.       false (X can unify with a)
*/

diff(X, Y) :- X \== Y.


/* ─────────────────────────────────────────────
   SECTION 1f - DEFINING ALL PREDICATES
   ───────────────────────────────────────────── */

/* Sibling: share at least one parent */
sibling(X, Y) :- parent(P, X), parent(P, Y), X \== Y.

/* Brother: sibling who is male */
brother(X, Y) :- sibling(X, Y), male(X).

/* Sister: sibling who is female */
sister(X, Y) :- sibling(X, Y), female(X).

/* Grandparent: parent of a parent */
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

/* Grandmother: grandparent who is female */
grandmother(X, Z) :- grandparent(X, Z), female(X).

/* Grandfather: grandparent who is male */
grandfather(X, Z) :- grandparent(X, Z), male(X).

/* Blood uncle: brother of a parent */
bl_uncle(X, Y) :- parent(P, Y), brother(X, P).

/* Uncle in law: married to an aunt */
uncle_in_law(X, Y) :- parent(P, Y), sister(S, P), married(X, S).

/* Uncle: any type of uncle */
uncle(X, Y) :- bl_uncle(X, Y).
uncle(X, Y) :- uncle_in_law(X, Y).

/* Aunt: sister of a parent */
aunt(X, Y) :- parent(P, Y), sister(X, P).

/* Ancestor */
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

/* Descendant */
descendant(X, Y) :- ancestor(Y, X).

/* First cousin: parents are siblings */
firstcousin(X, Y) :-
    parent(PX, X),
    parent(PY, Y),
    sibling(PX, PY),
    X \== Y.

/* Aunt and uncle (any type) */
aunt_uncle(X, Y) :- aunt(X, Y).
aunt_uncle(X, Y) :- uncle(X, Y).


/* ─────────────────────────────────────────────
   SECTION 3 - AI BASED QUESTIONS
   Using setof to organise sets
   ───────────────────────────────────────────── */

/* Get all sisters of X as a list */
sister_list(X, L) :- setof(Y, sister(Y, X), L).

/* Get all brothers of X as a list */
brother_list(X, L) :- setof(Y, brother(Y, X), L).

/* Get all siblings of X as a list */
sibling_list(X, L) :- setof(Y, sibling(Y, X), L).

/* Get all grandparents of X as a list */
grandparent_list(X, L) :- setof(Y, grandparent(Y, X), L).

/* Get cousins of X as a list */
cousin_list(X, L) :- setof(Y, firstcousin(Y, X), L).


