'''
 * User: Hojun Lim
 * Date: 2020-12-31
'''

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city_map = {}
        for path in paths:
            source, dest = path[0], path[1]

            if dest not in city_map: city_map[dest] = []

            if source not in city_map: city_map[source] = [dest]
            else: city_map[source].append(dest)


        for (key, val) in city_map.items():
            if len(val) == 0:
                return key

