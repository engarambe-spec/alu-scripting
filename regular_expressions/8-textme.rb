#!/usr/bin/env ruby
a = /\[from:(.*?)\].*\[to:(.*?)\].*\[flags:(.*?)\]/
b = ARGV[0].match(a)
puts "#{b[1]},#{b[2]},#{b[3]}"
