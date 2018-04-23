#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
#include <unistd.h>

/**
 * check_cycle - check for loop
 * @list: the list.
 *
 * Return: Always 0 or 1.
 */

int check_cycle(listint_t *list)
{
listint_t *fast;
listint_t *slow;

fast = list;
slow = list;
while (fast != NULL && slow != NULL)
{
if (fast->next != NULL)
{
fast = fast->next->next;
}
slow = slow->next;
if (fast == slow)
return(1);
}
return(0);
}
