#include "lists.h"
/**
 * is_palindrome - checks if a single linked list is a palindrome
 *
 * @head: pointer to the head of the list
 * Return: 1 if list is palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ahead;
	listint_t *behind;
	int count = 1;
	int i, j;

	ahead = *head;
	behind = *head;

	if (*head == NULL)
		return (1);

	while (ahead->next != NULL)
	{
		count++;
		ahead = ahead->next;
	}
	ahead = *head;

	for (i = 1; i < count; i++)
	{
		j =1;
		while (j <= count - i)
		{
			if (ahead->next != NULL)
				ahead = ahead->next;
			j++;
		}
		if (ahead->n != behind->n)
			return (0);

		behind = behind->next;
		ahead = behind;
	}

	return (1);
}
