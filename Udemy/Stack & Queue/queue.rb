require 'rubygems'
require 'algorithms'

# To not have to type "Containers::" before each class, use:
include Containers
q = Containers::Queue.new([1, 2, 3, 4, 5])
# p q.next #=> 1
# p q.size #=> 3
# p q.empty?
# q.each{|c| p c}
# p q.pop
# q.push(1)
# q.size

def reverseQueue(q)
  st = Stack.new
  q.each{|c| p c}
  st.push(q.pop) while !q.empty?
  q.push(st.pop) while !st.empty?  
  p "Reversed"
  q.each{|c| p c}
end
reverseQueue(q)

#use priority queue
def maxSumOfSlidingWindow(arr, w)
  
end