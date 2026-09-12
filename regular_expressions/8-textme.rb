#!/usr/bin/env ruby
result = ARGV[0].scan(/\[from:([^\]]*)\].*\[to:([^\]]*)\].*\[flags:([^\]]*)\]/)
puts result.join(',')
