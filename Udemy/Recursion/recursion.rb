def towers_of_hanoi(disks, start=1, yend=3)
  if disks != 0
    towers_of_hanoi(disks-1, start, 6-start-yend)
    puts "Move disk #{disks} from Peg #{start} to Peg #{yend}"
    towers_of_hanoi(disks-1, 6-start-yend, yend)
  end
end
# towers_of_hanoi(3)

#sort an Array
def check_array_is_sorted(arr)
  l = arr.length 
  return true if arr.length == 1    
  return arr[0] <= arr[1] &&  check_array_is_sorted(arr[1..l])
end

# puts check_array_is_sorted([4,1,2,5,3,4])

#Generate all binary strings with n bits. Assume A[0..n-1] is an array of size n
def appendAtFront(x,l)
  return l.map{|i| x+i}
end

def bitStrings(n)
  return [] if n==0
  return ['0', '1'] if n==1
  sa = bitStrings(n-1)
  return  (appendAtFront('0', sa) + appendAtFront('1', sa))
end
# puts bitStrings(3)

def rangeToList(k)
  return (0..k).map {|i| i.to_s}
end

def baseKStrings(n,k)
  return [] if n==0
  return rangeToList(k) if n==1
  for digit in baseKStrings(1,k) do 
    return baseKStrings(n-1,k).map{|string| digit+string}
  end
end
# puts baseKStrings(4,5)
  
#List of connected cells of 1's
def getRegionSize(matrix, r, c)  
  return 0 if r<0 || c <0 || r >=matrix.length || c>=matrix[r].length
  return 0 if matrix[r][c] == 0
  matrix[r][c] = 0
  size = 1
  for row in (r-1..r+1) do
    for col in (c-1..c+1) do
      puts "row: #{row} and col: #{col} and size: #{size}"
      size = size + getRegionSize(matrix, row, col) if (row !=r || col !=c)
    end
  end
  return size
end

def getMaxRegion(matrix)
  maxSize = 0
  for r in 0..matrix.length-1 do 
    for c in 0..matrix[r].length-1 do 
      if matrix[r][c]==1
        size = getRegionSize(matrix, r,c)
        maxSize = size if size > maxSize   
      end   
    end
  end
  return maxSize
end
mat = [ [0, 0, 1, 1, 0],
        [1, 0, 1, 1, 0], 
        [0, 1, 0, 0, 0], 
        [0, 0, 0, 0, 1]]
puts mat.length
puts mat[0].length
puts getMaxRegion(mat)