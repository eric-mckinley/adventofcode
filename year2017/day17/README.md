### Part 1 vs 2
Part1 uses expanding list up to 2017 elements, no way that would work for 50,000,000 list size. 

Had to spend time looking at how the sequence grows, once realised that 0 never seems to rotates and always at pos [0].

Then looked at how oftens sequence[1] changes and noticed its value matches the rotation count between changes. 

Not sure how this works, but then part2 just becomes simulating the roation and counting the rotations between sequnce[1] changing.
