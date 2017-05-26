import tensorflow as tf


class Test(tf.test.TestCase):
    def testVersion(self):
        with self.test_session():
            print('TensorFlow version: {}'.format(tf.__version__))

    def testPrint(self):
        with self.test_session() as sess:
            hello = tf.constant('Hello, TensorFlow!')
            print(sess.run(hello))

    def testSquare(self):
        with self.test_session():
            x = tf.square([2, 3])
            self.assertAllEqual(x.eval(), [4, 9])


if __name__ == '__main__':
    tf.test.main()
