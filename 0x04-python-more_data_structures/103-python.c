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
	PyListObject *list;
	PyObject *obj;

	size = PyList_Size(p);
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, obj->ob_type->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
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
	/*PyBytesObject *bytes = (PyBytesObject *)p;*/
	Py_ssize_t size, i, limit;
	unsigned char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
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
