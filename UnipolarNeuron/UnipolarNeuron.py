from threading import Thread 


class UnipolarNeuron:
	# A thread that consumes data 
	def consumer(self, neuron_num, in_queue): 
		while True: 
			# Get some data 
			data = in_queue.get() 
			#print(f"Data from neuron {neuron_num}: ", data)

	def start(self, neuron_num, queue):
		t1 = Thread(target = self.consumer, args =(neuron_num, queue, ))
		t1.start()
