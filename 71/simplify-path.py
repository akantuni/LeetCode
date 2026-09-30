class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        new_path = []
        for d in path:
            if d == "." or d == "":
                continue
            if d == "..":
                if new_path:
                    new_path.pop()
            else:
                new_path.append(d)

        return "/" + "/".join(new_path)
