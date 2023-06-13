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
	int count = 0;

	ahead = *head;
	behind = *head;

	if (*head == NULL)
		return (1);

	while (ahead->next != NULL) {
		count++;
		ahead = ahead->next;
	}

	if (count % 2 == 0) {
		while (behind != NULL) {
			if (ahead->n != behind->n)
				return (0);

			ahead = ahead->next;
			behind = behind->next->next;
		}
	} else {
		while (behind != NULL) {
			if (ahead->n != behind->n)
				return (0);

			ahead = ahead->next->next;
			behind = behind->next;
		}
	}

	return (1);
}

