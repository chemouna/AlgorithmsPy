
class LargestRectangleInHistogram:

    def largestRectangleArea(self, heights):
        max_area = 0
        stack = list()
        i = 0
        while i < len(heights):
            if len(stack) == 0 or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                curr_top_index = stack[-1]
                stack.pop()

                if len(stack) == 0:
                    area = heights[curr_top_index] * i
                else:
                    area = heights[curr_top_index] * (i - stack[-1] - 1)

                max_area = max(max_area, area)

        while len(stack) > 0:
            curr_top_index = stack[-1]
            stack.pop()
            if len(stack) == 0:
                area = heights[curr_top_index] * i
            else:
                area = heights[curr_top_index] * (i - stack[-1] - 1)

            max_area = max(max_area, area)

        return max_area
