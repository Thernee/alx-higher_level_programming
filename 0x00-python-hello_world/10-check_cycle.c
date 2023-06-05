#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a circle in it
 *
 * @list: the list to check
 * Return: 1 if a circle exists, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *ahead = list;
	listint_t *behind = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (ahead != NULL && ahead->next != NULL)
	{
		behind = behind->next;
		ahead = ahead->next->next;

		if (behind == ahead)
			return (1);
	}

	return (0);
}
