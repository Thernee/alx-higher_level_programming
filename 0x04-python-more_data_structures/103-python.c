#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *obj;

	size = PySequence_Length(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		obj = PySequence_GetItem(p, i);
		printf("Element %zd: %s\n", i, obj->ob_type->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		Py_DECREF(obj);
	}
}

/**
 * print_python_bytes - Prints information of python bytes
 *
 * @p: The Python Object to be worked on
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i, limit;
	unsigned char *str;

	printf("[.] bytes object info\n");

	if (!PyObject_IsInstance(p, (PyObject *)&PyBytes_Type))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyObject_Length(p);
	str = (unsigned char *)((PyBytesObject *)p)->ob_sval;

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);

	limit = size <= 10 ? size : 10;

	printf("  first %zd bytes:", limit);

	for (i = 0; i < limit; i++)
		printf(" %02x", str[i]);

	printf("\n");
}
