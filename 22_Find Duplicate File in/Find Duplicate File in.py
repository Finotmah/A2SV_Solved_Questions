from collections import defaultdict

class Solution(object):
    def findDuplicate(self, paths):
        content_paths = dict()
        duplicate_paths = []
        
        for path in paths:
            contents = path.split()
            for content in contents:
                if '(' in content:
                    index = content.index('(')
                    key = content[index + 1: -1]
                    if key not in content_paths:
                        content_paths[content[index+1:-1]] = []
                    content_paths[key].append(contents[0] + "/" + content[:index])
        
        
        for group_path in content_paths.values():
            if len(group_path) > 1:
                duplicate_paths.append(group_path)
        
        return duplicate_paths

