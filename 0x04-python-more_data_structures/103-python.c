#include <Python.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	const char *type;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", alloc);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PySequence_GetItem(p, i);

		type = item->ob_type->tp_name;
		printf("Element %zd: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
	}
}
/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
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
	size = PyBytes_Size(p);
	str = (unsigned char *)PyBytes_AsString(p);
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);
	limit = size <= 10 ? size : 10;
	printf("  first %zd bytes:", limit);
	for (i = 0; i < limit; i++)
		printf(" %02x", str[i]);
	printf("\n");
}
