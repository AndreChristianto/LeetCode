class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Assign the nodes
list11 = ListNode(2)
list12 = ListNode(4)
list13 = ListNode(3)

list21 = ListNode(5)
list22 = ListNode(6)
list23 = ListNode(4)

# Connect the nodes
list11.next = list12
list12.next = list13

list21.next = list22
list22.next = list23

# Do my thing
# Check the length of each lists
length1 = 0
length2 = 0

curr = list11
while curr:
    length1 += 1
    curr = curr.next
# print(length1)

curr = list21
while curr:
    length2 += 1
    curr = curr.next
# print(length2)

result = ListNode()
current = ListNode()
curr1 = list11
curr2 = list21
First = True

while length1 > length2:
    current = ListNode(curr1.val)
    if First is True:
        result = current
        First = False
    curr1 = curr1.next
    length1 -= 1
    # print("do")

while length1 < length2:
    current = ListNode(curr2.val)
    if First is True:
        result = current
        First is False
    curr2 = curr2.next
    length2 -= 1
    # print('done')

keep = 0
while length1 > 0 and length2 > 0 and curr1 is not None and curr2 is not None:
    temp = curr1.val + curr2.val
    follow = temp % 10

    if temp > 9:
        keep = temp / 10

    print(current.val)
    if First is True:
        if keep == 0:
            current = ListNode(follow)
            result = current
        else:
            current = ListNode(follow + keep)
            result = current
        First = False
        print("woo")
    else:
        if keep == 0:
            new = ListNode(follow)
            current.next = new
            current = new
        else:
            new = ListNode(follow + keep)
            current.next = new
            current = new
        print("boo")

    # print(follow)
    # print(keep)

    curr1 = curr1.next
    curr2 = curr2.next

print(result.val)
result = result.next
print(result.val)
