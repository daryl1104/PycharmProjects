# -*- coding:utf-8 -*-
'''def sample():
    yield 'hello'
    yield 'python'
    yield 'world'

if __name__=='__main__':
    print(' '.join(sample()))'''
'''import sys
s = '{name} has {num} messages'
name='yixin'
num= 50
a = 'a'
print(s.format_map(vars()))
print(sys._getframe(0))'''
'''import numpy as np
a=np.array([
        [[1.0,2.0,3.0,4.0],
        [5.0,6.0,7.0,8.0],
        [8.0,7.0,6.0,5.0],
        [4.0,3.0,2.0,1.0]],
        [[4.0,3.0,2.0,1.0],
         [8.0,7.0,6.0,5.0],
         [1.0,2.0,3.0,4.0],
         [5.0,6.0,7.0,8.0]]
    ])
a=np.reshape(a,[1,4,4,2])
print(a)'''
# import tensorflow as tf
# import numpy as np
#
# c=np.random.random([5,1])
# b=tf.nn.embedding_lookup(c,[1,3])
#
# with tf.Session() as sess:
#     sess.run(tf.initialize_all_variables())
#     print(c)
#     print(sess.run(b))
'''import numpy as np
var1=np.ndarray(shape=(1,5),buffer=np.array([1,2,3,4,5,6,7,8,9]),dtype=int)
print(var1)'''
# class JustCounter:
#     __secretCount=0
#     publicCount=0
#
#     def count(self):
#         self.__secretCount+=1
#         self.publicCount+=1
#         print(self.__secretCount)
#
# counter=JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter._JustCounter__secretCount)
#
'''from __future__ import absolute_import
from __future__ import division
from __future__ import print_function'''

# Imports
import numpy as np
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)

# Our application logic will be added here

if __name__ == "__main__":
  tf.app.run()