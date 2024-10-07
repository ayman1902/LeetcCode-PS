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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode listNode = head;
        if(listNode==null || listNode.next==null){
            return head;
        }
        while(listNode!=null && listNode.next!=null){
            if(listNode.val==listNode.next.val){
                listNode.next=listNode.next.next;
            }else{
                listNode=listNode.next;
            }
        }
        return head;
        
    }
}