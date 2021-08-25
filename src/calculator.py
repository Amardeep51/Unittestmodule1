class Calculator(object):
    """Perform basic arithmetic"""
    
    
    def __init__(self):
        self._result = 0
    
    def setResult(self, result):
        self._result = result
        
    def result(self):
        return self._result
    
    def add(self, *nums):
        """Add all numbers in *nums sequentially"""
        total = 0
        for i in nums:
            total += i
        self.setResult(total)
        return total
    
    def multiply(self, *nums):
        """Multiply all numbers in *nums sequentially"""
        if len(nums) == 0:
            return 0
        total = 1
        for i in nums:
            total *= i
        self.setResult(total)
        return total
        
        
    def divide(self, *nums):
        """Divide all numbers in *nums sequentially"""
        if len(nums) == 0:
            return 0
        total = 1
        for i in nums:
            total /= i
        self.setResult(total)
        return total
