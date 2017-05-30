"""
FCA - Python libraries to support FCA tasks
Copyright (C) 2017  Victor Codocedo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
# Kyori code.
import sys
from fca.algorithms.addIntent import add_intent
from fca.defs import ConceptLattice
from fca.defs.patterns import IcebergSetPattern
from fca.reader import read_representations


"""
In this example we mine frequent formal concepts
Frequent Formal Concepts cannot be directly mined with addIntent
which is a bottom up concept builder

Luckily, we can just invert the notions of extents and intents
and go on exactly as with a normal setting
"""
if __name__ == "__main__":
    # Notice that we have imported a different kind of pattern
    # IcebergSetPattern allows setting a min sup value
    IcebergSetPattern.MIN_SUP = 5


    '''
    # This is a hack
    # We are going to invert the tags for Intents and Extents
    ConceptLattice.EXTENT_MARK = 'in'
    ConceptLattice.INTENT_MARK = 'ex'
    '''

    __lattice__ = add_intent(read_representations(sys.argv[1]), pattern=IcebergSetPattern)

    for concept_id, concept in __lattice__.as_dict().items():
        # Another option is to invert intent and extents when getting the lattice
        print ('{} - ({}, {})'.format(
            concept_id,
            concept[ConceptLattice.INTENT_MARK],
            concept[ConceptLattice.EXTENT_MARK])
              )