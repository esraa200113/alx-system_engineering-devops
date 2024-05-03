#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - Entry point
 *
 * Return: Always 0
 */
int main(void)
{
    pid_t child_pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        child_pid = fork();
        if (child_pid == -1)
        {
            perror("fork");
            exit(EXIT_FAILURE);
        }
        if (child_pid == 0)
        {
            // Child process
            exit(EXIT_SUCCESS);
        }
        else
        {
            // Parent process
            printf("Zombie process created, PID: %d\n", child_pid);
            sleep(1); // Sleep to ensure parent prints before child exits
        }
    }

    infinite_while(); // Infinite loop to keep the parent process running

    return (0);
}

