#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - determines if linked list is a plaindrom
 * @head: pointer to head of list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy1 = *head;
	listint_t *copy2 = *head;
	int x;
	int count = 1;
	int array[10];

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	while (copy1 != NULL)
	{
		copy1 = copy1->next;
		count ++;
	}
	for (x = 0; x < count; x++)
	{
		array[x] = copy2->n;
		copy2 = copy2->next;
		count++;
	}
	for (x = 0; x < count; x++)
		if (array[x] != array[count - 1 - x])
			return(0);
	return(1);
}
