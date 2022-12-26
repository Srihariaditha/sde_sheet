FIXNUM_MIN = -(2**(0.size * 8 -2))
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
def set_zeroes(matrix)
  row_count, col_count = matrix.length, matrix[0].length
  m2 = Array.new(row_count){Array.new(col_count, 'x')}
  matrix.each_with_index do |r,i|
      r.each_with_index do |c,j|
          if c==0
              m2[i] = Array.new(col_count, 0)
              row_count.times { |k| m2[k][j] = 0}
          else
              m2[i][j] = c if m2[i][j] !=0
          end
      end
      matrix[i] = m2[i]
   end
end
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# set_zeroes(matrix)
# puts matrix

# Given an integer numRows, return the first numRows of Pascal's triangle.
# 
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
# 
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 
# Input: numRows = 1
# Output: [[1]]

#Ncr is the value at any position in pascal triangle

def pascal_triangle(row_index)
  tr = Array.new(row_index+1)
  (row_index+1).times do |i|
    if i == 0
      tr[i] = [1]
    elsif i == 1
      tr[i] = [1, 1]
    else
      tr[i] = Array.new(i)
      (i+1).times do |j|
        if j==0 || j==i
          tr[i][j] = 1
        else
          tr[i][j] = tr[i-1][j-1] + tr[i-1][j]
        end
      end
    end
  end
  return tr[row_index]
end
# puts pascal_triangle(3)

# Given an array of integers nums, find the next permutation of nums.
# 
# The replacement must be in place and use only constant extra memory.
# Example 1:
# 
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:
# 
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:
# 
# Input: nums = [1,1,5]
# Output: [1,5,1]

def next_permutation(nums)
    index = 0
    for i in 0..(nums.count-2)
      if nums[i] > nums[i+1]
        index = i-1
        break
      end
    end
    retrun
    for i in 0..nums.count
      if arr[nums.count-1-]
end