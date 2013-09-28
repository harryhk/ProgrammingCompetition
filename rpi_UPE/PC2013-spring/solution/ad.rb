def solve stdin
  problems = stdin.readline.to_i

  problems.times do
    # Read in the numbers for this problem
    n = stdin.readline.to_i
    nums = n.times.map { stdin.readline.to_i }

    # max is our current best
    max = 0
    # total_size is the sum of the whole set, which is the largest size bucket
    # we can create
    total_size = nums.reduce(:+)

    # Start at 1 and work our way up
    (1..total_size).each do |target|
      # We're trying to make chunks of size target; we can do a shortcut
      # optimization here and say that if we can't theoretically divide the
      # entire bucket in more ways than our current max, there's no point in
      # continuing.
      break if total_size / target < max

      # Start with an empty set and a counter of 0 sets found
      current = []
      chunks = 0

      # Add each number to the current set, one by one
      nums.each do |i|
        current << i

        # If we filled the set more than our target, remove elements from the
        # front (old ones) until we are in good shape. This creates a sliding
        # window of size < target.
        while current.reduce(0, :+) > target
          current.shift
        end

        # If we made a set of our target size, great. Count it and clean up so
        # that we can start over with the next number.
        if current.reduce(:+) == target
          chunks += 1
          current = []
        end
      end

      # Record our result
      max = [max, chunks].max
    end

    puts max
  end
end
