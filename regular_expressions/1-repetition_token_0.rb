#!/usr/bin/env ruby
#put the 1st arg in a variable
input = ARGV[0]
#check if the arg matchs
puts input.scan(/hbt+{2,5}n/).join
