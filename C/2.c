struct ListNode {
    int val;
    struct ListNode * next;
};


struct ListNode * addTwoNumbers(struct ListNode * l1, struct ListNode * l2){
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val = 0;
    newNode->next = NULL;
    struct ListNode* currentNode = newNode;
    int carry = 0, val;
    while (l1 || l2){
        val = carry;
        if (l1){
            val += l1->val;
            l1 = l1->next;
        }
        if (l2){
            val += l2->val;
            l2 = l2->next;
        }
        carry = val / 10;
        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = val % 10;
        node->next = NULL;
        currentNode->next = node;
        currentNode = currentNode->next;
    }
    
    if (carry == 1){
        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = 1;
        node->next = NULL;
        currentNode->next = node;
    }
    
    return newNode->next;
}
