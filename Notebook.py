# Databricks notebook source
# MAGIC %ls

# COMMAND ----------

from shared import *

print(reverse('edoc detropmi gnisu'))

# COMMAND ----------

import unittest

class TestHelpers(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse('abc'), 'cba')

r = unittest.main(argv=[''], verbosity=2, exit=False)
assert r.result.wasSuccessful(), 'Test failed; see logs above'

# COMMAND ----------

def reverse(s):
    return s[::-1]

import unittest

class TestHelpers(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse('abc'), 'abc')

r = unittest.main(argv=[''], verbosity=2, exit=False)
assert r.result.wasSuccessful(), 'Test failed; see logs above'

# COMMAND ----------

help(dbutils.widgets.dropdown)

# COMMAND ----------

dbutils.widgets.dropdown(name='Mode', defaultValue='Test', choices=['Test','Normal'])

# COMMAND ----------

if dbutils.widgets.get('Mode') == 'Test':
    assert reverse('abc') == 'cba'
    print('Test passed')
else:
    print(reverse('abc'))

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------


