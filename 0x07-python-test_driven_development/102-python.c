#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object
 * Return: nothing
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(p);

	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf("  type: compact ascii\n");
		printf("  length: %ld\n", length);
		printf("  value: %s\n", PyUnicode_AsUTF8AndSize(p, &length));
	}
	else
	{
		printf("  type: compact unicode object\n");
		printf("  length: %ld\n", length);
		printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
	}
}

