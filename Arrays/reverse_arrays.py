class Array:
  def __init__(self):
    self.array = []
    self.length = 0
  
  def reverse(self):
    for i in range(len(self.array)/2):
      current_position = i
      swap_position = len(self.array) - (i + 1)
      
      temp = self.array[swap_position]
      current_value = self.array[current_position]
      self.array[swap_position] = current_value
      self.array[current_position] = temp
    
    return self.array
  

array = Array()
array.append(1)
array.append(2)
array.append(3)
array.append(4)
array.append(5)
array.append(6)
array.append(7)
print array.reverse()

