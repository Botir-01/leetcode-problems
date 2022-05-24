# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# 1. State the problem clearly (Done)
# Given a list of strings. The task is to find longest common prefix among them
# If there is no common prefix, return "".
# 2. Come up with some example input & outputs. Try to conver all edge cases (Done
# 3. Come up with a correct solution for the problem. State it in plain English.


tests = []


case1 = {
    'input': ['botir', 'bonu', 'bola'],
    'output': 'bo'
}


case2 = {
    'input': ['barbi', 'bargage', 'barbaris'],
    'output': 'bar'
}


case3 = {
    'input': ['crocodile', 'cron', 'cross'],
    'output': 'cro'
}

# no common prefix
case4 = {
    'input': ['jasur', 'botir', 'alisher'],
    'output': ''
}

# all words the same
case5 = {
    'input': ['share', 'share', 'share'],
    'output': 'share'
}


case6 = {
    'input': ['welong', 'webelong', 'wearethelongest'],
    'output': 'we'
}

# if the list is empty, the program returns an empty string
case8 = {
    'input': [''],
    'output': ''
}

# if there is only one string in the list, the program returns an empty string
case9 = {
    'input': ['greeting'],
    'output': 'greeting'
}

tests.append(case1)
tests.append(case2)
tests.append(case3)
tests.append(case4)
tests.append(case5)
tests.append(case6)
tests.append(case8)
tests.append(case9)


class Solution:
    def __init__(self):
        self.prefix = ''

    def longest_common_prefix(self, strs):
        # Retrieve the first string, if it exists, if not return an empty string
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        self.prefix = strs[0]
        for index in range(1, len(strs)):
            # iterate until to find the common prefix
            while strs[index].find(self.prefix) != 0:
                self.prefix = self.prefix[:-1]
        return self.prefix


# Test the solution
sol = Solution()
for position, test in enumerate(tests):
    result = sol.longest_common_prefix(test['input']) == test['output']
    if result:
        print(f'The test in position {position+1} is succeeded')
    else:
        print(f"The test in position {position+1} is failed")



