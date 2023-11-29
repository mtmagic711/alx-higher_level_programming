#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "lists.h"

/**
* insert_node - insert node in the right place.
* @head: the head of the lists.
* @number: the data to insert.
* Return: the address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *temp, *previous;

	if (head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t *));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;
	temp = (*head)->next;
	previous = *head;
	if (number < (*head)->n)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	else
	{
		while (temp != NULL)
		{
			if (number < temp->n)
			{
				previous->next = node;
				node->next = temp;
				return (node);
			}
			else
				temp = temp->next;
		}
	}
}
