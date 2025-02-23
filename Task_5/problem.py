class Solution:
    def sampleStats(self, count):
        minimum = 0
        for k in range(len(count)):
            if count[k] > 0:
                minimum = k
                break

        maximum = 0
        for k in range(len(count) - 1, -1, -1):
            if count[k] > 0:
                maximum = k
                break
        
        total = 0
        length = 0
        for k in range(len(count)):
            total += k * count[k]
            if count[k] > 0:
                length += count[k]
        mean = float(total) / length  

        median = 0
        index = 0
        prev = 0

        for k in range(len(count)):
            if index + count[k] <= length // 2:
                index += count[k]
                if count[k] > 0:
                    prev = k
                continue

            if length % 2 == 1:
                median = k
            elif index < length // 2 < index + count[k]:
                median = k
            else:
                median = (k + prev) / 2.0 

            break

        mode = 0
        m = 0
        for k in range(len(count)):
            if count[k] > m:
                m = count[k]
                mode = k

        return [float(minimum), float(maximum), mean, median, float(mode)]
