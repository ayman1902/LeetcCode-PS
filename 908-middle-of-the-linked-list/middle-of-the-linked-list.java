/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode listNodelow = head;
        ListNode listNodeHight = head;

        while(listNodeHight!=null && listNodeHight.next!=null){
            listNodelow=listNodelow.next;
            listNodeHight=listNodeHight.next.next;
        }
        return listNodelow;
        
    }
}