import unittest
from modules.todo import ToDo

class TestToDo(unittest.TestCase):
    # inicializo datos
    def setUp(self):
        self.todo = ToDo()
        self.todo.add_task('Tarea 1')
        self.todo.add_task('Tarea 2')
    
    def test_add_task(self):
        self.todo.add_task('Tarea 3')
        self.assertEqual(self.todo.tasks, ['Tarea 1','Tarea 2', 'Tarea 3'])
        self.assertIn('Tarea 3', self.todo.tasks)
    
    def test_remove_task(self):
        self.todo.remove_task('Tarea 1')
        self.assertEqual(self.todo.tasks, ['Tarea 2'])
        self.assertNotIn('Tarea 1', self.todo.tasks)
    
    def test_get_tasks(self):
        tasks = self.todo.get_task()
        self.assertEqual(len(tasks), 2)
        self.assertIn('Tarea 1', tasks)
        self.assertIn('Tarea 2', tasks)
    
    def test_is_instances(self):
        self.assertIsInstance(self.todo, ToDo)

    

