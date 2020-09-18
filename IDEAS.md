* use `functools.cmp_to_key` and switch to Python 3
* save/resume state (would allow 'undo')
* allow items to compare as equal priority
* top-N sorting, to avoid comparing items low down on the priority list
* multiple dimensions for comparison:
  - first sort by one dimension (e.g. urgency) into buckets (e.g. now,
    tomorrow, next week, next month, next year)
  - then sort top buckets by another dimension (e.g. customer impact)
  - finally break ties by another (e.g. size estimation)
* top-N sorting, with multiple dimensions:
  - choose a low M > N, e.g. for M=15 (for N=10)
  - first assign items by one dimension (e.g. urgency) into buckets
    (e.g. now, tomorrow, next week, next month, next year), until top buckets
    (e.g. now, tomorrow, next week) have M items in total
  - continue applying key function, but now the questions become simpler
    e.g. now, tomorrow, next week, later
  - continue simplifying the questions based on how many of the top buckets are
    needed before we have M items
  - after key function is applied for that dimension, repeat with another
    dimension (e.g. customer impact, and high, medium, low)
  - finally, top 15 can be sorted using comparison function with prompt
- Interesting ideas here:
  https://stackoverflow.com/questions/867224/looking-for-a-sort-algorithm-with-as-few-as-possible-compare-operations
