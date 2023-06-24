#include "lists.h"

/**
 * is_palindrome - checks if a single linked list is a palindrome
 *
 * @head: pointer to the head of the list
 * Return: 1 if list is a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ahead, *behind;
	int count = 0, i, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	ahead = behind = *head;

	while (ahead != NULL)
	{
		count++;
		ahead = ahead->next;
	}

	for (i = 0; i < count / 2; i++)
	{
		ahead = *head;
		for (j = 0; j < count - i - 1; j++)
			ahead = ahead->next;

		if (behind->n != ahead->n)
			return (0);

		behind = behind->next;
	}

	return (1);
}

