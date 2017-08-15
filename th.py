import threading 
import time

def main():
	t1_stop= threading.Event()
	t1 = threading.Thread(target=thread1, args=(1, t1_stop)).start()
	duration = 2
	time.sleep(duration)
	#stop the thread2
	t1_stop.set()
	

def thread1(arg1, stop_event):
	i = 0
	while(not stop_event.is_set()):
		dur = 0.01
		print(str(i),end='\r')
		i = round( i + dur, len(str(0.0001)))
		time.sleep(dur)
	print()
	#execute command when thread is terminated
	print ("isset")
	
main()