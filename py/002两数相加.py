# 2. 两数相加
# 中等
# 相关标签
# 相关企业
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# l1 = [9, 9, 9, 9, 9, 9, 9]
# l2 = [9, 9, 9, 9]
# l3 = [8, 9, 9, 9, 0, 0, 0, 1]
#

#
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         total = max(len(l1), len(l2))  # 计算出哪一个列表内容比较多
#         res = []
#         front = 0
#         for index in range(total):
#
#             try:
#                 n1 = l1[index]
#             except:
#                 n1 = 0
#             try:
#                 n2 = l2[index]
#             except:
#                 n2 = 0
#             n3 = n1 + n2 + front
#             front = 0
#             if n3 >= 10:
#                 n3 -= 10
#                 front = 1
#             res.append(n3)
#             if front == 1 and index == total-1:
#                 print("进位")
#                 res.append(front)
#         return res
#
#
# if __name__ == '__main__':
#     obj = Solution()
#     print(obj.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))

class Solution(object):
    # l1 = [9, 9, 9, 9, 9, 9, 9]
    # l2 = [9, 9, 9, 9]
    # l3 = [8, 9, 9, 9, 0, 0, 0, 1]
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        l1表示链表的一个节点
        要求每次执行返回一个节点
        """
        if not l1:
            return l2
        if not l2:
            return l1

        l1.val += l2.val  # 将两数相加，赋值给 l1 节点
        if l1.val >= 10:
            # 如果节点的值大于10 则需要给下一个节点进位
            l1.next = self.addTwoNumbers(ListNode(l1.val // 10), l1.next)  # 这里因为左边节点他的next为none 所以最终返回的节点 val 是两节点的和 ，next 是右边这个节点
            l1.val %= 10

        l1.next = self.addTwoNumbers(l1.next, l2.next)
        return l1


class ListNode:
    """表示链表中的一个节点"""

    def __init__(self, x=0, n=None):
        self.val = x
        self.next = n  # 下一个节点对象


if __name__ == '__main__':
    print()
