import lab2.wtiproj02_consumer_1 as c1
import lab2.wtiproj02_consumer_2 as c2
import lab2.wtiproj02_producer as p


if __name__ == '__main__':
    usr_in = input("type p for producer, c1 for consumer_1 or c2 for consumer_2 \n")
    if usr_in == 'p':
        p.producer_2('wti2')
    elif usr_in == 'c1':
        c1.consumer_1('wti2')
    elif usr_in == 'c2':
        c2.consumer_2('wti2')
