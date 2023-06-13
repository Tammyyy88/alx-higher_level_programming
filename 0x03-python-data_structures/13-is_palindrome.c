#include <stddef.h>
#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
listint_t *reverse_list(listint_t *head);
int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev = NULL;
listint_t *temp;
int is_palindrome = 1;
if (*head == NULL || (*head)->next == NULL)
return (is_palindrome);
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
temp = slow->next;
slow->next = prev;
prev = slow;
slow = temp;
}
if (fast != NULL)
slow = slow->next;
while (prev != NULL)
{
if (prev->n != slow->n)
{
is_palindrome = 0;
break;
}
prev = prev->next;
slow = slow->next;
}
*head = reverse_list(*head);
return (is_palindrome);
}
/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to the head of the linked list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
listint_t *prev = NULL;
listint_t *current = head;
listint_t *next;
while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
return (prev);
}
