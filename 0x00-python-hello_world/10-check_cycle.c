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
	while (list && b2 && b2->nex)
	{
		list = list->nex;
		b2 = b2->nex->nex;

		if (list == b2)
		{
			list = pre;
			pre =  b2;
			while (1)
			{
				b2 = pre;
				while (b2->nex != list && b2->nex != pre)
				{
					b2 = b2->nex;
				}
				if (b2->nex == list)
					break;

				list = list->nex;
			}
			return (1);
		}
	}

	return (0);
}
