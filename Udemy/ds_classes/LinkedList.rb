require_relative './Node'

class LinkedList  
  attr_accessor :head
  
  def initialize(value)
    @head = Node.new(value, nil)
  end
  
  def addition(value)
    current_node = @head
    while current_node.next_node != nil
      current_node = current_node.next_node
    end
    current_node.next_node = Node.new(value, nil)
    return current_node.next_node
  end
  
  def find(value)
    current_node = @head
    puts current_node.value
    return false if !current_node.next_node
    return current_node if current_node.value == value
    while (current_node = current_node.next_node)
      return current_node if current_node.value == value
    end
  end

  def deletion(value)
    current_node = @head
    if current_node.value == value
      @head = current_node.next_node
    else
      while (current_node.next_node != nil) && (current_node.next_node.value != value)
        if (current_node.next_node == nil) || (current_node.next_node.value == value)
          current_node.next_node = current_node.next_node.next_node
        else
          current_node = current_node.next_node
        end
      end
      current_node.next_node = current_node.next_node.next_node
    end
  end

  def print_list
    current_node = @head
    puts current_node.value
    while (current_node = current_node.next_node)
      puts current_node.value
    end
  end
  
  def length_of_list
    temp = @head
    count = 0
    while temp != nil
      temp = temp.next_node
      count += 1
    end
    return count
  end
  
  def nthNodeFromEndwithTwoPointers(n)    
    return nil if (n < 0)
    temp = @head
    count = 1
    while count<n && temp != nil
      temp = temp.next_node
      count += 1
    end
   return nil if count < n || temp == nil
   nth = @head
   while temp.next_node != nil
     temp = temp.next_node
     nth = nth.next_node
   end
   return nth.value    
  end
  
  def nthNodeFromEndUsingHash(n)    
    return nil if (n < 0)
    n_hash = Hash.new
    temp = @head
    count = 1
    while temp.next_node != nil
      n_hash[count] = temp.value
      temp = temp.next_node
      count += 1
    end
    return nil if count < n
    nth = count-n+1
    return n_hash[nth] 
  end
  
  def nthNodeFromEndWithoutUsingHash(n)
    return nil if (n < 0)
    n_hash = Hash.new
    temp = @head
    len = self.length_of_list
    return nil if len < n
    nth = @head
    m = len-n + 1
    while m > 1
      nth = nth.next_node
      m -= 1
    end
    return nth.value 
  end
  
  def checkForLoopInListWithHash
    current_node = @head
    h = Hash.new
    i = 0
    while current_node
      puts h
      return true if !h.empty? && (h.values.include? current_node.__id__)
      h[i] = current_node.__id__
      i += 1
      current_node = current_node.next_node
    end
    return false
  end
  
  def checkForLoopInListWithTwoPointers
    slowPtr = @head
    fastPtr = @head.next_node
    while slowPtr && fastPtr && slowPtr != fastPtr
      slowPtr = slowPtr.next_node rescue nil
      fastPtr = fastPtr.next_node.next_node rescue nil
    end
    return false unless fastPtr
    fastPtr = fastPtr.next_node
    count =1
    while slowPtr != fastPtr
      fastPtr = fastPtr.next_node
      count += 1
    end
    p "Length #{count}"
    slowPtr = @head
    while (slowPtr != fastPtr.next_node)
      fastPtr = fastPtr.next_node
      slowPtr = slowPtr.next_node
    end
    p slowPtr.value
    p fastPtr.value
    # p slowPtr.next_node.value
    return true
  end
  
  def insertNode(val)
    current_node = @head
    if val <= current_node.value
      node= Node.new(val, current_node)
      @head = node
      return @head.next_node.value
    end 
    prev_node = current_node
    while current_node && val > current_node.value 
      prev_node = current_node
      current_node = current_node.next_node
    end
    node= Node.new(val, current_node)
    prev_node.next_node = node
    return prev_node.value
  end

  def reverseListByIteration
    cur = @head.next_node
    prev = @head
    while cur
      temp = cur.next_node
      cur.next_node = prev
      prev = cur
      cur = temp
    end   
    return prev    
  end
  
  def reverseListByRecursion(node)
    return nil unless node
    unless node.next_node 
      @head = node
      return node
    end
    node1 = reverseListByRecursion(node.next_node)
    node1.next_node = node
    node.next_node = nil
    return node    
  end
  
  def middleNode
    p1 = p2 = @head
    i = 0
    while p1.next_node
      if i==0
        p1 = p1.next_node 
        i = 1
      elsif i==1
        p1 = p1.next_node
        p2 = p2.next_node
        i = 0
      end
    end
    return p2.value    
  end
end