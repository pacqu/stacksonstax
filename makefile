all: main.py pika_script
	python main.py pika_script

clean:
	rm *.pyc
	rm pic.ppm
	rm *~
