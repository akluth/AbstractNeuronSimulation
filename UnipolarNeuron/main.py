import os
import psutil
from numpy import random
from time import sleep
from queue import Queue 
from threading import Thread 
from UnipolarNeuron import UnipolarNeuron

def producer(out_queue):
	while True:
		data = [random.random() for _ in range(5)]
		out_queue.put(data);

pid = os.getpid()
psutil_pid = psutil.Process(pid)
max_neurons = 9000
unipolar_neurons = []

queue = Queue()
producer_thread = Thread(target = producer, args =(queue, ))

print(f'Starting {max_neurons} unipolar neuron threads...')

for neuron_num in range(max_neurons):
	unipolar_neuron = UnipolarNeuron()
	unipolar_neuron.start(neuron_num, queue)
	unipolar_neurons.append(unipolar_neuron)


print(f'Started {neuron_num} unipolar neuron threads.')

producer_thread.start()
print(f'Started producer thread.')

print(f'Using {psutil_pid.memory_info()[0]/2.**30:.3f} GB RAM')