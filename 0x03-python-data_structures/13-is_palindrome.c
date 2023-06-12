#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *curr = *head;
	listint_t *pal = *head;
	int count = 0, j = 0;
	int i;

	if (!*head)
		return (1);

	while (curr)
	{
		curr = curr->next;
		count++;
	}

	curr = *head;

	i = 0;
	while (i <= count)
	{
		for (j = i; j <= count - i; j++)
			pal = pal->next;
		if (curr->n != pal->n)
			return (0);
		curr = curr->next;
		pal = curr;
		i++;
	}
	return (1);
}
