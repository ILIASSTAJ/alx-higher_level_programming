#include "lists.h"

/**
 *insert_node - Insert number into a sorted singly-linked list
 *@head: pointer to the head of the list
 *@number: The number to be inserted
 *
 *Return: NULL in case of failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *helper;
	listint_t *temp;
	temp = (*head);
	new = malloc(sizeof(listint_t));
	new->n = number;
	if((*head) == NULL || (*head)->n > number)
	{
		helper = (*head);
		(*head) = new;
		new = helper;
		return (*head);
	}
	while(temp->next && temp->next->n < number)
	{
		temp = temp->next;
	}
	helper = temp->next;
	temp->next = new;
	new->next = helper;
	return (*head);

}
