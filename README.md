# In-Memory Database Assignment

My implementation of an in-memory database with transaction support.

## Files

* `inmemory_db.py` - main database implementation
* `test_inmemory_db.py` - test cases from assignment

## How to Run

Important: Requires current Python version

1. Download both files (inmemory_db.py & test_inmemory_db.py) to the same folder
2. Run: `python test_inmemory_db.py`

## Operations

* `get(key)` - returns value or None
* `put(key, val)` - sets value (requires active transaction)
* `begin_transaction()` - starts transaction
* `commit()` - saves changes
* `rollback()` - discards changes

## Implementation

Uses two dictionaries: one for committed data and one for transaction data. When a transaction starts, it copies the main data. Changes go to the temp storage. Commit applies changes, rollback discards them. The key challenge was ensuring `get()` only returns committed data.

## Assignment Improvements

1. **Clarify nested transactions** - Explicitly state what happens if `begin_transaction()` is called twice. Should it error or support nesting?

2. **Add delete method** - Include `delete(key)` to make it more realistic and complete.

3. **Provide test file** - Give students a test suite upfront so they can verify their code before submission.

4. **More edge cases** - Specify behavior for duplicate puts in one transaction, empty keys, or invalid inputs.

5. **Performance requirements** - Add bonus points for optimizations or require discussing time/space complexity tradeoffs.
