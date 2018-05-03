#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
      listint_t *temp = *head;
      listint_t *temp2 = *head;
      listint_t *new;
      int x = 0, i = 0;

      if ((*head == NULL) || (head == NULL))
	    return(NULL);
      while (temp->n < number)
      {
	    temp = temp->next;
	    i++;
      }
      new = malloc(sizeof(listint_t));
      if (new == NULL)
	    return(NULL);
      if (i == 0)
      {
	    *head = new;
	    new->n = number;
      }
      while (x < i - 1)
      {
	    temp2 = temp2->next;
	    x++;
      }
      new->next = temp2->next;
      temp2->next = new;
      new->n = number;
      return(new);
}
