'''
 * User: Hojun Lim
 * Date: 2021-01-03
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)


        return list(set_1 & set_2) # return the intersection with O(n+m) time complexity in average, O(n*m) in worst case.


"""
facebook solution in JAVA with O(n) and O(1) of time and space complexity, respectively.

    function intersections(l1, l2) {
        l1.sort((a, b) => a - b) // assume sorted
    l2.sort((a, b) => a - b) // assume sorted
    const intersections = []
    let l = 0, r = 0;
    while ((l2[l] && l1[r]) !== undefined) {
    const left = l1[r], right = l2[l];
    if (right === left) {
    intersections.push(right)
    while (left === l1[r]) r++;
    while (right === l2[l]) l++;
    continue;
}
if (right > left) while (left === l1[r]) r++;
else while (right === l2[l]) l++;

}
return intersections;
}

"""