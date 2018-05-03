#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
      listint_t *temp = *head;
      listint_t *temp2 = *head;
      listint_t *new;
      int x = 0, i = 0;

      while (temp->n < number)
      {
	    temp = temp->next;
	    i++;
      }
      while (x < i - 1)
      {
	    temp2 = temp2->next;
	    x++;
      }
      new = malloc(sizeof(listint_t));
      new->next = temp2->next;
      temp2->next = new;
      new->n = number;
      return(new);
}
