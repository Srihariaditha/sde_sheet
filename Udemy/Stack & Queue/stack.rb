require 'rubygems'
require 'algorithms'

# To not have to type "Containers::" before each class, use:
include Containers
stack  = Stack.new([1,11, 12])
# p stack.empty?
# p stack.size
# p stack.pop
# stack.each { |x| p x}
# p stack.push(30)
# p stack.empty?

#Balacing parenthesis
s = "(((({345(xcv)56[rt]thhg}}}}}"

PAIRS = {
  "]" => "[",
  "}" => "{",
  ")" => "("
}

def balancedParanthesis(str)
  st = Stack.new
  key = PAIRS.keys
  val = PAIRS.values
  str.split('').each do |c|
    next unless (key + val).include? c
    if val.include? c
      st.push(c)
      next
    end
    return false if st.empty? || st.pop != PAIRS[c]
  end
  return true
end  

# p balancedParanthesis(s)

def pushToStack(s, m, data)
  s.push(data)
  m.push(data) if m.empty? || m.next >= data
end

def popFromStack(s, m)
  return nil if s.empty?
  x = s.pop
  m.pop if m.next >=x && !m.empty?
  return x
end
st_el = Stack.new()
st_min = Stack.new()

# pushToStack(st_el, st_min, 2)
# pushToStack(st_el, st_min, 6)
# pushToStack(st_el, st_min, 4)
# pushToStack(st_el, st_min, 1)
# pushToStack(st_el, st_min, 5)
# pushToStack(st_el, st_min, -1)
# def getMinimum(s, m)
#   p m.next
# end
# getMinimum(st_el, st_min)
# popFromStack(st_el, st_min)
# popFromStack(st_el, st_min)
# getMinimum(st_el, st_min)
# popFromStack(st_el, st_min)
# getMinimum(st_el, st_min)
# popFromStack(st_el, st_min)
# popFromStack(st_el, st_min)
# getMinimum(st_el, st_min)


def checkPalindrome(s)
  st = Stack.new
  foundX = false
  s.split('').each do |c|
    if c=='X'
      foundX = true
    elsif !foundX
      st.push(c) 
    else
      return false if st.empty? || st.pop != c
    end
  end
  return true
end

# p checkPalindrome('sssXsss')
st = Stack.new([1,2,3,4,5])
# st.each{ |x| p x}

def insertAtBottom(s, data)
  if s.empty?
    s.push(data)
    return
  end
  temp = s.pop
  insertAtBottom(s, data)
  s.push(temp)
  
end

def reverseStack(s)
  return if s.empty?
  data = s.pop
  reverseStack(s)
  insertAtBottom(s, data)
end

# reverseStack(st)
# st.each{ |x| p x}

def spanOfStocks(arr)
  st = Stack.new()
  s = []
  arr.each_with_index do |x, i|
    while !st.empty?
       if x > arr[st.next]
         st.pop
       else
         break
       end
    end    
    if st.empty?
      p = -1
    else
      p = st.next
    end
    s[i] = i-p
    st.push(i)
  end
  return s
end

# p spanOfStocks([6,7,3,4,5, 6,2])

def max_area_histogram(hist)
  st = Stack.new()
  max_area = 0
  index = 0
  while (index < hist.length)
    if st.empty? || hist[st.next] <= hist[index]
      p "if #{index}"
      p "top :#{hist[st.next]} and index #{ hist[index]}" if !st.empty?
      st.push(index)
      index += 1
      l = ''
      st.each{ |x| l =l+ ' '+x.to_s}
      p l
    else
      p "else #{index}"
      l = ''
      st.each{ |x| l =l+ ' '+x.to_s}
      p l
      st_top = st.pop
      area = hist[st_top] * (st.empty? ? index : (index-st.next-1))
      max_area = area if max_area < area    
      p "max_area : #{max_area} area #{area}"  
    end
  end
  while !st.empty?
    st_top = st.pop
    area = hist[st_top] * (st.empty? ? index : (index-st.next-1) )
    max_area = area if max_area < area
  end
  max_area
end

p max_area_histogram([6, 2, 5, 4, 5, 1, 6])

p max_area_histogram([1, 2, 3 ,4, 5, 6])

p max_area_histogram([5, 4, 3, 2, 1])