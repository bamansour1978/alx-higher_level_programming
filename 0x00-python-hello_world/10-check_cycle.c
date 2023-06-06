#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *sl = list;
	listint_t *fa = list;

	while (sl != NULL && fa != NULL && fa->next != NULL)
	{
		sl = sl->next;
		fa = fa->next->next;

		if (sl == fa)
			return (1);
	}

	return (0);
}
