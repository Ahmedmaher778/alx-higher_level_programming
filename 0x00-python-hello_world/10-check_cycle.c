#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *b2;
	listint_t *pre;

	b2 = list;
	pre = list;
	while (list && b2 && b2->next)
	{
		list = list->next;
		b2 = b2->next->next;

		if (list == b2)
		{
			list = pre;
			pre =  b2;
			while (1)
			{
				b2 = pre;
				while (b2->next != list && b2->next != pre)
				{
					b2 = b2->next;
				}
				if (b2->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
