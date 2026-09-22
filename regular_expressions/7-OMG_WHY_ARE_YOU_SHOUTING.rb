#!/usr/bin/env ruby
a = /[A-Z]/
puts ARGV[0].scan(a).join
