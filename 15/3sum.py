class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        n, z, p = [], [], []

        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        ns, ps = set(n), set(p)

        if z:
            if len(z) >= 3:
                ans.add((0, 0, 0))
            for i in p:
                if -i in ns:
                    ans.add((-i, 0, i))

        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -(n[i] + n[j])
                if target in ps:
                     ans.add(tuple(sorted((n[i], n[j], target))))

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -(p[i] + p[j])
                if target in ns:
                     ans.add(tuple(sorted((p[i], p[j], target))))

        return [list(x) for x in ans]
