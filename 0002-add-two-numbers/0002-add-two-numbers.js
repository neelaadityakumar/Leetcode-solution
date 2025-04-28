/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    var head = null;
    var tail = null;
    var sum = 0;
    var carry = 0;

    while (l1 !== null || l2 !== null || sum > 0) {
        if (l1 !== null) {
            sum = sum + l1.val;
            l1 = l1.next;
        }
        if (l2 !== null) {
            sum = sum + l2.val;
            l2 = l2.next;
        }

        if (sum >= 10) {
            carry = Math.floor(sum / 10);
            sum = sum % 10;
        }

        var newNode = new ListNode(sum);

        if (head === null) {
            head = newNode;
            tail = head;
        } else {
            tail.next = newNode;
            tail = newNode;
        }

        sum = carry;
        carry = 0;
    }

    return head;
};
