#include "lists.h"

/**
 * is_palindrome - a function in C that checks if a singly
 * linked list is a palindrome.
 *
 * @head: double pointer
 *
 * Return: 1 or NULL
 */

int is_palindrome(listint_t **head)
{
	listint_t *curr = *head;
	listint_t *pal = *head;
	int count = 0, j = 0;
	int i = 0;

	if (!*head)
		return (1);

	while (curr)
	{
		curr = curr->next;
		count++;
	}

	curr = *head;

	for (i = 1; i <= count; i++)
	{
		for (j = i; j <= count - i; j++)
			pal = pal->next;
		if (curr->n != pal->n)
			return (0);
		curr = curr->next;
		pal = curr;
	}
	return (1);
}
