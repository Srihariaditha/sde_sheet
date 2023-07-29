#!/usr/bin/ruby
require_relative './ds_classes/LinkedList'
list = LinkedList.new(2)
list.addition(5)
list.addition(6)
list.addition(8)
list.addition(9)
list.addition(7)
list.addition(10)
list.deletion(5)
# list.print_list
# puts list.length_of_list
# puts list.nthNodeFromEndwithTwoPointers(6)
# puts list.nthNodeFromEndUsingHash(6)
# puts list.nthNodeFromEndWithoutUsingHash(6)

c_list = LinkedList.new(1)
c_list.addition(2)
c_list.addition(3)
loop_start = c_list.addition(4)
c_list.addition(5)
c_list.addition(4)
c_list.addition(7)
c_list.addition(8)
x = c_list.addition(9)
x.next_node = loop_start
# p "Check for Loop"
# puts c_list.checkForLoopInListWithHash
# puts list.checkForLoopInListWithHash
# p "Two Pointers and return value"
# puts c_list.checkForLoopInListWithTwoPointers
# puts list.checkForLoopInListWithTwoPointers

sorted_list = LinkedList.new(1)
sorted_list.addition(5)
sorted_list.addition(8)
sorted_list.addition(15)
sorted_list.addition(20)
sorted_list.addition(25)
sorted_list.addition(30)
sorted_list.addition(31)

# p sorted_list.insertNode(6)

#Reverse a lst
# x =  sorted_list.reverseListByIteration
p sorted_list.head
sorted_list.reverseListByRecursion(sorted_list.head)
p sorted_list.head

def findCommonMergePointofTwoListsByStacks(l1, l2)
  s1 = []
  s2 = []
  while l1
    s1 << l1.__id__
    l1 = l1.next_node
  end
  while l2
    s2 << l2.__id__
    l2 = l2.next_node
  end
  begin
    e1 = s1.pop
    e2 = s2.pop
  end  while e1 != e2
  
  return e1
  p Node.methods 
end

def findCommonMergePointofTwoListsByDifference(l1, l2)
  s1 = 0
  s2 = 0
  while l1
    s1 +=1
    l1 = l1.next_node
  end
  while l2
    s2 +=1
    l2 = l2.next_node
  end
  d = s1-s2
  head = l1
  if s1 < s2
    head = l2
    d = s2-s1
  end
  while d>0
    head = head.next_node
    d -= 1
  end
  return head
end

p sorted_list.middleNode