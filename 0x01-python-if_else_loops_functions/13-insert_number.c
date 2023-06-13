#include "lists.h"

/**
 * insert_node - inserts a number in a sorted linked list
 *
 * @head: pointer to the head of the list
 * @number: number to be inserted
 * Return: Address of new node, NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ahead;
	listint_t *behind;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	ahead = *head;
	behind = *head;
	new_node->n = number;
	new_node->next = NULL;

	if (ahead == NULL || number < ahead->n)
	{
		new_node->next = ahead;
		ahead = new_node;
		return (new_node);
	}

	while (ahead != NULL && ahead->n < number)
	{
		behind = ahead;
		ahead = ahead->next;
	}

	new_node->next = ahead;
	behind->next = new_node;

	return (*head);
}

