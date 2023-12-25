def merge_array(nums1, nums2):
    ans = []
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            ans.append(nums1[i])
            i += 1
        else:
            ans.append(nums2[j])
            j += 1

    while i < len(nums1):
        ans.append(nums1[i])
        i += 1
    while j < len(nums2):
        ans.append(nums2[j])
        j += 1
    return ans


res = merge_array([1, 4, 7, 20], [3, 5, 6])

print(res)
