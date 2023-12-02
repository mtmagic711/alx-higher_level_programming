#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stddef.h>

/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: the head of the list.
* Return: 0 if it is not a palindrome, 1 if it is a palindrome.
*/

int is_palindrome(listint_t **head)
{
	int cmpt = 0, i = 0, j = 0, flag = 0;
	listint_t *temp;
	int *p;

	if (head == NULL)
		return (1);
	temp = *head;
	while (temp != NULL)
	{
		cmpt++;
		temp = temp->next;
	}
	p = (int *)malloc(sizeof(int) * cmpt);
	if (p == NULL)
		return (0);
	temp = *head;
	while (temp != NULL)
	{
		*(p + i) = temp->n;
		temp = temp->next;
		i++;
	}
	for (i = 0, j = cmpt - 1; i <= (cmpt / 2) && j >= cmpt / 2; i++, j--)
	{
		if (*(p + i) == *(p + j))
			flag = 0;
		else
		{
			flag = 1;
			return (0);
		}
	}
	if (flag == 0)
		return (1);
	return (1);
}
